name: Application Security Architecture - Core
use_when: When designing, implementing, or reviewing security architecture for applications, APIs, or system components.
content: |
  Core principles and practices for application security architecture:
  1.  **Security by Design**: Implement security from the start; use threat modeling, defense in depth, least privilege, and secure defaults.
  2.  **Authentication Architecture**: Implement OAuth 2.0/OIDC, MFA, strong password hashing (Argon2id), and secure session management.
  3.  **Authorization Framework**: Implement RBAC/ABAC; ensure proper permission granularity, context-aware authorization, and centralized services.
  4.  **API Security**: Implement authentication, rate limiting, input validation, proper error handling, CORS, and API key rotation.
  5.  **Data Protection**: Implement encryption at rest/in transit (TLS 1.3), proper key management, data classification, and minimization.
  6.  **Secure Communication**: Use mutual TLS, secure protocols, network segmentation, and proper firewall/WAF configuration.
  7.  **Vulnerability Management**: Implement automated security scanning (CI/CD), dependency scanning, and proper patch management.
  8.  **Logging & Monitoring**: Implement comprehensive security logging, centralized log management, SIEM, and alerting for incidents.
  9.  **Secure Development Practices**: Implement secure coding standards, automated security testing, code review for security, and training.
  10. **Incident Response**: Implement clear procedures, incident classification, forensic readiness, and business continuity planning.
  Apply these principles for comprehensive protection of the system and its data.

