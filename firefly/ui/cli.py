"""
Command Line Interface for Firefly

Provides interactive CLI for financial planning and retirement projections.
"""

import click
from datetime import datetime, date
from typing import Optional
from tabulate import tabulate

from ..models.financial_data import FinancialProfile
from ..models.retirement_plan import RetirementPlan
from ..calculations.scenario_analyzer import ScenarioAnalyzer
from ..calculations.retirement_projector import RetirementProjector
from ..utils.formatters import format_currency, format_percentage


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """
    Firefly - Financial Independence and Retirement Planning
    
    A comprehensive tool for financial planning that helps you create tailored
    plans for your unique goals and model various 'what-if' scenarios.
    """
    pass


@cli.command()
def create_profile():
    """Create a new financial profile interactively."""
    click.echo("=== Create Your Financial Profile ===\n")
    
    # Personal Information
    name = click.prompt("Full name")
    birth_year = click.prompt("Birth year", type=int)
    birth_month = click.prompt("Birth month (1-12)", type=int)
    birth_day = click.prompt("Birth day", type=int)
    birth_date = date(birth_year, birth_month, birth_day)
    
    retirement_age = click.prompt("Target retirement age", default=65, type=int)
    
    # Income
    annual_income = click.prompt("Annual income", type=float)
    income_growth_rate = click.prompt("Expected annual income growth rate", default=0.03, type=float)
    
    # Expenses
    monthly_expenses = click.prompt("Monthly expenses", type=float)
    expense_growth_rate = click.prompt("Expected annual expense growth rate", default=0.025, type=float)
    
    # Savings
    current_savings = click.prompt("Current savings/cash", default=0.0, type=float)
    monthly_savings = click.prompt("Monthly savings amount", default=0.0, type=float)
    
    # Create profile
    profile = FinancialProfile(
        name=name,
        birth_date=birth_date,
        retirement_age=retirement_age,
        annual_income=annual_income,
        income_growth_rate=income_growth_rate,
        monthly_expenses=monthly_expenses,
        expense_growth_rate=expense_growth_rate,
        current_savings=current_savings,
        monthly_savings=monthly_savings
    )
    
    # Display summary
    display_profile_summary(profile)
    
    # Ask if user wants to add investments/debts
    if click.confirm("Would you like to add investment accounts?"):
        add_investment_accounts(profile)
    
    if click.confirm("Would you like to add retirement accounts?"):
        add_retirement_accounts(profile)
    
    if click.confirm("Would you like to add debts?"):
        add_debts(profile)
    
    click.echo(f"\n✓ Profile created successfully for {profile.name}!")
    return profile


@cli.command()
@click.option('--profile-file', help='Load profile from file')
def analyze(profile_file: Optional[str]):
    """Analyze financial situation and retirement readiness."""
    
    # For demo, create a sample profile if no file provided
    if not profile_file:
        click.echo("Creating sample profile for demonstration...\n")
        profile = create_sample_profile()
    else:
        # In a real implementation, this would load from file
        click.echo(f"Loading profile from {profile_file}...")
        profile = create_sample_profile()
    
    # Create retirement plan
    plan = RetirementPlan(
        target_retirement_age=profile.retirement_age,
        target_annual_income=profile.annual_income * 0.8,  # 80% replacement
        target_income_replacement_ratio=0.8,
        estimated_social_security=profile.annual_income * 0.25  # Rough estimate
    )
    
    # Display analysis
    display_financial_analysis(profile, plan)


@cli.command()
@click.option('--profile-file', help='Load profile from file')
def scenarios(profile_file: Optional[str]):
    """Run what-if scenario analysis."""
    
    # For demo, create a sample profile if no file provided
    if not profile_file:
        profile = create_sample_profile()
    else:
        profile = create_sample_profile()
    
    plan = RetirementPlan(
        target_retirement_age=profile.retirement_age,
        target_annual_income=profile.annual_income * 0.8,
        estimated_social_security=profile.annual_income * 0.25
    )
    
    click.echo("=== What-If Scenario Analysis ===\n")
    
    analyzer = ScenarioAnalyzer(profile, plan)
    
    # Run various scenarios
    scenarios_to_run = [
        ("20% Income Increase", analyzer.analyze_income_change(0.20)),
        ("10% Income Decrease", analyzer.analyze_income_change(-0.10)),
        ("Increase Savings Rate to 20%", analyzer.analyze_savings_rate_change(0.20)),
        ("Retire 5 Years Earlier", analyzer.analyze_retirement_age_change(profile.retirement_age - 5)),
        ("Conservative 5% Returns", analyzer.analyze_return_rate_change(0.05)),
        ("Aggressive 9% Returns", analyzer.analyze_return_rate_change(0.09)),
        ("30% Market Crash", analyzer.analyze_market_crash(-0.30))
    ]
    
    results = [result for _, result in scenarios_to_run]
    
    # Display scenario results
    display_scenario_results(results)
    
    # Display comparison
    comparison = analyzer.compare_scenarios(results)
    display_scenario_comparison(comparison)


@cli.command()
@click.option('--profile-file', help='Load profile from file')
def project(profile_file: Optional[str]):
    """Generate detailed retirement projections."""
    
    if not profile_file:
        profile = create_sample_profile()
    else:
        profile = create_sample_profile()
    
    plan = RetirementPlan(
        target_retirement_age=profile.retirement_age,
        target_annual_income=profile.annual_income * 0.8,
        estimated_social_security=profile.annual_income * 0.25
    )
    
    projector = RetirementProjector(profile, plan)
    
    click.echo("=== Retirement Projections ===\n")
    
    # Generate projections
    retirement_proj = projector.project_to_retirement()
    fire_metrics = projector.calculate_fire_metrics()
    
    # Display projections
    display_retirement_projections(retirement_proj, fire_metrics)
    
    # Monte Carlo analysis
    if click.confirm("\nWould you like to run Monte Carlo analysis?"):
        monte_carlo = projector.monte_carlo_retirement_analysis()
        display_monte_carlo_results(monte_carlo)


def create_sample_profile() -> FinancialProfile:
    """Create a sample financial profile for demonstration."""
    return FinancialProfile(
        name="Sample User",
        birth_date=date(1985, 6, 15),
        retirement_age=65,
        annual_income=75000,
        income_growth_rate=0.03,
        monthly_expenses=4500,
        expense_growth_rate=0.025,
        current_savings=25000,
        monthly_savings=1200,
        investment_accounts={"401k": 45000, "IRA": 15000},
        retirement_accounts={"Roth IRA": 20000},
        debts={"Mortgage": 180000, "Car Loan": 12000}
    )


def add_investment_accounts(profile: FinancialProfile):
    """Add investment accounts to profile."""
    while True:
        account_name = click.prompt("Investment account name (or 'done' to finish)")
        if account_name.lower() == 'done':
            break
        balance = click.prompt(f"Current balance for {account_name}", type=float)
        profile.investment_accounts[account_name] = balance


def add_retirement_accounts(profile: FinancialProfile):
    """Add retirement accounts to profile."""
    while True:
        account_name = click.prompt("Retirement account name (or 'done' to finish)")
        if account_name.lower() == 'done':
            break
        balance = click.prompt(f"Current balance for {account_name}", type=float)
        profile.retirement_accounts[account_name] = balance


def add_debts(profile: FinancialProfile):
    """Add debts to profile."""
    while True:
        debt_name = click.prompt("Debt name (or 'done' to finish)")
        if debt_name.lower() == 'done':
            break
        balance = click.prompt(f"Current balance for {debt_name}", type=float)
        profile.debts[debt_name] = balance


def display_profile_summary(profile: FinancialProfile):
    """Display a summary of the financial profile."""
    click.echo("\n=== Financial Profile Summary ===")
    
    data = [
        ["Name", profile.name],
        ["Age", profile.age],
        ["Years to Retirement", profile.years_to_retirement],
        ["Annual Income", format_currency(profile.annual_income)],
        ["Monthly Expenses", format_currency(profile.monthly_expenses)],
        ["Monthly Savings", format_currency(profile.monthly_savings)],
        ["Savings Rate", format_percentage(profile.savings_rate)],
        ["Current Net Worth", format_currency(profile.net_worth)],
        ["Total Assets", format_currency(profile.total_assets)],
        ["Total Debts", format_currency(profile.total_debts)]
    ]
    
    click.echo(tabulate(data, headers=["Metric", "Value"], tablefmt="grid"))


def display_financial_analysis(profile: FinancialProfile, plan: RetirementPlan):
    """Display comprehensive financial analysis."""
    click.echo("=== Financial Analysis ===\n")
    
    # Calculate key metrics
    readiness_score = plan.calculate_retirement_readiness_score(profile)
    required_savings = plan.calculate_monthly_savings_needed(profile)
    required_portfolio = plan.calculate_required_portfolio_value(profile)
    
    # Basic metrics
    data = [
        ["Retirement Readiness Score", f"{readiness_score:.1f}%"],
        ["Required Portfolio Value", format_currency(required_portfolio)],
        ["Current Assets", format_currency(profile.total_assets)],
        ["Gap to Fill", format_currency(max(0, required_portfolio - profile.total_assets))],
        ["Required Monthly Savings", format_currency(required_savings)],
        ["Current Monthly Savings", format_currency(profile.monthly_savings)],
        ["Monthly Savings Gap", format_currency(max(0, required_savings - profile.monthly_savings))]
    ]
    
    click.echo(tabulate(data, headers=["Metric", "Value"], tablefmt="grid"))
    
    # Recommendations
    click.echo("\n=== Recommendations ===")
    
    if readiness_score >= 90:
        click.echo("✓ Excellent! You're well on track for retirement.")
    elif readiness_score >= 70:
        click.echo("✓ Good progress! Minor adjustments may help optimize your plan.")
    elif readiness_score >= 50:
        click.echo("⚠ On track but room for improvement. Consider increasing savings.")
    else:
        click.echo("⚠ Significant changes needed to meet retirement goals.")
    
    if required_savings > profile.monthly_savings:
        gap = required_savings - profile.monthly_savings
        click.echo(f"• Consider increasing monthly savings by {format_currency(gap)}")
    
    if profile.savings_rate < 0.15:
        click.echo(f"• Target savings rate: 15-20% (current: {format_percentage(profile.savings_rate)})")


def display_scenario_results(results):
    """Display scenario analysis results."""
    data = []
    for result in results:
        data.append([
            result.scenario_name,
            f"{result.retirement_readiness_score:.1f}%",
            format_currency(result.required_monthly_savings),
            f"{result.years_to_fi} years" if result.years_to_fi > 0 else "Achieved"
        ])
    
    headers = ["Scenario", "Readiness Score", "Monthly Savings Needed", "Years to FI"]
    click.echo(tabulate(data, headers=headers, tablefmt="grid"))


def display_scenario_comparison(comparison):
    """Display scenario comparison analysis."""
    click.echo("\n=== Scenario Comparison ===")
    
    click.echo(f"Best Scenario: {comparison['best_scenario']['name']} "
              f"(Score: {comparison['best_scenario']['score']:.1f}%)")
    
    click.echo(f"Worst Scenario: {comparison['worst_scenario']['name']} "
              f"(Score: {comparison['worst_scenario']['score']:.1f}%)")
    
    click.echo(f"Lowest Savings Needed: {comparison['lowest_savings_needed']['name']} "
              f"({format_currency(comparison['lowest_savings_needed']['monthly_savings'])})")


def display_retirement_projections(projection, fire_metrics):
    """Display retirement projection results."""
    click.echo(f"Final Portfolio Value: {format_currency(projection.final_portfolio_value)}")
    click.echo(f"Total Contributions: {format_currency(projection.total_contributions)}")
    click.echo(f"Total Returns: {format_currency(projection.total_returns)}")
    click.echo(f"Retirement Feasible: {'Yes' if projection.retirement_feasible else 'No'}")
    click.echo(f"Years of Retirement Funded: {projection.years_of_retirement_funded}")
    
    click.echo("\n=== FIRE Metrics ===")
    fire_data = [
        ["FIRE Number (25x expenses)", format_currency(fire_metrics['fire_number'])],
        ["Coast FIRE Number", format_currency(fire_metrics['coast_fire_number'])],
        ["Lean FIRE Number", format_currency(fire_metrics['lean_fire_number'])],
        ["Fat FIRE Number", format_currency(fire_metrics['fat_fire_number'])],
        ["Current Progress", f"{fire_metrics['current_progress_percent']:.1f}%"],
        ["Years to FIRE", f"{fire_metrics['years_to_fire']:.1f} years"]
    ]
    
    click.echo(tabulate(fire_data, headers=["Metric", "Value"], tablefmt="grid"))


def display_monte_carlo_results(results):
    """Display Monte Carlo analysis results."""
    click.echo("\n=== Monte Carlo Analysis ===")
    
    data = [
        ["Success Rate", f"{results['success_rate']:.1%}"],
        ["Median Final Value", format_currency(results['median_final_value'])],
        ["10th Percentile (Conservative)", format_currency(results['percentile_10'])],
        ["90th Percentile (Optimistic)", format_currency(results['percentile_90'])],
        ["Required Portfolio Value", format_currency(results['required_portfolio_value'])]
    ]
    
    click.echo(tabulate(data, headers=["Metric", "Value"], tablefmt="grid"))


if __name__ == "__main__":
    cli()