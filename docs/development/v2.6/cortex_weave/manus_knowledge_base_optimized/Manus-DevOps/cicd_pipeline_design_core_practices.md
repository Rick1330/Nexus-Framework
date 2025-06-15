name: CI/CD Pipeline Design - Core Practices
use_when: When designing, implementing, or optimizing continuous integration and continuous deployment pipelines.
content: |
  Core practices for CI/CD pipeline design:
  1.  **Pipeline Architecture**: Implement multi-stage pipelines with clear separation of concerns; use GitHub Actions; design for parallel execution and reusability.
  2.  **Source Control Integration**: Trigger pipelines on PRs/merges; enforce branch protection; use status checks and required reviews.
  3.  **Build Process**: Use consistent containerized environments; implement caching, deterministic builds, and proper artifact versioning.
  4.  **Testing Strategy**: Implement automated testing at multiple levels; use parallelization, code coverage, and various testing types (e.g., visual, contract, performance).
  5.  **Code Quality**: Integrate static analysis, linting, formatting, security/dependency scanning, and complexity analysis with quality gates.
  6.  **Artifact Management**: Use GitHub Packages; implement proper versioning, immutability, signing, metadata, and retention policies.
  7.  **Deployment Strategy**: Implement environment promotion; use IaC; employ blue/green or canary deployments; enable automated rollbacks and approval gates.
  8.  **Environment Management**: Use consistent configurations; implement environment-specific variables, secrets management, and provisioning automation.
  9.  **Monitoring & Feedback**: Collect pipeline metrics; use dashboards, automated notifications, post-deployment verification, and feedback loops.
  10. **Documentation & Compliance**: Generate documentation automatically; implement change logs, audit trails, and approval workflows for compliance.
  Apply these practices for reliable, efficient, and maintainable CI/CD processes.

