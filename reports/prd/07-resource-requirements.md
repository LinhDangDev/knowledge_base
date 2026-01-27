# Resource Requirements & Budget Estimation

**Document Version**: 1.0
**Date**: January 27, 2026
**Project**: SHUNCOM RULR IoT Platform
**Related Documents**: [06-Implementation Roadmap](./06-implementation-roadmap.md)

---

## 1. Team Composition & Staffing

### 1.1 Development Team Structure

#### Core Development Team (Full-Time)
```yaml
Project Manager (1):
  Duration: 8 months
  Responsibilities:
    - Overall project coordination
    - Stakeholder management
    - Sprint planning and execution
    - Risk management
    - Budget tracking
  Qualifications:
    - 5+ years PM experience
    - PMP or equivalent certification
    - IoT/SaaS project experience
  Cost: $12,000/month × 8 months = $96,000

Technical Lead / Architect (1):
  Duration: 8 months
  Responsibilities:
    - System architecture design
    - Technology stack decisions
    - Code review oversight
    - Technical debt management
    - Cross-team coordination
  Qualifications:
    - 8+ years software development
    - Distributed systems experience
    - IoT platform expertise
  Cost: $15,000/month × 8 months = $120,000

Backend Developer - Senior (2):
  Duration: 8 months
  Responsibilities:
    - Core API development
    - Rule engine implementation
    - Database design and optimization
    - IoT protocol integration
  Qualifications:
    - 5+ years backend development
    - Node.js/NestJS expertise
    - PostgreSQL, Redis experience
    - MQTT/IoT protocols
  Cost: $10,000/month × 2 × 8 months = $160,000

Backend Developer - Mid-Level (1):
  Duration: 8 months
  Responsibilities:
    - Feature development
    - API endpoint implementation
    - Unit/integration testing
    - Bug fixes
  Qualifications:
    - 3+ years backend development
    - Node.js experience
    - RESTful API design
  Cost: $7,000/month × 8 months = $56,000

Frontend Developer - Senior (1):
  Duration: 8 months
  Responsibilities:
    - Dashboard UI architecture
    - GIS map integration
    - Real-time updates (WebSocket)
    - Performance optimization
  Qualifications:
    - 5+ years frontend development
    - React.js expertise
    - Leaflet.js / mapping libraries
    - WebSocket implementation
  Cost: $9,000/month × 8 months = $72,000

Frontend Developer - Mid-Level (1):
  Duration: 8 months
  Responsibilities:
    - Component development
    - Form validation
    - Responsive design
    - UI testing
  Qualifications:
    - 3+ years frontend development
    - React.js, TypeScript
    - CSS frameworks (Ant Design/Material-UI)
  Cost: $6,500/month × 8 months = $52,000

DevOps Engineer (1):
  Duration: 8 months
  Responsibilities:
    - CI/CD pipeline setup
    - Infrastructure provisioning
    - Monitoring and logging
    - Deployment automation
    - Security hardening
  Qualifications:
    - 4+ years DevOps experience
    - Docker, Kubernetes
    - AWS/Azure/GCP
    - Terraform/Ansible
  Cost: $9,500/month × 8 months = $76,000

QA Engineer - Senior (1):
  Duration: 6 months (months 3-8)
  Responsibilities:
    - Test strategy and planning
    - Automated test framework
    - Performance testing
    - Security testing
  Qualifications:
    - 4+ years QA experience
    - Test automation (Jest, Cypress)
    - Performance testing tools
  Cost: $7,500/month × 6 months = $45,000

QA Engineer - Junior (1):
  Duration: 6 months (months 3-8)
  Responsibilities:
    - Manual testing
    - Test case creation
    - Bug reporting
    - Regression testing
  Qualifications:
    - 1-2 years QA experience
    - Test case design
    - Bug tracking tools
  Cost: $4,500/month × 6 months = $27,000
```

**Core Team Total**: $704,000

---

#### Specialized Roles (Part-Time / Contract)

```yaml
UI/UX Designer (1):
  Duration: 3 months (months 1-3)
  Commitment: 50% (80 hours/month)
  Responsibilities:
    - Interface design
    - User experience research
    - Wireframes and mockups
    - Design system creation
  Qualifications:
    - 3+ years UI/UX design
    - Figma/Sketch proficiency
    - Dashboard design experience
  Cost: $6,000/month × 3 months = $18,000

IoT Integration Specialist (1):
  Duration: 4 months (months 2-5)
  Commitment: 75% (120 hours/month)
  Responsibilities:
    - Device protocol implementation
    - Gateway firmware coordination
    - Hardware vendor liaison
    - Field testing
  Qualifications:
    - 5+ years IoT experience
    - Zigbee, LoRa, NB-IoT protocols
    - Embedded systems knowledge
  Cost: $8,000/month × 4 months = $32,000

Security Consultant (1):
  Duration: 2 months (months 7-8)
  Commitment: 25% (40 hours/month)
  Responsibilities:
    - Security audit
    - Penetration testing
    - Compliance review (GDPR)
    - Security best practices
  Qualifications:
    - CISSP or equivalent
    - Application security expertise
    - IoT security knowledge
  Cost: $5,000/month × 2 months = $10,000

Technical Writer (1):
  Duration: 2 months (months 7-8)
  Commitment: 100%
  Responsibilities:
    - User documentation
    - API documentation
    - Admin guides
    - Video tutorials
  Qualifications:
    - 2+ years technical writing
    - Software documentation
    - Video editing skills
  Cost: $5,000/month × 2 months = $10,000

Data Analyst (1):
  Duration: 1 month (month 7)
  Commitment: 50%
  Responsibilities:
    - Analytics requirements
    - KPI definition
    - Report templates
    - Data validation
  Qualifications:
    - 3+ years data analysis
    - SQL expertise
    - BI tools (Tableau/PowerBI)
  Cost: $4,000/month × 1 month = $4,000
```

**Specialized Roles Total**: $74,000

---

### 1.2 Total Team Cost Summary

| Category | Headcount | Duration | Total Cost |
|----------|-----------|----------|------------|
| **Core Development Team** | 10 FTE | 6-8 months | $704,000 |
| **Specialized Roles** | 5 contractors | 1-4 months | $74,000 |
| **Recruitment & Onboarding** | - | - | $15,000 |
| **Training & Development** | - | - | $10,000 |
| **Team Total** | - | - | **$803,000** |

---

## 2. Infrastructure & Cloud Costs

### 2.1 Development Environment (8 months)

```yaml
Cloud Services (AWS):
  EC2 Instances (Dev/Staging):
    - 3× t3.medium (Dev): $30/month × 3 × 8 = $720
    - 2× t3.large (Staging): $60/month × 2 × 8 = $960
  RDS PostgreSQL (Dev/Staging):
    - db.t3.medium: $50/month × 8 = $400
  ElastiCache Redis:
    - cache.t3.micro: $15/month × 8 = $120
  S3 Storage:
    - 100GB storage: $2.30/month × 8 = $18
  Data Transfer:
    - Outbound: $20/month × 8 = $160
  Total Development Cloud: $2,378

CI/CD & Tools:
  GitHub Enterprise: $21/user/month × 12 users × 8 = $2,016
  Docker Hub (Team): $7/user/month × 12 × 8 = $672
  Sentry (Error Tracking): $26/month × 8 = $208
  Total CI/CD: $2,896

Development Tools:
  JetBrains Licenses: $199/year × 12 = $2,388
  Figma (Design): $12/user/month × 2 × 8 = $192
  Postman (API Testing): $12/user/month × 5 × 8 = $480
  Total Dev Tools: $3,060
```

**Development Environment Total**: $8,334

---

### 2.2 Production Environment (First Year)

```yaml
Compute - Kubernetes Cluster:
  Frontend Nodes:
    - 3× c5.xlarge (4 vCPU, 8GB): $122/month × 3 = $366
  Backend Nodes:
    - 5× c5.2xlarge (8 vCPU, 16GB): $244/month × 5 = $1,220
  Worker Nodes:
    - 3× c5.xlarge: $122/month × 3 = $366
  Load Balancer (ALB): $25/month
  Total Compute: $1,977/month

Database - RDS PostgreSQL:
  Primary Instance:
    - db.r5.2xlarge (8 vCPU, 64GB): $900/month
  Read Replicas (2):
    - db.r5.xlarge × 2: $450/month × 2 = $900
  Automated Backups: $50/month
  Total Database: $1,850/month

Cache - ElastiCache Redis:
  Cluster Mode (6 nodes):
    - cache.r5.xlarge × 6: $180/month × 6 = $1,080
  Total Cache: $1,080/month

Storage:
  S3 Object Storage:
    - 1TB storage: $23/month
    - Requests: $20/month
    - Data transfer: $90/month
  EBS Volumes (Kubernetes):
    - 500GB SSD: $50/month
  Total Storage: $183/month

MQTT Broker (EMQX):
  EC2 Instances:
    - 3× c5.2xlarge (cluster): $244/month × 3 = $732
  Total MQTT: $732/month

Monitoring & Logging:
  Prometheus + Grafana (EC2): $100/month
  ELK Stack (Elasticsearch): $300/month
  CloudWatch Logs: $50/month
  Total Monitoring: $450/month

CDN - CloudFlare:
  Pro Plan: $20/month
  Bandwidth (estimated): $80/month
  Total CDN: $100/month

Networking:
  VPC, NAT Gateway: $45/month
  Data Transfer: $200/month
  Total Networking: $245/month

Total Monthly (Production): $6,617/month
Total Annual (Production): $79,404/year
```

**Production Infrastructure (Year 1)**: $79,404

---

### 2.3 Third-Party Services

```yaml
GIS Mapping:
  Provider: Mapbox / Google Maps API
  Usage: 500,000 map loads/month
  Cost: $400/month × 12 = $4,800/year

Email Service (Transactional):
  Provider: SendGrid / AWS SES
  Volume: 100,000 emails/month
  Cost: $80/month × 12 = $960/year

SMS Service:
  Provider: Twilio
  Volume: 5,000 SMS/month
  Cost: $350/month × 12 = $4,200/year

Push Notifications:
  Provider: Firebase Cloud Messaging
  Volume: Unlimited (free tier)
  Cost: $0/year

Monitoring & APM:
  Provider: Datadog / New Relic
  Infrastructure monitoring: $15/host × 15 hosts = $225/month
  APM: $31/host × 5 hosts = $155/month
  Total: $380/month × 12 = $4,560/year

SSL Certificates:
  Provider: Let's Encrypt (free) or Wildcard SSL
  Cost: $200/year

Domain & DNS:
  Domain registration: $20/year
  Route 53 DNS: $50/month × 12 = $600/year
  Total: $620/year

Backup & DR:
  S3 Glacier (long-term backup): $50/month × 12 = $600/year
  Cross-region replication: $100/month × 12 = $1,200/year
  Total: $1,800/year

Security Services:
  WAF (Web Application Firewall): $100/month × 12 = $1,200/year
  DDoS Protection: $200/month × 12 = $2,400/year
  Total: $3,600/year
```

**Third-Party Services Total (Year 1)**: $20,540

---

### 2.4 Infrastructure Total Summary

| Category | Development (8 months) | Production (Year 1) |
|----------|------------------------|---------------------|
| Cloud Services | $8,334 | $79,404 |
| Third-Party Services | $3,000 (prorated) | $20,540 |
| **Subtotal** | **$11,334** | **$99,944** |
| **Total Infrastructure** | - | **$111,278** |

---

## 3. Hardware & Equipment

### 3.1 Development Equipment

```yaml
Workstations (12 team members):
  Laptops (MacBook Pro / High-end PC):
    - $2,500 × 12 = $30,000
  External Monitors (2 per developer):
    - $300 × 2 × 10 developers = $6,000
  Accessories (keyboard, mouse, headset):
    - $200 × 12 = $2,400

Total Development Equipment: $38,400

Office Equipment:
  Meeting room setup (camera, mic, TV): $3,000
  Whiteboard, projector: $1,500

Total Office Equipment: $4,500
```

**Development Hardware Total**: $42,900

---

### 3.2 IoT Device Testing Equipment

```yaml
Gateway Devices:
  Smart Gateways (Star Box):
    - 10 units × $350 = $3,500

Light Controllers:
  Zigbee Controllers: 20 units × $45 = $900
  NB-IoT Controllers: 10 units × $70 = $700
  LoRa Controllers: 10 units × $60 = $600

Lighting Fixtures:
  LED Fixtures (test): 20 units × $150 = $3,000

Meters & Sensors:
  Smart Meters: 5 units × $250 = $1,250
  Loop Controllers: 5 units × $120 = $600

Testing Tools:
  Multimeters, oscilloscopes: $2,000
  Protocol analyzers: $1,500
  Network testing equipment: $1,000

Total IoT Testing Equipment: $15,050
```

**IoT Equipment Total**: $15,050

---

### 3.3 Hardware Total Summary

| Category | Cost |
|----------|------|
| Development Equipment | $42,900 |
| IoT Testing Equipment | $15,050 |
| **Hardware Total** | **$57,950** |

---

## 4. Software Licenses & Subscriptions

### 4.1 Development Tools (8 months)

```yaml
IDE & Development:
  JetBrains All Products Pack: $199/year × 12 = $2,388
  Visual Studio Code: Free

Design Tools:
  Figma Professional: $12/user/month × 2 × 8 = $192
  Adobe Creative Cloud: $53/user/month × 1 × 8 = $424

Collaboration:
  Slack Business+: $12.50/user/month × 15 × 8 = $1,500
  Zoom Pro: $15/user/month × 3 × 8 = $360
  Notion Team: $8/user/month × 15 × 8 = $960

Project Management:
  Jira Software: $7/user/month × 15 × 8 = $840
  Confluence: $5/user/month × 15 × 8 = $600

Version Control:
  GitHub Enterprise: $21/user/month × 12 × 8 = $2,016

Testing & QA:
  BrowserStack: $99/month × 8 = $792
  Postman Team: $12/user/month × 5 × 8 = $480

Total Software Licenses (8 months): $10,552
```

**Software Licenses Total**: $10,552

---

## 5. Training & Professional Development

```yaml
Technical Training:
  Online courses (Udemy, Coursera): $500/person × 12 = $6,000
  Conference attendance (2 team members):
    - Registration: $1,500 × 2 = $3,000
    - Travel & accommodation: $2,000 × 2 = $4,000

Certifications:
  AWS Certified Solutions Architect: $300 × 2 = $600
  Kubernetes certifications: $300 × 1 = $300

Total Training: $13,900
```

**Training Total**: $13,900

---

## 6. Contingency & Miscellaneous

```yaml
Contingency Reserve:
  10% of total project cost: $110,000

Recruitment & Hiring:
  Recruiter fees: $10,000
  Interview expenses: $3,000
  Onboarding: $2,000
  Total Recruitment: $15,000

Legal & Compliance:
  Contract reviews: $3,000
  GDPR compliance audit: $5,000
  Terms of service, privacy policy: $2,000
  Total Legal: $10,000

Marketing & Launch:
  Landing page development: $5,000
  Launch materials: $3,000
  Total Marketing: $8,000

Travel & Meetings:
  Team offsites: $15,000
  Client meetings: $5,000
  Total Travel: $20,000

Total Miscellaneous: $163,000
```

**Contingency & Misc Total**: $163,000

---

## 7. Total Budget Summary

### 7.1 One-Time Costs (Year 1)

| Category | Cost |
|----------|------|
| **Team Costs** | $803,000 |
| Development Infrastructure (8 months) | $11,334 |
| Production Infrastructure (4 months) | $33,315 |
| Hardware & Equipment | $57,950 |
| Software Licenses | $10,552 |
| Training & Development | $13,900 |
| Contingency & Miscellaneous | $163,000 |
| **Total Year 1** | **$1,093,051** |

**Rounded Total**: **$1,100,000**

---

### 7.2 Ongoing Costs (Annual, Year 2+)

| Category | Annual Cost |
|----------|-------------|
| **Reduced Team** (6 FTE) | $450,000 |
| Production Infrastructure | $99,944 |
| Third-Party Services | $20,540 |
| Software Licenses | $15,000 |
| Training & Development | $8,000 |
| Support & Maintenance | $50,000 |
| Contingency (5%) | $32,000 |
| **Total Year 2+** | **$675,484** |

**Rounded Annual**: **$680,000**

---

## 8. Revenue Model & ROI Analysis

### 8.1 Pricing Strategy

```yaml
Subscription Tiers:

Starter Tier:
  Devices: Up to 500
  Users: Up to 10
  Features: Basic device management, simple rules
  Price: $500/month ($6,000/year)

Professional Tier:
  Devices: Up to 5,000
  Users: Up to 50
  Features: All features + GIS + Advanced alarms
  Price: $2,000/month ($24,000/year)

Enterprise Tier:
  Devices: Up to 50,000
  Users: Unlimited
  Features: All features + Dedicated support
  Price: $8,000/month ($96,000/year)

Custom Tier:
  Devices: 50,000+
  Price: Custom negotiation
```

---

### 8.2 Customer Acquisition Projections

```yaml
Year 1 (Months 9-12, post-launch):
  Starter: 10 customers × $6,000 = $60,000
  Professional: 5 customers × $24,000 = $120,000
  Enterprise: 2 customers × $96,000 = $192,000
  Total Year 1 Revenue: $372,000

Year 2:
  Starter: 30 customers × $6,000 = $180,000
  Professional: 20 customers × $24,000 = $480,000
  Enterprise: 8 customers × $96,000 = $768,000
  Total Year 2 Revenue: $1,428,000

Year 3:
  Starter: 50 customers × $6,000 = $300,000
  Professional: 40 customers × $24,000 = $960,000
  Enterprise: 15 customers × $96,000 = $1,440,000
  Total Year 3 Revenue: $2,700,000
```

---

### 8.3 ROI Calculation

```yaml
Total Investment (Year 1): $1,100,000
Year 1 Revenue (4 months): $372,000
Year 1 Net: -$728,000

Year 2 Revenue: $1,428,000
Year 2 Costs: $680,000
Year 2 Net: +$748,000

Cumulative by End of Year 2: +$20,000 (Break-even)

Year 3 Revenue: $2,700,000
Year 3 Costs: $680,000
Year 3 Net: +$2,020,000

ROI by End of Year 3:
  Total Revenue: $4,500,000
  Total Costs: $2,460,000
  Net Profit: $2,040,000
  ROI: 183%
```

**Break-even Point**: End of Year 2 (24 months)
**3-Year ROI**: 183%

---

## 9. Cost Optimization Strategies

### 9.1 Infrastructure Optimization

```yaml
Strategies:
  ✅ Use reserved instances (30% savings on EC2)
  ✅ Implement auto-scaling (reduce over-provisioning)
  ✅ Use spot instances for non-critical workloads
  ✅ Compress and archive old data (reduce storage costs)
  ✅ Optimize database queries (reduce compute needs)

Potential Savings: 20-25% of infrastructure costs
```

### 9.2 Team Optimization

```yaml
Strategies:
  ✅ Hire junior developers for routine tasks
  ✅ Use contractors for specialized work
  ✅ Offshore development for non-core features
  ✅ Cross-train team members

Potential Savings: 15-20% of team costs
```

---

**Next Document**: [08-Risk Assessment](./08-risk-assessment.md)

---

## Document Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2026-01-27 | Initial resource requirements | AI Assistant |
