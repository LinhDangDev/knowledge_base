# 🤖 Automated Testing Setup Guide

> Complete guide for setting up automated testing infrastructure for SHUNCOM RULR IoT Platform

{% hint style="info" %}
**Platform:** SHUNCOM RULR IoT Platform v1.1 | **Last Updated:** January 2025
{% endhint %}

**Prerequisites**: Node.js 18+, npm/yarn, Docker (optional)

---

## 📋 Table of Contents

1. [Testing Stack Overview](#testing-stack-overview)
2. [Project Setup](#project-setup)
3. [Unit Testing with Jest](#unit-testing-with-jest)
4. [Integration Testing with Supertest](#integration-testing-with-supertest)
5. [E2E Testing with Cypress](#e2e-testing-with-cypress)
6. [E2E Testing with Playwright](#e2e-testing-with-playwright)
7. [Code Coverage Configuration](#code-coverage-configuration)
8. [Test Data Factories](#test-data-factories)
9. [CI/CD Integration](#cicd-integration)
10. [Performance Testing Setup](#performance-testing-setup)

---

## 🎯 Testing Stack Overview

### Recommended Testing Tools

```yaml
Unit Testing:
  Framework: Jest 29+
  Assertions: expect (built-in)
  Mocking: jest.mock / jest.spyOn
  Coverage: Istanbul (built-in)

Integration Testing:
  HTTP Testing: Supertest 6+
  Database: pg-mem (in-memory PostgreSQL)
  Fixtures: Factory pattern with Faker.js

E2E Testing (Primary):
  Framework: Cypress 13+
  Browser Support: Chrome, Firefox, Edge
  Component Testing: Cypress Component Testing
  API Testing: cy.request()

E2E Testing (Alternative):
  Framework: Playwright 1.40+
  Browser Support: Chromium, Firefox, WebKit
  Parallel Execution: Built-in
  Trace Viewer: Advanced debugging

Performance Testing:
  Load Testing: Artillery 2.0+
  API Testing: k6
  Monitoring: Lighthouse CI

Security Testing:
  SAST: SonarQube
  Dependency Scanning: Snyk
  Penetration Testing: OWASP ZAP
```

---

## 🚀 Project Setup

### Directory Structure

```bash
project-root/
├── src/                          # Application source code
├── tests/                        # Test files
│   ├── unit/                     # Unit tests
│   │   ├── services/
│   │   ├── controllers/
│   │   ├── utils/
│   │   └── models/
│   ├── integration/              # Integration tests
│   │   ├── api/
│   │   └── database/
│   ├── e2e/                      # End-to-end tests
│   │   ├── cypress/              # Cypress tests
│   │   │   ├── e2e/
│   │   │   ├── fixtures/
│   │   │   ├── support/
│   │   │   └── tsconfig.json
│   │   └── playwright/           # Playwright tests
│   │       ├── tests/
│   │       └── playwright.config.ts
│   ├── performance/              # Performance tests
│   │   └── artillery/
│   ├── security/                 # Security tests
│   └── helpers/                  # Test utilities
│       ├── factories/
│       ├── fixtures/
│       └── setup/
├── jest.config.js                # Jest configuration
├── cypress.config.ts             # Cypress configuration
├── playwright.config.ts          # Playwright configuration
└── .github/workflows/            # CI/CD workflows
    ├── test.yml
    ├── e2e.yml
    └── performance.yml
```

### Install Dependencies

```bash
# Initialize project (if not already done)
npm init -y

# Install Jest and testing utilities
npm install --save-dev \
  jest \
  @types/jest \
  ts-jest \
  @jest/globals

# Install Supertest for API testing
npm install --save-dev \
  supertest \
  @types/supertest

# Install Cypress for E2E testing
npm install --save-dev \
  cypress \
  @testing-library/cypress \
  @cypress/code-coverage

# Install Playwright for cross-browser E2E testing
npm install --save-dev \
  @playwright/test

# Install test data utilities
npm install --save-dev \
  @faker-js/faker \
  factory-girl

# Install database testing utilities
npm install --save-dev \
  pg-mem \
  @testcontainers/postgresql

# Install coverage and reporting
npm install --save-dev \
  nyc \
  codecov \
  jest-html-reporter

# Install performance testing tools
npm install --save-dev \
  artillery \
  k6

# Install security testing tools
npm install --save-dev \
  @zaproxy/zap-api-nodejs \
  snyk
```

---

## 🧪 Unit Testing with Jest

### Jest Configuration

Create `jest.config.js`:

```javascript
/** @type {import('jest').Config} */
module.exports = {
  // Use ts-jest for TypeScript support
  preset: 'ts-jest',
  testEnvironment: 'node',

  // Test file patterns
  testMatch: [
    '**/tests/unit/**/*.test.ts',
    '**/tests/unit/**/*.spec.ts'
  ],

  // Coverage configuration
  collectCoverageFrom: [
    'src/**/*.{ts,tsx}',
    '!src/**/*.d.ts',
    '!src/**/*.interface.ts',
    '!src/**/__tests__/**',
    '!src/index.ts'
  ],

  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  },

  coverageReporters: ['text', 'lcov', 'html', 'json-summary'],

  // Setup files
  setupFilesAfterEnv: ['<rootDir>/tests/helpers/setup/jest.setup.ts'],

  // Module path aliases
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/$1',
    '^@tests/(.*)$': '<rootDir>/tests/$1'
  },

  // Global setup and teardown
  globalSetup: '<rootDir>/tests/helpers/setup/global-setup.ts',
  globalTeardown: '<rootDir>/tests/helpers/setup/global-teardown.ts',

  // Performance
  maxWorkers: '50%',

  // Timeout
  testTimeout: 10000,

  // Clear mocks between tests
  clearMocks: true,
  resetMocks: true,
  restoreMocks: true,

  // Verbose output
  verbose: true
};
```

### Jest Setup File

Create `tests/helpers/setup/jest.setup.ts`:

```typescript
import { config } from 'dotenv';

// Load test environment variables
config({ path: '.env.test' });

// Set test environment
process.env.NODE_ENV = 'test';

// Increase test timeout for integration tests
jest.setTimeout(10000);

// Mock external services
jest.mock('@/services/email.service', () => ({
  EmailService: jest.fn().mockImplementation(() => ({
    sendEmail: jest.fn().mockResolvedValue(true)
  }))
}));

jest.mock('@/services/sms.service', () => ({
  SMSService: jest.fn().mockImplementation(() => ({
    sendSMS: jest.fn().mockResolvedValue(true)
  }))
}));

// Global test utilities
global.testUtils = {
  sleep: (ms: number) => new Promise(resolve => setTimeout(resolve, ms)),

  waitFor: async (
    condition: () => boolean | Promise<boolean>,
    options: { timeout?: number; interval?: number } = {}
  ) => {
    const { timeout = 5000, interval = 100 } = options;
    const startTime = Date.now();

    while (Date.now() - startTime < timeout) {
      if (await condition()) {
        return true;
      }
      await global.testUtils.sleep(interval);
    }

    throw new Error(`Condition not met within ${timeout}ms`);
  }
};

// Add custom matchers
expect.extend({
  toBeWithinRange(received: number, floor: number, ceiling: number) {
    const pass = received >= floor && received <= ceiling;
    return {
      pass,
      message: () =>
        pass
          ? `expected ${received} not to be within range ${floor} - ${ceiling}`
          : `expected ${received} to be within range ${floor} - ${ceiling}`
    };
  }
});
```

### Example Unit Test

Create `tests/unit/services/auth.service.test.ts`:

```typescript
import { AuthService } from '@/services/auth.service';
import { UserRepository } from '@/repositories/user.repository';
import { TokenService } from '@/services/token.service';
import { PasswordService } from '@/services/password.service';

// Mock dependencies
jest.mock('@/repositories/user.repository');
jest.mock('@/services/token.service');
jest.mock('@/services/password.service');

describe('AuthService', () => {
  let authService: AuthService;
  let userRepository: jest.Mocked<UserRepository>;
  let tokenService: jest.Mocked<TokenService>;
  let passwordService: jest.Mocked<PasswordService>;

  beforeEach(() => {
    // Clear all mocks
    jest.clearAllMocks();

    // Create mocked instances
    userRepository = new UserRepository() as jest.Mocked<UserRepository>;
    tokenService = new TokenService() as jest.Mocked<TokenService>;
    passwordService = new PasswordService() as jest.Mocked<PasswordService>;

    // Inject dependencies
    authService = new AuthService(
      userRepository,
      tokenService,
      passwordService
    );
  });

  describe('login', () => {
    const validCredentials = {
      username: 'admin@shuncom.com',
      password: 'ValidPassword123!'
    };

    const mockUser = {
      id: 'usr_123',
      username: 'admin@shuncom.com',
      passwordHash: '$2b$10$...',
      status: 'active',
      failedLoginAttempts: 0
    };

    it('should return access token for valid credentials', async () => {
      // Arrange
      userRepository.findByUsername.mockResolvedValue(mockUser);
      passwordService.compare.mockResolvedValue(true);
      tokenService.generateAccessToken.mockReturnValue('mock_access_token');
      tokenService.generateRefreshToken.mockReturnValue('mock_refresh_token');

      // Act
      const result = await authService.login(validCredentials);

      // Assert
      expect(result.success).toBe(true);
      expect(result.data).toMatchObject({
        accessToken: 'mock_access_token',
        refreshToken: 'mock_refresh_token'
      });
      expect(userRepository.findByUsername).toHaveBeenCalledWith('admin@shuncom.com');
      expect(passwordService.compare).toHaveBeenCalledWith(
        'ValidPassword123!',
        mockUser.passwordHash
      );
      expect(userRepository.resetFailedLoginAttempts).toHaveBeenCalledWith('usr_123');
    });

    it('should increment failed login attempts for invalid password', async () => {
      // Arrange
      userRepository.findByUsername.mockResolvedValue(mockUser);
      passwordService.compare.mockResolvedValue(false);

      // Act
      const result = await authService.login({
        ...validCredentials,
        password: 'WrongPassword'
      });

      // Assert
      expect(result.success).toBe(false);
      expect(result.error.code).toBe('AUTH_INVALID_CREDENTIALS');
      expect(userRepository.incrementFailedLoginAttempts).toHaveBeenCalledWith('usr_123');
    });

    it('should lock account after 5 failed attempts', async () => {
      // Arrange
      const userWithFailedAttempts = {
        ...mockUser,
        failedLoginAttempts: 4
      };
      userRepository.findByUsername.mockResolvedValue(userWithFailedAttempts);
      passwordService.compare.mockResolvedValue(false);

      // Act
      const result = await authService.login({
        ...validCredentials,
        password: 'WrongPassword'
      });

      // Assert
      expect(result.success).toBe(false);
      expect(result.error.code).toBe('AUTH_ACCOUNT_LOCKED');
      expect(userRepository.lockAccount).toHaveBeenCalledWith('usr_123');
    });

    it('should throw error for non-existent user', async () => {
      // Arrange
      userRepository.findByUsername.mockResolvedValue(null);

      // Act & Assert
      await expect(authService.login(validCredentials))
        .rejects
        .toThrow('User not found');
    });
  });

  describe('refreshToken', () => {
    it('should return new access token for valid refresh token', async () => {
      // Arrange
      const refreshToken = 'valid_refresh_token';
      const userId = 'usr_123';

      tokenService.verifyRefreshToken.mockReturnValue({ userId });
      tokenService.generateAccessToken.mockReturnValue('new_access_token');

      // Act
      const result = await authService.refreshToken(refreshToken);

      // Assert
      expect(result.success).toBe(true);
      expect(result.data.accessToken).toBe('new_access_token');
    });

    it('should reject invalid refresh token', async () => {
      // Arrange
      tokenService.verifyRefreshToken.mockImplementation(() => {
        throw new Error('Invalid token');
      });

      // Act
      const result = await authService.refreshToken('invalid_token');

      // Assert
      expect(result.success).toBe(false);
      expect(result.error.code).toBe('AUTH_INVALID_REFRESH_TOKEN');
    });
  });
});
```

### Running Unit Tests

Add to `package.json`:

```json
{
  "scripts": {
    "test": "jest",
    "test:unit": "jest --testPathPattern=tests/unit",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage",
    "test:debug": "node --inspect-brk node_modules/.bin/jest --runInBand"
  }
}
```

Run tests:

```bash
# Run all unit tests
npm run test:unit

# Run with coverage
npm run test:coverage

# Run in watch mode
npm run test:watch

# Run specific test file
npm test -- tests/unit/services/auth.service.test.ts

# Run tests matching pattern
npm test -- --testNamePattern="should return access token"
```

---

## 🔗 Integration Testing with Supertest

### Integration Test Setup

Create `tests/helpers/setup/integration.setup.ts`:

```typescript
import { Application } from 'express';
import { createApp } from '@/app';
import { DatabaseService } from '@/services/database.service';
import { newDb } from 'pg-mem';

let app: Application;
let dbService: DatabaseService;

export async function setupIntegrationTest() {
  // Create in-memory database
  const db = newDb();

  // Register PostgreSQL extensions
  db.public.registerFunction({
    name: 'gen_random_uuid',
    implementation: () => crypto.randomUUID()
  });

  // Get database connection
  const connection = await db.adapters.createTypeormConnection({
    type: 'postgres',
    entities: ['src/entities/**/*.ts']
  });

  // Initialize database service
  dbService = new DatabaseService(connection);
  await dbService.runMigrations();

  // Create Express app
  app = createApp(dbService);

  return { app, dbService };
}

export async function teardownIntegrationTest() {
  if (dbService) {
    await dbService.close();
  }
}

export async function resetDatabase() {
  if (dbService) {
    await dbService.query('TRUNCATE TABLE users, devices, projects CASCADE');
  }
}
```

### Example Integration Test

Create `tests/integration/api/devices.test.ts`:

```typescript
import request from 'supertest';
import { Application } from 'express';
import { setupIntegrationTest, teardownIntegrationTest, resetDatabase } from '@tests/helpers/setup/integration.setup';
import { DeviceFactory } from '@tests/helpers/factories/device.factory';
import { UserFactory } from '@tests/helpers/factories/user.factory';

describe('Device API Integration Tests', () => {
  let app: Application;
  let authToken: string;
  let testUser: any;

  beforeAll(async () => {
    const setup = await setupIntegrationTest();
    app = setup.app;
  });

  afterAll(async () => {
    await teardownIntegrationTest();
  });

  beforeEach(async () => {
    await resetDatabase();

    // Create test user and authenticate
    testUser = await UserFactory.create({
      username: 'test@shuncom.com',
      permissions: ['device.view', 'device.create', 'device.edit']
    });

    const loginResponse = await request(app)
      .post('/api/v1/auth/login')
      .send({
        username: 'test@shuncom.com',
        password: 'TestPassword123!'
      });

    authToken = loginResponse.body.data.accessToken;
  });

  describe('POST /api/v1/devices', () => {
    it('should create a new device with valid data', async () => {
      const deviceData = {
        name: 'TEST-CTRL-001',
        deviceType: 'light_controller_zigbee',
        projectId: 'prj_test_001',
        gatewayId: 'dev_gw_test_001',
        coordinates: {
          latitude: 31.2304,
          longitude: 121.4737
        }
      };

      const response = await request(app)
        .post('/api/v1/devices')
        .set('Authorization', `Bearer ${authToken}`)
        .send(deviceData)
        .expect('Content-Type', /json/)
        .expect(201);

      expect(response.body).toMatchObject({
        success: true,
        data: {
          name: 'TEST-CTRL-001',
          deviceType: 'light_controller_zigbee',
          status: 'offline'
        }
      });

      expect(response.body.data.id).toBeDefined();
      expect(response.body.data.createdAt).toBeDefined();
    });

    it('should validate required fields', async () => {
      const response = await request(app)
        .post('/api/v1/devices')
        .set('Authorization', `Bearer ${authToken}`)
        .send({ name: 'TEST-CTRL-002' })
        .expect(422);

      expect(response.body.error.code).toBe('VALIDATION_ERROR');
      expect(response.body.error.details).toEqual(
        expect.arrayContaining([
          expect.objectContaining({ field: 'deviceType' }),
          expect.objectContaining({ field: 'projectId' })
        ])
      );
    });

    it('should reject duplicate device names within same project', async () => {
      await DeviceFactory.create({
        name: 'DUPLICATE-DEVICE',
        projectId: 'prj_test_001'
      });

      const response = await request(app)
        .post('/api/v1/devices')
        .set('Authorization', `Bearer ${authToken}`)
        .send({
          name: 'DUPLICATE-DEVICE',
          deviceType: 'light_controller_zigbee',
          projectId: 'prj_test_001'
        })
        .expect(409);

      expect(response.body.error.code).toBe('DEVICE_NAME_EXISTS');
    });
  });

  describe('GET /api/v1/devices', () => {
    beforeEach(async () => {
      // Create test devices
      await DeviceFactory.createBatch(25, {
        projectId: 'prj_test_001',
        status: 'online'
      });

      await DeviceFactory.createBatch(15, {
        projectId: 'prj_test_001',
        status: 'offline'
      });
    });

    it('should return paginated device list', async () => {
      const response = await request(app)
        .get('/api/v1/devices?page=1&limit=20')
        .set('Authorization', `Bearer ${authToken}`)
        .expect(200);

      expect(response.body.data.devices).toHaveLength(20);
      expect(response.body.data.pagination).toMatchObject({
        page: 1,
        limit: 20,
        total: 40,
        totalPages: 2
      });
    });

    it('should filter devices by status', async () => {
      const response = await request(app)
        .get('/api/v1/devices?status=online')
        .set('Authorization', `Bearer ${authToken}`)
        .expect(200);

      expect(response.body.data.devices).toHaveLength(25);
      response.body.data.devices.forEach((device: any) => {
        expect(device.status).toBe('online');
      });
    });

    it('should filter devices by project', async () => {
      await DeviceFactory.createBatch(10, { projectId: 'prj_test_002' });

      const response = await request(app)
        .get('/api/v1/devices?projectId=prj_test_001')
        .set('Authorization', `Bearer ${authToken}`)
        .expect(200);

      expect(response.body.data.devices).toHaveLength(40);
      response.body.data.devices.forEach((device: any) => {
        expect(device.project.id).toBe('prj_test_001');
      });
    });

    it('should search devices by name', async () => {
      await DeviceFactory.create({
        name: 'SPECIAL-DEVICE-XYZ',
        projectId: 'prj_test_001'
      });

      const response = await request(app)
        .get('/api/v1/devices?search=SPECIAL-DEVICE')
        .set('Authorization', `Bearer ${authToken}`)
        .expect(200);

      expect(response.body.data.devices.length).toBeGreaterThan(0);
      expect(response.body.data.devices[0].name).toContain('SPECIAL-DEVICE');
    });
  });

  describe('PUT /api/v1/devices/:deviceId', () => {
    let testDevice: any;

    beforeEach(async () => {
      testDevice = await DeviceFactory.create({
        name: 'ORIGINAL-NAME',
        projectId: 'prj_test_001'
      });
    });

    it('should update device properties', async () => {
      const response = await request(app)
        .put(`/api/v1/devices/${testDevice.id}`)
        .set('Authorization', `Bearer ${authToken}`)
        .send({
          name: 'UPDATED-NAME',
          status: 'maintenance'
        })
        .expect(200);

      expect(response.body.data.name).toBe('UPDATED-NAME');
      expect(response.body.data.status).toBe('maintenance');
      expect(response.body.data.updatedAt).toBeDefined();
    });

    it('should reject invalid status values', async () => {
      const response = await request(app)
        .put(`/api/v1/devices/${testDevice.id}`)
        .set('Authorization', `Bearer ${authToken}`)
        .send({ status: 'invalid_status' })
        .expect(422);

      expect(response.body.error.code).toBe('VALIDATION_ERROR');
    });
  });

  describe('POST /api/v1/devices/batch/import', () => {
    it('should import devices from CSV file', async () => {
      const csvContent = `name,deviceType,projectId,gatewayId,latitude,longitude
LED-CTRL-001,light_controller_zigbee,prj_test_001,dev_gw_001,31.2304,121.4737
LED-CTRL-002,light_controller_zigbee,prj_test_001,dev_gw_001,31.2305,121.4738
LED-CTRL-003,light_controller_zigbee,prj_test_001,dev_gw_001,31.2306,121.4739`;

      const response = await request(app)
        .post('/api/v1/devices/batch/import')
        .set('Authorization', `Bearer ${authToken}`)
        .attach('file', Buffer.from(csvContent), 'devices.csv')
        .field('projectId', 'prj_test_001')
        .expect(202);

      expect(response.body.data.jobId).toBeDefined();
      expect(response.body.data.totalRecords).toBe(3);

      // Wait for job completion
      const jobId = response.body.data.jobId;
      await global.testUtils.waitFor(async () => {
        const statusResponse = await request(app)
          .get(`/api/v1/devices/batch/import/${jobId}`)
          .set('Authorization', `Bearer ${authToken}`);

        return statusResponse.body.data.status === 'completed';
      }, { timeout: 10000 });

      // Verify final status
      const finalStatus = await request(app)
        .get(`/api/v1/devices/batch/import/${jobId}`)
        .set('Authorization', `Bearer ${authToken}`)
        .expect(200);

      expect(finalStatus.body.data.results.successful).toBe(3);
      expect(finalStatus.body.data.results.failed).toBe(0);
    });
  });
});
```

### Running Integration Tests

```bash
# Run integration tests
npm run test:integration

# Run with database logs
DEBUG=database npm run test:integration

# Run specific integration test
npm test -- tests/integration/api/devices.test.ts
```

---

## 🎭 E2E Testing with Cypress

### Cypress Configuration

Create `cypress.config.ts`:

```typescript
import { defineConfig } from 'cypress';
import codeCoverageTask from '@cypress/code-coverage/task';

export default defineConfig({
  e2e: {
    baseUrl: 'http://localhost:3000',
    specPattern: 'tests/e2e/cypress/e2e/**/*.cy.{js,jsx,ts,tsx}',
    supportFile: 'tests/e2e/cypress/support/e2e.ts',
    fixturesFolder: 'tests/e2e/cypress/fixtures',

    setupNodeEvents(on, config) {
      // Code coverage
      codeCoverageTask(on, config);

      // Custom tasks
      on('task', {
        log(message) {
          console.log(message);
          return null;
        },
        table(message) {
          console.table(message);
          return null;
        }
      });

      return config;
    },

    // Viewport
    viewportWidth: 1280,
    viewportHeight: 720,

    // Timeouts
    defaultCommandTimeout: 10000,
    pageLoadTimeout: 30000,
    requestTimeout: 10000,

    // Video and screenshots
    video: true,
    screenshotOnRunFailure: true,

    // Retries
    retries: {
      runMode: 2,
      openMode: 0
    },

    // Environment variables
    env: {
      apiUrl: 'http://localhost:3000/api/v1',
      coverage: true
    }
  },

  component: {
    devServer: {
      framework: 'react',
      bundler: 'vite'
    },
    specPattern: 'src/**/*.cy.{js,jsx,ts,tsx}',
    supportFile: 'tests/e2e/cypress/support/component.ts'
  }
});
```

### Cypress Support File

Create `tests/e2e/cypress/support/e2e.ts`:

```typescript
import '@testing-library/cypress/add-commands';
import '@cypress/code-coverage/support';

// Custom commands
Cypress.Commands.add('login', (username: string, password: string) => {
  cy.session([username, password], () => {
    cy.visit('/login');
    cy.get('input[name="username"]').type(username);
    cy.get('input[name="password"]').type(password);
    cy.get('button[type="submit"]').click();
    cy.url().should('include', '/dashboard');
    cy.window().its('localStorage.accessToken').should('exist');
  });
});

Cypress.Commands.add('loginAsAdmin', () => {
  cy.login('admin@shuncom.com', 'AdminPassword123!');
});

Cypress.Commands.add('loginAsOperator', () => {
  cy.login('operator@shuncom.com', 'OperatorPassword123!');
});

Cypress.Commands.add('apiRequest', (method: string, url: string, body?: any) => {
  return cy.window().then((win) => {
    const token = win.localStorage.getItem('accessToken');

    return cy.request({
      method,
      url: `${Cypress.env('apiUrl')}${url}`,
      body,
      headers: {
        Authorization: `Bearer ${token}`
      }
    });
  });
});

Cypress.Commands.add('seedDatabase', (fixture: string) => {
  return cy.task('seedDatabase', fixture);
});

Cypress.Commands.add('resetDatabase', () => {
  return cy.task('resetDatabase');
});

// Type definitions
declare global {
  namespace Cypress {
    interface Chainable {
      login(username: string, password: string): Chainable<void>;
      loginAsAdmin(): Chainable<void>;
      loginAsOperator(): Chainable<void>;
      apiRequest(method: string, url: string, body?: any): Chainable<Response>;
      seedDatabase(fixture: string): Chainable<void>;
      resetDatabase(): Chainable<void>;
    }
  }
}
```

### Example Cypress E2E Test

Create `tests/e2e/cypress/e2e/device-management.cy.ts`:

```typescript
describe('Device Management', () => {
  beforeEach(() => {
    cy.resetDatabase();
    cy.seedDatabase('devices');
    cy.loginAsAdmin();
    cy.visit('/devices');
  });

  describe('Device List', () => {
    it('should display paginated device list', () => {
      cy.get('table tbody tr').should('have.length', 20);
      cy.get('.pagination').should('be.visible');
      cy.contains('Page 1 of').should('be.visible');
    });

    it('should filter devices by status', () => {
      cy.get('select[name="statusFilter"]').select('online');
      cy.get('button').contains('Apply Filters').click();

      cy.get('table tbody tr').each(($row) => {
        cy.wrap($row).find('.status-badge').should('have.class', 'status-online');
      });
    });

    it('should search devices by name', () => {
      cy.get('input[placeholder="Search devices"]').type('LED-CTRL');
      cy.get('table tbody tr').should('have.length.greaterThan', 0);
      cy.get('table tbody tr').first().should('contain', 'LED-CTRL');
    });
  });

  describe('Device Registration', () => {
    it('should register a new light controller', () => {
      cy.get('button').contains('Add Device').click();
      cy.get('.modal').should('be.visible');

      // Fill form
      cy.get('select[name="deviceType"]').select('Light Controller (Zigbee)');
      cy.get('input[name="name"]').type('CYPRESS-TEST-CTRL-001');
      cy.get('select[name="projectId"]').select('Smart Street Lighting');
      cy.get('select[name="gatewayId"]').select('Gateway-001');
      cy.get('input[name="latitude"]').type('31.2304');
      cy.get('input[name="longitude"]').type('121.4737');

      // Submit
      cy.get('button').contains('Register Device').click();

      // Verify success
      cy.get('.toast-success').should('be.visible');
      cy.get('.toast-success').should('contain', 'Device registered successfully');

      // Verify in list
      cy.get('input[placeholder="Search devices"]').type('CYPRESS-TEST-CTRL-001');
      cy.get('table tbody tr').first().should('contain', 'CYPRESS-TEST-CTRL-001');
    });

    it('should validate required fields', () => {
      cy.get('button').contains('Add Device').click();
      cy.get('button').contains('Register Device').click();

      cy.get('.form-error').should('have.length.greaterThan', 0);
      cy.contains('Device type is required').should('be.visible');
      cy.contains('Name is required').should('be.visible');
    });

    it('should show error for duplicate device name', () => {
      cy.get('button').contains('Add Device').click();

      cy.get('select[name="deviceType"]').select('Light Controller (Zigbee)');
      cy.get('input[name="name"]').type('EXISTING-DEVICE-001');
      cy.get('select[name="projectId"]').select('Smart Street Lighting');
      cy.get('button').contains('Register Device').click();

      cy.get('.toast-error').should('be.visible');
      cy.get('.toast-error').should('contain', 'Device name already exists');
    });
  });

  describe('Device Control', () => {
    it('should control device brightness', () => {
      cy.get('table tbody tr').first().click();
      cy.get('.device-detail').should('be.visible');

      cy.get('button').contains('Control').click();
      cy.get('.control-panel').should('be.visible');

      // Set brightness
      cy.get('input[name="brightness"]').clear().type('75');
      cy.get('button').contains('Set Brightness').click();

      // Verify command sent
      cy.get('.toast-success').should('contain', 'Command sent successfully');

      // Verify device attribute updated
      cy.wait(1000);
      cy.get('.device-detail').should('contain', 'Brightness: 75%');
    });
  });

  describe('Batch Operations', () => {
    it('should import devices from CSV', () => {
      cy.get('button').contains('Batch Import').click();
      cy.get('.modal').should('be.visible');

      const csvContent = `name,deviceType,projectId,gatewayId,latitude,longitude
BULK-001,light_controller_zigbee,prj_001,dev_gw_001,31.2304,121.4737
BULK-002,light_controller_zigbee,prj_001,dev_gw_001,31.2305,121.4738`;

      cy.get('input[type="file"]').selectFile({
        contents: Cypress.Buffer.from(csvContent),
        fileName: 'devices.csv',
        mimeType: 'text/csv'
      });

      cy.get('button').contains('Start Import').click();

      // Wait for completion
      cy.get('.progress-bar', { timeout: 30000 })
        .should('have.attr', 'aria-valuenow', '100');

      cy.get('.import-results').should('contain', '2 devices imported successfully');
    });
  });
});
```

### Running Cypress Tests

Add to `package.json`:

```json
{
  "scripts": {
    "cypress:open": "cypress open",
    "cypress:run": "cypress run",
    "test:e2e": "cypress run --spec 'tests/e2e/cypress/e2e/**/*.cy.ts'",
    "test:e2e:headed": "cypress run --headed",
    "test:e2e:chrome": "cypress run --browser chrome",
    "test:e2e:firefox": "cypress run --browser firefox"
  }
}
```

Run tests:

```bash
# Open Cypress GUI
npm run cypress:open

# Run all E2E tests
npm run test:e2e

# Run in specific browser
npm run test:e2e:chrome

# Run with headed mode (see browser)
npm run test:e2e:headed
```

---

## 🎪 E2E Testing with Playwright

### Playwright Configuration

Create `playwright.config.ts`:

```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests/e2e/playwright',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: [
    ['html'],
    ['json', { outputFile: 'playwright-report/results.json' }],
    ['junit', { outputFile: 'playwright-report/results.xml' }]
  ],

  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
    actionTimeout: 10000,
    navigationTimeout: 30000
  },

  projects: [
    // Desktop browsers
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] }
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] }
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] }
    },

    // Mobile browsers
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 5'] }
    },
    {
      name: 'Mobile Safari',
      use: { ...devices['iPhone 13'] }
    },

    // Tablet
    {
      name: 'iPad',
      use: { ...devices['iPad Pro'] }
    }
  ],

  webServer: {
    command: 'npm run start:test',
    port: 3000,
    reuseExistingServer: !process.env.CI
  }
});
```

### Example Playwright Test

Create `tests/e2e/playwright/device-management.spec.ts`:

```typescript
import { test, expect } from '@playwright/test';

test.describe('Device Management', () => {
  test.beforeEach(async ({ page }) => {
    // Login
    await page.goto('/login');
    await page.fill('input[name="username"]', 'admin@shuncom.com');
    await page.fill('input[name="password"]', 'AdminPassword123!');
    await page.click('button[type="submit"]');
    await expect(page).toHaveURL(/.*dashboard/);

    // Navigate to devices
    await page.click('a[href="/devices"]');
    await expect(page).toHaveURL(/.*devices/);
  });

  test('should display device list with pagination', async ({ page }) => {
    // Wait for table to load
    await expect(page.locator('table tbody tr')).toHaveCount(20);

    // Check pagination
    await expect(page.locator('.pagination')).toBeVisible();
    await expect(page.locator('.pagination')).toContainText('Page 1 of');
  });

  test('should register new device successfully', async ({ page }) => {
    // Click Add Device
    await page.click('button:has-text("Add Device")');
    await expect(page.locator('.modal')).toBeVisible();

    // Fill form
    await page.selectOption('select[name="deviceType"]', 'light_controller_zigbee');
    await page.fill('input[name="name"]', 'PLAYWRIGHT-TEST-001');
    await page.selectOption('select[name="projectId"]', 'prj_001');
    await page.selectOption('select[name="gatewayId"]', 'dev_gw_001');
    await page.fill('input[name="latitude"]', '31.2304');
    await page.fill('input[name="longitude"]', '121.4737');

    // Submit
    await page.click('button:has-text("Register Device")');

    // Verify success toast
    await expect(page.locator('.toast-success')).toBeVisible();
    await expect(page.locator('.toast-success')).toContainText('Device registered successfully');

    // Verify in list
    await page.fill('input[placeholder="Search devices"]', 'PLAYWRIGHT-TEST-001');
    await expect(page.locator('table tbody tr:first-child')).toContainText('PLAYWRIGHT-TEST-001');
  });

  test('should filter devices by status', async ({ page }) => {
    await page.selectOption('select[name="statusFilter"]', 'online');
    await page.click('button:has-text("Apply Filters")');

    // Verify all devices have online status
    const rows = page.locator('table tbody tr');
    const count = await rows.count();

    for (let i = 0; i < count; i++) {
      await expect(rows.nth(i).locator('.status-badge')).toHaveClass(/status-online/);
    }
  });

  test.describe('Mobile Responsiveness', () => {
    test.use({ viewport: { width: 375, height: 667 } });

    test('should display mobile menu', async ({ page }) => {
      await expect(page.locator('.mobile-menu-toggle')).toBeVisible();
      await page.click('.mobile-menu-toggle');
      await expect(page.locator('.mobile-menu')).toBeVisible();
    });

    test('should show device cards instead of table', async ({ page }) => {
      await expect(page.locator('.device-card')).toBeVisible();
      await expect(page.locator('table')).not.toBeVisible();
    });
  });
});
```

### Running Playwright Tests

```bash
# Install browsers
npx playwright install

# Run all tests
npx playwright test

# Run in headed mode
npx playwright test --headed

# Run specific browser
npx playwright test --project=chromium

# Run in debug mode
npx playwright test --debug

# Generate HTML report
npx playwright show-report
```

---

Continue with remaining sections in next response...
