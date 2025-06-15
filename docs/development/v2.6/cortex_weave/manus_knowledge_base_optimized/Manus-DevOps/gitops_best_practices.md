name: GitOps Best Practices
use_when: When implementing GitOps for continuous delivery, infrastructure management, or application deployment.
content: |
  Key best practices for GitOps:
  1.  **Declarative Configuration**: All system configurations (infrastructure, applications) are described declaratively in Git. Git is the single source of truth.
  2.  **Version Control**: Every change to the system is version-controlled, auditable, and revertible through Git commits. This enables a clear history and easy rollbacks.
  3.  **Automated Synchronization**: An automated process (e.g., Flux, Argo CD) continuously observes the desired state in Git and reconciles it with the actual state in the cluster.
  4.  **Pull Request Workflow**: All changes to the desired state are made via pull requests, enabling collaboration, code reviews, and automated testing before merging.
  5.  **Immutable Infrastructure**: Infrastructure components are treated as immutable; changes are made by replacing components rather than modifying them in place.
  6.  **Observability**: Comprehensive monitoring and logging are in place to observe the system's state and detect any drift from the desired state defined in Git.
  7.  **Security**: Implement strong access controls for Git repositories, sign commits, and ensure that the automated reconciliation agent has minimal necessary permissions.
  8.  **Secrets Management**: Integrate with external secrets management solutions (e.g., HashiCorp Vault, Kubernetes Secrets Store CSI Driver) to keep sensitive data out of Git.
  9.  **Environment Promotion**: Use Git branches or separate repositories to manage different environments (dev, staging, prod) and promote changes through a controlled merge process.
  10. **Testing**: Implement automated testing for infrastructure and application configurations within the GitOps pipeline to ensure correctness and prevent errors.
  Apply these practices for reliable, auditable, and automated deployments.

