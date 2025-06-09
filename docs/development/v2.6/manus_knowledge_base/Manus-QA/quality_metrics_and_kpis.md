name: Quality Assurance Metrics and KPIs
use_when: When establishing quality metrics, defining KPIs, or implementing quality dashboards for software development projects.
content: 
When implementing quality metrics for Nexus Framework v2.6, use these measurement practices:

1. **Code Quality Metrics**:
   - **Cyclomatic Complexity**: Maintain below 15 for all methods
   - **Code Coverage**: Maintain minimum 80% for unit tests, 60% for integration tests
   - **Duplicate Code**: Keep below 3% across codebase
   - **Technical Debt Ratio**: Maintain below 5% of total development time
   - **Comment Density**: Maintain 15-30% for complex components
   - **Function Length**: Keep below 50 lines per method
   - **Class Length**: Keep below 500 lines per class
   - **Code Churn**: Monitor frequency of changes to identify unstable components
   - **Static Analysis Violations**: Zero critical or blocker issues
   - **Dependency Freshness**: No dependencies more than 2 major versions behind

2. **Testing Effectiveness Metrics**:
   - **Defect Detection Percentage**: Target >85% defects found before release
   - **Test Case Effectiveness**: Track defects found per test case
   - **Requirements Coverage**: 100% of requirements covered by tests
   - **Mutation Score**: Maintain >75% for critical components
   - **Test Flakiness Rate**: Keep below 2% of all test executions
   - **Test Execution Time**: Monitor trends to detect performance degradation
   - **Test Maintenance Effort**: Track time spent maintaining tests
   - **Defect Density in Tests**: Monitor quality of test code itself
   - **Test-to-Code Ratio**: Maintain 1:1 to 2:1 for critical components
   - **Automated Test Percentage**: Maintain >80% of all test cases automated

3. **Defect Metrics**:
   - **Defect Density**: Track defects per 1000 lines of code
   - **Defect Severity Distribution**: Monitor ratio of critical/high/medium/low defects
   - **Defect Age**: Average time defects remain open
   - **Defect Resolution Time**: Average time to fix by severity
   - **Defect Escape Rate**: Defects found in production vs. testing
   - **Defect Injection Rate**: New defects introduced per sprint
   - **Regression Rate**: Percentage of defects that are regressions
   - **Defect Clustering**: Identify components with high defect concentration
   - **Reopened Defect Rate**: Percentage of defects reopened after fix
   - **Root Cause Analysis**: Track patterns in defect causes

4. **Performance Metrics**:
   - **Response Time**: 95th percentile under 300ms for critical APIs
   - **Throughput**: Requests per second capacity for key services
   - **Error Rate**: Keep below 0.1% for production services
   - **CPU Utilization**: Keep below 70% under normal load
   - **Memory Usage**: Track growth patterns to detect leaks
   - **Database Query Performance**: 95% of queries under 100ms
   - **Page Load Time**: Keep below 2 seconds for web interfaces
   - **API Latency**: Track by endpoint and method
   - **Resource Utilization**: Monitor trends across environments
   - **Scalability Metrics**: Performance change under increasing load

5. **Security Metrics**:
   - **Vulnerability Density**: Vulnerabilities per 1000 lines of code
   - **OWASP Top 10 Coverage**: 100% of applicable checks implemented
   - **Security Defect Age**: Average time security issues remain open
   - **Dependency Vulnerability Count**: Zero known vulnerabilities in production
   - **Security Test Coverage**: 100% of security requirements tested
   - **Time to Fix Security Issues**: Track by severity
   - **Security Debt**: Track unresolved security issues over time
   - **Security Review Coverage**: Percentage of code reviewed for security
   - **Authentication Failure Rate**: Monitor failed login attempts
   - **Security Patch Latency**: Time to apply security patches

6. **User Experience Metrics**:
   - **Usability Test Success Rate**: >90% task completion in usability tests
   - **User Error Rate**: Track frequency of user errors in interfaces
   - **User Satisfaction Score**: Maintain >4.5/5 in user surveys
   - **Accessibility Compliance**: 100% WCAG 2.1 AA compliance
   - **Feature Adoption Rate**: Track usage of new features
   - **Task Completion Time**: Monitor for user efficiency
   - **Abandonment Rate**: Track incomplete user workflows
   - **User Support Ticket Rate**: Monitor issues reported by users
   - **Cognitive Load Metrics**: Track complexity of user interactions
   - **Internationalization Coverage**: Support for required languages

7. **Process Metrics**:
   - **Build Success Rate**: Maintain >95% successful builds
   - **Deployment Success Rate**: Maintain >98% successful deployments
   - **Time to Deploy**: Track deployment efficiency
   - **Code Review Coverage**: 100% of code changes reviewed
   - **Code Review Depth**: Comments per 100 lines of code reviewed
   - **Time to Merge**: Average time from PR creation to merge
   - **Branch Lifetime**: Keep feature branches under 5 days
   - **Deployment Frequency**: Track deployment cadence
   - **Lead Time**: Time from commit to production
   - **Mean Time to Recovery**: Average time to recover from failures

8. **Documentation Metrics**:
   - **Documentation Coverage**: 100% of APIs and features documented
   - **Documentation Freshness**: No docs more than 2 sprints out of date
   - **Documentation Quality Score**: Based on peer reviews
   - **Documentation Feedback**: Track user ratings of documentation
   - **Documentation Usage Metrics**: Track most/least accessed docs
   - **Example Coverage**: Percentage of features with examples
   - **Documentation Build Success**: Ensure docs build without errors
   - **Broken Links**: Zero broken links in documentation
   - **Documentation Test Coverage**: Percentage of examples tested
   - **Internationalization Coverage**: Support for required languages

9. **Team Metrics**:
   - **Velocity Consistency**: Variation in team velocity <20%
   - **Sprint Completion Rate**: Percentage of planned work completed
   - **Estimation Accuracy**: Actual vs. estimated time
   - **Knowledge Distribution**: Bus factor for critical components
   - **Team Satisfaction**: Regular team health surveys
   - **Onboarding Time**: Time for new team members to become productive
   - **Innovation Time**: Percentage of time for exploration
   - **Cross-training Level**: Team members able to work across components
   - **Technical Debt Management**: Time allocated to debt reduction
   - **Continuous Improvement**: Track implemented improvements

10. **Quality Dashboard Implementation**:
    - Implement real-time quality dashboards with key metrics
    - Use trend visualization for all metrics
    - Implement alerting for metric thresholds
    - Provide drill-down capabilities for detailed analysis
    - Use consistent visualization patterns
    - Implement role-based views for different stakeholders
    - Provide context and targets for all metrics
    - Implement regular review cadence for metrics
    - Use automated data collection where possible
    - Document metric definitions and calculation methods

Apply these measurement practices consistently across all quality assurance activities to ensure comprehensive quality monitoring and continuous improvement.
