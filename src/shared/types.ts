/**
 * Core type definitions for Firefly Coast FIRE planning
 */

export type PhaseType = 'ACCUMULATION' | 'COAST' | 'RETIREMENT';

export type AccountType = 
  | 'QUALIFIED' 
  | 'ROTH' 
  | 'NON_QUALIFIED' 
  | 'CASH' 
  | 'LIFESTYLE' 
  | 'INSURANCE' 
  | 'HSA' 
  | 'OTHER';

export type LiabilityCadence = 'MONTHLY' | 'QUARTERLY' | 'ANNUAL' | 'OTHER';

export type EventType = 'EXPENSE' | 'INFLOW';

export type SnapshotExportMode = 'PROMPT' | 'ALWAYS' | 'NEVER';

export interface OwnerProfile {
  currentAge: number;
  targetRetirementAge: number;
  planningHorizonAge: number;
  baseYear: number;
}

export interface ContributionPolicy {
  status: 'ACTIVE' | 'PAUSED';
  annualContribution: number;
  sourceAccountIds: string[];
}

export interface Phase {
  phaseType: PhaseType;
  startAge: number;
  endAge: number;
  contributionPolicy: ContributionPolicy;
}

export interface PhaseSettings {
  phases: Phase[];
}

export interface BalanceSnapshot {
  date: string; // ISO 8601 format
  amount: number;
}

export interface AssetAccount {
  accountId: string;
  name: string;
  accountType: AccountType;
  balanceHistory: BalanceSnapshot[];
  costBasis?: number;
  allowRothContributionWithdrawals?: boolean;
  metadata?: Record<string, unknown>;
}

export interface Liability {
  liabilityId: string;
  name: string;
  interestRate: number;
  paymentCadence: LiabilityCadence;
  paymentAmount: number;
  balanceHistory: BalanceSnapshot[];
  payoffDate?: string;
  metadata?: Record<string, unknown>;
}

export interface Accounts {
  assets: AssetAccount[];
  liabilities: Liability[];
}

export interface ShortfallPolicy {
  primarySource: AccountType;
  trackRothContributions: boolean;
  earlyWithdrawalPenaltyRate: number;
}

export interface CoastIncome {
  annualNeed: number;
  annualIncome: number;
  shortfallPolicy: ShortfallPolicy;
}

export interface RetirementIncome {
  annualNeed: number;
  medicalNeed: number;
}

export interface SocialSecurity {
  startAge: number;
  baseAnnualBenefit: number;
  colaRate: number;
}

export interface OtherIncomeSource {
  sourceId: string;
  name: string;
  startAge: number;
  endAge: number;
  annualAmount: number;
}

export interface IncomeAssumptions {
  coastPhase: CoastIncome;
  retirementPhase: RetirementIncome;
  socialSecurity: SocialSecurity;
  otherIncomeSources: OtherIncomeSource[];
}

export interface ExpenseCategory {
  categoryId: string;
  name: string;
  inflationRate?: number;
}

export interface ExpenseAssumptions {
  globalInflationRate: number;
  expenseCategories: ExpenseCategory[];
}

export interface OneTimeEvent {
  eventId: string;
  name: string;
  eventType: EventType;
  age: number;
  amount: number;
  applyInflation: boolean;
}

export interface HousingTransition {
  enabled: boolean;
  targetAge: number;
  salePrice: number;
  replacementCost: number;
  transactionCostsModeled: boolean;
}

export interface ProjectionSettings {
  rateOfReturnByPhase: {
    ACCUMULATION: number;
    COAST: number;
    RETIREMENT: number;
  };
  analysisTimeframe: {
    startYear: number;
    endYear: number;
  };
  withdrawalOrder: AccountType[];
  projectionYears: number[];
}

export interface PersistencePolicy {
  snapshotExportMode: SnapshotExportMode;
  storagePath: string;
}

export interface CoastFirePlan {
  planId: string;
  label: string;
  version: number;
  createdAt: string;
  updatedAt: string;
  ownerProfile: OwnerProfile;
  phases: PhaseSettings;
  accounts: Accounts;
  incomeAssumptions: IncomeAssumptions;
  expenseAssumptions: ExpenseAssumptions;
  events: OneTimeEvent[];
  housingTransition: HousingTransition;
  projectionSettings: ProjectionSettings;
  persistencePolicy: PersistencePolicy;
}

export interface AnnualProjection {
  year: number;
  age: number;
  phase: PhaseType;
  socialSecurityIncome: number;
  salaryNeed: number;
  salaryIncome: number;
  investmentInterest: number;
  gap: number;
  remainingPrincipal: number;
  events: OneTimeEvent[];
}
