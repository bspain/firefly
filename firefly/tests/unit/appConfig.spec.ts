import { describe, expect, it } from 'vitest';
import { appConfig } from '../../src/lib/appConfig';

describe('appConfig', () => {
  it('exposes Firefly branding metadata', () => {
    expect(appConfig.name).toBe('Firefly Planner');
    expect(appConfig.productName).toBe('Firefly Planner');
    expect(appConfig.version).toMatch(/\d+\.\d+\.\d+/);
  });
});
