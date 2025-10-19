const appNameElement = document.getElementById('app-name');
const productNameElement = document.getElementById('product-name');
const versionElement = document.getElementById('app-version');

if (appNameElement && window.firefly) {
  appNameElement.textContent = window.firefly.appName;
}

if (productNameElement && window.firefly) {
  productNameElement.textContent = window.firefly.productName;
}

if (versionElement && window.firefly) {
  versionElement.textContent = window.firefly.version;
}
