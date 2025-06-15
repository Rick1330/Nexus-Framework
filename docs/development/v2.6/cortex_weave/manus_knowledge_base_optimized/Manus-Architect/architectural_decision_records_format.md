name: Architectural Decision Records (ADR) Format
use_when: When documenting significant architectural decisions, design choices, or reviewing architectural changes.
content: |
  Standard format for Architectural Decision Records (ADRs):
  # ADR-[NUMBER]: [TITLE]
  ## Status: [PROPOSED | ACCEPTED | IMPLEMENTED | DEPRECATED | SUPERSEDED]
  ## Context: Describe the problem or situation necessitating the decision.
  ## Decision: Clearly state the architectural decision made.
  ## Alternatives Considered:
    - **Alternative X**: Description, Pros, Cons, Why Not Chosen.
  ## Consequences:
    - **Positive**: Benefits of the decision.
    - **Negative**: Drawbacks or risks.
    - **Neutral**: Unchanged aspects.
  ## Compliance: How the decision aligns with architectural principles.
  ## Related Decisions: Links to other relevant ADRs.
  ## References: Supporting documentation or resources.
  All ADRs must be documented using this format and stored in a central repository, reviewed and approved by the architecture team.

