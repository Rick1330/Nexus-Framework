name: Asynchronous Processing Patterns
use_when: When implementing backend services that require asynchronous processing, background jobs, or event-driven architectures.
content: 
When implementing asynchronous processing in Nexus Framework v2.6, apply these patterns:

1. **Message Queue Pattern**:
   - Use RabbitMQ or Kafka for reliable message delivery
   - Implement proper queue naming conventions
   - Use appropriate exchange types for message routing
   - Implement dead letter queues for failed messages
   - Configure appropriate message persistence
   - Implement proper acknowledgment mechanisms
   - Use message TTL for expiration handling

2. **Event-Driven Architecture Pattern**:
   - Model domain events as first-class citizens
   - Use event sourcing for critical state changes
   - Implement event schema versioning
   - Use consistent event naming conventions
   - Include metadata with all events (timestamp, source, correlation ID)
   - Implement idempotent event handlers
   - Design for out-of-order event processing

3. **Background Job Processing**:
   - Use Celery for Python-based job processing
   - Implement job prioritization
   - Use appropriate retry policies with exponential backoff
   - Implement job monitoring and alerting
   - Use job batching for efficiency
   - Implement proper error handling and logging
   - Design for job idempotence

4. **Distributed Task Scheduling**:
   - Use appropriate task scheduling framework
   - Implement proper task partitioning
   - Design for task parallelization
   - Use distributed locks for mutual exclusion
   - Implement proper task result storage
   - Design for task cancellation
   - Implement task progress tracking

5. **Saga Pattern for Distributed Transactions**:
   - Implement choreography or orchestration based on complexity
   - Design compensating transactions for rollback
   - Use unique transaction IDs for correlation
   - Implement timeout handling
   - Design for partial failure recovery
   - Implement transaction monitoring
   - Use event sourcing to track transaction state

6. **Circuit Breaker Pattern**:
   - Implement circuit breakers for external service calls
   - Configure appropriate thresholds and timeouts
   - Implement fallback mechanisms
   - Design for graceful degradation
   - Implement circuit state monitoring
   - Use half-open state for recovery testing
   - Configure appropriate reset timeouts

7. **Bulkhead Pattern**:
   - Isolate critical system components
   - Implement resource limits per component
   - Use separate thread pools or process spaces
   - Configure appropriate timeouts
   - Implement resource usage monitoring
   - Design for failure isolation
   - Use adaptive resource allocation

8. **Retry Pattern**:
   - Implement exponential backoff with jitter
   - Set maximum retry attempts
   - Use retry-specific error handling
   - Implement retry monitoring and alerting
   - Design for idempotent operations
   - Use circuit breakers with retries
   - Implement retry storages for persistence

9. **Outbox Pattern**:
   - Store outgoing messages in a transactional outbox
   - Use a separate process to relay messages
   - Implement message deduplication
   - Design for exactly-once delivery semantics
   - Use message status tracking
   - Implement proper error handling
   - Design for recovery after system failure

10. **Scheduler Pattern**:
    - Use a reliable scheduling system
    - Implement proper job prioritization
    - Design for distributed scheduling
    - Use appropriate time zone handling
    - Implement schedule versioning
    - Design for schedule changes
    - Implement monitoring and alerting

Apply these patterns consistently across all asynchronous processing implementations to ensure reliability, scalability, and maintainability.
