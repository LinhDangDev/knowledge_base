# Research Report: Antigravity Claude Proxy

## Executive Summary

Antigravity Claude Proxy is a sophisticated Node.js middleware that bridges Claude Code CLI with Google's Antigravity Cloud Code service, enabling access to Claude 4.5 and Gemini models through an Anthropic-compatible API. The project demonstrates production-grade architecture with multi-account load balancing, intelligent retry logic, and comprehensive web management interface. Primary use case is personal development with Claude Code CLI, though carries inherent ToS compliance risks.

## Research Methodology

- Sources consulted: 6 (repository analysis via Repomix, README.md, package.json, config files, architecture docs)
- Date range of materials: Current version 1.2.6 (latest)
- Repository size: 119 files, 320K+ tokens, 1.3M+ characters
- Key search terms used: ["antigravity", "claude", "proxy", "oauth", "nodejs"]

## Key Findings

### 1. Technology Overview

**Core Purpose**: Acts as translation layer between Anthropic Messages API format and Google Generative AI format, routing requests through Antigravity's Cloud Code service to access Claude and Gemini models.

**Architecture Pattern**: Follows clean layered architecture:
```
Claude Code CLI → Express Server → Account Manager → CloudCode Client → Antigravity API
```

**Key Technologies**:
- **Runtime**: Node.js ≥18.0.0 (ES modules)
- **Framework**: Express.js for HTTP server
- **Database**: better-sqlite3 for local account storage
- **Authentication**: OAuth2 with Google accounts
- **Frontend**: Alpine.js + Tailwind CSS + DaisyUI
- **Build**: PostCSS + Tailwind compilation pipeline

### 2. Current State & Trends

**Version**: 1.2.6 (actively maintained, npm published)
**Release Cadence**: GitHub Actions auto-publish on release tags
**Community**: Growing adoption (star history tracking implemented)
**Documentation**: Comprehensive (README: 593 lines, architecture docs in CLAUDE.md)
**Testing**: Extensive test suite (15+ test scenarios, streaming, OAuth, multi-account)

### 3. Best Practices

**Multi-Account Load Balancing**:
- **Hybrid Strategy** (default): Combines health scoring, token bucket rate limiting, quota awareness
- **Sticky Strategy**: Cache optimization for prompt caching
- **Round-Robin**: Even distribution across accounts
- Automatic health tracking and cooldown management

**Security**:
- Optional API key protection for endpoints
- WebUI password protection
- Token caching with configurable TTL (5min default)
- Persistent storage optional (disabled by default)

**Error Handling**:
- Comprehensive retry logic (5 retries, exponential backoff)
- Rate limit detection from headers and error messages
- Automatic endpoint fallback (403/404 handling)
- Emergency fallback when all accounts exhausted

**Development Experience**:
- Live reload for development (`npm run dev`)
- CSS watching with Tailwind (`npm run dev:full`)
- Comprehensive CLI for account management
- Real-time web dashboard with metrics

### 4. Security Considerations

**Risks**:
- **ToS Violation Risk**: Explicitly acknowledged in documentation - may violate Google/Anthropic ToS
- **Account Suspension Risk**: Google accounts may be banned for detected proxy usage
- **Token Exposure**: OAuth tokens stored locally in SQLite database
- **No Commercial Use**: Explicitly not suitable for production/commercial applications

**Mitigations**:
- Personal use only (clearly documented)
- Optional token persistence (disabled by default)
- API key protection for endpoints
- WebUI password protection
- Clear risk warnings in documentation

### 5. Performance Insights

**Scalability Features**:
- Multi-account pool (up to 100 accounts, default 10)
- Intelligent load balancing with health scoring
- Client-side rate limiting (token bucket: 50 tokens max, 6/minute refill)
- Request timeout: 5 minutes configurable
- Automatic cooldown periods (60s default)

**Caching**:
- Session ID derivation for prompt caching optimization
- Token cache with TTL
- Sticky strategy maximizes cache hits

**Monitoring**:
- Real-time dashboard with metrics
- 30-day usage history persistence
- Account health and quota tracking
- Live log streaming with filtering

## Comparative Analysis

**vs claude-code-proxy (1rgs)**: More sophisticated account management, better UI, Antigravity-specific optimizations
**vs opencode-antigravity-auth (NoeFabris)**: Full proxy solution vs OAuth plugin, broader model support
**vs Official Claude Code**: Provides access to newer models (Claude 4.5, Gemini 3) not available in official API

## Implementation Recommendations

### Quick Start Guide

1. **Install via npm** (recommended):
```bash
npx antigravity-claude-proxy@latest start
```

2. **Add Google accounts** (Web UI method):
- Open `http://localhost:8080`
- Navigate to Accounts tab
- Click "Add Account" and complete OAuth

3. **Configure Claude Code**:
```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "http://localhost:8080",
    "ANTHROPIC_AUTH_TOKEN": "test",
    "ANTHROPIC_MODEL": "claude-opus-4-5-thinking"
  }
}
```

4. **Verify setup**:
```bash
curl http://localhost:8080/health
curl "http://localhost:8080/account-limits?format=table"
```

### Code Examples

**Multi-account load balancer initialization**:
```javascript
import { AccountManager } from './account-manager/index.js';
import { createStrategy } from './account-manager/strategies/index.js';

const accountManager = new AccountManager({
  strategy: createStrategy('hybrid'),
  maxAccounts: 10,
  persistTokenCache: false
});
```

**Request routing with fallback**:
```javascript
const response = await cloudCodeClient.sendMessage({
  message: transformedMessage,
  model: requestedModel,
  stream: shouldStream
}, {
  accountManager,
  maxRetries: 5,
  fallbackEnabled: true
});
```

### Common Pitfalls

1. **Token Expiration**: OAuth tokens expire, requires re-authentication
   - **Solution**: Use `npm run accounts:verify` regularly, implement refresh logic

2. **Rate Limiting**: Individual account limits can be hit quickly
   - **Solution**: Add multiple Google accounts, use hybrid load balancing

3. **WSL Network Issues**: Localhost binding may not work in WSL
   - **Solution**: Use `0.0.0.0` binding or Windows host networking

4. **Model Quota Exhaustion**: Free tier limits can be restrictive
   - **Solution**: Monitor `/account-limits` endpoint, implement quota awareness

5. **ToS Compliance**: Risk of account suspension
   - **Solution**: Personal use only, avoid high-volume automated usage

## Resources & References

### Official Documentation

- [GitHub Repository](https://github.com/badrisnarayanan/antigravity-claude-proxy)
- [npm Package](https://www.npmjs.com/package/antigravity-claude-proxy)
- [Architecture Documentation](./CLAUDE.md)

### Recommended Tutorials

- Setup: Follow README.md quick start section
- Account Management: Use Web UI at `http://localhost:8080`
- CLI Usage: `antigravity-claude-proxy --help` for full command reference

### Community Resources

- [GitHub Discussions](https://github.com/badrisnarayanan/antigravity-claude-proxy/discussions)
- [Issue Templates](https://github.com/badrisnarayanan/antigravity-claude-proxy/issues/new/choose)
- [Buy Me a Coffee](https://buymeacoffee.com/badrinarayanans) (creator support)

### Further Reading

- [Related: opencode-antigravity-auth](https://github.com/NoeFabris/opencode-antigravity-auth)
- [Related: claude-code-proxy](https://github.com/1rgs/claude-code-proxy)
- [macOS Menu Bar App](https://github.com/IrvanFza/antigravity-claude-proxy-bar)

## Installation Requirements

### System Requirements

**Node.js**: ≥18.0.0 (ES modules support required)
**npm**: Compatible with npm workspaces
**Git**: For cloning repository (if not using npm)
**Browser**: For OAuth authentication and Web UI

### Dependencies Analysis

**Production Dependencies** (4 total, lightweight):
- `async-mutex@^0.5.0` - Thread-safe account selection
- `better-sqlite3@^12.5.0` - Local account storage
- `cors@^2.8.5` - CORS handling
- `express@^4.18.2` - HTTP server

**Development Dependencies** (6 total):
- `@tailwindcss/forms@^0.5.7` - Form styling
- `autoprefixer@^10.4.16` - CSS post-processing  
- `concurrently@^8.2.2` - Parallel script execution
- `daisyui@^4.12.14` - UI component library
- `postcss@^8.4.32` - CSS processing
- `tailwindcss@^3.4.0` - Utility-first CSS

### WSL/Linux Specific Considerations

**Installation**:
- Standard Node.js installation works on WSL2/Linux
- SQLite native compilation handled automatically by better-sqlite3
- No additional system packages required

**Network Configuration**:
- Default localhost:8080 binding works in WSL2
- For WSL1, may need Windows host IP binding
- OAuth redirect URLs work with localhost in WSL2

**File Permissions**:
- Account storage in `~/.antigravity-claude-proxy/`
- Requires write permissions to home directory
- Config files use standard Unix permissions

**Browser Integration**:
- OAuth flows work with Windows browsers from WSL2
- Manual authorization mode available for headless setups
- `--no-browser` flag for SSH/remote scenarios

**Process Management**:
- Standard Node.js process handling
- Graceful shutdown with SIGTERM/SIGINT
- Can be daemonized with systemd if needed

## Appendices

### A. Glossary

- **Antigravity**: Google's internal AI model access service
- **Cloud Code**: Google's Generative AI API wrapper service
- **Session ID**: Derived identifier for prompt caching optimization
- **Token Bucket**: Rate limiting algorithm with refill mechanism
- **Health Score**: Account reliability metric for load balancing
- **Thinking Mode**: Extended reasoning capability in Claude models

### B. Version Compatibility Matrix

| Component | Version | Compatibility |
|-----------|---------|--------------|
| Node.js | ≥18.0.0 | ES modules required |
| Claude Code CLI | Latest | Anthropic API compatible |
| Google Accounts | Any | OAuth2 compatible |
| Browsers | Modern | ES6+ for Web UI |

### C. Configuration Reference

**Environment Variables**:
- `PORT` - Server port (default: 8080)
- `DEBUG` - Enable debug logging
- `API_KEY` - Protect API endpoints
- `WEBUI_PASSWORD` - Protect web interface
- `FALLBACK` - Enable model fallback mode

**Config File Location**:
- Primary: `~/.config/antigravity-proxy/config.json`
- Fallback: `./config.json` (project root)

## Unresolved Questions

1. **Long-term ToS compliance**: Will Google/Anthropic change detection methods?
2. **Scaling limits**: Maximum practical number of accounts before diminishing returns?
3. **Enterprise support**: Any plans for commercial licensing or enterprise features?
4. **Model availability**: Which new models will be supported as they're released?
5. **Alternative backends**: Potential support for other AI service providers?

