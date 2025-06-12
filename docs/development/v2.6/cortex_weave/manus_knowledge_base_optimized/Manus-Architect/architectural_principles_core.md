name: Architectural Principles - Core
use_when: When making architectural decisions, reviewing component designs, or evaluating implementation approaches for Nexus Framework v2.6.
content: |
  Core architectural principles for Nexus Framework v2.6:
  1.  **Layered Architecture**: Distinct layers (Interface, Orchestration, Agent, Cognitive, Integration) with clear responsibilities.
  2.  **Modularity**: Self-contained components with well-defined interfaces for independent development.
  3.  **Separation of Concerns**: Single, well-defined responsibility for each component.
  4.  **Explicit Interfaces**: All component interactions via explicit interfaces for loose coupling.
  5.  **Dependency Inversion**: High-level modules depend on abstractions, not low-level modules.
  6.  **Composition Over Inheritance**: Extend functionality through composition.
  7.  **Defense in Depth**: Multi-layered security with overlapping controls.
  8.  **Fail Secure**: Components fail in a secure state, preserving data.
  9.  **Observability by Design**: Comprehensive logging, metrics, and tracing.
  10. **Graceful Degradation**: Maintain core functionality during component failures.
  11. **Horizontal Scalability**: Stateless design and distributed processing for horizontal scaling.
  12. **Eventual Consistency**: Prioritize availability and partition tolerance, accepting eventual consistency.
  Apply these principles consistently for system coherence, quality, and maintainability.

