import { Given, When, Then } from '@cucumber/cucumber';
import { appConfig, AppConfig } from '../../src/lib/appConfig';

let configurationUnderTest: AppConfig | undefined;

Given('the application configuration is loaded', function () {
  configurationUnderTest = appConfig;
});

When('I inspect the exposed metadata', function () {
  if (!configurationUnderTest) {
    throw new Error('Application configuration has not been initialised.');
  }
});

Then('the application name is {string}', function (expectedName: string) {
  if (!configurationUnderTest) {
    throw new Error('Application configuration has not been initialised.');
  }

  if (configurationUnderTest.name !== expectedName) {
    throw new Error(
      `Expected application name to be ${expectedName} but received ${configurationUnderTest.name}.`
    );
  }
});

Then('the product name is {string}', function (expectedProductName: string) {
  if (!configurationUnderTest) {
    throw new Error('Application configuration has not been initialised.');
  }

  if (configurationUnderTest.productName !== expectedProductName) {
    throw new Error(
      `Expected product name to be ${expectedProductName} but received ${configurationUnderTest.productName}.`
    );
  }
});
