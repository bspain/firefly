"""
Configuration settings for Firefly application
"""

# Default financial assumptions
DEFAULT_INVESTMENT_RETURN_RATE = 0.07  # 7% annual return
DEFAULT_INFLATION_RATE = 0.025  # 2.5% annual inflation
DEFAULT_SAFE_WITHDRAWAL_RATE = 0.04  # 4% safe withdrawal rate
DEFAULT_INCOME_GROWTH_RATE = 0.03  # 3% annual income growth
DEFAULT_EXPENSE_GROWTH_RATE = 0.025  # 2.5% annual expense growth

# Retirement planning defaults
DEFAULT_RETIREMENT_AGE = 65
DEFAULT_INCOME_REPLACEMENT_RATIO = 0.8  # 80% of pre-retirement income
DEFAULT_SOCIAL_SECURITY_RATIO = 0.25  # 25% of income from Social Security

# Investment portfolio defaults
DEFAULT_STOCK_ALLOCATION = 0.7  # 70% stocks
DEFAULT_BOND_ALLOCATION = 0.3  # 30% bonds
DEFAULT_STOCK_RETURN = 0.10  # 10% expected stock return
DEFAULT_BOND_RETURN = 0.04  # 4% expected bond return
DEFAULT_MARKET_VOLATILITY = 0.15  # 15% annual volatility

# FIRE (Financial Independence, Retire Early) constants
FIRE_WITHDRAWAL_RATE = 0.04  # 4% rule
FIRE_MULTIPLIER = 25  # 25x annual expenses
LEAN_FIRE_RATIO = 0.6  # 60% of normal expenses
FAT_FIRE_RATIO = 1.5  # 150% of normal expenses
BARISTA_FIRE_RATIO = 0.7  # 70% of normal expenses (essentials)

# Monte Carlo simulation settings
DEFAULT_MONTE_CARLO_SIMULATIONS = 1000
DEFAULT_MONTE_CARLO_SUCCESS_THRESHOLD = 0.9  # 90% success rate target

# Application settings
APP_NAME = "Firefly"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Financial Independence and Retirement Planning"

# Display settings
CURRENCY_SYMBOL = "$"
DEFAULT_DECIMAL_PLACES = 2
PERCENTAGE_DECIMAL_PLACES = 1

# Validation limits
MIN_AGE = 18
MAX_AGE = 120
MIN_RETIREMENT_AGE = 50
MAX_RETIREMENT_AGE = 80
MAX_INCOME = 10_000_000  # $10M annually
MAX_SAVINGS_RATE = 0.8  # 80%
MAX_EXPENSE_RATIO = 2.0  # 200% of income

# File paths and data storage
DEFAULT_PROFILE_FILE = "financial_profile.json"
DEFAULT_REPORTS_DIR = "reports"
DEFAULT_CHARTS_DIR = "charts"