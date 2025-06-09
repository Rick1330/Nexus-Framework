name: GitHub Account Management for Distributed Development
use_when: When setting up GitHub accounts, repositories, and access controls for distributed multi-agent development teams.
content: 
# GitHub Account Management for Distributed Multi-Agent Development

## Account Strategy Recommendations

When implementing GitHub account management for Nexus Framework v2.6 distributed development with multiple Manus accounts, consider these approaches:

### Option 1: Single Organization Account with Role-Based Access (Recommended)

**Implementation:**
- Create one GitHub organization account (e.g., `NexusFramework`)
- Create team structures within the organization that mirror Manus account roles
- Assign repository permissions based on team roles
- Use branch protection rules to enforce workflow
- Configure commit signing for all contributors
- Use commit trailers to indicate which Manus account authored the commit

**Benefits:**
- Centralized administration and billing
- Simplified access management
- Better visibility across all repositories
- Easier integration with CI/CD tools
- Consistent security policies
- Clear audit trail

**Configuration Steps:**
1. Create GitHub organization
2. Create teams for each Manus account role (Architect, Backend, Frontend, etc.)
3. Configure repository access permissions by team
4. Set up branch protection rules
5. Configure required commit signing
6. Establish commit message templates with Manus account attribution

### Option 2: Multiple Individual Accounts with Shared Access

**Implementation:**
- Create separate GitHub accounts for each Manus account role
- Use repository collaborator invitations for shared access
- Implement consistent naming convention for accounts
- Use organization for centralized billing if needed

**Benefits:**
- Clear separation of identities
- Direct attribution of commits to specific roles
- Simplified access revocation if needed

**Drawbacks:**
- More complex administration
- Potential for inconsistent access patterns
- Multiple billing entities
- More difficult audit trail

## Repository Structure

Regardless of account strategy, implement this repository structure:

1. **Monorepo Approach (Recommended)**
   - Single repository containing all components
   - Clear directory structure mirroring architecture
   - Granular permissions at the directory level where possible
   - Comprehensive documentation in central location

2. **Multi-Repo Approach (Alternative)**
   - Separate repositories for major components
   - Consistent naming convention
   - Cross-repository references documented
   - Meta-repository for documentation and integration

## Access Control Best Practices

1. **Permission Levels**
   - **Admin:** Limited to organization owners and lead architects
   - **Maintain:** For team leads responsible for specific components
   - **Write:** For active developers on specific components
   - **Triage:** For QA and PM roles that need to manage issues
   - **Read:** For roles that need visibility but not write access

2. **Branch Protection Rules**
   - Require pull request reviews before merging
   - Require status checks to pass before merging
   - Require signed commits
   - Restrict who can push to matching branches
   - Include administrators in restrictions
   - Allow specified teams to bypass requirements when necessary

3. **Environment Protection**
   - Configure environment protection rules
   - Require approvals for deployments
   - Specify required reviewers by environment
   - Set wait timer for production deployments

## Commit Attribution and Identity

1. **Commit Signing**
   - Require GPG signing for all commits
   - Document key management procedures
   - Verify signatures in CI/CD pipeline

2. **Commit Attribution**
   - Use consistent email format: `role@nexusframework.org`
   - Include Manus account identifier in commit messages
   - Use commit trailers for additional metadata:
     ```
     Manus-Account: Architect
     Component: Orchestration
     ```

3. **Author vs Committer**
   - Understand distinction between author (who wrote the code) and committer (who committed it)
   - Preserve authorship information when integrating contributions

## Workflow Recommendations

1. **Branch Strategy**
   - Implement GitFlow or trunk-based development
   - Use consistent branch naming conventions:
     - `feature/manus-role/description`
     - `bugfix/manus-role/description`
     - `release/version`
   - Document branch lifecycle and cleanup procedures

2. **Pull Request Process**
   - Use pull request templates with required information
   - Implement required reviews from relevant teams
   - Use labels to indicate Manus account responsibility
   - Configure automatic assignment based on code ownership
   - Document review expectations and SLAs

3. **Issue Management**
   - Use issue templates for different types of work
   - Implement labels for categorization and filtering
   - Use projects for tracking work across repositories
   - Document issue lifecycle and resolution criteria

## Security Considerations

1. **Account Security**
   - Require two-factor authentication for all accounts
   - Regularly audit access permissions
   - Implement SAML SSO for enterprise accounts
   - Use personal access tokens with appropriate scopes
   - Regularly rotate credentials

2. **Secret Management**
   - Never commit secrets to repositories
   - Use GitHub Secrets for CI/CD credentials
   - Implement secret scanning
   - Document procedure for secret rotation

3. **Vulnerability Management**
   - Enable Dependabot alerts and security updates
   - Configure code scanning with CodeQL
   - Implement security policy (SECURITY.md)
   - Document vulnerability response procedure

## Integration with Development Tools

1. **CI/CD Integration**
   - Configure GitHub Actions workflows
   - Use repository secrets for sensitive information
   - Implement matrix builds for cross-platform testing
   - Document CI/CD pipeline architecture

2. **Code Quality Tools**
   - Configure code owners (CODEOWNERS file)
   - Implement automated code review tools
   - Configure linting and formatting checks
   - Document code quality expectations

## Recommended Approach for Nexus Framework v2.6

For Nexus Framework v2.6 development with multiple Manus accounts, the recommended approach is:

1. **Create a single GitHub organization** (`NexusFramework`)
2. **Implement team-based access control** with teams mirroring Manus account roles
3. **Use a monorepo structure** with clear component separation
4. **Implement branch protection** with required reviews from appropriate teams
5. **Require commit signing** and use commit trailers for Manus account attribution
6. **Document all procedures** in a central repository

This approach balances clear attribution, security, and administrative simplicity while supporting the distributed development model with specialized Manus accounts.
