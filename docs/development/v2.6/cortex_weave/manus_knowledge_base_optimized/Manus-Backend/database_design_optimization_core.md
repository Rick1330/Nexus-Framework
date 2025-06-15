name: Database Design & Optimization - Core
use_when: When designing database schemas, implementing data access layers, or optimizing database performance.
content: |
  Core guidelines for database design and optimization:
  1.  **Schema Design Principles**: Normalize data (3NF), denormalize strategically, use appropriate data types, and implement constraints and indexes.
  2.  **Database Access Patterns**: Implement repository pattern, use connection pooling, manage transactions, use prepared statements, and retry logic.
  3.  **Query Optimization Techniques**: Write efficient SQL, use EXPLAIN/ANALYZE, create indexes based on query patterns, and optimize JOINs.
  4.  **Performance Optimization**: Implement caching, use database-specific features, tune configuration, monitor slow queries, and partition tables.
  5.  **Data Migration Strategies**: Use versioned migrations, implement zero-downtime patterns, test thoroughly, and include rollback plans.
  6.  **Specific PostgreSQL Optimizations**: Use appropriate index types, VACUUM/ANALYZE, partial indexes, table partitioning, and configure parameters.
  7.  **MongoDB Best Practices**: Design schema for document model, use embedded documents, implement indexing, and sharding.
  8.  **Vector Database (Milvus) Optimization**: Choose appropriate index type, optimize vector dimension, partition, and balance recall/performance.
  9.  **Data Access Security**: Implement row-level security, use least privilege, encrypt data at rest, and audit access.
  10. **Monitoring & Maintenance**: Monitor performance, automate backups, schedule maintenance, and implement alerting.
  Apply these guidelines for performance, reliability, and maintainability.

