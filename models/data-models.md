# Data Models

This document describes the canonical schema for a Coast FIRE plan file. The schema is expressed in JSON Schema (`models/schema/plan.json`) and accompanied by representative sample data (`models/samples/coast-fire-001.json`).

## Overview
- Plans persist as a single JSON document (or equivalent map) per user scenario.
- All monetary amounts are stored in present-day nominal dollars; inflation is applied during projections.
- Ages are integers representing the user's age at the end of the calendar year.
- Dates follow ISO 8601 (`YYYY-MM-DD`) when specific calendar dates are required.
