module.exports = {
  default: {
    requireModule: ['ts-node/register'],
    require: ['tests/steps/*.ts'],
    format: ['progress', 'html:reports/cucumber-report.html'],
    formatOptions: { snippetInterface: 'async-await' },
    paths: ['features/**/*.feature']
  }
};
