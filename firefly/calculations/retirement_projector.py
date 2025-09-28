"""
Retirement Projector

Provides detailed retirement projections and analysis.
"""

from dataclasses import dataclass
from typing import List, Dict, Tuple
import numpy as np
from ..models.financial_data import FinancialProfile
from ..models.retirement_plan import RetirementPlan
from .financial_calculator import FinancialCalculator


@dataclass
class YearlyProjection:
    """
    Projection data for a single year.
    """
    year: int
    age: int
    portfolio_value: float
    annual_contribution: float
    annual_return: float
    expenses: float
    net_worth: float


@dataclass
class RetirementProjection:
    """
    Complete retirement projection results.
    """
    yearly_projections: List[YearlyProjection]
    total_contributions: float
    total_returns: float
    final_portfolio_value: float
    retirement_feasible: bool
    years_of_retirement_funded: int


class RetirementProjector:
    """
    Projects detailed retirement scenarios and creates year-by-year analysis.
    """
    
    def __init__(self, profile: FinancialProfile, plan: RetirementPlan):
        """
        Initialize retirement projector.
        
        Args:
            profile: Financial profile
            plan: Retirement plan
        """
        self.profile = profile
        self.plan = plan
    
    def project_to_retirement(self) -> RetirementProjection:
        """
        Project financial growth from current age to retirement.
        
        Returns:
            Detailed retirement projection
        """
        projections = []
        current_age = self.profile.age
        portfolio_value = self.profile.total_assets
        annual_contribution = self.profile.monthly_savings * 12
        annual_expenses = self.profile.annual_expenses
        
        total_contributions = 0
        total_returns = 0
        
        # Project each year until retirement
        for year_offset in range(self.plan.target_retirement_age - current_age + 1):
            age = current_age + year_offset
            year = 2024 + year_offset  # Assuming current year is 2024
            
            # Calculate returns for this year
            annual_return = portfolio_value * self.plan.investment_return_rate
            
            # Add contribution and returns
            portfolio_value += annual_contribution + annual_return
            
            # Adjust for inflation
            if year_offset > 0:  # Don't inflate first year
                annual_contribution *= (1 + self.profile.income_growth_rate)
                annual_expenses *= (1 + self.profile.expense_growth_rate)
            
            # Track totals
            total_contributions += annual_contribution
            total_returns += annual_return
            
            # Create yearly projection
            projection = YearlyProjection(
                year=year,
                age=age,
                portfolio_value=portfolio_value,
                annual_contribution=annual_contribution,
                annual_return=annual_return,
                expenses=annual_expenses,
                net_worth=portfolio_value - self.profile.total_debts
            )
            projections.append(projection)
        
        # Determine if retirement is feasible
        required_portfolio = self.plan.calculate_required_portfolio_value(self.profile)
        retirement_feasible = portfolio_value >= required_portfolio
        
        # Calculate years of retirement funded
        retirement_expenses = annual_expenses
        if self.plan.estimated_social_security:
            retirement_expenses -= self.plan.estimated_social_security
        
        years_funded = 0
        if retirement_expenses > 0:
            years_funded = int(portfolio_value / retirement_expenses)
        
        return RetirementProjection(
            yearly_projections=projections,
            total_contributions=total_contributions,
            total_returns=total_returns,
            final_portfolio_value=portfolio_value,
            retirement_feasible=retirement_feasible,
            years_of_retirement_funded=years_funded
        )
    
    def project_retirement_withdrawal(self, years_in_retirement: int = 30) -> List[YearlyProjection]:
        """
        Project withdrawal phase during retirement.
        
        Args:
            years_in_retirement: Number of retirement years to project
            
        Returns:
            List of yearly projections during retirement
        """
        retirement_projection = self.project_to_retirement()
        portfolio_value = retirement_projection.final_portfolio_value
        
        withdrawal_projections = []
        annual_expenses = self.profile.annual_expenses
        
        # Adjust expenses for inflation to retirement age
        years_to_retirement = self.plan.target_retirement_age - self.profile.age
        inflation_adjusted_expenses = annual_expenses * (
            (1 + self.plan.inflation_rate) ** years_to_retirement
        )
        
        # Subtract Social Security if available
        net_withdrawal_needed = inflation_adjusted_expenses
        if self.plan.estimated_social_security:
            # Inflate Social Security benefits too
            inflated_ss = self.plan.estimated_social_security * (
                (1 + self.plan.inflation_rate) ** years_to_retirement
            )
            net_withdrawal_needed -= inflated_ss
        
        retirement_start_year = 2024 + years_to_retirement
        
        for retirement_year in range(years_in_retirement):
            age = self.plan.target_retirement_age + retirement_year
            year = retirement_start_year + retirement_year
            
            # Calculate investment returns
            annual_return = portfolio_value * self.plan.investment_return_rate
            
            # Add returns then subtract withdrawal
            portfolio_value += annual_return
            portfolio_value -= net_withdrawal_needed
            
            # Adjust withdrawal for inflation
            net_withdrawal_needed *= (1 + self.plan.inflation_rate)
            
            projection = YearlyProjection(
                year=year,
                age=age,
                portfolio_value=max(0, portfolio_value),
                annual_contribution=-net_withdrawal_needed,  # Negative for withdrawal
                annual_return=annual_return,
                expenses=net_withdrawal_needed + (self.plan.estimated_social_security or 0),
                net_worth=max(0, portfolio_value)
            )
            withdrawal_projections.append(projection)
            
            # Stop if portfolio is depleted
            if portfolio_value <= 0:
                break
        
        return withdrawal_projections
    
    def monte_carlo_retirement_analysis(
        self, 
        simulations: int = 1000,
        market_volatility: float = 0.15
    ) -> Dict[str, any]:
        """
        Perform Monte Carlo analysis for retirement projections.
        
        Args:
            simulations: Number of simulations to run
            market_volatility: Annual market volatility
            
        Returns:
            Monte Carlo analysis results
        """
        success_count = 0
        final_values = []
        
        np.random.seed(42)  # For reproducible results
        
        for _ in range(simulations):
            portfolio_value = self.profile.total_assets
            annual_contribution = self.profile.monthly_savings * 12
            
            # Accumulation phase
            years_to_retirement = self.plan.target_retirement_age - self.profile.age
            for year in range(years_to_retirement):
                # Random return with volatility
                annual_return_rate = np.random.normal(
                    self.plan.investment_return_rate, 
                    market_volatility
                )
                annual_return = portfolio_value * annual_return_rate
                portfolio_value += annual_contribution + annual_return
                
                # Adjust contribution for income growth
                annual_contribution *= (1 + self.profile.income_growth_rate)
            
            # Check if accumulated enough for retirement
            required_portfolio = self.plan.calculate_required_portfolio_value(self.profile)
            if portfolio_value >= required_portfolio:
                success_count += 1
            
            final_values.append(portfolio_value)
        
        final_values.sort()
        success_rate = success_count / simulations
        
        return {
            "success_rate": success_rate,
            "median_final_value": final_values[len(final_values) // 2],
            "percentile_10": final_values[int(len(final_values) * 0.1)],
            "percentile_90": final_values[int(len(final_values) * 0.9)],
            "required_portfolio_value": required_portfolio,
            "simulations_run": simulations
        }
    
    def calculate_fire_metrics(self) -> Dict[str, float]:
        """
        Calculate Financial Independence, Retire Early (FIRE) metrics.
        
        Returns:
            Dictionary of FIRE-related metrics
        """
        annual_expenses = self.profile.annual_expenses
        
        # FIRE number (25x annual expenses for 4% withdrawal rate)
        fire_number = annual_expenses * 25
        
        # Coast FIRE (enough savings to grow to FIRE number by retirement age)
        years_to_retirement = self.plan.target_retirement_age - self.profile.age
        coast_fire_number = FinancialCalculator.present_value(
            fire_number,
            self.plan.investment_return_rate,
            years_to_retirement
        )
        
        # Barista FIRE (enough for partial retirement, cover basics)
        essential_expenses = annual_expenses * 0.7  # Assume 70% are essential
        barista_fire_number = essential_expenses * 25
        
        # Lean FIRE (minimal expenses)
        lean_expenses = annual_expenses * 0.6  # Assume 60% for lean FIRE
        lean_fire_number = lean_expenses * 25
        
        # Fat FIRE (comfortable lifestyle)
        fat_expenses = annual_expenses * 1.5  # 150% for comfortable lifestyle
        fat_fire_number = fat_expenses * 25
        
        # Current progress
        current_assets = self.profile.total_assets
        fire_progress = (current_assets / fire_number) * 100 if fire_number > 0 else 0
        
        # Time to FIRE with current savings rate
        additional_needed = max(0, fire_number - current_assets)
        monthly_savings = self.profile.monthly_savings
        
        years_to_fire = 0
        if monthly_savings > 0 and additional_needed > 0:
            monthly_rate = self.plan.investment_return_rate / 12
            if monthly_rate > 0:
                # Use future value of annuity formula
                months = np.log(1 + (additional_needed * monthly_rate / monthly_savings)) / np.log(1 + monthly_rate)
                years_to_fire = months / 12
            else:
                years_to_fire = additional_needed / (monthly_savings * 12)
        
        return {
            "fire_number": fire_number,
            "coast_fire_number": coast_fire_number,
            "barista_fire_number": barista_fire_number,
            "lean_fire_number": lean_fire_number,
            "fat_fire_number": fat_fire_number,
            "current_progress_percent": fire_progress,
            "years_to_fire": years_to_fire,
            "monthly_savings_for_fire": monthly_savings
        }