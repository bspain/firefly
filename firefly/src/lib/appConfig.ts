import packageJson from '../../package.json';

type PackageMetadata = {
  name: string;
  displayName?: string;
  version: string;
  description?: string;
};

const metadata = packageJson as PackageMetadata;

export const appConfig = {
  name: metadata.displayName ?? metadata.name,
  productName: metadata.displayName ?? metadata.name,
  version: metadata.version,
  description:
    metadata.description ?? 'Financial independence and retirement planning desktop application.'
};

export type AppConfig = typeof appConfig;
