# Glossary

## Phases
- **Accumulation Phase**: The career period focused on maximizing savings and investment contributions, generally ages 22-49 in the base plan.
- **Coast Phase**: The period when earned income can drop substantially because existing assets are projected to grow to the retirement target without additional contributions; typically ages 50-65.
- **Retirement Phase**: The period when portfolio withdrawals fully cover lifestyle expenses; begins once earned income ceases (default age 66 onward).

## Financial Terms
- **Coast FIRE**: A financial independence strategy where an individual accumulates sufficient assets early enough that those assets can grow to support retirement with minimal additional contributions, allowing reduced work later.
- **COLA (Cost of Living Adjustment)**: Annual percentage increase applied to Social Security benefits to keep pace with inflation (default 2.5%).
- **Deterministic Projection**: A financial model that uses fixed growth and inflation rates without stochastic variation.
- **Withdrawal Order**: The sequence in which account types are tapped to meet spending needs: Non-qualified, Qualified, HSA, Roth, Accumulated Life Insurance, Cash, Lifestyle Assets.
- **One-time Event**: A dated expense or inflow (e.g., major purchase, repair) recorded separately from recurring expenses.

## Data & Modeling
- **Asset Inventory**: The list of user-specified asset accounts and balances used to initialize and update projections.
- **Liability Schedule**: The set of user-entered debts including balances, interest rates, payment cadence, and payoff horizon.
- **Projection Table**: The annual view summarizing income sources, expense totals, investment returns, funding gaps, and remaining principal for each year of the plan.
- **Scenario Slider**: An interactive control on the summary page allowing quick adjustments to key assumptions (e.g., coast start age, inflation rate, rates of return).

## Application Assets and Concepts
- **Plan File**: The persisted data store containing all user inputs, assumptions, and projection parameters.
- **Snapshot Export**: Optional operation that saves the current asset and liability lists to a timestamped copy during plan saves.

## Development Practices
- **Specification by Example**: Requirements technique using concrete examples (Given-When-Then) to describe expected user and application behaviors.
