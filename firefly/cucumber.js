const common = ['--require-module ts-node/register', '--require features/steps/**/*.ts'].join(' ');

module.exports = {
  default: common
};
