name: Vector Database Optimization
use_when: When designing, implementing, or optimizing vector databases for AI applications, embeddings storage, or similarity search.
content: 
When implementing vector databases for Nexus Framework v2.6, follow these optimization practices:

1. **Vector Representation**:
   - Choose appropriate embedding models for specific domains
   - Standardize vector dimensions across similar content types
   - Use dimensionality reduction techniques when appropriate
   - Implement proper normalization for consistent similarity metrics
   - Use quantization for storage efficiency
   - Select appropriate precision based on accuracy requirements
   - Document embedding model versions and parameters

2. **Index Selection**:
   - Choose appropriate index types based on workload:
     - HNSW for high recall and performance balance
     - IVF for larger datasets with moderate recall requirements
     - FLAT for perfect recall with smaller datasets
   - Tune index parameters based on dataset characteristics
   - Implement hybrid indexes for complex query patterns
   - Use product quantization for large-scale deployments
   - Benchmark different index configurations
   - Document index selection rationale

3. **Query Optimization**:
   - Implement vector caching for frequent queries
   - Use approximate nearest neighbor search for large datasets
   - Implement proper beam search parameters
   - Use query vector preprocessing consistent with storage
   - Implement hybrid search (vector + keyword)
   - Use metadata filtering to reduce search space
   - Optimize k values for nearest neighbor searches

4. **Data Organization**:
   - Implement proper collection/table design
   - Use namespaces for logical separation
   - Implement sharding for large-scale deployments
   - Use appropriate partitioning strategies
   - Implement TTL for ephemeral vectors
   - Use metadata for efficient filtering
   - Implement versioning for evolving embeddings

5. **Performance Tuning**:
   - Configure appropriate memory allocation
   - Use SSD storage for index data
   - Implement proper caching strategies
   - Use batch processing for bulk operations
   - Configure thread counts based on hardware
   - Implement connection pooling
   - Monitor and tune query timeouts

6. **Scaling Strategies**:
   - Implement horizontal scaling with proper sharding
   - Use read replicas for query-heavy workloads
   - Implement proper load balancing
   - Use distributed deployment for large datasets
   - Implement proper failover mechanisms
   - Use auto-scaling based on load metrics
   - Document scaling thresholds and procedures

7. **Retrieval Strategies**:
   - Implement semantic chunking for text documents
   - Use hierarchical retrieval for large documents
   - Implement re-ranking for improved relevance
   - Use hybrid retrieval combining multiple strategies
   - Implement context-aware retrieval
   - Use query expansion techniques
   - Implement feedback loops for retrieval quality

8. **Monitoring and Maintenance**:
   - Track query latency and throughput
   - Monitor index performance metrics
   - Implement recall/precision evaluation
   - Use regular index maintenance procedures
   - Monitor storage utilization
   - Implement alerting for performance degradation
   - Document maintenance procedures and schedules

9. **Integration Patterns**:
   - Use standardized APIs for vector operations
   - Implement proper error handling and retries
   - Use connection pooling for efficient resource usage
   - Implement circuit breakers for resilience
   - Use asynchronous operations for non-blocking workflows
   - Implement proper logging and tracing
   - Document integration patterns and examples

10. **Security Considerations**:
    - Implement proper access controls
    - Use encryption for sensitive vector data
    - Implement network security for database access
    - Use secure credential management
    - Implement audit logging for sensitive operations
    - Use proper backup and recovery procedures
    - Document security controls and compliance

Apply these optimization practices consistently across all vector database implementations to ensure performance, scalability, and reliability.
