name: Security Testing Methodology
use_when: When designing, implementing, or reviewing security testing plans, vulnerability assessments, or penetration testing activities.
content: 
When implementing security testing for Nexus Framework v2.6, follow these methodologies:

1. **Security Testing Strategy**:
   - Implement a layered testing approach covering all security domains
   - Use a combination of automated and manual testing techniques
   - Integrate security testing throughout the development lifecycle
   - Implement risk-based testing prioritization
   - Design for comprehensive coverage of OWASP Top 10 and SANS 25
   - Use both positive and negative testing approaches
   - Implement proper test data management for security tests
   - Document security testing strategy and coverage

2. **Static Application Security Testing (SAST)**:
   - Integrate SAST tools into the CI/CD pipeline
   - Implement custom rules for framework-specific vulnerabilities
   - Use incremental scanning for faster feedback
   - Implement proper false positive management
   - Design for security debt tracking
   - Use trend analysis for security issues
   - Implement severity-based alerting
   - Document SAST tool configuration and exceptions

3. **Dynamic Application Security Testing (DAST)**:
   - Implement automated DAST in the deployment pipeline
   - Use authenticated and unauthenticated scanning
   - Implement proper scope definition for DAST
   - Design for safe testing of production environments
   - Use targeted DAST for high-risk features
   - Implement proper handling of DAST findings
   - Design for DAST tool tuning and optimization
   - Document DAST testing procedures and schedules

4. **Interactive Application Security Testing (IAST)**:
   - Implement IAST for development and test environments
   - Use runtime instrumentation for vulnerability detection
   - Implement proper performance impact management
   - Design for developer feedback integration
   - Use IAST for real-time security feedback
   - Implement proper IAST agent configuration
   - Design for integration with CI/CD pipeline
   - Document IAST coverage and limitations

5. **Penetration Testing**:
   - Conduct regular penetration testing by skilled professionals
   - Implement proper scoping and rules of engagement
   - Use a combination of black, gray, and white box testing
   - Implement proper reporting and remediation tracking
   - Design for targeted penetration testing of critical components
   - Use penetration testing for validation of security controls
   - Implement proper authorization for penetration testing
   - Document penetration testing methodology and findings

6. **Vulnerability Management**:
   - Implement a structured vulnerability management process
   - Use proper vulnerability classification and prioritization
   - Implement SLAs for vulnerability remediation by severity
   - Design for vulnerability verification after remediation
   - Use vulnerability trending and metrics
   - Implement proper vulnerability disclosure process
   - Design for coordination with security researchers
   - Document vulnerability management procedures

7. **Security Code Review**:
   - Implement security-focused code reviews
   - Use security checklists for different technology stacks
   - Implement pair review for security-critical code
   - Design for security knowledge sharing during reviews
   - Use automated tools to support manual reviews
   - Implement proper documentation of security decisions
   - Design for security review of third-party code
   - Document security code review process and findings

8. **API Security Testing**:
   - Implement comprehensive testing of API security controls
   - Use API fuzzing for robustness testing
   - Implement proper authentication and authorization testing
   - Design for API abuse case testing
   - Use contract-based security testing
   - Implement proper API parameter testing
   - Design for API versioning security testing
   - Document API security testing coverage

9. **Infrastructure Security Testing**:
   - Implement regular infrastructure vulnerability scanning
   - Use configuration compliance scanning
   - Implement container security scanning
   - Design for cloud security posture assessment
   - Use network security testing
   - Implement proper credential scanning
   - Design for infrastructure as code security testing
   - Document infrastructure security testing procedures

10. **Security Test Automation**:
    - Implement security test automation framework
    - Use security test orchestration
    - Implement proper security test reporting
    - Design for security test metrics and KPIs
    - Use security test coverage tracking
    - Implement proper security test maintenance
    - Design for continuous security testing
    - Document security test automation architecture

Apply these security testing methodologies consistently across all components to ensure comprehensive security validation and vulnerability management.
