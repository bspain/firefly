"""
Financial Calculator

Core financial calculation functions for retirement planning and investment projections.
"""


class FinancialCalculator:
    """
    Provides core financial calculation methods for retirement planning.
    
    This class implements fundamental financial mathematics used in retirement
    planning, investment analysis, and FIRE (Financial Independence, Retire Early)
    calculations.
    """
    
    @staticmethod
    def future_value(present_value: float, rate: float, periods: int) -> float:
        """
        Calculate future value of a present sum using compound interest.
        
        This function calculates what a current sum of money will be worth in the 
        future, given a specific interest rate and number of compounding periods.
        
        Formula: FV = PV * (1 + r)^n
        
        Args:
            present_value (float): Current value of the investment or deposit
            rate (float): Interest rate per period (as decimal, e.g., 0.07 for 7%)
            periods (int): Number of periods over which the investment compounds
            
        Returns:
            float: Future value of the investment
            
        Raises:
            ValueError: If present_value is negative, or periods is negative
            
        Examples:
            >>> calc = FinancialCalculator()
            >>> calc.future_value(1000, 0.07, 10)
            1967.15
            
            >>> calc.future_value(5000, 0.05, 5)
            6381.41
        """
        if present_value < 0:
            raise ValueError("Present value cannot be negative")
        if periods < 0:
            raise ValueError("Number of periods cannot be negative")
        
        return present_value * (1 + rate) ** periods