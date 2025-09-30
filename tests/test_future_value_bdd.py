"""
BDD step definitions for future value calculation feature
"""

import pytest
from pytest_bdd import given, when, then, scenarios
from firefly.calculations.financial_calculator import FinancialCalculator


# Load scenarios from feature file
scenarios('features/future_value.feature')


@pytest.fixture
def calculator():
    """Fixture providing a FinancialCalculator instance."""
    return FinancialCalculator()


@pytest.fixture
def calculation_context():
    """Fixture providing context for calculation parameters and results."""
    return {}


@given('the financial calculation service is available to a developer')
def financial_calculation_service_available(calculator):
    """Ensure the financial calculation service is available."""
    assert calculator is not None
    assert hasattr(calculator, 'future_value')


@when('the developer calls a function to calculate the future value of a present sum')
def call_future_value_function(calculation_context):
    """Initialize the function call context."""
    calculation_context['function_called'] = True


@when('the developer provides a present value of <present_value>')
@when('the developer provides a present value of 1000')
@when('the developer provides a present value of 5000') 
@when('the developer provides a present value of 0')
@when('the developer provides a present value of -1000')
def set_present_value(calculation_context, present_value=None):
    """Set the present value parameter."""
    if present_value is not None:
        calculation_context['present_value'] = float(present_value)
    elif 'present_value' not in calculation_context:
        # Extract from step text - this will be called by individual step methods
        pass


@when('the developer provides the interest rate per period of <rate>')
@when('the developer provides the interest rate per period of 0.07')
@when('the developer provides the interest rate per period of 0')
@when('the developer provides the interest rate per period of 0.05')
def set_interest_rate(calculation_context, rate=None):
    """Set the interest rate parameter."""
    if rate is not None:
        calculation_context['rate'] = float(rate)


@when('the developer provides the number of periods of <periods>')
@when('the developer provides the number of periods of 10')
@when('the developer provides the number of periods of 1')
@when('the developer provides the number of periods of -5')
def set_periods(calculation_context, periods=None):
    """Set the number of periods parameter."""
    if periods is not None:
        calculation_context['periods'] = int(periods)


# Specific step implementations for scenarios
@when('the developer provides a present value of 1000')
def set_present_value_1000(calculation_context):
    calculation_context['present_value'] = 1000.0


@when('the developer provides a present value of 5000')
def set_present_value_5000(calculation_context):
    calculation_context['present_value'] = 5000.0


@when('the developer provides a present value of 0')
def set_present_value_0(calculation_context):
    calculation_context['present_value'] = 0.0


@when('the developer provides a present value of -1000')
def set_present_value_negative_1000(calculation_context):
    calculation_context['present_value'] = -1000.0


@when('the developer provides the interest rate per period of 0.07')
def set_rate_007(calculation_context):
    calculation_context['rate'] = 0.07


@when('the developer provides the interest rate per period of 0')
def set_rate_0(calculation_context):
    calculation_context['rate'] = 0.0


@when('the developer provides the interest rate per period of 0.05')
def set_rate_005(calculation_context):
    calculation_context['rate'] = 0.05


@when('the developer provides the number of periods of 10')
def set_periods_10(calculation_context):
    calculation_context['periods'] = 10


@when('the developer provides the number of periods of 1')
def set_periods_1(calculation_context):
    calculation_context['periods'] = 1


@when('the developer provides the number of periods of -5')
def set_periods_negative_5(calculation_context):
    calculation_context['periods'] = -5


@then('the financial calculation service returns the future value of <expected_value>')
@then('the financial calculation service returns the future value of 1967.15')
@then('the financial calculation service returns the future value of 1000')
@then('the financial calculation service returns the future value of 5250')
@then('the financial calculation service returns the future value of 0')
def check_future_value_result(calculator, calculation_context, expected_value=None):
    """Verify the future value calculation result."""
    present_value = calculation_context['present_value']
    rate = calculation_context['rate']
    periods = calculation_context['periods']
    
    result = calculator.future_value(present_value, rate, periods)
    
    if expected_value is not None:
        expected = float(expected_value)
    else:
        # Extract expected value from step text
        expected = calculation_context.get('expected_value')
    
    assert abs(result - expected) < 0.01, f"Expected {expected}, got {result}"


@then('the financial calculation service returns the future value of 1967.15')
def check_future_value_1967_15(calculator, calculation_context):
    """Verify future value result is 1967.15."""
    present_value = calculation_context['present_value']
    rate = calculation_context['rate'] 
    periods = calculation_context['periods']
    
    result = calculator.future_value(present_value, rate, periods)
    expected = 1967.15
    
    assert abs(result - expected) < 0.01, f"Expected {expected}, got {result}"


@then('the financial calculation service returns the future value of 1000')
def check_future_value_1000(calculator, calculation_context):
    """Verify future value result is 1000."""
    present_value = calculation_context['present_value']
    rate = calculation_context['rate']
    periods = calculation_context['periods']
    
    result = calculator.future_value(present_value, rate, periods)
    expected = 1000.0
    
    assert abs(result - expected) < 0.01, f"Expected {expected}, got {result}"


@then('the financial calculation service returns the future value of 5250')
def check_future_value_5250(calculator, calculation_context):
    """Verify future value result is 5250."""
    present_value = calculation_context['present_value']
    rate = calculation_context['rate']
    periods = calculation_context['periods']
    
    result = calculator.future_value(present_value, rate, periods)
    expected = 5250.0
    
    assert abs(result - expected) < 0.01, f"Expected {expected}, got {result}"


@then('the financial calculation service returns the future value of 0')
def check_future_value_0(calculator, calculation_context):
    """Verify future value result is 0."""
    present_value = calculation_context['present_value']
    rate = calculation_context['rate']
    periods = calculation_context['periods']
    
    result = calculator.future_value(present_value, rate, periods)
    expected = 0.0
    
    assert abs(result - expected) < 0.01, f"Expected {expected}, got {result}"


@then('the financial calculation service raises a ValueError with message "<message>"')
@then('the financial calculation service raises a ValueError with message "Present value cannot be negative"')
@then('the financial calculation service raises a ValueError with message "Number of periods cannot be negative"')
def check_value_error(calculator, calculation_context, message=None):
    """Verify that a ValueError is raised with the expected message."""
    present_value = calculation_context['present_value']
    rate = calculation_context['rate']
    periods = calculation_context['periods']
    
    with pytest.raises(ValueError) as exc_info:
        calculator.future_value(present_value, rate, periods)
    
    if message:
        assert str(exc_info.value) == message
    else:
        # Check for specific error messages based on context
        if present_value < 0:
            assert str(exc_info.value) == "Present value cannot be negative"
        elif periods < 0:
            assert str(exc_info.value) == "Number of periods cannot be negative"