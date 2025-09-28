"""
Validation Utilities

Provides validation functions for financial data and user inputs.
"""

from typing import Union, Optional
from datetime import date


def validate_positive_number(value: Union[int, float], field_name: str = "Value") -> float:
    """
    Validate that a number is positive.
    
    Args:
        value: Number to validate
        field_name: Name of the field for error messages
        
    Returns:
        Validated number as float
        
    Raises:
        ValueError: If number is not positive
    """
    try:
        num_value = float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{field_name} must be a valid number")
    
    if num_value < 0:
        raise ValueError(f"{field_name} cannot be negative")
    
    return num_value


def validate_percentage(value: Union[int, float], field_name: str = "Percentage") -> float:
    """
    Validate that a percentage is within reasonable bounds (0-1 for decimal format).
    
    Args:
        value: Percentage to validate (as decimal, e.g., 0.07 for 7%)
        field_name: Name of the field for error messages
        
    Returns:
        Validated percentage as float
        
    Raises:
        ValueError: If percentage is not within valid range
    """
    try:
        pct_value = float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{field_name} must be a valid number")
    
    if pct_value < 0:
        raise ValueError(f"{field_name} cannot be negative")
    
    if pct_value > 1:
        # Assume user entered percentage as whole number (e.g., 7 instead of 0.07)
        if pct_value <= 100:
            pct_value = pct_value / 100
        else:
            raise ValueError(f"{field_name} cannot exceed 100%")
    
    return pct_value


def validate_age(age: int, field_name: str = "Age") -> int:
    """
    Validate age is within reasonable bounds.
    
    Args:
        age: Age to validate
        field_name: Name of the field for error messages
        
    Returns:
        Validated age
        
    Raises:
        ValueError: If age is not within valid range
    """
    try:
        age_value = int(age)
    except (TypeError, ValueError):
        raise ValueError(f"{field_name} must be a valid integer")
    
    if age_value < 0:
        raise ValueError(f"{field_name} cannot be negative")
    
    if age_value > 120:
        raise ValueError(f"{field_name} seems unreasonably high (over 120)")
    
    return age_value


def validate_date(date_value: date, field_name: str = "Date") -> date:
    """
    Validate date is reasonable.
    
    Args:
        date_value: Date to validate
        field_name: Name of the field for error messages
        
    Returns:
        Validated date
        
    Raises:
        ValueError: If date is not reasonable
    """
    if not isinstance(date_value, date):
        raise ValueError(f"{field_name} must be a valid date")
    
    current_date = date.today()
    
    # Check if birth date is in the future
    if date_value > current_date:
        raise ValueError(f"{field_name} cannot be in the future")
    
    # Check if birth date is unreasonably old (over 120 years ago)
    if (current_date - date_value).days > 120 * 365:
        raise ValueError(f"{field_name} indicates age over 120 years")
    
    return date_value


def validate_retirement_age(retirement_age: int, current_age: int) -> int:
    """
    Validate retirement age is reasonable relative to current age.
    
    Args:
        retirement_age: Target retirement age
        current_age: Current age
        
    Returns:
        Validated retirement age
        
    Raises:
        ValueError: If retirement age is not reasonable
    """
    retirement_age = validate_age(retirement_age, "Retirement age")
    
    if retirement_age < current_age:
        raise ValueError("Retirement age cannot be less than current age")
    
    if retirement_age < 50:
        raise ValueError("Retirement age seems unreasonably low (under 50)")
    
    if retirement_age > 80:
        raise ValueError("Retirement age seems unreasonably high (over 80)")
    
    return retirement_age


def validate_income(income: Union[int, float]) -> float:
    """
    Validate annual income is reasonable.
    
    Args:
        income: Annual income to validate
        
    Returns:
        Validated income
        
    Raises:
        ValueError: If income is not reasonable
    """
    income_value = validate_positive_number(income, "Annual income")
    
    # Reasonable bounds check (very generous)
    if income_value > 10_000_000:  # $10M annually
        raise ValueError("Annual income seems unreasonably high")
    
    return income_value


def validate_savings_rate(monthly_savings: float, annual_income: float) -> float:
    """
    Validate that savings rate is reasonable.
    
    Args:
        monthly_savings: Monthly savings amount
        annual_income: Annual income
        
    Returns:
        Validated monthly savings
        
    Raises:
        ValueError: If savings rate is not reasonable
    """
    savings_value = validate_positive_number(monthly_savings, "Monthly savings")
    
    if annual_income > 0:
        annual_savings = savings_value * 12
        savings_rate = annual_savings / annual_income
        
        if savings_rate > 0.8:  # 80% savings rate
            raise ValueError("Savings rate over 80% seems unreasonably high")
    
    return savings_value


def validate_expense_ratio(monthly_expenses: float, annual_income: float) -> float:
    """
    Validate that expense ratio is reasonable.
    
    Args:
        monthly_expenses: Monthly expenses
        annual_income: Annual income
        
    Returns:
        Validated monthly expenses
        
    Raises:
        ValueError: If expense ratio is not reasonable
    """
    expense_value = validate_positive_number(monthly_expenses, "Monthly expenses")
    
    if annual_income > 0:
        annual_expenses = expense_value * 12
        expense_ratio = annual_expenses / annual_income
        
        if expense_ratio > 2.0:  # 200% of income
            raise ValueError("Annual expenses exceed 200% of income - this seems unreasonable")
    
    return expense_value