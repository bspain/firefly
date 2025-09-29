# Contributing to Firefly

Welcome to the Firefly project! This document outlines our Software Development Lifecycle (SDLC) practices and contribution guidelines.

## Our SDLC Philosophy

Firefly follows a **Behavior-Driven Development (BDD)** approach that prioritizes executable specifications and comprehensive testing. Our goal is to enable independent work on different application experiences while maintaining high quality and reliability.

## Development Workflow

### The Core SDLC Process

Each "batch" of work follows this structured approach:

1. **Define Behavioral Requirements**
   - Capture requirements as executable specifications
   - Use Given-When-Then format to describe application behavior
   - Focus on user experiences and business value

2. **Create Executable Specifications**
   - Write specifications in code before implementation
   - Ensure specifications are clear, testable, and focused
   - Specifications should initially fail (Red phase)

3. **Verify Specifications Fail First**
   - Run specifications to confirm they fail as expected
   - This validates that specifications actually test the intended behavior
   - Follow true BDD "Red-Green-Refactor" cycle

4. **Develop Code to Meet Requirements**
   - Implement the minimum code necessary to make specifications pass
   - Follow TDD practices with comprehensive unit test coverage
   - Maintain clean, readable, and well-documented code

5. **Validate All Specifications Pass**
   - Ensure all new and existing specifications pass
   - Verify that changes don't break existing functionality
   - Maintain high code coverage standards

6. **CI/CD Pipeline Validation**
   - All specifications must pass in continuous integration
   - Automated testing validates the complete application
   - No pull request can be merged without passing specifications

7. **Deploy to Production**
   - Successful CI validation triggers continuous deployment
   - Production deployments are automated and reliable
   - Rollback procedures are available if issues arise

### Domain Architecture

The application is organized into distinct domains to support independent development:

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

## Contribution Guidelines

### Before You Start

1. **Understand the Domain**: Review relevant domain documentation and existing specifications
2. **Define the Experience**: Clearly articulate what user experience you're building
3. **Write Specifications First**: Create executable specifications before any implementation code

### Development Standards

#### Testing Requirements
- **100% specification coverage**: Every behavioral requirement must have executable specifications
- **Comprehensive unit tests**: All code must have thorough unit test coverage
- **Integration testing**: Validate interfaces between domains
- **Synthetic test data**: Create realistic test scenarios that don't require manual data entry

#### Code Quality
- **Clean code principles**: Write readable, maintainable, and well-documented code
- **Domain-driven design**: Organize code by business domain, not technical layers
- **Separation of concerns**: Keep business logic separate from infrastructure concerns
- **Financial accuracy**: Ensure all financial calculations are precise and auditable

#### Documentation
- **Specification documentation**: Clearly describe behavioral requirements
- **API documentation**: Document all interfaces and data contracts
- **Domain glossaries**: Maintain clear definitions of business terms
- **Architecture decisions**: Record significant design choices and rationale

### Pull Request Process

1. **Create Feature Branch**: Branch from main for each new feature or fix
2. **Write Specifications**: Create executable specifications for the intended behavior
3. **Implement Solution**: Write minimum code to satisfy specifications
4. **Verify Quality**: Ensure all tests pass and code meets quality standards
5. **Submit PR**: Include clear description of changes and business value
6. **Code Review**: At least one reviewer must approve changes
7. **CI Validation**: All automated checks must pass
8. **Merge and Deploy**: Successful validation triggers automatic deployment

### Isolated Development

Our SDLC supports three distinct experiences that can be developed independently:

1. **Data Creation Experience**: Creating profiles and initial financial data
2. **Analysis Experience**: Analyzing existing financial data and projections
3. **Data Update Experience**: Modifying and maintaining financial information

Each experience should:
- Have isolated executable specifications
- Use synthetic data for testing
- Be developable without dependencies on other experiences
- Have clear interfaces for data exchange

## Quality Assurance

### Automated Testing Strategy
- **Unit Tests**: Test individual components and calculations
- **Integration Tests**: Validate domain interactions
- **End-to-End Tests**: Verify complete user workflows
- **Performance Tests**: Ensure financial calculations are efficient
- **Security Tests**: Validate data protection and privacy

### Continuous Integration
- **Build Validation**: Code must compile and build successfully
- **Test Execution**: All specifications and tests must pass
- **Code Quality**: Maintain coding standards and coverage thresholds
- **Security Scanning**: Check for vulnerabilities and sensitive data
- **Documentation**: Verify documentation is current and complete

## Financial Domain Considerations

### Data Accuracy
- Use appropriate data types for currency calculations
- Avoid floating-point arithmetic for money values
- Implement proper rounding and precision handling
- Validate all financial inputs and calculations

### Security and Privacy
- Never store sensitive financial information in plain text
- Implement proper input validation and sanitization
- Follow OWASP guidelines for financial applications
- Ensure audit trails for all financial transactions

### Regulatory Compliance
- Document all financial calculation methodologies
- Provide references for financial formulas and approaches
- Ensure calculations are verifiable and auditable
- Consider regulatory requirements for financial planning tools

## Getting Help

If you have questions about contributing or need clarification on the SDLC process:

1. Review existing specifications and documentation
2. Check domain-specific guidelines and glossaries
3. Reach out to domain experts for technical guidance
4. Participate in code reviews to learn best practices

Thank you for contributing to Firefly and helping users achieve their financial independence goals!