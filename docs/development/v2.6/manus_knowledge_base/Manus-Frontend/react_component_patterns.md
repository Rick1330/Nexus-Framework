name: React Component Design Patterns
use_when: When designing, implementing, or reviewing React components for the frontend interface.
content: 
When developing React components for Nexus Framework v2.6, follow these design patterns:

1. **Component Composition Pattern**:
   - Create small, focused components with single responsibilities
   - Compose complex UIs from simple components
   - Use children props for flexible component composition
   - Implement compound components for related UI elements
   - Use render props for flexible rendering logic
   - Implement higher-order components for cross-cutting concerns

2. **State Management Patterns**:
   - Use local state for component-specific data
   - Implement Zustand for global state management
   - Use React Query for server state management
   - Implement context for shared state within component trees
   - Use reducers for complex state logic
   - Implement state machines for components with multiple states
   - Use immutable state updates for predictability

3. **Performance Optimization Patterns**:
   - Use React.memo for pure functional components
   - Implement useCallback for stable callback references
   - Use useMemo for expensive computations
   - Implement virtualization for long lists (react-window)
   - Use code splitting and lazy loading for large components
   - Implement proper dependency arrays in hooks
   - Use key props correctly for efficient list rendering

4. **Styling Patterns**:
   - Use TailwindCSS utility classes for styling
   - Implement consistent component styling with shadcn/ui
   - Use CSS variables for theming
   - Implement responsive design with mobile-first approach
   - Use CSS modules for component-scoped styles
   - Implement dark mode with tailwind-dark-mode
   - Use consistent spacing and sizing scales

5. **Form Handling Patterns**:
   - Use React Hook Form for form state management
   - Implement Zod for form validation
   - Use controlled components for form inputs
   - Implement form submission with proper loading states
   - Use field arrays for dynamic form fields
   - Implement proper error handling and display
   - Use form context for complex forms

6. **Data Fetching Patterns**:
   - Use React Query for data fetching and caching
   - Implement proper loading states
   - Use error boundaries for error handling
   - Implement optimistic updates for better UX
   - Use prefetching for anticipated data needs
   - Implement infinite scrolling for large datasets
   - Use polling for real-time data

7. **Routing Patterns**:
   - Use Next.js App Router for page routing
   - Implement nested routes for complex UIs
   - Use dynamic routes for resource-based pages
   - Implement route guards for protected routes
   - Use route parameters for dynamic content
   - Implement shallow routing for URL updates without data refetching
   - Use route loading states for better UX

8. **Accessibility Patterns**:
   - Use semantic HTML elements
   - Implement proper ARIA attributes
   - Use focus management for interactive elements
   - Implement keyboard navigation
   - Use proper color contrast
   - Implement screen reader announcements for dynamic content
   - Test with accessibility tools (axe, lighthouse)

9. **Testing Patterns**:
   - Use React Testing Library for component testing
   - Implement Jest for unit testing
   - Use Cypress for end-to-end testing
   - Implement mock service worker for API mocking
   - Use snapshot testing judiciously
   - Implement user event testing for interactions
   - Test accessibility compliance

10. **Error Handling Patterns**:
    - Use error boundaries for component error isolation
    - Implement fallback UI for failed components
    - Use try/catch for async operations
    - Implement global error handling
    - Use toast notifications for user feedback
    - Implement retry mechanisms for failed operations
    - Log errors for debugging

Apply these patterns consistently across all React components to ensure maintainability, performance, and accessibility.
