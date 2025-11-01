# Application Screenshots and UI Description

## Main Application Window

The Firefly application features a modern, professional user interface with the following components:

### Header Section
- **Title**: "🔥 Firefly" in large, purple gradient text
- **Subtitle**: "Coast FIRE Planning Application"
- Clean, white background with subtle shadow

### Plan Management Card
- **Buttons**:
  - "Load Plan" - Opens file dialog to load custom plan files
  - "Load Sample Plan" - Loads the included coast-fire-001.json sample
  - "Save Plan" - Saves modifications to the current plan
- **Status Messages**: 
  - Success: Green background with success icon
  - Error: Red background with error message
  - Info: Blue background for informational messages
- **Plan Info Display** (when loaded):
  - Plan name
  - Current age
  - Target retirement age

### Phase Configuration Card (Feature v1-001)
Displays three phase cards side-by-side:

1. **📈 Accumulation Phase** (Blue border)
   - Shows age range (start - end)
   - Status: "Active contributions"

2. **🏖️ Coast Phase** (Purple border)
   - Shows age range (start - end)
   - Status: "No contributions, growth only"

3. **🌴 Retirement Phase** (Green border)
   - Shows age range (start - end)
   - Status: "Withdrawal phase"

### Interactive Controls
- **Input Field**: "Target Coast Start Age"
  - Number input with validation (30-100)
- **Update Button**: "Update Coast Age"
  - Triggers phase boundary recalculation
  - Updates all phase displays in real-time

### Visual Design
- **Color Scheme**: 
  - Primary: Purple gradient (#667eea to #764ba2)
  - Accent colors for different phases
  - Clean white cards with subtle shadows
- **Typography**: 
  - System fonts (San Francisco on Mac, Segoe UI on Windows)
  - Clear hierarchy with different font sizes
  - Professional, readable layout

### User Experience Flow
1. User clicks "Load Sample Plan"
2. Plan information appears showing current age (48) and plan details
3. Phase configuration card becomes visible
4. Initial phases shown: Accumulation (22-49), Coast (50-65), Retirement (66-100)
5. User can modify coast start age to 52
6. Phases update: Accumulation (22-51), Coast (52-65), Retirement (66-100)
7. Success message confirms the update

## File Structure Display
When packaging the application, users receive:
- **macOS**: A .dmg file that can be dragged to Applications
- **Windows**: An .exe installer with standard Windows installation flow
- **Linux**: An .AppImage file that can be run directly

## Example Interaction

**Initial State:**
```
Accumulation: Ages 22-49 (27 years)
Coast:        Ages 50-65 (15 years)
Retirement:   Ages 66-100 (34 years)
```

**After Setting Coast Age to 52:**
```
Accumulation: Ages 22-51 (29 years) ← Extended by 2 years
Coast:        Ages 52-65 (13 years) ← Starts 2 years later
Retirement:   Ages 66-100 (34 years) ← Unchanged
```

This demonstrates Feature v1-001's core functionality: dynamic phase boundary recalculation based on user input.
