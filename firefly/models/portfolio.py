"""
Portfolio and Investment Models

Defines investment portfolio structures and individual investment holdings.
"""

from dataclasses import dataclass, field
from typing import Dict, List
from enum import Enum


class AssetClass(Enum):
    """Asset class categories for investments."""
    STOCKS = "stocks"
    BONDS = "bonds"
    REAL_ESTATE = "real_estate"
    COMMODITIES = "commodities"
    CASH = "cash"
    CRYPTOCURRENCY = "cryptocurrency"
    OTHER = "other"


@dataclass
class Investment:
    """
    Represents an individual investment holding.
    """
    symbol: str
    name: str
    asset_class: AssetClass
    shares: float
    current_price: float
    annual_return_rate: float = 0.07  # 7% default expected return
    annual_volatility: float = 0.15   # 15% default volatility
    
    @property
    def current_value(self) -> float:
        """Calculate current market value of the investment."""
        return self.shares * self.current_price
    
    def project_value(self, years: int) -> float:
        """
        Project future value of investment based on expected return rate.
        
        Args:
            years: Number of years to project
            
        Returns:
            Projected future value
        """
        return self.current_value * ((1 + self.annual_return_rate) ** years)


@dataclass
class Portfolio:
    """
    Represents an investment portfolio containing multiple investments.
    """
    name: str
    investments: List[Investment] = field(default_factory=list)
    
    @property
    def total_value(self) -> float:
        """Calculate total portfolio value."""
        return sum(investment.current_value for investment in self.investments)
    
    @property
    def asset_allocation(self) -> Dict[AssetClass, float]:
        """
        Calculate asset allocation as percentages by asset class.
        
        Returns:
            Dictionary mapping asset classes to percentage allocations
        """
        if self.total_value == 0:
            return {}
        
        allocation = {}
        for investment in self.investments:
            asset_class = investment.asset_class
            if asset_class not in allocation:
                allocation[asset_class] = 0.0
            allocation[asset_class] += investment.current_value
        
        # Convert to percentages
        for asset_class in allocation:
            allocation[asset_class] = allocation[asset_class] / self.total_value
        
        return allocation
    
    @property
    def weighted_return_rate(self) -> float:
        """
        Calculate portfolio's weighted average expected return rate.
        
        Returns:
            Weighted average annual return rate
        """
        if self.total_value == 0:
            return 0.0
        
        weighted_return = 0.0
        for investment in self.investments:
            weight = investment.current_value / self.total_value
            weighted_return += weight * investment.annual_return_rate
        
        return weighted_return
    
    def add_investment(self, investment: Investment):
        """Add an investment to the portfolio."""
        self.investments.append(investment)
    
    def remove_investment(self, symbol: str) -> bool:
        """
        Remove an investment from the portfolio by symbol.
        
        Args:
            symbol: Investment symbol to remove
            
        Returns:
            True if investment was found and removed, False otherwise
        """
        for i, investment in enumerate(self.investments):
            if investment.symbol == symbol:
                del self.investments[i]
                return True
        return False
    
    def project_value(self, years: int) -> float:
        """
        Project future portfolio value based on weighted return rate.
        
        Args:
            years: Number of years to project
            
        Returns:
            Projected future portfolio value
        """
        return self.total_value * ((1 + self.weighted_return_rate) ** years)