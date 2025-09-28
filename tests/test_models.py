"""
Unit tests for Firefly data models
"""

import unittest
from datetime import date
from firefly.models.financial_data import FinancialProfile
from firefly.models.retirement_plan import RetirementPlan
from firefly.models.portfolio import Portfolio, Investment, AssetClass


class TestFinancialProfile(unittest.TestCase):
    """Test cases for FinancialProfile model."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.profile = FinancialProfile(
            name="Test User",
            birth_date=date(1990, 1, 1),
            retirement_age=65,
            annual_income=75000,
            monthly_expenses=4000,
            current_savings=25000,
            monthly_savings=1000
        )
    
    def test_age_calculation(self):
        """Test age calculation from birth date."""
        # Assuming current date is around 2024
        expected_age = 2024 - 1990
        self.assertAlmostEqual(self.profile.age, expected_age, delta=1)
    
    def test_years_to_retirement(self):
        """Test years to retirement calculation."""
        expected_years = 65 - self.profile.age
        self.assertEqual(self.profile.years_to_retirement, expected_years)
    
    def test_net_worth_calculation(self):
        """Test net worth calculation."""
        # No debts in basic profile
        self.assertEqual(self.profile.net_worth, self.profile.total_assets)
    
    def test_savings_rate_calculation(self):
        """Test savings rate calculation."""
        expected_rate = (1000 * 12) / 75000  # 16%
        self.assertAlmostEqual(self.profile.savings_rate, expected_rate, places=4)
    
    def test_annual_expenses_calculation(self):
        """Test annual expenses calculation."""
        expected_annual = 4000 * 12
        self.assertEqual(self.profile.annual_expenses, expected_annual)
    
    def test_negative_income_validation(self):
        """Test that negative income raises ValueError."""
        with self.assertRaises(ValueError):
            FinancialProfile(
                name="Test",
                birth_date=date(1990, 1, 1),
                annual_income=-1000
            )


class TestRetirementPlan(unittest.TestCase):
    """Test cases for RetirementPlan model."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.profile = FinancialProfile(
            name="Test User",
            birth_date=date(1990, 1, 1),
            retirement_age=65,
            annual_income=75000,
            monthly_expenses=4000,
            current_savings=25000,
            monthly_savings=1000
        )
        
        self.plan = RetirementPlan(
            target_retirement_age=65,
            target_annual_income=60000,  # 80% of $75k
            estimated_social_security=18000
        )
    
    def test_required_portfolio_calculation(self):
        """Test required portfolio value calculation."""
        required = self.plan.calculate_required_portfolio_value(self.profile)
        
        # Should be (60000 - 18000) / 0.04 = $1,050,000
        expected = (60000 - 18000) / 0.04
        self.assertEqual(required, expected)
    
    def test_monthly_savings_needed(self):
        """Test monthly savings needed calculation."""
        monthly_needed = self.plan.calculate_monthly_savings_needed(self.profile)
        
        # Should be positive since current savings likely insufficient
        self.assertGreater(monthly_needed, 0)
    
    def test_retirement_readiness_score(self):
        """Test retirement readiness score calculation."""
        score = self.plan.calculate_retirement_readiness_score(self.profile)
        
        # Should be between 0 and 100
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 100)


class TestPortfolio(unittest.TestCase):
    """Test cases for Portfolio and Investment models."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.investment1 = Investment(
            symbol="SPY",
            name="S&P 500 ETF",
            asset_class=AssetClass.STOCKS,
            shares=100,
            current_price=400,
            annual_return_rate=0.07
        )
        
        self.investment2 = Investment(
            symbol="BND",
            name="Bond ETF",
            asset_class=AssetClass.BONDS,
            shares=200,
            current_price=80,
            annual_return_rate=0.04
        )
        
        self.portfolio = Portfolio(
            name="Test Portfolio",
            investments=[self.investment1, self.investment2]
        )
    
    def test_investment_current_value(self):
        """Test investment current value calculation."""
        expected_value = 100 * 400  # 100 shares * $400
        self.assertEqual(self.investment1.current_value, expected_value)
    
    def test_investment_project_value(self):
        """Test investment future value projection."""
        future_value = self.investment1.project_value(10)  # 10 years
        expected = 40000 * (1.07 ** 10)
        self.assertAlmostEqual(future_value, expected, places=2)
    
    def test_portfolio_total_value(self):
        """Test portfolio total value calculation."""
        expected = (100 * 400) + (200 * 80)  # $40,000 + $16,000
        self.assertEqual(self.portfolio.total_value, expected)
    
    def test_portfolio_asset_allocation(self):
        """Test portfolio asset allocation calculation."""
        allocation = self.portfolio.asset_allocation
        
        total_value = self.portfolio.total_value
        stock_allocation = (100 * 400) / total_value
        bond_allocation = (200 * 80) / total_value
        
        self.assertAlmostEqual(allocation[AssetClass.STOCKS], stock_allocation, places=4)
        self.assertAlmostEqual(allocation[AssetClass.BONDS], bond_allocation, places=4)
    
    def test_weighted_return_rate(self):
        """Test portfolio weighted return rate calculation."""
        weighted_return = self.portfolio.weighted_return_rate
        
        total_value = self.portfolio.total_value
        stock_weight = (100 * 400) / total_value
        bond_weight = (200 * 80) / total_value
        expected = (stock_weight * 0.07) + (bond_weight * 0.04)
        
        self.assertAlmostEqual(weighted_return, expected, places=4)


if __name__ == "__main__":
    unittest.main()