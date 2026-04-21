# Frontend

Modern web UI engineering — foundations through production-grade practice.

## Foundations (`FoundationsWeb/`)
HTML5 + semantics, Accessibility (ARIA, WCAG), CSS3, Flex/Grid/Container Queries, logical properties, architecture (BEM, ITCSS, SMACSS, OOCSS). CSS-in-JS (compiled/atomic). Tailwind utility-first. CSS Houdini, subgrid. Typography, color systems, design tokens, dark mode, RTL/i18n/l10n.

## JavaScript Core (`JavaScriptCore/`)
ES2015 → latest; scopes/closures; event loop + async/await; ESM/CJS; iterators/generators; Proxy/Reflect; WeakRefs; Temporal API; typed arrays; Workers (Web/Shared/Service); WASM integration.

## TypeScript (`TypeScript/`)
Types/interfaces, generics, conditional types, template literal types, decorators, strict config, narrowing, utility types, runtime validation (zod, io-ts).

## Frameworks (`Frameworks/`)
- **React** + RSC + Next.js (App Router) + Remix.
- **Vue 3** Composition API + Nuxt 3.
- **Svelte / SvelteKit**, **SolidJS**, **Angular (Signals)**, **Qwik (Resumability)**, **Astro (Islands)**, **Lit Web Components**, **Preact**.

## State Management (`StateManagement/`)
useState/useReducer, Redux Toolkit + RTK Query, MobX, Zustand, Jotai, Recoil, TanStack Query, SWR, Signals (Solid/Preact/Angular), Apollo GraphQL.

## Routing + Data Fetching (`Routing_DataFetching/`)
Client-side routing, route guards, prefetch/preload, Suspense for data, Server Actions/RSC, mutation + optimistic UI, pagination (offset / keyset / cursor), error boundaries.

## Rendering Strategies (`RenderingStrategies/`)
CSR, SSR, SSG, ISR, streaming HTTP, partial hydration/islands, edge rendering, prerender, hybrid.

## Performance (`Performance/`)
Core Web Vitals (LCP, INP replaced FID, CLS). Critical CSS, image optimization (AVIF, WebP, responsive srcset), font subset + `font-display`, code splitting/dynamic import, tree shaking, memoization, virtualization, IntersectionObserver, perf budgets. Tools: Lighthouse, WebPageTest, DevTools.

## Accessibility (`AccessibilityAndInclusivity/`)
Semantic HTML, ARIA roles/states, focus management, screen readers (NVDA/VoiceOver/JAWS), keyboard-only, color contrast, reduced motion, form a11y, live regions. Test: axe, pa11y.

## Security (`Security/`)
CSP, Trusted Types, SameSite cookies, XSS/CSRF prevention, clickjacking (frame-ancestors), SRI, permissions policy, OAuth PKCE, localStorage vs HTTP-only cookies.

## Testing (`TestingFE/`)
Vitest/Jest + React Testing Library. Playwright/Cypress E2E. Visual regression (Chromatic, Percy). Storybook. MSW for mocks. Accessibility tests via axe.

## Build Tools + DX (`BuildToolsAndDX/`)
Vite, Webpack, Rollup, esbuild, Parcel, Bun, Turbopack. Transforms via SWC/Babel. PostCSS. Monorepos: Nx, Turborepo, pnpm/yarn workspaces. Husky + lint-staged. ESLint/Prettier/Biome.

## PWA / Offline (`PWA_Offline/`)
Service Workers, Cache API strategies (stale-while-revalidate), background sync, push notifications, install manifest, offline-first DBs (IndexedDB/Dexie/RxDB).

## Animations + 3D (`Animations_3D/`)
CSS animations + transitions, FLIP technique. Framer Motion, GSAP, Lottie, Rive. WebGL, Three.js, R3F, BabylonJS, shader basics (GLSL), Canvas API, WebGPU.

## Design Systems (`DesignSystems/`)
Storybook + Chromatic. Radix Primitives, Headless UI, shadcn/ui, MUI, Ant Design, Chakra. Tailwind tokens, Style Dictionary, Figma token pipelines.

## Modern UX (`ModernUX_Topics/`)
Motion principles, Gestalt UI, micro-interactions, skeleton vs spinner, form UX, empty/error/zero states, progressive disclosure, dark patterns to avoid.

## Books + Refs
- MDN Web Docs (must).
- *CSS in Depth* — Keith J. Grant.
- *You Don't Know JS Yet* — Kyle Simpson.
- *JavaScript: The Definitive Guide* — Flanagan.
- web.dev (Google), smashingmagazine.com, patterns.dev.
