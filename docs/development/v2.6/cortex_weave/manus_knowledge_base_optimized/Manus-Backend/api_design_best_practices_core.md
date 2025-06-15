name: API Design Best Practices - Core
use_when: When designing, implementing, or reviewing API endpoints for backend services.
content: |
  Core API design best practices:
  1.  **RESTful Resource Modeling**: Model APIs around resources (nouns, plural for collections); use hierarchical relationships.
  2.  **HTTP Method Usage**: Use GET (retrieve), POST (create/trigger), PUT (replace), PATCH (partial update), DELETE (remove) appropriately.
  3.  **Status Code Usage**: Employ standard HTTP status codes (2xx for success, 4xx for client errors, 5xx for server errors).
  4.  **Request/Response Format**: Use consistent JSON structure (camelCase for properties, ISO 8601 for dates); include pagination metadata.
  5.  **Error Handling**: Return structured error responses with code, message, details, and correlation ID.
  6.  **Versioning**: Include version in URL path (e.g., `/v1/`); maintain backward compatibility within major versions.
  7.  **Security**: Require HTTPS; implement authentication, authorization, input validation, rate limiting, and CORS.
  8.  **Performance**: Implement efficient pagination, filtering, sorting; use compression and caching; optimize database queries.
  9.  **Documentation**: Document all endpoints with OpenAPI/Swagger; include examples, authentication, and rate limits.
  10. **Monitoring**: Log API requests/responses; track performance metrics, health, and rate limit usage.
  Adhere to these practices for robust, scalable, and maintainable APIs.

