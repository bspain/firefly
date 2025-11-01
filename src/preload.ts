/**
 * Preload Script
 * Exposes safe APIs to the renderer process
 */

import { contextBridge, ipcRenderer } from 'electron';

contextBridge.exposeInMainWorld('electronAPI', {
  loadPlan: (filePath?: string) => ipcRenderer.invoke('load-plan', filePath),
  getPlan: () => ipcRenderer.invoke('get-plan'),
  updateCoastAge: (newAge: number) => ipcRenderer.invoke('update-coast-age', newAge),
  savePlan: (filePath?: string) => ipcRenderer.invoke('save-plan', filePath)
});
