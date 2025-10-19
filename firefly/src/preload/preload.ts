import { contextBridge } from 'electron';
import { appConfig } from '../lib/appConfig';

type RendererApi = {
  appName: string;
  productName: string;
  version: string;
};

const api: RendererApi = {
  appName: appConfig.name,
  productName: appConfig.productName,
  version: appConfig.version
};

contextBridge.exposeInMainWorld('firefly', api);
