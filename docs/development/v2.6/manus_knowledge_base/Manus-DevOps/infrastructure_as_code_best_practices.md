name: Infrastructure as Code Best Practices
use_when: When designing, implementing, or reviewing infrastructure as code for cloud resources and deployment environments.
content: 
When implementing Infrastructure as Code (IaC) for Nexus Framework v2.6, follow these best practices:

1. **Declarative Over Imperative**:
   - Use declarative IaC tools like Terraform or CloudFormation
   - Define desired end state rather than steps to get there
   - Allow the IaC tool to determine the execution plan
   - Focus on "what" rather than "how"
   - Use modules to encapsulate complex resource relationships
   - Implement consistent resource naming conventions
   - Use resource attributes for dynamic references

2. **Modularization**:
   - Create reusable modules for common infrastructure patterns
   - Implement consistent module interfaces with input/output variables
   - Use composition to build complex infrastructure from simple modules
   - Maintain version control for modules
   - Document module usage and examples
   - Implement module testing
   - Use consistent module structure and organization

3. **State Management**:
   - Use remote state storage (e.g., S3, Azure Storage)
   - Implement state locking to prevent concurrent modifications
   - Use workspaces for environment isolation
   - Implement state backup strategies
   - Use partial state updates for large infrastructures
   - Document state dependencies
   - Implement proper access controls for state

4. **Environment Separation**:
   - Use separate state files for each environment
   - Implement consistent environment naming
   - Use environment-specific variable files
   - Maintain environment parity where possible
   - Implement promotion paths between environments
   - Use consistent tagging for environment identification
   - Document environment-specific configurations

5. **Security Best Practices**:
   - Use least privilege IAM roles for IaC execution
   - Implement secure secret management (e.g., HashiCorp Vault)
   - Use security groups with minimal required access
   - Implement network segmentation with proper VPC design
   - Enable encryption for data at rest and in transit
   - Use security scanning for IaC code
   - Implement compliance as code

6. **Change Management**:
   - Use version control for all IaC code
   - Implement peer review process for infrastructure changes
   - Use pull requests for change approval
   - Generate and review execution plans before applying
   - Document all changes with clear descriptions
   - Implement change validation testing
   - Use blue/green or canary deployments for critical changes

7. **Testing Strategies**:
   - Implement unit testing for modules
   - Use integration testing for complex infrastructure
   - Implement policy as code for compliance testing
   - Use infrastructure validation tools
   - Implement smoke tests after deployment
   - Use chaos engineering for resilience testing
   - Document test coverage and results

8. **Cost Optimization**:
   - Use cost estimation tools before deployment
   - Implement resource tagging for cost allocation
   - Use auto-scaling for dynamic workloads
   - Implement scheduled scaling for predictable patterns
   - Use appropriate instance types and sizes
   - Implement lifecycle policies for storage
   - Use spot instances where appropriate

9. **Documentation**:
   - Document infrastructure architecture and design decisions
   - Generate documentation from code where possible
   - Maintain README files for all modules
   - Document variables and outputs
   - Use diagrams for visual representation
   - Document dependencies and assumptions
   - Maintain runbooks for operational procedures

10. **CI/CD Integration**:
    - Integrate IaC into CI/CD pipelines
    - Implement automated testing for infrastructure
    - Use plan and apply stages in pipeline
    - Implement approval gates for production changes
    - Generate and store execution plans as artifacts
    - Implement drift detection
    - Use consistent pipeline structure across projects

Apply these best practices consistently across all infrastructure as code implementations to ensure reliability, security, and maintainability.
