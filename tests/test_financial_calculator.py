"""
Unit tests for FinancialCalculator
"""

import pytest
import math
from firefly.calculations.financial_calculator import FinancialCalculator


class TestFinancialCalculator:
    """Test suite for FinancialCalculator class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.calculator = FinancialCalculator()
    
    def test_future_value_basic_calculation(self):
        """Test basic future value calculation with typical values."""
        # Test case: $1000 at 7% for 10 years should equal $1967.15
        result = self.calculator.future_value(1000, 0.07, 10)
        expected = 1000 * (1.07 ** 10)
        assert abs(result - expected) < 0.01
        assert abs(result - 1967.15) < 0.01
    
    def test_future_value_zero_interest_rate(self):
        """Test future value calculation with zero interest rate."""
        # With 0% interest, future value should equal present value
        result = self.calculator.future_value(1000, 0, 10)
        assert result == 1000
    
    def test_future_value_zero_periods(self):
        """Test future value calculation with zero periods."""
        # With 0 periods, future value should equal present value
        result = self.calculator.future_value(1000, 0.07, 0)
        assert result == 1000
    
    def test_future_value_one_period(self):
        """Test future value calculation with one period."""
        # $5000 at 5% for 1 period should equal $5250
        result = self.calculator.future_value(5000, 0.05, 1)
        expected = 5000 * 1.05
        assert abs(result - expected) < 0.01
        assert abs(result - 5250) < 0.01
    
    def test_future_value_zero_present_value(self):
        """Test future value calculation with zero present value."""
        # Zero present value should always result in zero future value
        result = self.calculator.future_value(0, 0.07, 10)
        assert result == 0
    
    def test_future_value_high_interest_rate(self):
        """Test future value calculation with high interest rate."""
        # Test with 50% annual return for 5 years
        result = self.calculator.future_value(1000, 0.5, 5)
        expected = 1000 * (1.5 ** 5)
        assert abs(result - expected) < 0.01
    
    def test_future_value_fractional_interest_rate(self):
        """Test future value calculation with fractional interest rate."""
        # Test with 1.5% quarterly rate for 8 quarters (2 years)
        result = self.calculator.future_value(10000, 0.015, 8)
        expected = 10000 * (1.015 ** 8)
        assert abs(result - expected) < 0.01
    
    def test_future_value_large_number_of_periods(self):
        """Test future value calculation with large number of periods."""
        # Test long-term compounding: 30 years
        result = self.calculator.future_value(1000, 0.07, 30)
        expected = 1000 * (1.07 ** 30)
        assert abs(result - expected) < 0.01
    
    def test_future_value_very_small_interest_rate(self):
        """Test future value calculation with very small interest rate."""
        # Test with 0.1% annual rate
        result = self.calculator.future_value(1000, 0.001, 10)
        expected = 1000 * (1.001 ** 10)
        assert abs(result - expected) < 0.01
    
    def test_future_value_negative_interest_rate(self):
        """Test future value calculation with negative interest rate (deflation)."""
        # Test with -2% annual rate (deflation scenario)
        result = self.calculator.future_value(1000, -0.02, 5)
        expected = 1000 * (0.98 ** 5)
        assert abs(result - expected) < 0.01
        assert result < 1000  # Should be less than present value
    
    def test_future_value_negative_present_value_raises_error(self):
        """Test that negative present value raises ValueError."""
        with pytest.raises(ValueError, match="Present value cannot be negative"):
            self.calculator.future_value(-1000, 0.07, 10)
    
    def test_future_value_negative_periods_raises_error(self):
        """Test that negative periods raises ValueError."""
        with pytest.raises(ValueError, match="Number of periods cannot be negative"):
            self.calculator.future_value(1000, 0.07, -5)
    
    def test_future_value_mathematical_precision(self):
        """Test mathematical precision of future value calculation."""
        # Verify calculation matches manual computation precisely
        pv = 1234.56
        rate = 0.0789
        periods = 15
        
        result = self.calculator.future_value(pv, rate, periods)
        expected = pv * ((1 + rate) ** periods)
        
        # Should be mathematically identical
        assert result == expected
    
    def test_future_value_edge_case_very_large_numbers(self):
        """Test future value calculation with very large numbers."""
        # Test with large present value
        result = self.calculator.future_value(1000000000, 0.05, 10)
        expected = 1000000000 * (1.05 ** 10)
        assert abs(result - expected) < 1000  # Allow for some floating point precision
    
    def test_future_value_compound_growth_property(self):
        """Test compound growth property: FV(t1+t2) = FV(FV(t1), t2)."""
        # Calculate future value in two steps vs. one step
        pv = 1000
        rate = 0.08
        periods1 = 5
        periods2 = 3
        
        # Two-step calculation
        intermediate = self.calculator.future_value(pv, rate, periods1)
        two_step_result = self.calculator.future_value(intermediate, rate, periods2)
        
        # One-step calculation
        one_step_result = self.calculator.future_value(pv, rate, periods1 + periods2)
        
        # Should be equal (within floating point precision)
        assert abs(two_step_result - one_step_result) < 0.01
    
    def test_future_value_static_method_access(self):
        """Test that future_value can be called as a static method."""
        # Should be callable without instance
        result = FinancialCalculator.future_value(1000, 0.05, 5)
        expected = 1000 * (1.05 ** 5)
        assert abs(result - expected) < 0.01
    
    def test_future_value_docstring_examples(self):
        """Test examples from the docstring."""
        # Example 1: $1000 at 7% for 10 years
        result1 = self.calculator.future_value(1000, 0.07, 10)
        assert abs(result1 - 1967.15) < 0.01
        
        # Example 2: $5000 at 5% for 5 years  
        result2 = self.calculator.future_value(5000, 0.05, 5)
        assert abs(result2 - 6381.41) < 0.01
    
    def test_future_value_return_type(self):
        """Test that future_value returns a float."""
        result = self.calculator.future_value(1000, 0.07, 10)
        assert isinstance(result, float)
    
    def test_future_value_parameter_types(self):
        """Test future_value with different parameter types."""
        # Should accept int parameters and convert appropriately
        result1 = self.calculator.future_value(1000, 0.07, 10)
        result2 = self.calculator.future_value(1000.0, 0.07, 10.0)
        
        assert result1 == result2
        
        # Should work with integer periods
        result3 = self.calculator.future_value(1000.0, 0.07, 10)
        assert isinstance(result3, float)