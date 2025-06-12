name: Infrastructure as Code (IaC) Best Practices - Core
use_when: When designing, implementing, or reviewing infrastructure as code for cloud resources and deployment environments.
content: |
  Core best practices for Infrastructure as Code (IaC):
  1.  **Declarative Over Imperative**: Use declarative tools (Terraform, CloudFormation); define desired end state; focus on "what" not "how."
  2.  **Modularization**: Create reusable modules for common patterns; use consistent interfaces; maintain version control for modules.
  3.  **State Management**: Use remote state storage (S3); implement state locking; use workspaces for environment isolation.
  4.  **Environment Separation**: Use separate state files for each environment; implement consistent naming; maintain environment parity.
  5.  **Security Best Practices**: Use least privilege IAM roles; implement secure secret management; use security groups with minimal access.
  6.  **Change Management**: Use version control for all IaC code; implement peer review; use pull requests for change approval.
  7.  **Testing Strategies**: Implement unit, integration, and policy as code testing; use infrastructure validation tools.
  8.  **Cost Optimization**: Use cost estimation tools; implement resource tagging; use auto-scaling and appropriate instance types.
  9.  **Documentation**: Document infrastructure architecture; generate documentation from code; maintain READMEs for modules.
  10. **CI/CD Integration**: Integrate IaC into CI/CD pipelines; automate testing; use plan/apply stages; implement approval gates.
  Apply these practices for reliable, secure, and maintainable infrastructure deployments.

