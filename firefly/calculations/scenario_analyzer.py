"""
Scenario Analyzer

Provides "what-if" scenario analysis capabilities for financial planning.
"""

import math
from dataclasses import dataclass, replace
from typing import Dict, List, Any
from ..models.financial_data import FinancialProfile
from ..models.retirement_plan import RetirementPlan
from .financial_calculator import FinancialCalculator


@dataclass
class ScenarioResult:
    """
    Results from a scenario analysis.
    """
    scenario_name: str
    retirement_readiness_score: float
    required_monthly_savings: float
    projected_portfolio_value: float
    years_to_fi: int  # Years to financial independence
    changes_applied: Dict[str, Any]


class ScenarioAnalyzer:
    """
    Analyzes various "what-if" scenarios for financial planning.
    """
    
    def __init__(self, base_profile: FinancialProfile, base_plan: RetirementPlan):
        """
        Initialize scenario analyzer with base financial profile and plan.
        
        Args:
            base_profile: Base financial profile
            base_plan: Base retirement plan
        """
        self.base_profile = base_profile
        self.base_plan = base_plan
    
    def analyze_income_change(self, income_change_percent: float) -> ScenarioResult:
        """
        Analyze scenario with different income level.
        
        Args:
            income_change_percent: Percentage change in income (e.g., 0.20 for 20% increase)
            
        Returns:
            Scenario analysis results
        """
        modified_profile = replace(
            self.base_profile,
            annual_income=self.base_profile.annual_income * (1 + income_change_percent)
        )
        
        return self._calculate_scenario_result(
            "Income Change",
            modified_profile,
            {"income_change_percent": income_change_percent}
        )
    
    def analyze_savings_rate_change(self, new_savings_rate: float) -> ScenarioResult:
        """
        Analyze scenario with different savings rate.
        
        Args:
            new_savings_rate: New savings rate as percentage (e.g., 0.20 for 20%)
            
        Returns:
            Scenario analysis results
        """
        new_monthly_savings = (self.base_profile.annual_income * new_savings_rate) / 12
        modified_profile = replace(
            self.base_profile,
            monthly_savings=new_monthly_savings
        )
        
        return self._calculate_scenario_result(
            "Savings Rate Change",
            modified_profile,
            {"new_savings_rate": new_savings_rate}
        )
    
    def analyze_retirement_age_change(self, new_retirement_age: int) -> ScenarioResult:
        """
        Analyze scenario with different retirement age.
        
        Args:
            new_retirement_age: New target retirement age
            
        Returns:
            Scenario analysis results
        """
        modified_plan = replace(
            self.base_plan,
            target_retirement_age=new_retirement_age
        )
        
        return self._calculate_scenario_result(
            "Retirement Age Change",
            self.base_profile,
            {"new_retirement_age": new_retirement_age},
            modified_plan
        )
    
    def analyze_return_rate_change(self, new_return_rate: float) -> ScenarioResult:
        """
        Analyze scenario with different investment return rate.
        
        Args:
            new_return_rate: New expected annual return rate
            
        Returns:
            Scenario analysis results
        """
        modified_plan = replace(
            self.base_plan,
            investment_return_rate=new_return_rate
        )
        
        return self._calculate_scenario_result(
            "Return Rate Change",
            self.base_profile,
            {"new_return_rate": new_return_rate},
            modified_plan
        )
    
    def analyze_expense_change(self, expense_change_percent: float) -> ScenarioResult:
        """
        Analyze scenario with different expense level.
        
        Args:
            expense_change_percent: Percentage change in expenses
            
        Returns:
            Scenario analysis results
        """
        modified_profile = replace(
            self.base_profile,
            monthly_expenses=self.base_profile.monthly_expenses * (1 + expense_change_percent)
        )
        
        return self._calculate_scenario_result(
            "Expense Change",
            modified_profile,
            {"expense_change_percent": expense_change_percent}
        )
    
    def analyze_debt_payoff(self, debt_name: str) -> ScenarioResult:
        """
        Analyze scenario where a specific debt is paid off.
        
        Args:
            debt_name: Name of the debt to pay off
            
        Returns:
            Scenario analysis results
        """
        if debt_name not in self.base_profile.debts:
            raise ValueError(f"Debt '{debt_name}' not found in profile")
        
        modified_debts = self.base_profile.debts.copy()
        del modified_debts[debt_name]
        
        modified_profile = replace(
            self.base_profile,
            debts=modified_debts
        )
        
        return self._calculate_scenario_result(
            "Debt Payoff",
            modified_profile,
            {"debt_paid_off": debt_name}
        )
    
    def analyze_market_crash(self, crash_percent: float = -0.30) -> ScenarioResult:
        """
        Analyze scenario with market crash affecting current assets.
        
        Args:
            crash_percent: Percentage decline in portfolio value
            
        Returns:
            Scenario analysis results
        """
        # Reduce current savings and investment accounts
        modified_profile = replace(
            self.base_profile,
            current_savings=self.base_profile.current_savings * (1 + crash_percent),
            investment_accounts={
                k: v * (1 + crash_percent) for k, v in self.base_profile.investment_accounts.items()
            },
            retirement_accounts={
                k: v * (1 + crash_percent) for k, v in self.base_profile.retirement_accounts.items()
            }
        )
        
        return self._calculate_scenario_result(
            "Market Crash",
            modified_profile,
            {"crash_percent": crash_percent}
        )
    
    def compare_scenarios(self, scenarios: List[ScenarioResult]) -> Dict[str, Any]:
        """
        Compare multiple scenarios and provide insights.
        
        Args:
            scenarios: List of scenario results to compare
            
        Returns:
            Comparison analysis
        """
        if not scenarios:
            return {}
        
        # Find best and worst scenarios
        best_score = max(scenarios, key=lambda s: s.retirement_readiness_score)
        worst_score = min(scenarios, key=lambda s: s.retirement_readiness_score)
        
        lowest_savings_needed = min(scenarios, key=lambda s: s.required_monthly_savings)
        highest_savings_needed = max(scenarios, key=lambda s: s.required_monthly_savings)
        
        return {
            "best_scenario": {
                "name": best_score.scenario_name,
                "score": best_score.retirement_readiness_score,
                "changes": best_score.changes_applied
            },
            "worst_scenario": {
                "name": worst_score.scenario_name,
                "score": worst_score.retirement_readiness_score,
                "changes": worst_score.changes_applied
            },
            "lowest_savings_needed": {
                "name": lowest_savings_needed.scenario_name,
                "monthly_savings": lowest_savings_needed.required_monthly_savings,
                "changes": lowest_savings_needed.changes_applied
            },
            "highest_savings_needed": {
                "name": highest_savings_needed.scenario_name,
                "monthly_savings": highest_savings_needed.required_monthly_savings,
                "changes": highest_savings_needed.changes_applied
            },
            "score_range": best_score.retirement_readiness_score - worst_score.retirement_readiness_score
        }
    
    def _calculate_scenario_result(
        self,
        scenario_name: str,
        profile: FinancialProfile,
        changes: Dict[str, Any],
        plan: RetirementPlan = None
    ) -> ScenarioResult:
        """
        Calculate results for a given scenario.
        
        Args:
            scenario_name: Name of the scenario
            profile: Modified financial profile
            changes: Dictionary of changes applied
            plan: Modified retirement plan (uses base plan if None)
            
        Returns:
            Scenario result
        """
        if plan is None:
            plan = self.base_plan
        
        readiness_score = plan.calculate_retirement_readiness_score(profile)
        required_savings = plan.calculate_monthly_savings_needed(profile)
        
        # Calculate projected portfolio value at retirement
        years_to_retirement = plan.target_retirement_age - profile.age
        if years_to_retirement > 0:
            # Future value of current assets
            future_current = FinancialCalculator.future_value(
                profile.total_assets,
                plan.investment_return_rate,
                years_to_retirement
            )
            
            # Future value of monthly savings
            future_savings = FinancialCalculator.future_value_annuity(
                profile.monthly_savings,
                plan.investment_return_rate / 12,
                years_to_retirement * 12
            )
            
            projected_portfolio = future_current + future_savings
        else:
            projected_portfolio = profile.total_assets
        
        # Calculate years to financial independence (4% rule)
        annual_expenses = profile.annual_expenses
        fi_target = annual_expenses / 0.04  # 4% withdrawal rate
        
        years_to_fi = 0
        if profile.total_assets < fi_target and profile.monthly_savings > 0:
            # Simple calculation - more sophisticated would use iterative approach
            additional_needed = fi_target - profile.total_assets
            monthly_rate = plan.investment_return_rate / 12
            if monthly_rate > 0:
                months = math.log(1 + (additional_needed * monthly_rate / profile.monthly_savings)) / math.log(1 + monthly_rate)
                years_to_fi = int(months / 12)
            else:
                years_to_fi = int(additional_needed / (profile.monthly_savings * 12))
        
        return ScenarioResult(
            scenario_name=scenario_name,
            retirement_readiness_score=readiness_score,
            required_monthly_savings=required_savings,
            projected_portfolio_value=projected_portfolio,
            years_to_fi=years_to_fi,
            changes_applied=changes
        )