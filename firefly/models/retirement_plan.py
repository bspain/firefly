"""
Retirement Plan Model

Defines retirement planning structures and calculations.
"""

from dataclasses import dataclass
from typing import Optional
from .financial_data import FinancialProfile


@dataclass
class RetirementPlan:
    """
    Represents a retirement plan with goals and projections.
    """
    
    # Retirement Goals
    target_retirement_age: int
    target_annual_income: float  # Desired annual income in retirement
    target_income_replacement_ratio: float = 0.8  # 80% of pre-retirement income
    
    # Assumptions
    inflation_rate: float = 0.025  # 2.5% annual inflation
    investment_return_rate: float = 0.07  # 7% annual return
    withdrawal_rate: float = 0.04  # 4% safe withdrawal rate
    
    # Social Security (optional)
    estimated_social_security: Optional[float] = None
    
    def calculate_required_portfolio_value(self, financial_profile: FinancialProfile) -> float:
        """
        Calculate the portfolio value needed to support retirement income.
        
        Args:
            financial_profile: User's financial profile
            
        Returns:
            Required portfolio value at retirement
        """
        # Determine target annual income in retirement
        if self.target_annual_income > 0:
            target_income = self.target_annual_income
        else:
            # Use replacement ratio of current income
            target_income = financial_profile.annual_income * self.target_income_replacement_ratio
        
        # Subtract Social Security if available
        net_income_needed = target_income
        if self.estimated_social_security:
            net_income_needed -= self.estimated_social_security
        
        # Calculate required portfolio value using withdrawal rate
        return net_income_needed / self.withdrawal_rate
    
    def calculate_monthly_savings_needed(self, financial_profile: FinancialProfile) -> float:
        """
        Calculate monthly savings needed to reach retirement goals.
        
        Args:
            financial_profile: User's financial profile
            
        Returns:
            Required monthly savings amount
        """
        required_portfolio = self.calculate_required_portfolio_value(financial_profile)
        current_assets = financial_profile.total_assets
        additional_needed = max(0, required_portfolio - current_assets)
        
        years_to_retirement = self.target_retirement_age - financial_profile.age
        if years_to_retirement <= 0:
            return 0.0
        
        # Calculate future value of current savings
        future_value_current = current_assets * ((1 + self.investment_return_rate) ** years_to_retirement)
        
        # Calculate additional amount needed considering current savings growth
        net_additional_needed = max(0, required_portfolio - future_value_current)
        
        if net_additional_needed == 0:
            return 0.0
        
        # Calculate monthly payment needed using future value of annuity formula
        monthly_rate = self.investment_return_rate / 12
        months = years_to_retirement * 12
        
        if monthly_rate == 0:
            return net_additional_needed / months
        
        # Future value of annuity formula solved for payment
        fv_annuity_factor = (((1 + monthly_rate) ** months) - 1) / monthly_rate
        return net_additional_needed / fv_annuity_factor
    
    def is_on_track(self, financial_profile: FinancialProfile) -> bool:
        """
        Determine if the user is on track to meet retirement goals.
        
        Args:
            financial_profile: User's financial profile
            
        Returns:
            True if on track, False otherwise
        """
        required_monthly_savings = self.calculate_monthly_savings_needed(financial_profile)
        return financial_profile.monthly_savings >= required_monthly_savings
    
    def calculate_retirement_readiness_score(self, financial_profile: FinancialProfile) -> float:
        """
        Calculate a retirement readiness score from 0 to 100.
        
        Args:
            financial_profile: User's financial profile
            
        Returns:
            Score from 0 to 100 indicating retirement readiness
        """
        required_portfolio = self.calculate_required_portfolio_value(financial_profile)
        current_assets = financial_profile.total_assets
        
        if required_portfolio == 0:
            return 100.0
        
        # Project current trajectory
        years_to_retirement = self.target_retirement_age - financial_profile.age
        if years_to_retirement <= 0:
            # Already at retirement age
            return min(100.0, (current_assets / required_portfolio) * 100)
        
        # Project future value with current savings rate
        monthly_rate = self.investment_return_rate / 12
        months = years_to_retirement * 12
        
        # Future value of current assets
        future_current = current_assets * ((1 + self.investment_return_rate) ** years_to_retirement)
        
        # Future value of monthly savings
        if monthly_rate > 0 and financial_profile.monthly_savings > 0:
            fv_annuity_factor = (((1 + monthly_rate) ** months) - 1) / monthly_rate
            future_savings = financial_profile.monthly_savings * fv_annuity_factor
        else:
            future_savings = financial_profile.monthly_savings * months
        
        projected_total = future_current + future_savings
        
        return min(100.0, (projected_total / required_portfolio) * 100)