name: Container Orchestration Best Practices
use_when: When designing, implementing, or managing containerized applications and Kubernetes deployments.
content: 
When implementing container orchestration for Nexus Framework v2.6, follow these best practices:

1. **Container Design**:
   - Use minimal base images (e.g., Alpine, distroless)
   - Implement single concern per container
   - Use multi-stage builds to minimize image size
   - Never run containers as root
   - Implement proper health checks
   - Use environment variables for configuration
   - Implement proper signal handling for graceful shutdown

2. **Kubernetes Resource Management**:
   - Define resource requests and limits for all containers
   - Implement horizontal pod autoscaling
   - Use node affinity and anti-affinity for optimal scheduling
   - Implement pod disruption budgets for availability
   - Use namespace isolation for multi-tenant environments
   - Implement resource quotas for namespaces
   - Use limit ranges for default resource constraints

3. **Configuration Management**:
   - Use ConfigMaps for non-sensitive configuration
   - Implement Secrets for sensitive data
   - Use Helm for templated deployments
   - Implement proper secret rotation
   - Use environment-specific values files
   - Implement config validation
   - Use immutable ConfigMaps where appropriate

4. **Networking**:
   - Implement service mesh (Istio) for advanced networking
   - Use network policies for traffic control
   - Implement proper ingress configuration
   - Use service types appropriately (ClusterIP, NodePort, LoadBalancer)
   - Implement TLS termination
   - Use DNS for service discovery
   - Implement proper network segmentation

5. **Security**:
   - Implement pod security policies
   - Use network policies to restrict traffic
   - Implement RBAC for access control
   - Scan container images for vulnerabilities
   - Use admission controllers for policy enforcement
   - Implement runtime security monitoring
   - Use service accounts with minimal permissions

6. **Stateful Applications**:
   - Use StatefulSets for ordered deployment
   - Implement persistent volume claims with appropriate storage classes
   - Use volume snapshots for backups
   - Implement proper backup and restore procedures
   - Use init containers for data initialization
   - Implement proper scaling for stateful applications
   - Use headless services for direct pod addressing

7. **Monitoring and Observability**:
   - Implement Prometheus for metrics collection
   - Use Grafana for visualization
   - Implement distributed tracing with Jaeger
   - Use structured logging with Loki
   - Implement alerting with AlertManager
   - Use service level objectives (SLOs)
   - Implement custom metrics for business KPIs

8. **High Availability**:
   - Deploy across multiple availability zones
   - Implement pod anti-affinity for critical services
   - Use topology spread constraints
   - Implement proper replica counts
   - Use pod disruption budgets
   - Implement leader election for stateful applications
   - Use readiness and liveness probes effectively

9. **Disaster Recovery**:
   - Implement regular backups of state
   - Use GitOps for declarative configuration
   - Implement multi-region deployment
   - Use cluster federation where appropriate
   - Implement disaster recovery testing
   - Document recovery procedures
   - Use chaos engineering to test resilience

10. **Upgrade Strategy**:
    - Use rolling updates for zero-downtime deployments
    - Implement canary deployments for risk mitigation
    - Use blue/green deployments for critical services
    - Implement proper rollback procedures
    - Test upgrades in staging environments
    - Use feature flags for controlled rollouts
    - Document upgrade paths and procedures

Apply these best practices consistently across all containerized applications to ensure reliability, security, and maintainability.
