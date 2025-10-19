import { app, BrowserWindow } from 'electron';
import path from 'path';
import { appConfig } from '../lib/appConfig';

const createMainWindow = (): void => {
  const mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    title: appConfig.productName,
    webPreferences: {
      preload: path.join(__dirname, '..', 'preload', 'preload.js')
    }
  });

  const indexHtmlPath = path.join(__dirname, '..', 'renderer', 'index.html');
  void mainWindow.loadFile(indexHtmlPath);

  if (process.env.NODE_ENV === 'development') {
    mainWindow.webContents.openDevTools({ mode: 'undocked' });
  }
};

app.on('ready', () => {
  createMainWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createMainWindow();
    }
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});
