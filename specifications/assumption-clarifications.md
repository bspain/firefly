# Assumption Clarifications

Please provide answers to the questions below. Your responses will help refine the requirements document.

## Financial Timeline
- How do you define the phases of the plan (Accumulation, Coast, Retirement)?
Accumulation: The phase of a persons career where they are primarily working to accumulate wealth and make contributions to investment and retirement accounts.  In a Coast FIRE plan, this is typically from the ages of 22-50.
Coast: The phase when a person will continue to work, but can do so at a large reduction in salary.  A persons net worth should be high enough that an occupation in this phase can be more for enjoyment and personal fulfillment purposes instead of high accumulation of wealth.  A person may leverage some of their portfolio earnings to offset some costs during the Coast phase should they be unable to reduce their expenses.  In a Coast FIRE plan, this is typically from the ages of 50-65.
Retirement: A phase where a person has enough accumulated net worth to draw all living expenses from their portfolio and investment returns to not need any form of occupational income.

- When does the accumulation phase end and the coast phase begin in the base scenario?
Answer to this question can be found in the previous answer

- During the coast phase, do you plan to make ongoing contributions? If so, at what cadence and from which accounts?
In a typical Coast FIRE plan, one is not making ongoing contributions to their portfolio during the coast phase.

- At what age do withdrawals begin from each account type (qualified, Roth, taxable, HSA)?
Withdrawl plans will occur in the following order: Non-Qualified, Qualified, HSA, Roth, Accumulated Life Insurance, Cash Accounts, Lifestyle Assets

Note: It is NOT a goal of the Coast FIRE application to model the full complexity of a retirement plan.  It will be assumed that any actual retirement withdrawl strategy would be perfomed with the aid of a qualified financial planner and tax services professional.


## Income & Benefits
- Should Social Security benefits begin precisely at age 70? Do you expect cost-of-living adjustments (COLA)?
Yes, the plan can expect COLA to apply to Social Security benefits at a rate of 2.5% annual.  This rate can be adjusted in the application as part of visualizing changes to the plan.- Are there other income sources to include (part-time work, rental income, annuities)?

- During the coast phase, how should income shortfalls be covered (specific accounts, proportional drawdowns, new debt)?
Coast Fire plans should be built with a minimal shortfall during the Coast phase.  In the event that shortfalls are needed, the first source should be withdrawing from contributions to Roth (not from earnings until after 59.5 years of age).  The application should allow the user to enter the details of their contributions to any Roth accounts for this purpose.
For the version of the application, it can assume that any withdrawl from any other source will incur a 10% early withdrawl penalty.

## Expenses & Inflation
- Should lifestyle expenses and medical expenses use different inflation rates? If so, what rates should we model?
The first version of the application should assume the same inflation rate.

- Are there major one-time expenses to account for (e.g., travel, home repairs, college support)?
The application should allow the user to specify events (name of the event, the date, and the cost) of major one-time expenses.

- Do any expenses decrease or end at certain ages (e.g., mortgage payoff, insurance premiums)?
The first version of the application should not be concerned with expense decreases

## Housing Transition
- What is the expected sale price of the current residence and the anticipated closing year?
The application should allow this to be specified as part of building the plan.

- Which transaction costs (agent fees, taxes, moving) should we model for the sale and purchase?
The first version of the application should not be concerned with modeling transaction costs.

- Will the replacement residence and travel trailer be purchased outright? If financed, what loan terms apply?
The default behavior of the application should assume that any replacement of the primary residence will be paid for in cash.

## Liabilities
- For each liability, what are the interest rate, payment schedule, and payoff horizon?
The application should allow the user to specify that as part of the plan.
- Do you plan to maintain these liabilities during the coast phase, or target payoff before retirement?
See former question.

## Investment Assumptions
- Should investment returns be modeled as deterministic averages, or do you want variability (e.g., Monte Carlo bands) in a later version?
The first version of the application can be modeled as deterministic.  Future versions may allow for variability simulations.
- Do you want to model account-specific fees or tax drag?
This is not necessary in the first version of the application
- How should asset allocation shift over time, if at all?
The application should not be concerned about this in the first version.

## Scenario Management
- Do you want to save and compare multiple scenarios within the app?
This will not be a feature of the first version of the app, but it can be expected to be part of a version soon after the first.
- Should the tool track revisions or provide version history for scenarios?
This will not be a feature of the first version of the app, but it can be expected to be part of a version soon after the first.

## Data Maintenance
- How frequently will you update asset balances and liabilities (monthly, quarterly)?
Users can expect to update twice a month.  A future version of the app may allow for the user to provide connectivity to accounts to retrive asset and liability information.
- Do you want to import/export data via CSV or other formats in the initial version?
The first version should allow the user to createa a list of assets and liabilities, and then provide initial values.  The user must be able to add and remove liabilities from the plan in subsequent sessions with the application.  The application file format does not need to maintain a history of previous assets and liabilities, but should present the user an oppertunity to save a copy of the asset and liability information anytime they are about to save changes in the asset and liability list.

## Other Considerations
- Are there legal or tax jurisdictions we should assume for calculations?
Not for the first version
- Should the app support “what-if” toggles for early retirement, disability, or survivor benefits?
Not for the first version
- Are there accessibility or security requirements we should note at this stage?
Not for the first version