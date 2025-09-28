"""
Formatting Utilities

Provides formatting functions for currency, percentages, and other display values.
"""

import locale
from typing import Union

# Try to set locale for currency formatting
try:
    locale.setlocale(locale.LC_ALL, '')
except locale.Error:
    # Fallback if locale setting fails
    pass


def format_currency(amount: Union[int, float], include_cents: bool = True) -> str:
    """
    Format a number as currency.
    
    Args:
        amount: Amount to format
        include_cents: Whether to include cents in the display
        
    Returns:
        Formatted currency string
    """
    if include_cents:
        try:
            return locale.currency(amount, grouping=True)
        except (locale.Error, ValueError):
            return f"${amount:,.2f}"
    else:
        try:
            return locale.currency(amount, grouping=True, symbol=True).split('.')[0]
        except (locale.Error, ValueError):
            return f"${amount:,.0f}"


def format_percentage(rate: float, decimal_places: int = 1) -> str:
    """
    Format a decimal rate as a percentage.
    
    Args:
        rate: Rate as decimal (e.g., 0.075 for 7.5%)
        decimal_places: Number of decimal places to show
        
    Returns:
        Formatted percentage string
    """
    percentage = rate * 100
    return f"{percentage:.{decimal_places}f}%"


def format_large_number(number: Union[int, float], precision: int = 1) -> str:
    """
    Format large numbers with K, M, B suffixes.
    
    Args:
        number: Number to format
        precision: Decimal places for abbreviated numbers
        
    Returns:
        Formatted number string
    """
    if abs(number) >= 1_000_000_000:
        return f"{number / 1_000_000_000:.{precision}f}B"
    elif abs(number) >= 1_000_000:
        return f"{number / 1_000_000:.{precision}f}M"
    elif abs(number) >= 1_000:
        return f"{number / 1_000:.{precision}f}K"
    else:
        return f"{number:.{precision}f}"


def format_years(years: float) -> str:
    """
    Format years in a human-readable way.
    
    Args:
        years: Number of years (can be fractional)
        
    Returns:
        Formatted years string
    """
    if years < 1:
        months = int(years * 12)
        return f"{months} month{'s' if months != 1 else ''}"
    elif years == int(years):
        years_int = int(years)
        return f"{years_int} year{'s' if years_int != 1 else ''}"
    else:
        return f"{years:.1f} years"


def format_age_range(start_age: int, end_age: int) -> str:
    """
    Format an age range.
    
    Args:
        start_age: Starting age
        end_age: Ending age
        
    Returns:
        Formatted age range string
    """
    return f"Age {start_age}-{end_age}"


def format_account_summary(accounts: dict) -> str:
    """
    Format a dictionary of accounts and balances.
    
    Args:
        accounts: Dictionary of account names to balances
        
    Returns:
        Formatted account summary string
    """
    if not accounts:
        return "None"
    
    lines = []
    for account, balance in accounts.items():
        lines.append(f"  {account}: {format_currency(balance)}")
    
    return "\n" + "\n".join(lines)


def truncate_text(text: str, max_length: int = 50) -> str:
    """
    Truncate text to a maximum length with ellipsis.
    
    Args:
        text: Text to truncate
        max_length: Maximum length including ellipsis
        
    Returns:
        Truncated text string
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."