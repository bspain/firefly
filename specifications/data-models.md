# Data Models

This document describes the canonical schema for a Coast FIRE plan file. The schema is expressed as logical data structures with enumerations, followed by a full sample dataset that aligns with the current requirements and glossary.

## Overview
- Plans persist as a single JSON document (or equivalent map) per user scenario.
- All monetary amounts are stored in present-day nominal dollars; inflation is applied during projections.
- Ages are integers representing the user's age at the end of the calendar year.
- Dates follow ISO 8601 (`YYYY-MM-DD`) when specific calendar dates are required.

## Enumerations
| Name | Values | Notes |
| --- | --- | --- |
| PhaseType | `ACCUMULATION`, `COAST`, `RETIREMENT` | Defines lifecycle segments.
| AccountType | `QUALIFIED`, `ROTH`, `NON_QUALIFIED`, `CASH`, `LIFESTYLE`, `INSURANCE`, `HSA`, `OTHER` | Asset categories.
| LiabilityCadence | `MONTHLY`, `QUARTERLY`, `ANNUAL`, `OTHER` | Payment frequency for liabilities.
| EventType | `EXPENSE`, `INFLOW` | Distinguishes cash outflows vs inflows.
| SnapshotExportMode | `PROMPT`, `ALWAYS`, `NEVER` | Controls export prompt behavior.

## Entity Definitions

### Plan
| Field | Type | Description |
| --- | --- | --- |
| `planId` | string | Unique identifier within the application.
| `label` | string | Human-friendly name.
| `version` | integer | Incremented on schema changes.
| `createdAt` | date | Plan creation timestamp.
| `updatedAt` | date | Last modification timestamp.
| `ownerProfile` | OwnerProfile | Core demographics.
| `phases` | PhaseSettings | Phase boundaries and policies.
| `accounts` | Accounts | Asset and liability inventories.
| `incomeAssumptions` | IncomeAssumptions | Earned income and benefits rules.
| `expenseAssumptions` | ExpenseAssumptions | Recurring costs and inflation.
| `events` | OneTimeEvent[] | Explicit dated inflows or expenses.
| `housingTransition` | HousingTransition | Downsizing scenario settings.
| `projectionSettings` | ProjectionSettings | Return rates and modeling knobs.
| `persistencePolicy` | PersistencePolicy | Save and export preferences.

### OwnerProfile
| Field | Type | Description |
| --- | --- | --- |
| `currentAge` | integer | User age at `updatedAt`.
| `targetRetirementAge` | integer | Desired retirement start age.
| `planningHorizonAge` | integer | Expected age of death for projections.
| `baseYear` | integer | Calendar year for `currentAge` (e.g., 2025).

### PhaseSettings
| Field | Type | Description |
| --- | --- | --- |
| `phases` | Phase[] | Ordered by start age.

#### Phase
| Field | Type | Description |
| --- | --- | --- |
| `phaseType` | PhaseType | Lifecycle label.
| `startAge` | integer | Inclusive start age.
| `endAge` | integer | Inclusive end age.
| `contributionPolicy` | ContributionPolicy | Contribution rules for this phase.

#### ContributionPolicy
| Field | Type | Description |
| --- | --- | --- |
| `status` | `ACTIVE` or `PAUSED` | Indicates whether contributions occur.
| `annualContribution` | number | Amount contributed if status is `ACTIVE`.
| `sourceAccountIds` | string[] | Asset accounts receiving contributions.

### Accounts
| Field | Type | Description |
| --- | --- | --- |
| `assets` | AssetAccount[] | Asset inventory.
| `liabilities` | Liability[] | Liability inventory.

#### AssetAccount
| Field | Type | Description |
| --- | --- | --- |
| `accountId` | string | Unique identifier.
| `name` | string | Display label.
| `accountType` | AccountType | Category aligned with withdrawal order.
| `currentBalance` | number | Balance at `updatedAt`.
| `costBasis` | number | Original contributions or basis (optional).
| `allowRothContributionWithdrawals` | boolean | Indicates if Roth contributions can be accessed.
| `metadata` | object | Provider-specific or user notes.

#### Liability
| Field | Type | Description |
| --- | --- | --- |
| `liabilityId` | string | Unique identifier.
| `name` | string | Display label.
| `balance` | number | Principal outstanding at `updatedAt`.
| `interestRate` | number | Annual percentage rate (decimal form).
| `paymentCadence` | LiabilityCadence | Frequency of regular payments.
| `paymentAmount` | number | Regular payment amount.
| `payoffDate` | date | Expected payoff date if known.
| `metadata` | object | Additional lender notes.

### IncomeAssumptions
| Field | Type | Description |
| --- | --- | --- |
| `coastPhase` | CoastIncome | Earned income vs need during coast.
| `retirementPhase` | RetirementIncome | Income sources after coast.
| `socialSecurity` | SocialSecurity | Benefit start and growth.
| `otherIncomeSources` | OtherIncomeSource[] | Optional additional inflows (default empty).

#### CoastIncome
| Field | Type | Description |
| --- | --- | --- |
| `annualNeed` | number | Total desired spending during coast.
| `annualIncome` | number | Expected earned income.
| `shortfallPolicy` | ShortfallPolicy | Withdrawal rules for deficits.

#### ShortfallPolicy
| Field | Type | Description |
| --- | --- | --- |
| `primarySource` | AccountType | First account type tapped (default `ROTH`).
| `trackRothContributions` | boolean | Whether to differentiate contributions vs earnings.
| `earlyWithdrawalPenaltyRate` | number | Penalty applied to non-exempt withdrawals (decimal form).

#### RetirementIncome
| Field | Type | Description |
| --- | --- | --- |
| `annualNeed` | number | Lifestyle spending requirement in retirement.
| `medicalNeed` | number | Annual medical spending.

#### SocialSecurity
| Field | Type | Description |
| --- | --- | --- |
| `startAge` | integer | Age when benefits commence.
| `baseAnnualBenefit` | number | Benefit at start age before COLA.
| `colaRate` | number | Annual COLA percentage (decimal form).

#### OtherIncomeSource
| Field | Type | Description |
| --- | --- | --- |
| `sourceId` | string | Identifier.
| `name` | string | Label.
| `startAge` | integer | Age when income begins.
| `endAge` | integer | Age when income ends.
| `annualAmount` | number | Amount per year.

### ExpenseAssumptions
| Field | Type | Description |
| --- | --- | --- |
| `globalInflationRate` | number | Default inflation applied to expenses (decimal form).
| `expenseCategories` | ExpenseCategory[] | Optional sub-category overrides.

#### ExpenseCategory
| Field | Type | Description |
| --- | --- | --- |
| `categoryId` | string | Identifier.
| `name` | string | Category label.
| `inflationRate` | number | Override rate (optional).

### OneTimeEvent
| Field | Type | Description |
| --- | --- | --- |
| `eventId` | string | Unique identifier.
| `name` | string | Description.
| `eventType` | EventType | Expense or inflow.
| `age` | integer | User age when event occurs.
| `amount` | number | Nominal amount at `age`.
| `applyInflation` | boolean | Whether to inflate from base year.

### HousingTransition
| Field | Type | Description |
| --- | --- | --- |
| `enabled` | boolean | Whether the transition is modeled.
| `targetAge` | integer | Age when sale occurs.
| `salePrice` | number | Expected inflow from sale.
| `replacementCost` | number | Combined outflow for new residence and trailer.
| `transactionCostsModeled` | boolean | First version defaults to `false`.

### ProjectionSettings
| Field | Type | Description |
| --- | --- | --- |
| `rateOfReturnByPhase` | object | Map of `PhaseType` to deterministic rate.
| `analysisTimeframe` | object | Range of calendar years (derived from ages and base year).
| `withdrawalOrder` | AccountType[] | Ordered list controlling draw-down sequence.
| `projectionYears` | integer[] | Explicit list of projection years (optional cache).

### PersistencePolicy
| Field | Type | Description |
| --- | --- | --- |
| `snapshotExportMode` | SnapshotExportMode | Controls export prompting.
| `storagePath` | string | File location hint.

## Sample Dataset

```json
{
  "planId": "sample-coast-fire-001",
  "label": "Base Coast FIRE Scenario",
  "version": 1,
  "createdAt": "2025-10-01",
  "updatedAt": "2025-10-25",
  "ownerProfile": {
    "currentAge": 48,
    "targetRetirementAge": 60,
    "planningHorizonAge": 100,
    "baseYear": 2025
  },
  "phases": {
    "phases": [
      {
        "phaseType": "ACCUMULATION",
        "startAge": 22,
        "endAge": 49,
        "contributionPolicy": {
          "status": "ACTIVE",
          "annualContribution": 38000,
          "sourceAccountIds": ["asset-qualified"]
        }
      },
      {
        "phaseType": "COAST",
        "startAge": 50,
        "endAge": 65,
        "contributionPolicy": {
          "status": "PAUSED",
          "annualContribution": 0,
          "sourceAccountIds": []
        }
      },
      {
        "phaseType": "RETIREMENT",
        "startAge": 66,
        "endAge": 100,
        "contributionPolicy": {
          "status": "PAUSED",
          "annualContribution": 0,
          "sourceAccountIds": []
        }
      }
    ]
  },
  "accounts": {
    "assets": [
      {
        "accountId": "asset-qualified",
        "name": "Qualified Investment Accounts",
        "accountType": "QUALIFIED",
        "currentBalance": 1000000,
        "costBasis": 680000,
        "allowRothContributionWithdrawals": false,
        "metadata": {
          "notes": "401k, IRA, pension combined"
        }
      },
      {
        "accountId": "asset-roth",
        "name": "Roth Accounts",
        "accountType": "ROTH",
        "currentBalance": 225000,
        "costBasis": 185000,
        "allowRothContributionWithdrawals": true,
        "metadata": {}
      },
      {
        "accountId": "asset-insurance",
        "name": "Accumulated Life Insurance Value",
        "accountType": "INSURANCE",
        "currentBalance": 100000,
        "costBasis": 75000,
        "allowRothContributionWithdrawals": false,
        "metadata": {}
      },
      {
        "accountId": "asset-non-qualified",
        "name": "Taxable Brokerage",
        "accountType": "NON_QUALIFIED",
        "currentBalance": 65000,
        "costBasis": 50000,
        "allowRothContributionWithdrawals": false,
        "metadata": {}
      },
      {
        "accountId": "asset-cash",
        "name": "Cash Accounts",
        "accountType": "CASH",
        "currentBalance": 30000,
        "costBasis": 30000,
        "allowRothContributionWithdrawals": false,
        "metadata": {}
      },
      {
        "accountId": "asset-hsa",
        "name": "Health Savings Accounts",
        "accountType": "HSA",
        "currentBalance": 30000,
        "costBasis": 30000,
        "allowRothContributionWithdrawals": false,
        "metadata": {}
      },
      {
        "accountId": "asset-lifestyle",
        "name": "Primary Residence",
        "accountType": "LIFESTYLE",
        "currentBalance": 650000,
        "costBasis": 420000,
        "allowRothContributionWithdrawals": false,
        "metadata": {
          "notes": "Sold during housing transition"
        }
      }
    ],
    "liabilities": [
      {
        "liabilityId": "liability-mortgage",
        "name": "Primary Mortgage",
        "balance": 130000,
        "interestRate": 0.04,
        "paymentCadence": "MONTHLY",
        "paymentAmount": 1400,
        "payoffDate": "2034-06-01",
        "metadata": {}
      },
      {
        "liabilityId": "liability-auto",
        "name": "Automobile Loan",
        "balance": 28000,
        "interestRate": 0.05,
        "paymentCadence": "MONTHLY",
        "paymentAmount": 550,
        "payoffDate": "2028-09-01",
        "metadata": {}
      },
      {
        "liabilityId": "liability-card",
        "name": "Credit Card",
        "balance": 3000,
        "interestRate": 0.21,
        "paymentCadence": "MONTHLY",
        "paymentAmount": 200,
        "payoffDate": "2026-02-01",
        "metadata": {}
      }
    ]
  },
  "incomeAssumptions": {
    "coastPhase": {
      "annualNeed": 125000,
      "annualIncome": 60000,
      "shortfallPolicy": {
        "primarySource": "ROTH",
        "trackRothContributions": true,
        "earlyWithdrawalPenaltyRate": 0.10
      }
    },
    "retirementPhase": {
      "annualNeed": 125000,
      "medicalNeed": 17000
    },
    "socialSecurity": {
      "startAge": 70,
      "baseAnnualBenefit": 55000,
      "colaRate": 0.025
    },
    "otherIncomeSources": []
  },
  "expenseAssumptions": {
    "globalInflationRate": 0.025,
    "expenseCategories": []
  },
  "events": [
    {
      "eventId": "event-roof-replacement",
      "name": "Roof Replacement",
      "eventType": "EXPENSE",
      "age": 55,
      "amount": 15000,
      "applyInflation": true
    }
  ],
  "housingTransition": {
    "enabled": true,
    "targetAge": 50,
    "salePrice": 650000,
    "replacementCost": 400000,
    "transactionCostsModeled": false
  },
  "projectionSettings": {
    "rateOfReturnByPhase": {
      "ACCUMULATION": 0.10,
      "COAST": 0.06,
      "RETIREMENT": 0.04
    },
    "analysisTimeframe": {
      "startYear": 2026,
      "endYear": 2078
    },
    "withdrawalOrder": [
      "NON_QUALIFIED",
      "QUALIFIED",
      "HSA",
      "ROTH",
      "INSURANCE",
      "CASH",
      "LIFESTYLE"
    ],
    "projectionYears": []
  },
  "persistencePolicy": {
    "snapshotExportMode": "PROMPT",
    "storagePath": "~/Documents/firefly/sample-coast-fire-001.json"
  }
}
```
