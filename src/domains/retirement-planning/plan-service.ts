/**
 * Plan Service
 * Main service for creating and managing Coast FIRE plans
 */

import { CoastFirePlan, OwnerProfile } from '../../shared/types';
import { createDefaultPhases, updateCoastStartAge } from './phase-config';
import { generateAnnualProjections } from './projections';

/**
 * Creates a new Coast FIRE plan with default settings
 * 
 * @param ownerProfile - User's profile information
 * @returns A new Coast FIRE plan with default phase boundaries
 * 
 * @example
 * const profile = { currentAge: 48, targetRetirementAge: 60, planningHorizonAge: 100, baseYear: 2025 };
 * const plan = createPlan(profile);
 */
export function createPlan(ownerProfile: OwnerProfile): CoastFirePlan {
  const now = new Date().toISOString().split('T')[0];
  const phases = createDefaultPhases(ownerProfile);
  
  const plan: CoastFirePlan = {
    planId: `plan-${Date.now()}`,
    label: 'My Coast FIRE Plan',
    version: 1,
    createdAt: now,
    updatedAt: now,
    ownerProfile,
    phases,
    accounts: {
      assets: [],
      liabilities: []
    },
    incomeAssumptions: {
      coastPhase: {
        annualNeed: 0,
        annualIncome: 0,
        shortfallPolicy: {
          primarySource: 'ROTH',
          trackRothContributions: true,
          earlyWithdrawalPenaltyRate: 0.1
        }
      },
      retirementPhase: {
        annualNeed: 0,
        medicalNeed: 0
      },
      socialSecurity: {
        startAge: 70,
        baseAnnualBenefit: 0,
        colaRate: 0.025
      },
      otherIncomeSources: []
    },
    expenseAssumptions: {
      globalInflationRate: 0.025,
      expenseCategories: []
    },
    events: [],
    housingTransition: {
      enabled: false,
      targetAge: 0,
      salePrice: 0,
      replacementCost: 0,
      transactionCostsModeled: false
    },
    projectionSettings: {
      rateOfReturnByPhase: {
        ACCUMULATION: 0.1,
        COAST: 0.06,
        RETIREMENT: 0.04
      },
      analysisTimeframe: {
        startYear: ownerProfile.baseYear + 1,
        endYear: ownerProfile.baseYear + (ownerProfile.planningHorizonAge - ownerProfile.currentAge)
      },
      withdrawalOrder: [
        'NON_QUALIFIED',
        'QUALIFIED',
        'HSA',
        'ROTH',
        'INSURANCE',
        'CASH',
        'LIFESTYLE'
      ],
      projectionYears: []
    },
    persistencePolicy: {
      snapshotExportMode: 'PROMPT',
      storagePath: ''
    }
  };
  
  return plan;
}

/**
 * Updates the coast start age and recalculates projections
 * 
 * @param plan - Current plan
 * @param newCoastStartAge - New target age for coast phase to begin
 * @returns Updated plan with new phase boundaries and recalculated projections
 */
export function setCoastStartAge(
  plan: CoastFirePlan,
  newCoastStartAge: number
): CoastFirePlan {
  const updatedPhases = updateCoastStartAge(plan.phases, newCoastStartAge);
  
  const updatedPlan: CoastFirePlan = {
    ...plan,
    phases: updatedPhases,
    updatedAt: new Date().toISOString().split('T')[0]
  };
  
  return updatedPlan;
}

/**
 * Loads a plan from JSON data
 * 
 * @param jsonData - Plan data in JSON format
 * @returns Parsed Coast FIRE plan
 */
export function loadPlan(jsonData: string): CoastFirePlan {
  const plan = JSON.parse(jsonData) as CoastFirePlan;
  return plan;
}

/**
 * Saves a plan to JSON format
 * 
 * @param plan - The plan to save
 * @returns JSON string representation of the plan
 */
export function savePlan(plan: CoastFirePlan): string {
  return JSON.stringify(plan, null, 2);
}

/**
 * Gets annual projections for a plan
 * 
 * @param plan - The Coast FIRE plan
 * @returns Array of annual projections
 */
export function getProjections(plan: CoastFirePlan) {
  return generateAnnualProjections(plan);
}
