name: Application Security Architecture
use_when: When designing, implementing, or reviewing security architecture for applications, APIs, or system components.
content: 
When implementing security architecture for Nexus Framework v2.6, follow these principles and practices:

1. **Security by Design**:
   - Implement security requirements from the beginning of development
   - Use threat modeling for all components and features
   - Apply defense in depth with multiple security layers
   - Implement secure defaults for all configurations
   - Use principle of least privilege for all access controls
   - Design for fail-secure behavior
   - Implement security testing throughout the development lifecycle
   - Document security assumptions and dependencies

2. **Authentication Architecture**:
   - Implement OAuth 2.0 with OpenID Connect for authentication
   - Use multi-factor authentication for sensitive operations
   - Implement proper password hashing with Argon2id
   - Use secure session management with proper timeouts
   - Implement JWT with appropriate signing algorithms (RS256)
   - Use secure cookie attributes (Secure, HttpOnly, SameSite)
   - Implement proper credential storage and management
   - Design for identity federation where appropriate

3. **Authorization Framework**:
   - Implement role-based access control (RBAC) as baseline
   - Use attribute-based access control (ABAC) for complex scenarios
   - Implement proper permission granularity
   - Design for context-aware authorization
   - Use centralized authorization services
   - Implement proper authorization checks at all layers
   - Design for delegation of authority where needed
   - Document authorization matrix for all resources

4. **API Security**:
   - Implement proper authentication for all endpoints
   - Use rate limiting and throttling to prevent abuse
   - Implement input validation for all parameters
   - Use proper error handling without information leakage
   - Implement proper CORS configuration
   - Use API keys with proper rotation policies
   - Implement API versioning for security updates
   - Design for proper API documentation with security requirements

5. **Data Protection**:
   - Implement encryption at rest for sensitive data
   - Use TLS 1.3 for all data in transit
   - Implement proper key management with rotation
   - Use data classification to identify protection requirements
   - Implement data minimization principles
   - Design for proper data retention and deletion
   - Use tokenization for sensitive data where appropriate
   - Implement proper backup security

6. **Secure Communication**:
   - Use mutual TLS for service-to-service communication
   - Implement proper certificate management
   - Use secure protocols for all communications
   - Implement network segmentation
   - Design for proper firewall and WAF configuration
   - Use VPC and security groups for cloud deployments
   - Implement proper DNS security
   - Design for secure service discovery

7. **Vulnerability Management**:
   - Implement automated security scanning in CI/CD
   - Use dependency scanning for third-party vulnerabilities
   - Implement proper patch management processes
   - Design for secure dependency updating
   - Use vulnerability disclosure process
   - Implement security regression testing
   - Design for quick vulnerability response
   - Document vulnerability management procedures

8. **Logging and Monitoring**:
   - Implement comprehensive security logging
   - Use centralized log management
   - Implement proper log protection and retention
   - Design for security event detection
   - Use security information and event management (SIEM)
   - Implement alerting for security incidents
   - Design for proper audit trails
   - Use log correlation for security analysis

9. **Secure Development Practices**:
   - Implement secure coding standards
   - Use automated security testing in development
   - Implement proper code review for security
   - Design for security training and awareness
   - Use security champions within development teams
   - Implement proper security documentation
   - Design for security knowledge sharing
   - Use security metrics for continuous improvement

10. **Incident Response**:
    - Implement incident response procedures
    - Use proper incident classification
    - Implement forensic readiness
    - Design for business continuity
    - Use tabletop exercises for preparation
    - Implement proper communication plans
    - Design for lessons learned process
    - Document incident response roles and responsibilities

Apply these security architecture principles consistently across all components to ensure comprehensive protection of the system and its data.
