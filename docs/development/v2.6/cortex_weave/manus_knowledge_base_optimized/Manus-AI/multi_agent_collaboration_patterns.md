name: Multi-Agent Collaboration Patterns
use_when: When designing and implementing systems involving multiple AI agents that need to coordinate, communicate, and collaborate to achieve shared goals.
content: |
  Effective multi-agent collaboration patterns include:
  1.  **Centralized Orchestration**: A single orchestrator agent manages task distribution, communication, and conflict resolution among other agents. Suitable for well-defined tasks with clear dependencies.
  2.  **Decentralized Coordination**: Agents coordinate directly with each other using agreed-upon protocols, without a central authority. Promotes resilience and scalability but requires robust communication mechanisms.
  3.  **Blackboard Systems**: Agents communicate indirectly by writing and reading information from a shared data structure (blackboard). Useful for complex problems where agents contribute partial solutions.
  4.  **Contract Net Protocol**: A negotiation-based protocol where a 'manager' agent announces a task, and 'bidder' agents propose solutions. The manager selects the best bid. Ideal for dynamic task allocation.
  5.  **Hierarchical Collaboration**: Agents are organized in a hierarchy, with higher-level agents setting goals and lower-level agents executing sub-tasks. Combines centralized control with distributed execution.
  6.  **Swarm Intelligence**: Agents exhibit simple behaviors that, when combined, lead to complex, emergent collective intelligence. Applicable for optimization problems or distributed sensing.
  7.  **Shared Mental Models**: Agents develop a common understanding of the task, environment, and each other's capabilities, reducing miscommunication and improving coordination.
  8.  **Intelligent Handoffs**: Seamless transfer of tasks or information between agents, ensuring continuity and efficiency in workflows.
  9.  **Asynchronous Communication**: Agents communicate without requiring immediate responses, allowing for parallel processing and improved throughput, especially in distributed environments.
  10. **Conflict Resolution Mechanisms**: Strategies and protocols for identifying and resolving disagreements or conflicting actions among agents, maintaining system coherence.
  Apply these patterns to build robust, efficient, and scalable multi-agent systems.

