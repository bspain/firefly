# Copilot Instructions for Firefly

## Project Overview
Firefly is a financial independence and retirement planning project. This repository helps users track their financial journey toward FIRE (Financial Independence, Retire Early).

## Coding Guidelines

### Language and Framework Preferences
- Use modern, well-supported languages and frameworks appropriate for financial applications
- Prioritize security, accuracy, and performance in financial calculations
- Follow industry best practices for handling financial data

### Code Style
- Write clean, readable, and well-documented code
- Use meaningful variable and function names, especially for financial terms
- Include comprehensive error handling for financial calculations
- Add unit tests for all financial calculations and core business logic

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
- Document all financial formulas and calculations
- Provide clear examples for financial functions
- Include references to financial concepts and methodologies used
- Maintain a glossary of financial terms used in the codebase

### Testing
- Write comprehensive tests for all financial calculations
- Include edge case testing for financial scenarios
- Test with realistic financial data ranges
- Validate calculations against known financial formulas

## Project Structure
- Keep financial calculation logic separate from presentation layer
- Organize code by financial domain (investments, budgeting, retirement planning, etc.)
- Use clear module/package names that reflect financial concepts

## Dependencies
- Prefer well-maintained, security-audited libraries
- Avoid dependencies with known security vulnerabilities
- Keep dependencies minimal and focused on project needs
- Regularly update dependencies to maintain security

## Contribution Guidelines
- All financial calculations should be reviewed by at least one other developer
- Include tests that verify calculations with known expected results
- Document the source of any financial formulas or methodologies used
- Consider the impact of changes on existing user data and calculations