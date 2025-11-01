/**
 * Phase Configuration Service
 * Handles Coast FIRE plan phase boundary calculations and updates
 */

import { Phase, PhaseSettings, PhaseType, OwnerProfile } from '../../shared/types';

/**
 * Creates default phase boundaries for a new Coast FIRE plan
 * 
 * @param ownerProfile - The user's profile containing current age and planning parameters
 * @returns PhaseSettings with default phase boundaries
 * 
 * @example
 * const profile = { currentAge: 48, targetRetirementAge: 60, planningHorizonAge: 100, baseYear: 2025 };
 * const phases = createDefaultPhases(profile);
 * // Returns phases: Accumulation (22-49), Coast (50-65), Retirement (66-100)
 */
export function createDefaultPhases(ownerProfile: OwnerProfile): PhaseSettings {
  const { currentAge, planningHorizonAge } = ownerProfile;
  
  // Default phase boundaries
  const accumulationEnd = currentAge + 1; // One year after current age
  const coastStart = accumulationEnd + 1;
  const coastEnd = 65; // Standard Social Security full retirement age
  const retirementStart = coastEnd + 1;
  
  const phases: Phase[] = [
    {
      phaseType: 'ACCUMULATION',
      startAge: 22, // Typical career start age
      endAge: accumulationEnd,
      contributionPolicy: {
        status: 'ACTIVE',
        annualContribution: 0,
        sourceAccountIds: []
      }
    },
    {
      phaseType: 'COAST',
      startAge: coastStart,
      endAge: coastEnd,
      contributionPolicy: {
        status: 'PAUSED',
        annualContribution: 0,
        sourceAccountIds: []
      }
    },
    {
      phaseType: 'RETIREMENT',
      startAge: retirementStart,
      endAge: planningHorizonAge,
      contributionPolicy: {
        status: 'PAUSED',
        annualContribution: 0,
        sourceAccountIds: []
      }
    }
  ];
  
  return { phases };
}

/**
 * Updates phase boundaries when the target coast start age changes
 * 
 * @param phaseSettings - Current phase settings
 * @param newCoastStartAge - The new target age for coast phase to begin
 * @returns Updated PhaseSettings with recomputed boundaries
 * 
 * @example
 * const updated = updateCoastStartAge(currentPhases, 52);
 * // Accumulation now ends at 51, Coast starts at 52
 */
export function updateCoastStartAge(
  phaseSettings: PhaseSettings,
  newCoastStartAge: number
): PhaseSettings {
  const updatedPhases = phaseSettings.phases.map((phase): Phase => {
    if (phase.phaseType === 'ACCUMULATION') {
      return {
        ...phase,
        endAge: newCoastStartAge - 1
      };
    }
    if (phase.phaseType === 'COAST') {
      return {
        ...phase,
        startAge: newCoastStartAge
      };
    }
    return phase;
  });
  
  return { phases: updatedPhases };
}

/**
 * Retrieves a specific phase by type
 * 
 * @param phaseSettings - Current phase settings
 * @param phaseType - The type of phase to retrieve
 * @returns The phase object or undefined if not found
 */
export function getPhaseByType(
  phaseSettings: PhaseSettings,
  phaseType: PhaseType
): Phase | undefined {
  return phaseSettings.phases.find(p => p.phaseType === phaseType);
}

/**
 * Determines which phase applies at a given age
 * 
 * @param phaseSettings - Current phase settings
 * @param age - The age to check
 * @returns The phase type that applies at the given age, or undefined
 */
export function getPhaseAtAge(
  phaseSettings: PhaseSettings,
  age: number
): PhaseType | undefined {
  const phase = phaseSettings.phases.find(
    p => age >= p.startAge && age <= p.endAge
  );
  return phase?.phaseType;
}

/**
 * Validates phase boundaries for logical consistency
 * 
 * @param phaseSettings - Phase settings to validate
 * @returns Array of validation error messages (empty if valid)
 */
export function validatePhases(phaseSettings: PhaseSettings): string[] {
  const errors: string[] = [];
  const { phases } = phaseSettings;
  
  if (phases.length === 0) {
    errors.push('At least one phase is required');
    return errors;
  }
  
  // Check for gaps and overlaps
  const sortedPhases = [...phases].sort((a, b) => a.startAge - b.startAge);
  
  for (let i = 0; i < sortedPhases.length - 1; i++) {
    const current = sortedPhases[i];
    const next = sortedPhases[i + 1];
    
    if (current.endAge >= next.startAge) {
      errors.push(
        `Phase overlap: ${current.phaseType} (ends ${current.endAge}) overlaps with ${next.phaseType} (starts ${next.startAge})`
      );
    }
    
    if (current.endAge + 1 < next.startAge) {
      errors.push(
        `Phase gap: Gap between ${current.phaseType} (ends ${current.endAge}) and ${next.phaseType} (starts ${next.startAge})`
      );
    }
  }
  
  // Validate each phase
  phases.forEach(phase => {
    if (phase.startAge > phase.endAge) {
      errors.push(
        `Invalid phase ${phase.phaseType}: start age (${phase.startAge}) is greater than end age (${phase.endAge})`
      );
    }
  });
  
  return errors;
}
