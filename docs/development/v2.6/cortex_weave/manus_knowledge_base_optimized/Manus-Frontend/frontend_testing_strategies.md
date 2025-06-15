name: Frontend Testing Strategies
use_when: When designing and implementing testing strategies for frontend applications, ensuring quality, performance, and user experience.
content: |
  Key strategies for frontend testing:
  1.  **Unit Testing**: Test individual components or functions in isolation. Focus on logic, props, and state. Use Jest, React Testing Library, or similar frameworks.
  2.  **Component Testing**: Test UI components in isolation or small groups, simulating user interactions and verifying visual output. Useful for design systems and reusable components.
  3.  **Integration Testing**: Verify interactions between different parts of the frontend application (e.g., component-to-API, component-to-store). Ensures modules work together correctly.
  4.  **End-to-End (E2E) Testing**: Simulate real user flows across the entire application, including backend interactions. Use tools like Cypress, Playwright, or Selenium. Focus on critical user journeys.
  5.  **Visual Regression Testing**: Detect unintended visual changes in the UI. Capture screenshots of components or pages and compare them against baselines. Tools like Storybook with Chromatic or Percy.
  6.  **Accessibility Testing (A11y)**: Ensure the application is usable by people with disabilities. Use automated tools (axe-core, Lighthouse) and manual checks (keyboard navigation, screen reader testing).
  7.  **Performance Testing**: Measure and optimize frontend performance metrics (e.g., page load time, interactivity, rendering speed). Use Lighthouse, WebPageTest, or RUM (Real User Monitoring).
  8.  **Cross-Browser/Device Testing**: Verify application functionality and appearance across different browsers, operating systems, and devices (desktop, tablet, mobile). Use tools like BrowserStack or Sauce Labs.
  9.  **Usability Testing**: Gather feedback from real users to identify usability issues and improve the user experience. Can be moderated or unmoderated.
  10. **Snapshot Testing**: Capture the rendered output of components (e.g., React components) and compare them against previous snapshots to detect unexpected changes. Useful for UI stability.
  Apply these strategies to build high-quality, performant, and user-friendly frontend applications.

