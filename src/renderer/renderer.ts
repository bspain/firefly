/**
 * Renderer Process Script
 * Handles UI interactions and communication with main process
 */

// Export to make this a module
export {};

declare global {
  interface Window {
    electronAPI: {
      loadPlan: (filePath?: string) => Promise<any>;
      getPlan: () => Promise<any>;
      updateCoastAge: (newAge: number) => Promise<any>;
      savePlan: (filePath?: string) => Promise<any>;
    };
  }
}

interface Phase {
  phaseType: string;
  startAge: number;
  endAge: number;
}

interface Plan {
  planId: string;
  label: string;
  ownerProfile: {
    currentAge: number;
    targetRetirementAge: number;
  };
  phases: {
    phases: Phase[];
  };
}

let currentPlan: Plan | null = null;

// UI Elements
const loadPlanBtn = document.getElementById('loadPlanBtn') as HTMLButtonElement;
const loadSampleBtn = document.getElementById('loadSampleBtn') as HTMLButtonElement;
const savePlanBtn = document.getElementById('savePlanBtn') as HTMLButtonElement;
const updateCoastBtn = document.getElementById('updateCoastBtn') as HTMLButtonElement;
const coastAgeInput = document.getElementById('coastAgeInput') as HTMLInputElement;
const statusDiv = document.getElementById('status') as HTMLDivElement;
const planInfoDiv = document.getElementById('planInfo') as HTMLDivElement;
const phaseConfigCard = document.getElementById('phaseConfigCard') as HTMLDivElement;

// Event Listeners
loadPlanBtn.addEventListener('click', async () => {
  const result = await window.electronAPI.loadPlan();
  handleLoadResult(result);
});

loadSampleBtn.addEventListener('click', async () => {
  // Load the sample plan from models/samples/coast-fire-001.json
  const result = await window.electronAPI.loadPlan('./models/samples/coast-fire-001.json');
  handleLoadResult(result);
});

savePlanBtn.addEventListener('click', async () => {
  const result = await window.electronAPI.savePlan();
  if (result.success) {
    showStatus('Plan saved successfully!', 'success');
  } else {
    showStatus(`Error saving plan: ${result.error}`, 'error');
  }
});

updateCoastBtn.addEventListener('click', async () => {
  const newAge = parseInt(coastAgeInput.value);
  
  if (isNaN(newAge) || newAge < 30 || newAge > 100) {
    showStatus('Please enter a valid age between 30 and 100', 'error');
    return;
  }
  
  const result = await window.electronAPI.updateCoastAge(newAge);
  
  if (result.success) {
    currentPlan = result.plan;
    updatePhaseDisplay();
    showStatus('Coast age updated successfully!', 'success');
  } else {
    showStatus(`Error updating coast age: ${result.error}`, 'error');
  }
});

function handleLoadResult(result: any) {
  if (result.success) {
    currentPlan = result.plan;
    showStatus(`Plan loaded: ${currentPlan!.label}`, 'success');
    displayPlanInfo();
    updatePhaseDisplay();
    savePlanBtn.disabled = false;
    phaseConfigCard.classList.remove('hidden');
  } else {
    showStatus(`Error loading plan: ${result.error}`, 'error');
  }
}

function displayPlanInfo() {
  if (!currentPlan) return;
  
  planInfoDiv.innerHTML = `
    <p><strong>Plan:</strong> ${currentPlan.label}</p>
    <p><strong>Current Age:</strong> ${currentPlan.ownerProfile.currentAge}</p>
    <p><strong>Target Retirement:</strong> ${currentPlan.ownerProfile.targetRetirementAge}</p>
  `;
  planInfoDiv.classList.remove('hidden');
}

function updatePhaseDisplay() {
  if (!currentPlan) return;
  
  const phases = currentPlan.phases.phases;
  
  const accumulation = phases.find((p: Phase) => p.phaseType === 'ACCUMULATION');
  const coast = phases.find((p: Phase) => p.phaseType === 'COAST');
  const retirement = phases.find((p: Phase) => p.phaseType === 'RETIREMENT');
  
  if (accumulation) {
    const accAges = document.getElementById('accAges');
    if (accAges) {
      accAges.textContent = `${accumulation.startAge} - ${accumulation.endAge}`;
    }
  }
  
  if (coast) {
    const coastAges = document.getElementById('coastAges');
    if (coastAges) {
      coastAges.textContent = `${coast.startAge} - ${coast.endAge}`;
    }
    coastAgeInput.value = coast.startAge.toString();
  }
  
  if (retirement) {
    const retAges = document.getElementById('retAges');
    if (retAges) {
      retAges.textContent = `${retirement.startAge} - ${retirement.endAge}`;
    }
  }
}

function showStatus(message: string, type: 'success' | 'error' | 'info') {
  statusDiv.textContent = message;
  statusDiv.className = `status ${type}`;
  statusDiv.classList.remove('hidden');
  
  setTimeout(() => {
    statusDiv.classList.add('hidden');
  }, 5000);
}

// Initialize
console.log('Firefly renderer loaded');
