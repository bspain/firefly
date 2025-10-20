Feature: Configure Coast FIRE plan phases
  Background:
    Given a user aged 48 with a Coast FIRE plan
    And the plan defines three phases: Accumulation (ages 22-49), Coast (ages 50-65), Retirement (ages 66-100)
    And the plan contains the sample data from the existing spreadsheet
  Scenario: Establish the default phase boundaries
    When the user creates a new plan
    Then the accumulation phase ends at age 49 and the coast phase begins at age 50
    And the coast phase ends at age 65 and the retirement phase begins at age 66
  Scenario: Adjust the target coast start age
    When the user sets the target coast age to 52
    Then the plan recomputes phase boundaries so accumulation ends at 51 and coast begins at 52
    And projections update in the annual timeline to reflect two additional accumulation years

Feature: Manage asset and liability inventories
  Background:
    Given a plan with the following assets:
      | type             | amount  |
      | Qualified        | 1000000 |
      | Roth             | 225000  |
      | Non-qualified    | 65000   |
      | Cash             | 30000   |
    And the following liabilities:
      | name              | balance | rate | payment cadence |
      | Primary Mortgage  | 130000  | 4.0% | monthly         |
      | Automobile Loan   | 28000   | 5.0% | monthly         |
  Scenario: Update asset balances twice per month
    When the user edits the plan on the 1st of the month and updates the qualified asset balance to 1005000
    And the user returns on the 15th and updates the qualified asset balance to 1010000
    Then both updates persist in the plan file without requiring historical versioning
  Scenario: Add a new liability mid-plan
    When the user adds a "Home Improvement Loan" liability with a 12000 balance, 6.5% interest, and monthly payments
    Then the plan stores the liability details
    And the annual projection includes the payoff horizon implied by the payment schedule

Feature: Capture income assumptions
  Background:
    Given the plan models Social Security benefits starting at age 70 with a 2.5% annual COLA
    And the plan records no other external income sources by default
  Scenario: Apply Coast-phase income shortfall rules
    When the user sets coast-phase salary need to 125000 and coast-phase salary income to 60000
    And the projection finds a 65000 annual shortfall during coast years
    Then the plan withdraws from Roth contributions first to fill the shortfall, tracking contribution vs earnings
    And any additional withdrawal required uses other accounts while applying a 10% early withdrawal penalty
  Scenario: Adjust Social Security COLA
    When the user changes the Social Security COLA assumption to 3.0%
    Then the projected Social Security income column grows at 3.0% annually starting at age 70

Feature: Model expenses and one-time events
  Background:
    Given lifestyle and medical expenses inflate at the global inflation rate (default 2.5%)
  Scenario: Record a one-time expense
    When the user creates an event named "Roof Replacement" costing 15000 in 2032
    Then the annual projection shows a 15000 expense in 2032 adjusted for inflation to that year
  Scenario: Maintain static expense structure
    When the user reviews expenses beyond age 70
    Then lifestyle and medical expenses persist without automatic decreases unless the user edits them

Feature: Execute housing transition
  Background:
    Given the plan includes a primary residence valued at 650000 and a target downsizing event during the coast start year
  Scenario: Capture sale and replacement purchase
    When the user sets the residence sale price to 650000, target sale year to 2027, and replacement purchases totaling 400000
    Then the projection adds an inflow of 650000 in 2027 from the sale
    And subtracts 400000 in 2027 to account for cash purchases of the replacement residence and travel trailer
    And omits transaction cost modeling in the first version

Feature: Apply withdrawal ordering
  Background:
    Given the withdrawal order is Non-qualified, Qualified, HSA, Roth, Accumulated Life Insurance, Cash, Lifestyle Assets
  Scenario: Withdraw across multiple account types
    When the retirement-phase expenses exceed income by 80000 in 2035
    Then the plan deducts from remaining non-qualified balances first
    And continues down the withdrawal order only if prior account types are exhausted

Feature: Present annual projection table
  Background:
    Given the plan spans calendar years 2026 through 2078
  Scenario: Display yearly projection metrics
    When the user opens the plan summary page
    Then the table lists each year with columns for Social Security income, salary need, investment interest, gap, and remaining principal balance
    And the table reflects the latest asset balances, expenses, and event adjustments
  Scenario: Recalculate after slider adjustments
    Given the plan summary page exposes sliders for coast start age, inflation rate, and rate-of-return assumptions per phase
    When the user adjusts the coast start age slider from 50 to 52
    Then the annual projection table updates immediately with the recomputed values

Feature: Maintain plan data
  Background:
    Given users can save the plan file locally and optionally export asset/liability snapshots
  Scenario: Save plan changes with export prompt
    When the user saves modifications to assets or liabilities
    Then the application prompts the user to export the current asset and liability list to a timestamped copy before finalizing the save
  Scenario: Persist user-defined plan parameters
    When the user closes the application and reopens it later
    Then all plan phases, assets, liabilities, income assumptions, events, and slider settings load from the saved file
