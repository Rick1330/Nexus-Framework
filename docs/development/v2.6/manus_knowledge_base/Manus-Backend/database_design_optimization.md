name: Database Design and Optimization
use_when: When designing database schemas, implementing data access layers, or optimizing database performance.
content: 
When designing and optimizing databases for Nexus Framework v2.6, follow these guidelines:

1. **Schema Design Principles**:
   - Normalize data to eliminate redundancy (aim for 3NF)
   - Use denormalization strategically for read-heavy operations
   - Design for query patterns, not just data storage
   - Use appropriate data types for columns
   - Implement proper constraints (primary keys, foreign keys, unique)
   - Use indexes strategically for query optimization

2. **Database Access Patterns**:
   - Implement repository pattern for data access abstraction
   - Use connection pooling for efficient resource utilization
   - Implement proper transaction management
   - Use prepared statements to prevent SQL injection
   - Implement retry logic for transient failures
   - Use appropriate isolation levels for transactions

3. **Query Optimization Techniques**:
   - Write efficient SQL queries (avoid SELECT *)
   - Use EXPLAIN/ANALYZE to understand query execution plans
   - Create indexes based on query patterns
   - Use covering indexes for frequently accessed columns
   - Optimize JOIN operations (use proper join types)
   - Implement pagination for large result sets
   - Use appropriate WHERE clauses to limit result sets

4. **Performance Optimization**:
   - Implement caching for frequently accessed data
   - Use database-specific optimization features
   - Optimize database configuration for workload
   - Monitor and tune slow queries
   - Implement database partitioning for large tables
   - Use read replicas for read-heavy workloads
   - Implement connection pooling and statement caching

5. **Data Migration Strategies**:
   - Use versioned migrations for schema changes
   - Implement zero-downtime migration patterns
   - Test migrations thoroughly before production
   - Include rollback plans for all migrations
   - Document all schema changes and their impact
   - Coordinate migrations with application deployments

6. **Specific PostgreSQL Optimizations**:
   - Use appropriate index types (B-tree, GiST, GIN)
   - Implement VACUUM and ANALYZE regularly
   - Use partial indexes for filtered queries
   - Implement proper table partitioning
   - Use appropriate PostgreSQL extensions
   - Configure connection pooling (pgBouncer)
   - Optimize PostgreSQL configuration parameters

7. **MongoDB Best Practices**:
   - Design schema for document model (not relational)
   - Use embedded documents for related data
   - Implement proper indexing strategy
   - Use aggregation pipeline for complex queries
   - Implement sharding for horizontal scaling
   - Use appropriate write concern and read preference
   - Optimize document structure for query patterns

8. **Vector Database (Milvus) Optimization**:
   - Choose appropriate index type for vector similarity
   - Optimize vector dimension and precision
   - Implement proper partitioning strategy
   - Balance recall and performance in similarity search
   - Use scalar filtering to reduce search space
   - Implement proper connection pooling
   - Monitor and tune query performance

9. **Data Access Security**:
   - Implement row-level security where appropriate
   - Use database roles with least privilege
   - Encrypt sensitive data at rest
   - Audit database access and changes
   - Implement proper authentication and authorization
   - Use connection string security best practices

10. **Monitoring and Maintenance**:
    - Monitor database performance metrics
    - Implement automated backups and verify restores
    - Schedule regular maintenance operations
    - Monitor disk space and growth trends
    - Implement alerting for database issues
    - Document database architecture and operations

Apply these guidelines consistently across all database implementations to ensure performance, reliability, and maintainability.
