export {};

declare global {
  interface Window {
    firefly?: {
      appName: string;
      productName: string;
      version: string;
    };
  }
}
