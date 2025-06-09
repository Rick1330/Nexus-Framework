name: API Design Best Practices
use_when: When designing, implementing, or reviewing API endpoints for backend services.
content: 
When designing APIs for Nexus Framework v2.6, adhere to these best practices:

1. **RESTful Resource Modeling**:
   - Model APIs around resources, not actions
   - Use nouns for resource names (e.g., `/agents` not `/getAgents`)
   - Use plural nouns for collection resources
   - Use hierarchical relationships for nested resources (e.g., `/agents/{id}/capabilities`)

2. **HTTP Method Usage**:
   - GET: Retrieve resources (idempotent, safe)
   - POST: Create new resources or trigger processes
   - PUT: Replace resources completely (idempotent)
   - PATCH: Update resources partially (idempotent)
   - DELETE: Remove resources (idempotent)

3. **Status Code Usage**:
   - 200 OK: Successful operation with response body
   - 201 Created: Resource successfully created
   - 204 No Content: Successful operation with no response body
   - 400 Bad Request: Invalid request format or parameters
   - 401 Unauthorized: Authentication required
   - 403 Forbidden: Authentication succeeded but insufficient permissions
   - 404 Not Found: Resource not found
   - 409 Conflict: Request conflicts with current state
   - 422 Unprocessable Entity: Validation errors
   - 429 Too Many Requests: Rate limit exceeded
   - 500 Internal Server Error: Unexpected server error

4. **Request/Response Format**:
   - Use consistent JSON structure across all endpoints
   - Include a root element for resource representations
   - Use camelCase for property names
   - Use ISO 8601 for date/time values (e.g., `2025-06-09T04:53:36Z`)
   - Include pagination metadata for collection responses

5. **Error Handling**:
   - Return structured error responses:
     ```json
     {
       "error": {
         "code": "VALIDATION_ERROR",
         "message": "The request contains invalid parameters",
         "details": [
           {
             "field": "name",
             "message": "Name is required"
           }
         ],
         "correlationId": "550e8400-e29b-41d4-a716-446655440000"
       }
     }
     ```
   - Use consistent error codes across all APIs
   - Provide actionable error messages
   - Include correlation IDs for traceability

6. **Versioning**:
   - Include version in URL path (e.g., `/v1/agents`)
   - Maintain backward compatibility within major versions
   - Document breaking changes clearly
   - Support at least one previous major version

7. **Security**:
   - Require HTTPS for all endpoints
   - Implement proper authentication and authorization
   - Validate all input parameters
   - Implement rate limiting and throttling
   - Set appropriate CORS headers

8. **Performance**:
   - Implement efficient pagination for large collections
   - Support filtering, sorting, and field selection
   - Use compression for response bodies
   - Implement caching with appropriate cache headers
   - Optimize database queries for API operations

9. **Documentation**:
   - Document all endpoints with OpenAPI/Swagger
   - Include example requests and responses
   - Document authentication requirements
   - Specify rate limits and quotas
   - Provide SDK examples in multiple languages

10. **Monitoring**:
    - Log all API requests and responses (excluding sensitive data)
    - Track performance metrics (response time, error rate)
    - Implement health check endpoints
    - Monitor rate limit usage
    - Track API usage by consumer

All APIs must be reviewed against these best practices before implementation and deployment.
