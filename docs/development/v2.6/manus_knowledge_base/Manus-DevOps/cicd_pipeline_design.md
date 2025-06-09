name: CI/CD Pipeline Design
use_when: When designing, implementing, or optimizing continuous integration and continuous deployment pipelines.
content: 
When implementing CI/CD pipelines for Nexus Framework v2.6, follow these best practices:

1. **Pipeline Architecture**:
   - Implement multi-stage pipelines with clear separation of concerns
   - Use GitHub Actions as the primary CI/CD platform
   - Design for parallel execution where possible
   - Implement proper dependency management between stages
   - Use conditional execution for environment-specific stages
   - Design for reusability with composite actions
   - Implement proper error handling and notifications

2. **Source Control Integration**:
   - Trigger pipelines on pull requests and merges
   - Implement branch protection rules
   - Use status checks to enforce quality gates
   - Implement required reviews for critical branches
   - Use feature flags for in-progress features
   - Implement trunk-based development workflow
   - Use semantic versioning for releases

3. **Build Process**:
   - Use consistent build environments with containers
   - Implement caching for dependencies and build artifacts
   - Use deterministic builds for reproducibility
   - Implement proper versioning for all artifacts
   - Use build matrices for multi-platform builds
   - Implement parallel builds for efficiency
   - Use build timeouts to prevent hanging pipelines

4. **Testing Strategy**:
   - Implement automated testing at multiple levels
   - Use test parallelization for faster feedback
   - Implement code coverage reporting and thresholds
   - Use test splitting for large test suites
   - Implement visual regression testing
   - Use contract testing for service interfaces
   - Implement performance testing for critical paths

5. **Code Quality**:
   - Integrate static code analysis tools
   - Implement linting for all languages
   - Use code formatting enforcement
   - Implement security scanning for vulnerabilities
   - Use dependency scanning for outdated packages
   - Implement complexity analysis
   - Use quality gates with minimum thresholds

6. **Artifact Management**:
   - Use GitHub Packages for artifact storage
   - Implement proper versioning for all artifacts
   - Use immutable artifacts
   - Implement artifact signing for security
   - Use artifact metadata for traceability
   - Implement retention policies for artifacts
   - Use proper access controls for artifact repositories

7. **Deployment Strategy**:
   - Implement environment promotion workflow
   - Use infrastructure as code for all environments
   - Implement blue/green deployments for zero downtime
   - Use canary releases for risk mitigation
   - Implement automated rollback capabilities
   - Use feature flags for controlled releases
   - Implement deployment approval gates

8. **Environment Management**:
   - Use consistent environment configurations
   - Implement environment-specific variables
   - Use secrets management for sensitive data
   - Implement environment provisioning automation
   - Use environment locks to prevent concurrent deployments
   - Implement environment cleanup for ephemeral environments
   - Use environment monitoring and validation

9. **Monitoring and Feedback**:
   - Implement pipeline metrics collection
   - Use dashboards for pipeline visibility
   - Implement automated notifications for failures
   - Use post-deployment verification
   - Implement synthetic monitoring
   - Use deployment tracking and correlation
   - Implement feedback loops for continuous improvement

10. **Documentation and Compliance**:
    - Generate deployment documentation automatically
    - Implement change logs from commit messages
    - Use deployment tracking for compliance
    - Implement audit trails for all pipeline actions
    - Use approval workflows for regulated environments
    - Implement evidence collection for compliance
    - Use pipeline visualization for documentation

Apply these best practices consistently across all CI/CD pipelines to ensure reliability, efficiency, and maintainability of the deployment process.
