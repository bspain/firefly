"""
Financial Calculator

Core financial calculation functions for retirement planning and investment projections.
"""

import math
from typing import List, Tuple
import numpy as np


class FinancialCalculator:
    """
    Provides core financial calculation methods for retirement planning.
    """
    
    @staticmethod
    def future_value(present_value: float, rate: float, periods: int) -> float:
        """
        Calculate future value of a present sum.
        
        Args:
            present_value: Current value
            rate: Interest rate per period
            periods: Number of periods
            
        Returns:
            Future value
        """
        return present_value * (1 + rate) ** periods
    
    @staticmethod
    def present_value(future_value: float, rate: float, periods: int) -> float:
        """
        Calculate present value of a future sum.
        
        Args:
            future_value: Future value
            rate: Discount rate per period
            periods: Number of periods
            
        Returns:
            Present value
        """
        return future_value / (1 + rate) ** periods
    
    @staticmethod
    def future_value_annuity(payment: float, rate: float, periods: int) -> float:
        """
        Calculate future value of an ordinary annuity.
        
        Args:
            payment: Payment amount per period
            rate: Interest rate per period
            periods: Number of periods
            
        Returns:
            Future value of annuity
        """
        if rate == 0:
            return payment * periods
        return payment * (((1 + rate) ** periods - 1) / rate)
    
    @staticmethod
    def present_value_annuity(payment: float, rate: float, periods: int) -> float:
        """
        Calculate present value of an ordinary annuity.
        
        Args:
            payment: Payment amount per period
            rate: Interest rate per period
            periods: Number of periods
            
        Returns:
            Present value of annuity
        """
        if rate == 0:
            return payment * periods
        return payment * (1 - (1 + rate) ** -periods) / rate
    
    @staticmethod
    def payment_annuity(present_value: float, rate: float, periods: int) -> float:
        """
        Calculate payment amount for an annuity given present value.
        
        Args:
            present_value: Present value of annuity
            rate: Interest rate per period
            periods: Number of periods
            
        Returns:
            Payment amount per period
        """
        if rate == 0:
            return present_value / periods
        return present_value * rate / (1 - (1 + rate) ** -periods)
    
    @staticmethod
    def compound_annual_growth_rate(beginning_value: float, ending_value: float, periods: int) -> float:
        """
        Calculate compound annual growth rate (CAGR).
        
        Args:
            beginning_value: Starting value
            ending_value: Ending value
            periods: Number of periods
            
        Returns:
            Compound annual growth rate
        """
        if beginning_value <= 0 or periods <= 0:
            return 0.0
        return (ending_value / beginning_value) ** (1 / periods) - 1
    
    @staticmethod
    def rule_of_72(rate: float) -> float:
        """
        Calculate time to double money using Rule of 72.
        
        Args:
            rate: Annual interest rate (as decimal, e.g., 0.07 for 7%)
            
        Returns:
            Years to double money
        """
        if rate <= 0:
            return float('inf')
        return 0.72 / rate
    
    @staticmethod
    def inflation_adjusted_value(nominal_value: float, inflation_rate: float, years: int) -> float:
        """
        Calculate inflation-adjusted (real) value.
        
        Args:
            nominal_value: Nominal value
            inflation_rate: Annual inflation rate
            years: Number of years
            
        Returns:
            Real (inflation-adjusted) value
        """
        return nominal_value / (1 + inflation_rate) ** years
    
    @staticmethod
    def real_return_rate(nominal_rate: float, inflation_rate: float) -> float:
        """
        Calculate real return rate adjusted for inflation.
        
        Args:
            nominal_rate: Nominal return rate
            inflation_rate: Inflation rate
            
        Returns:
            Real return rate
        """
        return (1 + nominal_rate) / (1 + inflation_rate) - 1
    
    @staticmethod
    def safe_withdrawal_rate_calculation(portfolio_value: float, annual_expenses: float) -> float:
        """
        Calculate the withdrawal rate based on portfolio value and expenses.
        
        Args:
            portfolio_value: Total portfolio value
            annual_expenses: Annual expenses needed
            
        Returns:
            Withdrawal rate as percentage
        """
        if portfolio_value <= 0:
            return 0.0
        return annual_expenses / portfolio_value
    
    @staticmethod
    def monte_carlo_projection(
        initial_value: float,
        annual_return: float,
        volatility: float,
        years: int,
        annual_contribution: float = 0,
        simulations: int = 1000
    ) -> Tuple[List[float], float, float]:
        """
        Perform Monte Carlo simulation for investment projections.
        
        Args:
            initial_value: Starting portfolio value
            annual_return: Expected annual return (mean)
            volatility: Annual volatility (standard deviation)
            years: Number of years to project
            annual_contribution: Annual contribution amount
            simulations: Number of simulations to run
            
        Returns:
            Tuple of (final_values, median_value, confidence_90th_percentile)
        """
        np.random.seed(42)  # For reproducible results
        final_values = []
        
        for _ in range(simulations):
            value = initial_value
            for year in range(years):
                # Generate random return for this year
                annual_return_this_year = np.random.normal(annual_return, volatility)
                # Apply return and add contribution
                value = value * (1 + annual_return_this_year) + annual_contribution
            final_values.append(value)
        
        final_values.sort()
        median_value = final_values[len(final_values) // 2]
        # 90th percentile (conservative estimate)
        percentile_90 = final_values[int(len(final_values) * 0.1)]
        
        return final_values, median_value, percentile_90