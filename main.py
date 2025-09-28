#!/usr/bin/env python3
"""
Firefly - Main Application Entry Point

This is the main entry point for the Firefly financial planning application.
It provides a command-line interface for users to interact with the financial
planning tools and create retirement projections.
"""

import click
from firefly.ui.cli import cli


if __name__ == "__main__":
    cli()