name: Cloud Architecture Patterns
use_when: When designing and implementing cloud-native applications, selecting cloud services, or optimizing cloud infrastructure.
content: |
  Key cloud architecture patterns:
  1.  **Serverless Architecture**: Utilize FaaS (Functions as a Service) like AWS Lambda or Google Cloud Functions for event-driven, scalable, and cost-effective microservices. Focus on stateless functions and managed services.
  2.  **Microservices Architecture**: Decompose applications into small, independent, loosely coupled services. Each service can be developed, deployed, and scaled independently. Emphasize clear APIs and inter-service communication patterns (e.g., message queues, gRPC).
  3.  **Event-Driven Architecture**: Design systems around events, where services communicate by producing and consuming events. Use message brokers (Kafka, RabbitMQ) or event buses (AWS EventBridge) for asynchronous communication and loose coupling.
  4.  **Containerization**: Package applications and their dependencies into portable containers (Docker). Orchestrate containers using platforms like Kubernetes for automated deployment, scaling, and management.
  5.  **API-First Design**: Treat APIs as first-class products. Design clear, consistent, and well-documented APIs (REST, GraphQL) that serve as the primary interface for all interactions.
  6.  **Infrastructure as Code (IaC)**: Manage and provision infrastructure using code (Terraform, CloudFormation). Ensure version control, automation, and reproducibility of infrastructure deployments.
  7.  **Managed Services Preference**: Prioritize the use of managed cloud services (e.g., managed databases, message queues, identity services) to reduce operational overhead and increase reliability.
  8.  **Resilience Patterns**: Implement patterns like Circuit Breaker, Bulkhead, Retry, and Fallback to ensure application resilience against failures and graceful degradation.
  9.  **Observability**: Design systems for comprehensive monitoring, logging, and tracing. Use tools like Prometheus, Grafana, Jaeger, and centralized logging solutions to gain insights into system behavior.
  10. **Cost Optimization**: Implement strategies for cost efficiency, including right-sizing resources, utilizing spot instances, implementing auto-scaling, and monitoring cloud spend.
  Apply these patterns to build robust, scalable, and cost-effective cloud-native solutions.

