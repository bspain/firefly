Feature: Configure Coast FIRE plan phases

  Scenario: Establish the default phase boundaries
    Given a user aged 48 without a Coast FIRE plan
    When the user creates a plan
    Then the accumulation phase ends at age 49 and the coast phase begins at age 50
    And the coast phase ends at age 65 and the retirement phase begins at age 66

  Scenario: Adjust the target coast start age
    Given a user aged 48 with a Coast FIRE plan
    And the plan defines three phases: Accumulation (ages 22-49), Coast (ages 50-65), Retirement (ages 66-100)
    When the user sets the target coast age to 52
    Then the plan recomputes phase boundaries so accumulation ends at 51 and coast begins at 52
    And projections update in the annual timeline to reflect two additional accumulation years
