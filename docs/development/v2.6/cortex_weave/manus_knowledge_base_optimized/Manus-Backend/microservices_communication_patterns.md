name: Microservices Communication Patterns
use_when: When designing communication mechanisms between microservices, ensuring reliability, scalability, and maintainability.
content: |
  Key communication patterns for microservices:
  1.  **Synchronous Communication (REST/gRPC)**: Direct request-response communication. Suitable for real-time interactions where immediate responses are needed. Use REST for simplicity and gRPC for high-performance, language-agnostic communication.
  2.  **Asynchronous Communication (Message Queues/Event Streams)**: Services communicate via messages or events through a broker (e.g., Kafka, RabbitMQ). Decouples services, improves resilience, and enables event-driven architectures. Ideal for long-running processes or when immediate response is not critical.
  3.  **API Gateway**: A single entry point for all client requests. Handles request routing, composition, authentication, and rate limiting. Reduces complexity for clients and centralizes cross-cutting concerns.
  4.  **Service Mesh (e.g., Istio, Linkerd)**: A dedicated infrastructure layer for handling service-to-service communication. Provides features like traffic management, load balancing, service discovery, security, and observability without modifying service code.
  5.  **Choreography vs. Orchestration**: 
      - **Choreography**: Services communicate directly through events, leading to a decentralized workflow. Suitable for simpler workflows with fewer dependencies.
      - **Orchestration**: A central orchestrator service manages and coordinates the workflow by sending commands to participant services. Better for complex, multi-step workflows.
  6.  **Idempotent Operations**: Design service operations to produce the same result if called multiple times. Crucial for asynchronous communication and retries to prevent data inconsistencies.
  7.  **Circuit Breaker**: Prevents a service from repeatedly trying to invoke a failing remote service. It opens the circuit, preventing further calls, and closes it after a timeout, allowing calls to resume.
  8.  **Retry Mechanism**: Automatically re-attempts failed operations. Implement with exponential backoff and jitter to avoid overwhelming the failing service.
  9.  **Distributed Tracing**: Tools (e.g., Jaeger, Zipkin) to trace requests as they flow through multiple microservices. Essential for debugging and performance monitoring in distributed systems.
  10. **Consumer-Driven Contracts (CDC)**: A testing practice where each consumer of an API defines its expectations of the API in a contract. Ensures compatibility between services and prevents breaking changes.
  Apply these patterns to build robust, scalable, and maintainable microservices architectures.

