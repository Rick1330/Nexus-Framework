name: Container Orchestration Best Practices - Core
use_when: When designing, implementing, or managing containerized applications and Kubernetes deployments.
content: |
  Core best practices for container orchestration:
  1.  **Container Design**: Use minimal base images, single concern per container, multi-stage builds, and proper health checks.
  2.  **Kubernetes Resource Management**: Define resource requests/limits, use HPA, node affinity, and pod disruption budgets.
  3.  **Configuration Management**: Use ConfigMaps for non-sensitive data, Secrets for sensitive data, and Helm for templated deployments.
  4.  **Networking**: Implement service mesh (Istio), network policies, proper ingress configuration, and appropriate service types.
  5.  **Security**: Implement pod security policies, network policies, RBAC, image scanning, and admission controllers.
  6.  **Stateful Applications**: Use StatefulSets, persistent volume claims, volume snapshots, and init containers.
  7.  **Monitoring & Observability**: Implement Prometheus, Grafana, distributed tracing (Jaeger), structured logging (Loki), and alerting.
  8.  **High Availability**: Deploy across multiple availability zones, use pod anti-affinity, topology spread constraints, and proper replica counts.
  9.  **Disaster Recovery**: Implement regular backups, GitOps, multi-region deployment, and disaster recovery testing.
  10. **Upgrade Strategy**: Use rolling updates, canary deployments, blue/green deployments, and proper rollback procedures.
  Apply these practices for reliable, secure, and maintainable containerized applications.

