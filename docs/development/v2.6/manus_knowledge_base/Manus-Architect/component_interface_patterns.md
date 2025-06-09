name: Component Interface Design Patterns
use_when: When designing interfaces between components, defining API contracts, or reviewing interface implementations.
content: 
When designing component interfaces for Nexus Framework v2.6, apply these design patterns:

1. **Contract-First Design**: Define the interface contract before implementation, including endpoints, data formats, error handling, and performance requirements.

2. **Interface Segregation**: Create focused interfaces with minimal methods rather than large, monolithic interfaces. Components should only depend on methods they actually use.

3. **Uniform Interface**: Use consistent patterns across all interfaces, including naming conventions, error handling, and response formats.

4. **Versioning Strategy**: Include explicit versioning in all interfaces. Use semantic versioning (MAJOR.MINOR.PATCH) and maintain backward compatibility within major versions.

5. **Error Handling Pattern**: Use standardized error responses with:
   - Error code (machine-readable)
   - Error message (human-readable)
   - Error details (contextual information)
   - Correlation ID (for tracing)

6. **Pagination Pattern**: For collection resources, implement consistent pagination with:
   - Page size and number parameters
   - Total count information
   - Links to next/previous pages
   - Consistent ordering parameters

7. **Filtering Pattern**: Provide consistent query parameters for filtering collections, with support for multiple filter criteria and logical operators.

8. **Asynchronous Pattern**: For long-running operations, implement:
   - Immediate acknowledgment with operation ID
   - Status endpoint for polling
   - Webhook callbacks for completion notification
   - Timeout and cancellation mechanisms

9. **Bulk Operation Pattern**: Support efficient batch processing with:
   - Atomic or non-atomic operation mode
   - Partial success handling
   - Detailed results for each item in the batch

10. **Caching Pattern**: Include cache control mechanisms:
    - ETag support
    - Last-modified timestamps
    - Cache-Control headers
    - Conditional requests

11. **Documentation Pattern**: Document interfaces with:
    - OpenAPI/Swagger specifications
    - Example requests and responses
    - Rate limiting information
    - Authentication requirements

12. **Health Check Pattern**: Provide standardized health check endpoints with:
    - Overall status
    - Component-specific health indicators
    - Dependency status information
    - Performance metrics

Apply these patterns consistently across all component interfaces to ensure coherence, maintainability, and ease of integration.
