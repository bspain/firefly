# Copilot Instructions for Firefly

## Project Overview
Firefly is a comprehensive financial independence and retirement planning application that helps users track their financial journey toward FIRE (Financial Independence, Retire Early). The application provides users with a holistic view of their finances, enabling them to create tailored plans for their unique goals and model various 'what-if' scenarios to achieve financial independence and retire on their terms.

## Application Goals
Refer to the README.md for complete details, but key goals include:
- Comprehensive financial profiling and tracking
- Advanced retirement planning and FIRE calculations
- What-if scenario analysis and Monte Carlo simulations
- Interactive interfaces with professional output and validation

## Development Philosophy
Contributions to this codebase adhere to the conventional commit standard:
- "fix:" a commit of the type FIX patches a bug in the codebase (this correlates with PATCH in Semantic Versioning).
- "feat:" a commit of the type feat introduces a new FEATURE to the codebase (this correlates with MINOR in Semantic Versioning).

types other than fix: and feat: are allowed, for example build:, chore:, ci:, docs:, style:, refactor:, perf:, test:, and others.

### SDLC Requirements
**CRITICAL**: All FEATURE contributions must follow the Behavior-Driven Development (BDD) process:

1. **Define behavioral requirements first** - capture as executable specifications
2. **Create specifications before implementation** - use Given-When-Then format
3. **Verify specifications fail first** - ensure Red-Green-Refactor cycle
4. **Develop code to meet specifications** - implement minimum necessary code
5. **Validate all specifications pass** - maintain comprehensive coverage
6. **CI/CD pipeline compliance** - all specifications must pass before merge

All FIX contributions must follow standard Testing Strategy (MANDITORY) guidelines below

### Domain Architecture
Organize work by business domains, not technical layers:
- **Financial Data Management**: Core financial profile and data handling
- **Investment Analysis**: Portfolio management and performance tracking  
- **Retirement Planning**: FIRE calculations and retirement projections
- **Scenario Analysis**: What-if modeling and comparative analysis
- **User Interfaces**: CLI, web dashboard, and API layers

Each domain should have:
- Clear interfaces and data contracts
- Independent executable specifications
- Comprehensive test coverage
- Isolated development capabilities

## Coding Guidelines

### Testing Strategy (MANDATORY)
- **Specifications first**: Write executable behavioral specifications before any feature implementation
- **TDD approach**: All code must have comprehensive unit test coverage
- **Synthetic test data**: Create realistic test scenarios without manual data entry
- **Isolated testing**: Enable independent development of different user experiences
- **Coverage requirements**: Maintain 95% test coverage standards

### Language and Framework Preferences
- Use modern, well-supported languages and frameworks appropriate for financial applications
- Prioritize security, accuracy, and performance in financial calculations
- Follow industry best practices for handling financial data

### Code Style
- Write clean, readable code
- Use meaningful variable and function names, especially for financial terms
- Include comprehensive error handling for financial calculations
- Follow domain-driven design principles

### Financial Data Handling
- Always use appropriate data types for currency (avoid floating-point arithmetic for money)
- Implement proper validation for financial inputs
- Consider edge cases in financial calculations (negative values, zero division, etc.)
- Ensure all financial calculations are accurate and auditable

### Security Considerations
- Never hardcode sensitive financial information
- Implement proper input validation and sanitization
- Use secure methods for storing and transmitting financial data
- Follow OWASP guidelines for web application security

### Documentation
- Document all functions with accurate descriptions
- Document all function paramaters with pertinent examples
- Provide clear examples for financial functions
- Include references to financial concepts and methodologies used
- Maintain a glossary of financial terms used in the codebase

## Project Structure
- Keep financial calculation logic separate from presentation layer
- Organize code by financial domain (investments, budgeting, retirement planning, etc.)
- Use clear module/package names that reflect financial concepts
- Design for independent development of user experiences

## Dependencies
- Prefer well-maintained, security-audited libraries
- Avoid dependencies with known security vulnerabilities
- Keep dependencies minimal and focused on project needs
- Regularly update dependencies to maintain security

## Contribution Guidelines

### Pre-Implementation Requirements
- **ALWAYS** start with behavioral specifications for FEATURES using Given-When-Then format
- Ensure specifications cover the intended user experience completely
- Validate that specifications fail before implementing code (Red phase)
- Design for testability and isolated development

### Implementation Standards
- All financial calculations should be reviewed by at least one other developer
- Include tests that verify calculations with known expected results
- Document the source of any financial formulas or methodologies used
- Consider the impact of changes on existing user data and calculations
- Follow the complete BDD cycle: Red-Green-Refactor
- Adhere to trunk-based development: Feature branches should be scoped small and short-lived

### Quality Assurance
- Maintain 100% specification coverage for behavioral requirements
- Ensure comprehensive unit test coverage for all code
- Validate that changes don't break existing functionality
- Test with realistic synthetic data that doesn't require manual setup

## User Experience Focus

The application supports three distinct experiences that must be developable independently:

1. **Data Creation Experience**: Creating profiles and initial financial data
2. **Analysis Experience**: Analyzing existing financial data and projections  
3. **Data Update Experience**: Modifying and maintaining financial information

When working on any feature:
- Clearly identify which experience(s) you're addressing
- Create specifications that test the experience in isolation
- Use synthetic data to avoid dependencies on manual data entry
- Design interfaces that support independent development

## Integration with CI/CD

Remember that this project aims for:
- Automated specification execution in CI pipelines
- Continuous deployment upon successful validation
- No manual intervention required for releases
- Rollback capabilities for production issues

All code contributions must support this automated pipeline approach.
