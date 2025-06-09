name: Agent Reasoning System Design
use_when: When designing, implementing, or optimizing reasoning systems for AI agents, cognitive architectures, or decision-making components.
content: 
When implementing agent reasoning systems for Nexus Framework v2.6, follow these design principles:

1. **Reasoning Architecture**:
   - Implement a layered reasoning approach with reactive, deliberative, and reflective layers
   - Use a modular design with specialized reasoning components
   - Implement proper separation between knowledge representation and reasoning processes
   - Design for transparent reasoning with explainable steps
   - Use hybrid reasoning combining multiple approaches
   - Implement meta-reasoning for self-monitoring and adaptation
   - Design for graceful degradation under uncertainty

2. **Knowledge Representation**:
   - Use appropriate representation formats for different knowledge types:
     - Semantic networks for conceptual relationships
     - Frames or schemas for structured knowledge
     - Rules for procedural knowledge
     - Probabilistic models for uncertain knowledge
   - Implement proper ontology design for domain knowledge
   - Use consistent naming conventions and relationships
   - Design for knowledge evolution and versioning
   - Implement efficient knowledge retrieval mechanisms
   - Use hybrid representations for complex domains

3. **Reasoning Strategies**:
   - Implement multiple reasoning methods appropriate to different tasks:
     - Deductive reasoning for logical inference
     - Inductive reasoning for pattern recognition
     - Abductive reasoning for explanation generation
     - Analogical reasoning for novel problem solving
   - Use chain-of-thought reasoning for complex problems
   - Implement tree-of-thought for decision exploration
   - Use case-based reasoning for experience-based decisions
   - Implement constraint satisfaction for structured problems
   - Design for reasoning under uncertainty with probabilistic methods

4. **Decision Making**:
   - Implement utility-based decision making with clear evaluation criteria
   - Use multi-criteria decision analysis for complex choices
   - Implement proper handling of uncertainty in decisions
   - Design for explainable decision processes
   - Use decision trees for structured decision spaces
   - Implement Monte Carlo methods for stochastic scenarios
   - Design for ethical decision making with explicit principles

5. **Planning and Problem Solving**:
   - Implement hierarchical task network planning
   - Use goal decomposition for complex objectives
   - Implement means-end analysis for problem solving
   - Design for replanning when conditions change
   - Use partial-order planning for flexible execution
   - Implement contingency planning for uncertain environments
   - Design for collaborative planning with other agents

6. **Learning Integration**:
   - Implement experience-based learning to improve reasoning
   - Use reinforcement learning for adaptive behavior
   - Design for transfer learning across similar domains
   - Implement meta-learning for strategy adaptation
   - Use active learning for knowledge acquisition
   - Design for continuous learning during operation
   - Implement proper validation of learned knowledge

7. **Context Management**:
   - Design for proper context representation and tracking
   - Implement context-sensitive reasoning
   - Use working memory management for active context
   - Design for context switching with proper state preservation
   - Implement attention mechanisms for focus control
   - Use context hierarchies for nested reasoning scenarios
   - Design for multi-context reasoning with proper isolation

8. **Reasoning Optimization**:
   - Implement anytime algorithms for time-constrained reasoning
   - Use progressive refinement for incremental improvement
   - Design for resource-aware reasoning with bounded computation
   - Implement caching for repeated reasoning patterns
   - Use parallel reasoning for independent sub-problems
   - Design for reasoning reuse across similar problems
   - Implement proper termination conditions for reasoning processes

9. **Evaluation and Verification**:
   - Design for reasoning transparency and explainability
   - Implement self-verification of reasoning steps
   - Use formal verification for critical reasoning components
   - Design for reasoning consistency checking
   - Implement performance metrics for reasoning quality
   - Use benchmark problems for comparative evaluation
   - Design for human-in-the-loop verification when appropriate

10. **Integration with Other Systems**:
    - Design clean interfaces between reasoning and perception
    - Implement proper integration with knowledge bases
    - Use standardized formats for reasoning inputs and outputs
    - Design for reasoning about external system capabilities
    - Implement proper error handling for reasoning failures
    - Use logging for reasoning process transparency
    - Design for distributed reasoning across agent systems

Apply these design principles consistently across all agent reasoning systems to ensure effective, explainable, and reliable cognitive capabilities.
