name: Next.js Performance Optimization
use_when: When implementing or optimizing Next.js applications for performance, SEO, and user experience.
content: 
When optimizing Next.js applications for Nexus Framework v2.6, implement these techniques:

1. **Rendering Strategy Selection**:
   - Use Server Components for data-fetching and non-interactive UI
   - Implement Client Components only when interactivity is required
   - Use Static Site Generation (SSG) for content that rarely changes
   - Implement Incremental Static Regeneration (ISR) for semi-dynamic content
   - Use Server-Side Rendering (SSR) for highly dynamic, personalized content
   - Apply streaming for improved TTFB and user experience

2. **Image Optimization**:
   - Use Next.js Image component (`next/image`) for all images
   - Implement proper sizing with responsive variants
   - Use WebP or AVIF formats with proper fallbacks
   - Implement lazy loading for below-the-fold images
   - Set appropriate priority for above-the-fold images
   - Use blur placeholders for large hero images
   - Implement proper caching strategies with cache-control headers

3. **Font Optimization**:
   - Use `next/font` for automatic font optimization
   - Implement font subsetting to reduce file size
   - Use variable fonts where appropriate
   - Implement font-display: swap for text visibility during loading
   - Preload critical fonts
   - Use system font stacks as fallbacks
   - Limit font weight and style variations

4. **JavaScript Optimization**:
   - Implement code splitting with dynamic imports
   - Use React.lazy for component-level code splitting
   - Implement proper tree shaking with ES modules
   - Minimize third-party dependencies
   - Use bundle analyzer to identify large packages
   - Implement route-based code splitting
   - Use production builds with minification

5. **Data Fetching Optimization**:
   - Implement React Server Components for server-side data fetching
   - Use React Query for client-side data management
   - Implement SWR for data revalidation
   - Use proper caching strategies with cache tags
   - Implement parallel data fetching where possible
   - Use streaming for progressive loading
   - Implement data prefetching for anticipated user journeys

6. **Route Optimization**:
   - Use App Router for improved routing performance
   - Implement route groups for code organization
   - Use parallel routes for complex layouts
   - Implement intercepting routes for modal patterns
   - Use loading.js for route loading states
   - Implement error.js for graceful error handling
   - Use route handlers for API endpoints

7. **SEO Optimization**:
   - Implement proper metadata with `next/metadata`
   - Use dynamic metadata for page-specific SEO
   - Implement canonical URLs for duplicate content
   - Use structured data (JSON-LD) for rich results
   - Implement proper Open Graph and Twitter card metadata
   - Use sitemap.xml and robots.txt
   - Implement proper status codes for error pages

8. **Caching Strategy**:
   - Use Route Cache for rendered content
   - Implement Data Cache for fetch requests
   - Use Full Route Cache for static routes
   - Implement Router Cache for client-side navigation
   - Use appropriate cache revalidation strategies
   - Implement cache tags for targeted invalidation
   - Use stale-while-revalidate pattern for improved performance

9. **Edge Runtime Optimization**:
   - Deploy to Edge runtime for reduced latency
   - Use Edge API Routes for dynamic API endpoints
   - Implement geolocation-based customization
   - Use Edge Middleware for request-time processing
   - Implement A/B testing at the edge
   - Use Edge Config for runtime configuration
   - Implement edge caching for improved performance

10. **Monitoring and Analytics**:
    - Use Next.js Analytics for Core Web Vitals
    - Implement Real User Monitoring (RUM)
    - Use Lighthouse for performance auditing
    - Implement custom metrics for business-specific KPIs
    - Use performance budget monitoring
    - Implement error tracking and reporting
    - Use server timing headers for backend performance

Apply these optimization techniques consistently across the Next.js application to ensure optimal performance, SEO, and user experience.
