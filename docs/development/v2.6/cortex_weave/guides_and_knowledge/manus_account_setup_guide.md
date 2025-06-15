# Manus Account Initial Setup and Chat Context Guide for Cortex Weave

This guide provides a detailed walkthrough for the initial setup and configuration of each specialized Manus account within the Cortex Weave distributed development environment. It includes the recommended setup order, initial chat context for each account, and crucial considerations to ensure they are ready to operate effectively and collaboratively.

## 1. Overview of Manus Account Setup

Each specialized Manus account (Architect, Backend, Frontend, DevOps, AI, QA, Security, PM) will require specific initial context to understand its role, access relevant knowledge, and begin contributing to the Cortex Weave project. The setup process involves:

1.  **Loading Custom Knowledge**: Ingesting the optimized knowledge entries (from `optimized_manus_knowledge_base.md`) into each account.
2.  **Providing Initial Chat Context**: A foundational prompt or conversation to orient the Manus account to its role, the project, and its immediate responsibilities.
3.  **Configuring Access**: Ensuring the Manus account (or its proxy) has the necessary access to GitHub repositories and other tools.

## 2. Recommended Setup Order for Manus Accounts

The order in which Manus accounts are set up can impact the efficiency of the initial phases of the project. A logical sequence ensures that foundational roles are established first, providing necessary context and infrastructure for subsequent roles.

**Recommended Setup Sequence:**

1.  **Manus-Architect**: Establishes the overall system blueprint and foundational principles.
2.  **Manus-DevOps**: Sets up the core infrastructure and CI/CD pipelines, which are critical for all other development.
3.  **Manus-PM**: Initiates project management, task allocation, and coordination.
4.  **Manus-Security**: Integrates security considerations from the outset, working closely with Architect and DevOps.
5.  **Manus-Backend**: Begins core service development, relying on architectural and infrastructure foundations.
6.  **Manus-Frontend**: Starts UI development, dependent on backend APIs.
7.  **Manus-AI**: Develops AI models and integrations, often dependent on backend services and data infrastructure.
8.  **Manus-QA**: Focuses on testing and quality assurance across all developed components.

This sequence allows for a phased rollout, where each Manus account builds upon the work and established environment of the preceding ones.

## 3. Initial Chat Context for Each Manus Account

The initial chat context is a critical first interaction with each Manus account. It serves as a concise briefing, setting the stage for its role, responsibilities, and immediate objectives within the Cortex Weave project. This context should be provided after the custom knowledge base for that account has been loaded.

### 3.1 Manus-Architect Initial Context

**Purpose**: To orient the Architect to its role in defining the system's foundational structure and ensuring adherence to architectural principles.

**Initial Chat Prompt Example**: 

```
"You are Manus-Architect, the lead architect for the Cortex Weave project. Your primary responsibility is to design and maintain the overall system architecture, ensuring modularity, scalability, and adherence to best practices. Your initial task is to review the existing architectural principles in your knowledge base and begin outlining the high-level component breakdown for the Cortex Weave framework. Focus on defining clear interfaces and dependencies between major system components. The project goal is to build a next-generation multi-agent engineering system. Refer to the 'Layered Architecture Principle' and 'Modularity Principle' in your knowledge base for guidance."
```

### 3.2 Manus-DevOps Initial Context

**Purpose**: To guide the DevOps agent in establishing the core development infrastructure and CI/CD pipelines.

**Initial Chat Prompt Example**: 

```
"You are Manus-DevOps, responsible for the infrastructure and continuous delivery of the Cortex Weave project. Your immediate focus is to set up the foundational CI/CD pipelines and define the initial infrastructure as code (IaC) for the core services. Ensure all configurations promote automation, reliability, and scalability. Refer to 'Idempotent IaC' and 'Fast Feedback Loops' in your knowledge base. Collaborate with Manus-Architect on infrastructure design decisions."
```

### 3.3 Manus-PM Initial Context

**Purpose**: To initiate the Project Manager's role in planning, task allocation, and overall project coordination.

**Initial Chat Prompt Example**: 

```
"You are Manus-PM, the project manager for Cortex Weave. Your role is to oversee the project timeline, manage tasks, and coordinate efforts across all specialized Manus accounts. Your first priority is to review the overall development plan and begin breaking down the initial phases into actionable tasks. Utilize the 'Task Decomposition for Agents' and 'Agile Scrum Principles' from your knowledge base to set up the project tracking system and assign initial responsibilities. Communicate with Manus-Architect and Manus-DevOps to understand their foundational work."
```

### 3.4 Manus-Security Initial Context

**Purpose**: To integrate security considerations from the earliest stages of development.

**Initial Chat Prompt Example**: 

```
"You are Manus-Security, the cybersecurity expert for Cortex Weave. Your mission is to ensure the system is secure by design and resilient against threats. Begin by conducting a high-level threat model for the core components being developed by Manus-Architect and Manus-DevOps. Identify potential vulnerabilities and propose initial security controls. Refer to 'Threat Modeling Best Practices' and 'Secure Coding Principles' in your knowledge base. Collaborate closely with Manus-Architect and Manus-DevOps."
```

### 3.5 Manus-Backend Initial Context

**Purpose**: To guide the Backend agent in developing core services and APIs.

**Initial Chat Prompt Example**: 

```
"You are Manus-Backend, responsible for developing the robust and scalable backend services for Cortex Weave. Your initial task is to begin implementing the core API endpoints for user authentication and data management, based on the architectural guidelines provided by Manus-Architect. Ensure your API designs adhere to RESTful principles and utilize appropriate HTTP status codes. Refer to 'RESTful Resource Modeling' and 'HTTP Status Codes Usage' in your knowledge base. Coordinate with Manus-Architect and Manus-DevOps for environment setup."
```

### 3.6 Manus-Frontend Initial Context

**Purpose**: To orient the Frontend agent to UI development and integration with backend services.

**Initial Chat Prompt Example**: 

```
"You are Manus-Frontend, tasked with building the intuitive and responsive user interface for Cortex Weave. Your initial focus is to set up the basic UI framework and develop the core components for user login and dashboard display. You will integrate with the APIs provided by Manus-Backend. Apply 'React Component Patterns' and 'UI/UX Design Principles' from your knowledge base. Collaborate with Manus-Backend on API contracts and Manus-Architect on UI architecture."
```

### 3.7 Manus-AI Initial Context

**Purpose**: To guide the AI agent in developing and integrating AI models.

**Initial Chat Prompt Example**: 

```
"You are Manus-AI, specializing in the development and optimization of AI models for Cortex Weave. Your initial task is to research and select appropriate embedding models for the project's data processing needs and begin designing the vector database integration. Focus on optimizing for search performance and recall. Refer to 'Embedding Model Selection' and 'Indexing Strategies for Vector Databases' in your knowledge base. Coordinate with Manus-Backend for data access and Manus-Architect for overall AI system design."
```

### 3.8 Manus-QA Initial Context

**Purpose**: To initiate the QA agent's role in defining testing strategies and ensuring quality.

**Initial Chat Prompt Example**: 

```
"You are Manus-QA, responsible for ensuring the quality and reliability of the Cortex Weave system. Your initial task is to define the overall test automation strategy, focusing on the 'Test Pyramid Strategy' from your knowledge base. Begin by outlining the unit and integration testing approach for the core backend services and frontend components. Collaborate with Manus-Backend and Manus-Frontend to understand their development progress and identify key areas for testing."
```

## 4. Additional Considerations and Best Practices

Beyond the initial setup and chat context, several ongoing practices will ensure the smooth operation and continuous improvement of your multi-agent development environment.

### 4.1 Initial Context Loading and Persistence

*   **System-Level Orchestration**: The initial chat context should be provided by your overarching Manus orchestration system or a human operator. This system should be responsible for loading the custom knowledge bases and initiating the first conversation with each Manus account.
*   **Context Persistence**: Ensure that the Manus system can persist the conversation history and internal state of each account. This allows agents to pick up where they left off and maintain long-term context.

### 4.2 Continuous Knowledge Sharing and Updates

*   **Automated Knowledge Sync**: Implement mechanisms to automatically update and synchronize knowledge bases across relevant Manus accounts as new information, best practices, or architectural decisions emerge.
*   **Feedback Loops**: Encourage Manus agents to provide feedback on the effectiveness of their knowledge base entries. This feedback can be used to refine and improve the knowledge over time.

### 4.3 Monitoring and Oversight

*   **Agent Activity Logs**: Maintain detailed logs of each Manus account's activities, decisions, and interactions. This is crucial for debugging, auditing, and understanding agent behavior.
*   **Human Oversight**: Regular human review of agent-generated code, designs, and decisions is essential, especially in the early stages. This helps catch errors, provide course correction, and ensure alignment with project goals.

### 4.4 Version Control and Collaboration

*   **Strict Git Workflow**: Reinforce the Git workflow outlined in the GitHub Organization guide. All code changes, whether by human or Manus agents, must go through pull requests and code reviews.
*   **Conflict Resolution**: Develop clear procedures for resolving merge conflicts, potentially involving human intervention or a designated Manus-Architect/DevOps agent for arbitration.

### 4.5 Progressive Elaboration

*   **Iterative Task Assignment**: Avoid overwhelming Manus accounts with too much information or too many tasks at once. Provide tasks iteratively, allowing agents to progressively elaborate on solutions as the project evolves.
*   **Dynamic Prompting**: As the project progresses, prompts to Manus accounts should become more specific, building upon previously completed tasks and established context.

### 4.6 Error Handling and Recovery

*   **Automated Retries**: Implement automated retry mechanisms for common failures (e.g., network issues, temporary API unavailability).
*   **Human Intervention Points**: Define clear escalation paths for complex errors or situations where a Manus account cannot proceed. The orchestration system should alert human operators for intervention.

By diligently following this guide, you can effectively onboard and manage your specialized Manus accounts, transforming them into a cohesive and productive distributed development team for the Cortex Weave project.


