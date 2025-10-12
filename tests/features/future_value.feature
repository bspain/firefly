Feature: Financial Calculation Service - Future Value
    As a developer using the Firefly financial calculation service
    I want to calculate the future value of a present sum
    So that I can build retirement planning and investment projection features

    Background:
        Given the financial calculation service is available to a developer

    Scenario: Calculate future value with positive interest rate
        When the developer calls a function to calculate the future value of a present sum
        And the developer provides a present value of 1000
        And the developer provides the interest rate per period of 0.07
        And the developer provides the number of periods of 10
        Then the financial calculation service returns the future value of 1967.15