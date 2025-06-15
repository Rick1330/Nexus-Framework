name: Component Interface Design Patterns - Core
use_when: When designing interfaces between components, defining API contracts, or reviewing interface implementations.
content: |
  Core design patterns for component interfaces:
  1.  **Contract-First Design**: Define interface contract (endpoints, data formats, error handling) before implementation.
  2.  **Interface Segregation**: Create focused interfaces; components depend only on methods they use.
  3.  **Uniform Interface**: Use consistent patterns (naming, error handling, response formats) across all interfaces.
  4.  **Versioning Strategy**: Include explicit semantic versioning (MAJOR.MINOR.PATCH); maintain backward compatibility.
  5.  **Error Handling Pattern**: Standardized error responses with code, message, details, and correlation ID.
  6.  **Pagination Pattern**: Consistent pagination for collection resources (page size, number, total count, links).
  7.  **Filtering Pattern**: Provide consistent query parameters for filtering collections.
  8.  **Asynchronous Pattern**: For long-running operations, implement immediate acknowledgment, status endpoints, and callbacks.
  9.  **Bulk Operation Pattern**: Support efficient batch processing with atomic/non-atomic modes and partial success handling.
  10. **Caching Pattern**: Include cache control mechanisms (ETag, Last-modified, Cache-Control headers).
  11. **Documentation Pattern**: Document interfaces with OpenAPI/Swagger, examples, rate limiting, and authentication.
  12. **Health Check Pattern**: Standardized health check endpoints with overall status, component-specific indicators, and dependency status.
  Apply these patterns consistently for coherence, maintainability, and ease of integration.

