# Firefly

Firefly is a comprehensive financial independence and retirement planning application that helps users track their financial journey toward FIRE (Financial Independence, Retire Early). The application provides users with a holistic view of their finances, enabling them to create tailored plans for their unique goals and model various 'what-if' scenarios to achieve financial independence and retire on their terms.

## Goals and Key Features

### 📊 Core Financial Planning
- **Comprehensive Financial Profiling**: Track income, expenses, assets, debts, and savings with automatic validation
- **Retirement Planning**: Calculate required savings, portfolio values, and retirement readiness scores
- **Investment Portfolio Management**: Model different asset allocations and expected returns
- **FIRE Calculations**: Support for Financial Independence, Retire Early planning with multiple FIRE types (Lean, Coast, Barista, Fat)

### 🔍 Advanced Analysis
- **What-If Scenario Analysis**: Multiple scenario types including income changes, savings rate adjustments, retirement age variations, and market conditions
- **Monte Carlo Simulations**: Probabilistic analysis of retirement success with comprehensive simulations
- **Year-by-Year Projections**: Detailed breakdown of financial growth from current age to retirement
- **Retirement Withdrawal Modeling**: Project portfolio sustainability during retirement years

### 💻 User Interface
- **Electron Desktop App**: Native desktop application for Windows, macOS, and Linux
- **Interactive UI**: User-friendly interface for comprehensive financial analysis
- **Professional Output**: Formatted tables and comprehensive analysis reports
- **Input Validation**: Robust error handling and data validation throughout

## Current Implementation Status

**Version 0.1.0** - Feature v1-001 Complete

✅ **Implemented Features:**
- Feature v1-001: Configure Coast FIRE plan phases
  - Create default phase boundaries (Accumulation, Coast, Retirement)
  - Adjust target coast start age dynamically
  - Automatic phase boundary recalculation
  - Annual timeline projection updates

## Getting Started

### Prerequisites

- Node.js (v18 or higher)
- npm (v9 or higher)
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bspain/firefly.git
   cd firefly
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Build the application:
   ```bash
   npm run build
   ```

4. Run the application:
   ```bash
   npm start
   ```

### Development Mode

For development with automatic rebuilds:

```bash
npm run dev
```

### Running Tests

```bash
# Run BDD specifications
npm test

# Run linter
npm run lint
```

### Building Distributable Packages

To create installable packages for your platform:

```bash
npm run package
```

This will create platform-specific installers in the `release/` directory:
- **macOS**: .dmg file
- **Windows**: .exe installer
- **Linux**: .AppImage file

## Using the Application

### Loading a Plan

1. Launch the application
2. Click **"Load Sample Plan"** to load the pre-configured Coast FIRE scenario
3. Or click **"Load Plan"** to open your own plan file

### Configuring Phase Boundaries (Feature v1-001)

The application displays three phases:
- **📈 Accumulation Phase**: Active contribution years
- **🏖️ Coast Phase**: No contributions, investment growth only
- **🌴 Retirement Phase**: Withdrawal phase

To adjust the coast start age:
1. Enter a new age in the "Target Coast Start Age" field
2. Click **"Update Coast Age"**
3. The phase boundaries will automatically recalculate
4. The accumulation phase end age adjusts accordingly

### Sample Data

A sample Coast FIRE plan is included at `models/samples/coast-fire-001.json`:
- User age: 48
- Current phases: Accumulation (22-49), Coast (50-65), Retirement (66-100)
- Comprehensive asset and liability tracking
- Income and expense assumptions

## Project Structure

```
firefly/
├── src/                    # TypeScript source code
│   ├── main.ts            # Electron main process
│   ├── preload.ts         # Preload script for IPC
│   ├── renderer/          # Electron renderer process (UI)
│   ├── domains/           # Domain logic (organized by business capability)
│   │   └── retirement-planning/
│   │       ├── phase-config.ts    # Phase boundary logic
│   │       ├── plan-service.ts    # Plan management
│   │       └── projections.ts     # Financial projections
│   └── shared/            # Shared utilities and types
├── features/              # BDD specifications (Cucumber/Gherkin)
├── tests/                 # Test support code
│   └── steps/            # Cucumber step definitions
├── models/               # Data models and schemas
│   ├── schema/          # JSON schemas
│   └── samples/         # Sample data files
└── specifications/       # Requirements documentation
```

## Development

See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed development guidelines.

### Key Principles

- **BDD-First**: All features start with executable specifications
- **TDD**: Comprehensive test coverage required
- **Domain-Driven Design**: Code organized by business capability
- **Trunk-Based Development**: Small, short-lived feature branches

## Project Vision

Firefly aims to democratize sophisticated financial planning tools by providing:
- Accurate financial calculations and projections
- Multiple scenario modeling capabilities  
- Comprehensive retirement planning tools
- Clear, actionable insights for financial decision-making

## License

ISC

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on how to contribute to this project.
