"""
BDD step definitions for future value calculation feature
"""

import pytest
from pytest_bdd import given, scenarios, then, when

from firefly.calculations.financial_calculator import FinancialCalculator

# Load scenarios from feature file
scenarios("features/future_value.feature")


@pytest.fixture
def calculator():
    """Fixture providing a FinancialCalculator instance."""
    return FinancialCalculator()


@pytest.fixture
def calculation_context():
    """Fixture providing context for calculation parameters and results."""
    return {}


@given("the financial calculation service is available to a developer")
def financial_calculation_service_available(calculator):
    """Ensure the financial calculation service is available."""
    assert calculator is not None
    assert hasattr(calculator, "future_value")


@when("the developer calls a function to calculate the future value of a present sum")
def call_future_value_function(calculation_context):
    """Initialize the function call context."""
    calculation_context["function_called"] = True


@when("the developer provides a present value of 1000")
def set_present_value_1000(calculation_context):
    """Set present value to 1000."""
    calculation_context["present_value"] = 1000.0


@when("the developer provides the interest rate per period of 0.07")
def set_rate_007(calculation_context):
    """Set interest rate to 0.07."""
    calculation_context["rate"] = 0.07


@when("the developer provides the number of periods of 10")
def set_periods_10(calculation_context):
    """Set periods to 10."""
    calculation_context["periods"] = 10


@then("the financial calculation service returns the future value of 1967.15")
def check_future_value_1967_15(calculator, calculation_context):
    """Verify future value result is 1967.15."""
    present_value = calculation_context["present_value"]
    rate = calculation_context["rate"]
    periods = calculation_context["periods"]

    result = calculator.future_value(present_value, rate, periods)
    expected = 1967.15

    assert abs(result - expected) < 0.01, f"Expected {expected}, got {result}"
