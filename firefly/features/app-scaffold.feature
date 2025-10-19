Feature: Application scaffold metadata
  The desktop application should expose core metadata so that
  renderer components and acceptance tests can verify the scaffold.

  Scenario: Firefly metadata is available to the renderer
    Given the application configuration is loaded
    When I inspect the exposed metadata
    Then the application name is "Firefly Planner"
    And the product name is "Firefly Planner"
