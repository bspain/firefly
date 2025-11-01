/**
 * Projection Service
 * Handles annual financial projections for Coast FIRE plans
 */

import { 
  CoastFirePlan, 
  AnnualProjection, 
  PhaseType
} from '../../shared/types';
import { getPhaseAtAge } from './phase-config';

/**
 * Generates annual projections for the entire planning horizon
 * 
 * @param plan - The complete Coast FIRE plan
 * @returns Array of annual projections from start year to end year
 * 
 * @example
 * const projections = generateAnnualProjections(plan);
 * // Returns array of projections for each year in the planning horizon
 */
export function generateAnnualProjections(plan: CoastFirePlan): AnnualProjection[] {
  const projections: AnnualProjection[] = [];
  const { startYear, endYear } = plan.projectionSettings.analysisTimeframe;
  const { currentAge, baseYear } = plan.ownerProfile;
  
  for (let year = startYear; year <= endYear; year++) {
    const age = currentAge + (year - baseYear);
    const phase = getPhaseAtAge(plan.phases, age);
    
    if (!phase) {
      continue; // Skip years outside phase boundaries
    }
    
    const projection = calculateYearProjection(plan, year, age, phase);
    projections.push(projection);
  }
  
  return projections;
}

/**
 * Calculates projection for a specific year
 * 
 * @param plan - The complete Coast FIRE plan
 * @param year - Calendar year
 * @param age - User's age at end of year
 * @param phase - Phase type for this year
 * @returns Annual projection for the specified year
 */
function calculateYearProjection(
  plan: CoastFirePlan,
  year: number,
  age: number,
  phase: PhaseType
): AnnualProjection {
  const { socialSecurity } = plan.incomeAssumptions;
  const { coastPhase, retirementPhase } = plan.incomeAssumptions;
  
  // Calculate Social Security income
  let socialSecurityIncome = 0;
  if (age >= socialSecurity.startAge) {
    const yearsFromStart = age - socialSecurity.startAge;
    socialSecurityIncome = socialSecurity.baseAnnualBenefit * 
      Math.pow(1 + socialSecurity.colaRate, yearsFromStart);
  }
  
  // Calculate salary need and income based on phase
  let salaryNeed = 0;
  let salaryIncome = 0;
  
  if (phase === 'COAST') {
    salaryNeed = coastPhase.annualNeed;
    salaryIncome = coastPhase.annualIncome;
  } else if (phase === 'RETIREMENT') {
    salaryNeed = retirementPhase.annualNeed + retirementPhase.medicalNeed;
    salaryIncome = 0;
  }
  
  // Get events for this year
  const eventsThisYear = plan.events.filter(e => {
    const eventYear = plan.ownerProfile.baseYear + (e.age - plan.ownerProfile.currentAge);
    return eventYear === year;
  });
  
  // Calculate investment interest (simplified - actual implementation would track portfolio)
  // const rateOfReturn = plan.projectionSettings.rateOfReturnByPhase[phase];
  
  // Calculate gap (simplified)
  const totalIncome = socialSecurityIncome + salaryIncome;
  const totalExpenses = salaryNeed;
  const gap = totalExpenses - totalIncome;
  
  // For now, use placeholder values for investment interest and principal
  // Real implementation would track portfolio balance over time
  const investmentInterest = 0;
  const remainingPrincipal = 0;
  
  return {
    year,
    age,
    phase,
    socialSecurityIncome,
    salaryNeed,
    salaryIncome,
    investmentInterest,
    gap,
    remainingPrincipal,
    events: eventsThisYear
  };
}

/**
 * Checks if projections need to be recalculated
 * This would be called when phase boundaries change
 * 
 * @param plan - The Coast FIRE plan
 * @returns true if projections should be regenerated
 */
export function shouldRecalculateProjections(_plan: CoastFirePlan): boolean {
  // Always recalculate when phase settings change
  // In a real implementation, this would compare with cached projections
  return true;
}
