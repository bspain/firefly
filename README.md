# Firefly 🔥
## Financial Independence and Retirement Planning Application

Firefly is a comprehensive financial planning and retirement projection application that provides users with a holistic view of their finances, enabling them to create tailored plans for their unique goals and model various 'what-if' scenarios. This helps users achieve financial independence and retire on their terms.

## Features 🚀

### Core Functionality
- **Comprehensive Financial Profiling**: Track income, expenses, assets, debts, and savings
- **Retirement Planning**: Calculate required savings for retirement goals
- **Investment Portfolio Management**: Model different asset allocations and returns
- **Scenario Analysis**: Run "what-if" scenarios to understand impact of changes
- **FIRE Calculations**: Support for Financial Independence, Retire Early planning
- **Monte Carlo Simulations**: Probabilistic analysis of retirement success

### Key Capabilities
- **Holistic Financial View**: Complete picture of your financial situation
- **Tailored Planning**: Customized recommendations based on your unique goals
- **Interactive Analysis**: Command-line interface for easy exploration
- **Flexible Modeling**: Adjust assumptions and see immediate impact
- **Detailed Projections**: Year-by-year breakdown of financial growth

## Installation 📦

### Requirements
- Python 3.8 or higher
- pip package manager

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Install Application
```bash
pip install -e .
```

## Quick Start 🏁

### 1. Create Your Financial Profile
```bash
python main.py create-profile
```

This interactive command will guide you through creating your financial profile including:
- Personal information (age, retirement goals)
- Income and expenses
- Current savings and investments
- Debts and liabilities

### 2. Analyze Your Financial Situation
```bash
python main.py analyze
```

Get a comprehensive analysis of your retirement readiness including:
- Retirement readiness score
- Required monthly savings
- Gap analysis
- Personalized recommendations

### 3. Run What-If Scenarios
```bash
python main.py scenarios
```

Explore various scenarios such as:
- Income changes (raises, job loss)
- Different savings rates
- Early/late retirement
- Market conditions
- Debt payoff strategies

### 4. Generate Detailed Projections
```bash
python main.py project
```

Create detailed projections including:
- Year-by-year financial growth
- FIRE (Financial Independence, Retire Early) metrics
- Monte Carlo probability analysis
- Retirement withdrawal scenarios

## Example Usage 💡

### Sample Analysis Output
```
=== Financial Analysis ===
┌─────────────────────────────┬──────────────┐
│ Metric                      │ Value        │
├─────────────────────────────┼──────────────┤
│ Retirement Readiness Score  │ 67.3%        │
│ Required Portfolio Value    │ $1,050,000   │
│ Current Assets              │ $105,000     │
│ Gap to Fill                 │ $945,000     │
│ Required Monthly Savings    │ $1,456       │
│ Current Monthly Savings     │ $1,200       │
│ Monthly Savings Gap         │ $256         │
└─────────────────────────────┴──────────────┘

=== Recommendations ===
⚠ On track but room for improvement. Consider increasing savings.
• Consider increasing monthly savings by $256
• Target savings rate: 15-20% (current: 19.2%)
```

### Scenario Analysis Example
```
=== What-If Scenario Analysis ===
┌──────────────────────────┬─────────────────┬──────────────────────┬─────────────┐
│ Scenario                 │ Readiness Score │ Monthly Savings Needed │ Years to FI │
├──────────────────────────┼─────────────────┼──────────────────────┼─────────────┤
│ 20% Income Increase      │ 78.9%           │ $1,156               │ 23 years    │
│ 10% Income Decrease      │ 58.2%           │ $1,687               │ 29 years    │
│ Increase Savings to 20%  │ 82.4%           │ $1,100               │ 21 years    │
│ Retire 5 Years Earlier   │ 51.7%           │ $2,134               │ 25 years    │
│ Conservative 5% Returns  │ 45.8%           │ $2,287               │ 32 years    │
│ Aggressive 9% Returns    │ 89.6%           │ $967                 │ 19 years    │
│ 30% Market Crash        │ 47.1%           │ $1,823               │ 31 years    │
└──────────────────────────┴─────────────────┴──────────────────────┴─────────────┘
```

## Architecture 🏗️

### Project Structure
```
firefly/
├── firefly/                 # Main application package
│   ├── models/              # Data models
│   │   ├── financial_data.py    # User financial profile
│   │   ├── portfolio.py         # Investment portfolio
│   │   └── retirement_plan.py   # Retirement planning
│   ├── calculations/        # Financial calculation engines
│   │   ├── financial_calculator.py  # Core calculations
│   │   ├── scenario_analyzer.py     # What-if analysis
│   │   └── retirement_projector.py  # Retirement projections
│   ├── ui/                  # User interfaces
│   │   ├── cli.py               # Command-line interface
│   │   └── dashboard.py         # Dashboard (future)
│   └── utils/               # Utilities
│       ├── formatters.py        # Display formatting
│       └── validators.py        # Input validation
├── tests/                   # Unit tests
├── main.py                  # Application entry point
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

### Key Components

#### Financial Models
- **FinancialProfile**: Complete user financial situation
- **RetirementPlan**: Retirement goals and assumptions  
- **Portfolio**: Investment holdings and asset allocation

#### Calculation Engines
- **FinancialCalculator**: Core financial math functions
- **ScenarioAnalyzer**: What-if scenario modeling
- **RetirementProjector**: Detailed retirement projections

#### User Interface
- **CLI**: Interactive command-line interface
- **Formatters**: Pretty-print financial data
- **Validators**: Input validation and error checking

## Financial Concepts 📈

### FIRE (Financial Independence, Retire Early)
- **FIRE Number**: 25x annual expenses for 4% withdrawal rate
- **Lean FIRE**: Minimal expenses (60% of normal)
- **Coast FIRE**: Enough invested to grow to FIRE by retirement
- **Barista FIRE**: Enough for essential expenses (70%)
- **Fat FIRE**: Comfortable lifestyle (150% of normal)

### Retirement Planning
- **4% Rule**: Safe withdrawal rate in retirement
- **Replacement Ratio**: Percentage of pre-retirement income needed
- **Glide Path**: Asset allocation changes over time
- **Monte Carlo**: Probabilistic success analysis

### Investment Concepts
- **Asset Allocation**: Mix of stocks, bonds, and other investments
- **Rebalancing**: Maintaining target allocation over time
- **Dollar-Cost Averaging**: Regular investment regardless of market
- **Compound Growth**: Reinvestment of returns for exponential growth

## Testing 🧪

Run the test suite:
```bash
python -m pytest tests/
```

Or run individual test files:
```bash
python -m unittest tests.test_models
```

## Configuration ⚙️

Key configuration options in `config.py`:
- Investment return assumptions
- Inflation rates
- Withdrawal rates
- Default retirement age
- Risk tolerance settings

## Contributing 🤝

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer ⚠️

This application is for educational and planning purposes only. It does not constitute financial advice. Always consult with qualified financial professionals for important financial decisions.

## Support 💬

For questions, issues, or feature requests, please open an issue on GitHub.

---

**Firefly** - Helping you achieve financial independence and retire on your terms! 🔥🚀
