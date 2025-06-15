name: Asynchronous Processing Patterns - Core
use_when: When implementing backend services that require asynchronous processing, background jobs, or event-driven architectures.
content: |
  Core asynchronous processing patterns:
  1.  **Message Queue Pattern**: Use reliable message brokers (RabbitMQ, Kafka); implement dead letter queues, proper acknowledgments, and message persistence.
  2.  **Event-Driven Architecture**: Model domain events; use event sourcing; implement event schema versioning and idempotent handlers.
  3.  **Background Job Processing**: Use job queues (Celery); implement prioritization, retry policies, monitoring, and idempotence.
  4.  **Distributed Task Scheduling**: Use appropriate frameworks; implement task partitioning, parallelization, and distributed locks.
  5.  **Saga Pattern**: For distributed transactions, use choreography or orchestration; design compensating transactions and handle timeouts.
  6.  **Circuit Breaker Pattern**: Implement for external service calls; configure thresholds, fallbacks, and monitoring.
  7.  **Bulkhead Pattern**: Isolate critical components; implement resource limits and failure isolation.
  8.  **Retry Pattern**: Implement exponential backoff with jitter; set max attempts; design for idempotent operations.
  9.  **Outbox Pattern**: Store outgoing messages transactionally; use a separate relay process; implement deduplication.
  10. **Scheduler Pattern**: Use reliable scheduling systems; implement job prioritization and distributed scheduling.
  Apply these patterns for reliable, scalable, and maintainable asynchronous systems.

