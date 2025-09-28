"""
Firefly UI Package

Contains user interface components including CLI and dashboard functionality.
"""

from .cli import cli
from .dashboard import Dashboard

__all__ = ["cli", "Dashboard"]