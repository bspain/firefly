/**
 * Electron Main Process
 * Entry point for the Firefly application
 */

import { app, BrowserWindow, ipcMain, dialog } from 'electron';
import * as path from 'path';
import * as fs from 'fs';
import { CoastFirePlan } from './shared/types';
import { loadPlan, setCoastStartAge } from './domains/retirement-planning/plan-service';

let mainWindow: BrowserWindow | null = null;
let currentPlan: CoastFirePlan | null = null;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,
      contextIsolation: true
    }
  });

  mainWindow.loadFile(path.join(__dirname, '../renderer/index.html'));

  // Open DevTools in development
  if (process.env.NODE_ENV === 'development') {
    mainWindow.webContents.openDevTools();
  }

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

// App lifecycle
app.on('ready', createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});

// IPC Handlers
ipcMain.handle('load-plan', async (event, filePath?: string) => {
  try {
    let targetPath = filePath;
    
    if (!targetPath) {
      const result = await dialog.showOpenDialog({
        properties: ['openFile'],
        filters: [
          { name: 'JSON Files', extensions: ['json'] },
          { name: 'All Files', extensions: ['*'] }
        ]
      });
      
      if (result.canceled || result.filePaths.length === 0) {
        return { success: false, error: 'No file selected' };
      }
      
      targetPath = result.filePaths[0];
    }
    
    const data = fs.readFileSync(targetPath, 'utf-8');
    currentPlan = loadPlan(data);
    
    return { success: true, plan: currentPlan };
  } catch (error) {
    console.error('Error loading plan:', error);
    return { 
      success: false, 
      error: error instanceof Error ? error.message : 'Unknown error' 
    };
  }
});

ipcMain.handle('get-plan', async () => {
  if (!currentPlan) {
    return { success: false, error: 'No plan loaded' };
  }
  return { success: true, plan: currentPlan };
});

ipcMain.handle('update-coast-age', async (event, newAge: number) => {
  try {
    if (!currentPlan) {
      return { success: false, error: 'No plan loaded' };
    }
    
    currentPlan = setCoastStartAge(currentPlan, newAge);
    
    return { success: true, plan: currentPlan };
  } catch (error) {
    console.error('Error updating coast age:', error);
    return { 
      success: false, 
      error: error instanceof Error ? error.message : 'Unknown error' 
    };
  }
});

ipcMain.handle('save-plan', async (event, filePath?: string) => {
  try {
    if (!currentPlan) {
      return { success: false, error: 'No plan to save' };
    }
    
    let targetPath = filePath;
    
    if (!targetPath) {
      const result = await dialog.showSaveDialog({
        filters: [
          { name: 'JSON Files', extensions: ['json'] }
        ],
        defaultPath: currentPlan.label.replace(/[^a-z0-9]/gi, '-').toLowerCase() + '.json'
      });
      
      if (result.canceled || !result.filePath) {
        return { success: false, error: 'Save cancelled' };
      }
      
      targetPath = result.filePath;
    }
    
    const jsonData = JSON.stringify(currentPlan, null, 2);
    fs.writeFileSync(targetPath, jsonData, 'utf-8');
    
    return { success: true, path: targetPath };
  } catch (error) {
    console.error('Error saving plan:', error);
    return { 
      success: false, 
      error: error instanceof Error ? error.message : 'Unknown error' 
    };
  }
});
