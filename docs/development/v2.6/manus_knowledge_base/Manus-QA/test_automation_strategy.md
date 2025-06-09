name: Test Automation Strategy
use_when: When designing, implementing, or reviewing test automation frameworks, test plans, or quality assurance processes.
content: 
When implementing test automation for Nexus Framework v2.6, follow these strategic practices:

1. **Test Pyramid Implementation**:
   - Build a balanced test pyramid with proper distribution:
     - Unit tests (70%): Fast, focused component testing
     - Integration tests (20%): Service interaction testing
     - End-to-end tests (10%): Full system workflow testing
   - Implement proper isolation between test levels
   - Use appropriate tools for each test level
   - Design for test independence and parallelization
   - Implement consistent patterns across test levels
   - Document test coverage goals for each level
   - Use metrics to maintain pyramid balance

2. **Test Automation Framework Design**:
   - Implement page object model for UI testing
   - Use service objects for API testing
   - Implement proper abstraction layers
   - Design for test data management
   - Use consistent assertion patterns
   - Implement proper setup and teardown mechanisms
   - Design for cross-browser and cross-platform testing
   - Use BDD frameworks for behavior-driven tests

3. **Test Data Management**:
   - Implement test data factories for consistent generation
   - Use database seeding for integration tests
   - Implement proper test data isolation
   - Design for data cleanup after tests
   - Use realistic but sanitized test data
   - Implement data versioning for test scenarios
   - Use appropriate test data for different environments
   - Design for data-driven testing

4. **Continuous Testing Integration**:
   - Integrate tests into CI/CD pipelines
   - Implement proper test parallelization
   - Use test splitting for efficient execution
   - Implement test result reporting and visualization
   - Design for fast feedback cycles
   - Use test prioritization for critical paths
   - Implement flaky test detection and management
   - Design for environment-specific test execution

5. **API Testing Strategy**:
   - Implement contract testing with consumer-driven contracts
   - Use schema validation for response verification
   - Implement proper API mocking for unit tests
   - Design for API versioning in tests
   - Use appropriate assertion levels for different endpoints
   - Implement performance testing for critical APIs
   - Design for API security testing
   - Use proper test organization by API domain

6. **UI Testing Strategy**:
   - Implement visual testing for UI components
   - Use selector strategies resilient to UI changes
   - Implement proper wait mechanisms for asynchronous UI
   - Design for responsive testing across screen sizes
   - Use component testing for isolated UI elements
   - Implement accessibility testing in UI tests
   - Design for cross-browser compatibility testing
   - Use proper error handling for UI interactions

7. **Performance Testing**:
   - Implement load testing for system capacity verification
   - Use stress testing for system limits identification
   - Implement endurance testing for stability verification
   - Design for performance regression detection
   - Use appropriate performance metrics and thresholds
   - Implement distributed load generation
   - Design for realistic user simulation
   - Use proper performance test data management

8. **Security Testing Automation**:
   - Implement SAST integration in build pipeline
   - Use DAST for deployed application testing
   - Implement dependency scanning for vulnerabilities
   - Design for security regression testing
   - Use automated penetration testing tools
   - Implement compliance verification tests
   - Design for security test data management
   - Use proper security test reporting

9. **Test Reporting and Analytics**:
   - Implement comprehensive test reporting dashboards
   - Use trend analysis for quality metrics
   - Implement test coverage visualization
   - Design for failure analysis and categorization
   - Use proper test result storage and history
   - Implement test execution time tracking
   - Design for test reliability metrics
   - Use proper integration with issue tracking systems

10. **Test Maintenance Strategy**:
    - Implement test code reviews
    - Use proper test documentation
    - Implement test refactoring practices
    - Design for test maintainability
    - Use proper version control for test code
    - Implement test deprecation processes
    - Design for test evolution with system changes
    - Use proper test ownership and responsibility assignment

Apply these strategic practices consistently across all test automation implementations to ensure comprehensive quality assurance and reliable system behavior.
