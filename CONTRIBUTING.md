# Contributing to Firefly

Thank you for your interest in contributing to Firefly! This document provides guidelines for developing and contributing to the application.

## Development Setup

### Prerequisites

- Node.js (v18 or higher)
- npm (v9 or higher)
- Git

### Initial Setup

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

4. Run the application in development mode:
   ```bash
   npm run dev
   ```

## Development Workflow

### Behavior-Driven Development (BDD)

**CRITICAL**: All FEATURE contributions must follow the Behavior-Driven Development process:

1. **Define behavioral requirements first** - Capture requirements as executable specifications in the `features/` directory using Gherkin syntax (Given-When-Then format)

2. **Create specifications before implementation** - Write the feature file describing the expected behavior

3. **Verify specifications fail first** - Run `npm test` to ensure the specifications fail (Red phase)

4. **Develop code to meet specifications** - Implement the minimum necessary code in `src/` to make the tests pass

5. **Validate all specifications pass** - Run `npm test` again to ensure all specifications pass (Green phase)

6. **Refactor** - Clean up the code while keeping all tests passing

### Testing Requirements

- **Specifications first**: Write executable behavioral specifications before any feature implementation
- **TDD approach**: All code must have comprehensive test coverage
- **Synthetic test data**: Create realistic test scenarios without manual data entry
- **Coverage requirements**: Maintain 95% test coverage standards

### Running Tests

```bash
# Run all BDD specifications
npm test

# Run unit tests (when available)
npm run test:unit

# Build the TypeScript code
npm run build
```

### Linting

```bash
# Lint the codebase
npm run lint
```

## Project Structure

```
firefly/
├── src/                    # TypeScript source code
│   ├── main.ts            # Electron main process
│   ├── renderer/          # Electron renderer process
│   ├── domains/           # Domain logic (organized by business capability)
│   │   ├── financial-data/
│   │   ├── investment-analysis/
│   │   ├── retirement-planning/
│   │   └── scenario-analysis/
│   └── shared/            # Shared utilities and types
├── features/              # BDD specifications (Cucumber/Gherkin)
├── tests/                 # Test support code
│   ├── steps/            # Cucumber step definitions
│   └── fixtures/         # Test data and fixtures
├── models/               # Data models and schemas
│   ├── schema/          # JSON schemas
│   └── samples/         # Sample data files
└── specifications/       # Requirements documentation
```

## Domain Architecture

Organize work by business domains, not technical layers:

- **Financial Data Management**: Core financial profile and data handling
- **Investment Analysis**: Portfolio management and performance tracking
- **Retirement Planning**: FIRE calculations and retirement projections
- **Scenario Analysis**: What-if modeling and comparative analysis

Each domain should have:
- Clear interfaces and data contracts
- Independent executable specifications
- Comprehensive test coverage
- Isolated development capabilities

## Coding Standards

### TypeScript Guidelines

- Use TypeScript's strict mode
- Define explicit types for all function parameters and return values
- Use interfaces for data contracts
- Avoid `any` type; use `unknown` when type is truly unknown

### Financial Data Handling

- Always use appropriate data types for currency (never use floating-point for money calculations)
- Use integers for cents/pennies or decimal libraries for precision
- Implement proper validation for financial inputs
- Consider edge cases (negative values, zero division, etc.)
- Ensure all financial calculations are accurate and auditable

### Code Style

- Write clean, readable code
- Use meaningful variable and function names
- Include comprehensive error handling
- Follow domain-driven design principles
- Document functions with accurate descriptions and parameter examples

## Commit Standards

We follow the Conventional Commits standard:

- `feat:` A new feature (correlates with MINOR in Semantic Versioning)
- `fix:` A bug fix (correlates with PATCH in Semantic Versioning)
- `docs:` Documentation changes
- `style:` Code style changes (formatting, missing semicolons, etc.)
- `refactor:` Code refactoring without changing functionality
- `test:` Adding or updating tests
- `chore:` Maintenance tasks, dependency updates, etc.
- `ci:` CI/CD configuration changes

Example:
```
feat: implement coast fire phase configuration

- Add phase boundary calculations
- Support dynamic phase adjustment
- Update projections based on phase changes
```

## Pull Request Process

1. Create a feature branch from `main`:
   ```bash
   git checkout -b feat/your-feature-name
   ```

2. Follow the BDD process (specifications first, then implementation)

3. Ensure all tests pass:
   ```bash
   npm test
   ```

4. Ensure code is linted:
   ```bash
   npm run lint
   ```

5. Commit your changes following conventional commits

6. Push your branch and create a pull request

7. Ensure CI checks pass

## CI/CD Pipeline

The project uses GitHub Actions for continuous integration and deployment:

- **On Pull Request**: Runs linting, builds, and tests
- **On Merge to Main**: Creates release builds for macOS, Windows, and Linux

All specifications must pass before code can be merged.

## Security Considerations

- Never hardcode sensitive information
- Implement proper input validation and sanitization
- Use secure methods for storing and transmitting financial data
- Follow OWASP guidelines for application security
- Run security audits on dependencies regularly

## Getting Help

- Review existing [specifications](./specifications/requirements-v1.md)
- Check [data models documentation](./models/data-models.md)
- Refer to the [README](./README.md) for project overview

## License

By contributing to Firefly, you agree that your contributions will be licensed under the project's license.
