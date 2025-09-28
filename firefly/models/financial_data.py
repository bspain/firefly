"""
Financial Data Models

Defines the core financial data structures for user profiles, including income,
expenses, assets, and liabilities.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
from datetime import date


@dataclass
class FinancialProfile:
    """
    Represents a user's complete financial profile including income, expenses,
    assets, and liabilities.
    """
    
    # Personal Information
    name: str
    birth_date: date
    retirement_age: int = 65
    
    # Income
    annual_income: float = 0.0
    income_growth_rate: float = 0.03  # 3% default
    
    # Expenses
    monthly_expenses: float = 0.0
    expense_growth_rate: float = 0.025  # 2.5% default
    
    # Assets
    current_savings: float = 0.0
    monthly_savings: float = 0.0
    
    # Investment accounts
    investment_accounts: Dict[str, float] = field(default_factory=dict)
    
    # Retirement accounts
    retirement_accounts: Dict[str, float] = field(default_factory=dict)
    
    # Debts
    debts: Dict[str, float] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate the financial profile data."""
        if self.annual_income < 0:
            raise ValueError("Annual income cannot be negative")
        if self.monthly_expenses < 0:
            raise ValueError("Monthly expenses cannot be negative")
        if self.current_savings < 0:
            raise ValueError("Current savings cannot be negative")
    
    @property
    def age(self) -> int:
        """Calculate current age based on birth date."""
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
    
    @property
    def years_to_retirement(self) -> int:
        """Calculate years until retirement."""
        return max(0, self.retirement_age - self.age)
    
    @property
    def total_assets(self) -> float:
        """Calculate total assets including savings and investments."""
        investment_total = sum(self.investment_accounts.values())
        retirement_total = sum(self.retirement_accounts.values())
        return self.current_savings + investment_total + retirement_total
    
    @property
    def total_debts(self) -> float:
        """Calculate total debts."""
        return sum(self.debts.values())
    
    @property
    def net_worth(self) -> float:
        """Calculate net worth (assets - debts)."""
        return self.total_assets - self.total_debts
    
    @property
    def annual_expenses(self) -> float:
        """Calculate total annual expenses."""
        return self.monthly_expenses * 12
    
    @property
    def savings_rate(self) -> float:
        """Calculate savings rate as percentage of income."""
        if self.annual_income == 0:
            return 0.0
        annual_savings = self.monthly_savings * 12
        return annual_savings / self.annual_income