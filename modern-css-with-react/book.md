# Module 1: CSS Landscape 2026 — React Edition

Est. study time: 2.5h
Language: en

## Learning Objectives
- Map every major CSS approach in React and its 2026 status
- Evaluate approaches along 6 decision axes
- Select appropriate approach for a given React project context

---

## Core Content

### The 2026 CSS Approaches in React

Six major approaches exist. Each takes a different stance on where CSS lives, how it scopes, and what runs at runtime.

| Approach | Runtime cost | RSC compatible | Scoping | Popular in 2026 |
|----------|-------------|----------------|---------|-----------------|
| Plain CSS / Sass | None | Yes | Global / BEM | Mature codebases |
| CSS Modules | None | Yes | File-scoped | Next.js, Vite defaults |
| Tailwind CSS | Minimal (JIT) | Yes | Utility classes | Dominant new projects |
| Runtime CSS-in-JS | High | Partial | Component-scoped | Declining for new apps |
| Zero-runtime CSS-in-JS | None | Yes | Component-scoped | Rising (Vanilla Extract) |
| CSS with `@scope` | None | Yes | Scoped (native) | Emerging (Chrome 118+) |

> **Think**: A teammate proposes "let's use styled-components for our new Next.js app". What 3 questions should you ask before agreeing?
>
> *Answer: (1) Do we use RSC? styled-components needs client components. (2) What's our SSR story? styled-components has known hydration mismatch issues. (3) Team familiarity — is CSS-in-JS worth the bundle cost vs CSS Modules or Tailwind?*

### Decision Axes Framework

Every CSS approach decision reduces to tradeoffs along 6 axes:

**1. Runtime cost**

Runtime CSS-in-JS injects style tags at runtime. Each styled component call parses template literal → generates class → inserts into DOM. For an app with 200+ styled components, this means re-parsing CSS string on every client render.

Zero-runtime alternatives extract styles at build time. Vanilla Extract reads `.css.ts` files during build, outputs static `.css` files. RSC can stream these without JS.

> Example bundle impact:
> ```
> Runtime CSS-in-JS lib: ~12-15 kB gzip (styled-components/emotion runtime)
> Vanilla Extract: 0 kB runtime
> Tailwind: ~0.5 kB runtime (resets only)
> CSS Modules: 0 kB runtime
> ```

**2. RSC / Server Component compatibility**

React Server Components separate server-rendered components from client bundles. Any CSS approach that requires JavaScript to resolve styles is incompatible with RSC.
- CSS Modules, Tailwind, plain CSS: fully compatible — styles are static, resolved at build
- Runtime CSS-in-JS: requires `"use client"` — style injection only happens in browser
- Zero-runtime CSS-in-JS: compatible because no JS needed for styles

> **Think**: RSC-first app (Next.js App Router) — which approaches are eliminated?
>
> *Answer: Runtime CSS-in-JS (styled-components, Emotion) requires client boundary for every styled component, defeating RSC benefits. Tailwind, CSS Modules, Vanilla Extract work seamlessly.*

**3. Developer experience**

- Tailwind: fast iteration once class names memorized. No context-switching between files.
- CSS Modules: familiar CSS syntax, TypeScript autocomplete via `.module.css.d.ts`
- Runtime CSS-in-JS: dynamic styling via props natural (`color: ${p => p.$variant === 'danger' ? 'red' : 'blue'}`)
- Zero-runtime: TypeScript-first, typed styles, but requires `.css.ts` file per component

**4. Scoping & isolation**

- Plain CSS: global namespace — naming conventions needed (BEM, etc.)
- CSS Modules: automatically scoped — `styles.button` becomes unique `.Button_button_abc123`
- CSS-in-JS: automatic scoping via generated class names
- Tailwind: scoped to utility classes applied directly; no cascade conflicts
- `@scope`: native CSS scoping (`@scope(.card) { ... }`)

**5. Dynamic styling**

| Approach | Dynamic styles | Mechanism |
|----------|---------------|-----------|
| Plain CSS | Limited | Class toggling, inline styles |
| CSS Modules | Via class composition | `clsx(styles.base, isActive && styles.active)` |
| Tailwind | Via class composition | `clsx('text-base', isLarge && 'text-lg')` |
| Runtime CSS-in-JS | Native | Props → CSS template interpolation |
| Zero-runtime CSS-in-JS | Via vars/recipes | CSS custom properties + recipe variants |

**6. Bundle footprint**

- Plain CSS / CSS Modules: as authored
- Tailwind: purge unused utilities — typically 5-15 kB gzip
- Runtime CSS-in-JS: library runtime + all style strings in JS bundle
- Zero-runtime CSS-in-JS: extracted to CSS files, not in JS bundle

> **Think**: Your team ships a moderate React app (50 components). How would bundle sizes differ between (a) Tailwind, (b) CSS Modules, (c) styled-components?
>
> *Answer: (a) Tailwind: ~10 kB compressed CSS, <1 kB runtime. (b) CSS Modules: ~5-8 kB CSS, 0 kB runtime. (c) styled-components: ~14 kB runtime lib + authored CSS strings in JS bundle (~15-25 kB total gzip). For 50 components, runtime CSS-in-JS adds ~10-15 kB of library overhead beyond the styles themselves.*

### When Each Approach Wins

- **Plain CSS / Sass**: legacy project, strict design system already in CSS, team knows Sass well, no React-specific CSS needs
- **CSS Modules**: framework default (Next.js, Vite), zero-runtime, TypeScript support, team prefers standard CSS syntax
- **Tailwind**: rapid prototyping, team consistency via constraint system, design tokens built-in, utility-first
- **Runtime CSS-in-JS**: heavy dynamic styling, design system with hundreds of variants, team already uses and accepts tradeoffs. **Declining** for greenfield
- **Zero-runtime CSS-in-JS**: type-safe styles, design system needing build-time extraction, RSC-compatible, want CSS-in-JS syntax without runtime cost
- **`@scope`**: native scoping without tooling, new Chrome-only projects, supplement to other approaches

> **Think**: When would runtime CSS-in-JS still be the right choice in 2026?
>
> *Answer: Greenfield? Rare. But existing large styled-components/Emotion codebase: migration cost outweighs runtime cost. Also: electron apps with heavy dynamic theming where RSC compatibility irrelevant.*

---

### Why This Matters

Choosing wrong CSS approach costs months in refactoring. styled-components in an RSC app means you can't use server components with those components. Tailwind in a design system means consumers inherit utility-first DX. Plain CSS in a 50-component app cascades into specificity hell.

React in 2026 has moved toward RSC and server-first rendering. CSS decisions that don't account for this produce either runtime bloat or broken SSR.

---

### Common Questions

**Q: Can I mix approaches in one React app?**
A: Yes, and many do. Example: Tailwind for page layouts, CSS Modules for complex component states, small amount of global CSS for reset/fonts. Each serves a scope. Key rule: one approach per component — don't use styled-components + CSS Modules + inline styles in one file.

**Q: Is `@scope` the future that kills all other approaches?**
A: `@scope` gives native CSS scoping but doesn't solve dynamic styling, bundle optimization, or design token enforcement. It replaces naming conventions like BEM but not CSS Modules or CSS-in-JS entirely. More likely: `@scope` + Tailwind or `@scope` + Vanilla Extract becomes common.

**Q: Does Next.js or Vite recommend anything?**
A: Next.js defaults to CSS Modules (global CSS only in `layout.tsx`). Tailwind integration is first-class. Vite has built-in CSS Modules support. Both support plain CSS. Neither recommends runtime CSS-in-JS — it requires client components.

**Q: How do I decide which approach to use for each part of my app?**
A: Use the layer model: global foundation (reset, fonts, tokens) → layout (grid, flex) → component (variants, states) → overrides (per-page adjustments). Each layer can use a different approach. Global → plain CSS. Layout → Tailwind. Component → CSS Modules or Vanilla Extract. Overrides → inline styles or className props. Module 16 covers this in depth.

---

### Hybrid Strategy: How to Mix Approaches Effectively

A single CSS approach rarely fits every part of an app. The question isn't "which approach?" but "which approach for which layer?"

**The Layer Model:**

```text
┌─────────────────────────────────┐
│  Layer 1: Global Foundation     │  ← Plain CSS / Sass
│  (reset, fonts, CSS vars,       │     One global file
│   keyframes, print styles)      │
├─────────────────────────────────┤
│  Layer 2: Layout & Structure    │  ← Tailwind utility classes
│  (grid, flex, spacing,          │     Fast, consistent,
│   responsive breakpoints)       │     design-constraint system
├─────────────────────────────────┤
│  Layer 3: Component Styles      │  ← CSS Modules / Vanilla Extract
│  (variants, states, animations, │     Scoped, zero runtime,
│   pseudo-elements, media qs)    │     type-safe variants
├─────────────────────────────────┤
│  Layer 4: Per-Instance Override │  ← className prop + twMerge
│  (one-off adjustments,          │     or inline style for
│   dynamic values from data)     │     truly dynamic values
└─────────────────────────────────┘
```

Each layer has different needs:
- **Global**: Browser reset, font-face declarations, CSS custom properties, animation keyframes — never changes per component
- **Layout**: Responsive grids, page structure, spacing systems — benefit from utility-first speed
- **Component**: Scoped styles with variants and states — need isolation and type safety
- **Override**: Per-use-case tweaks — escape hatch, not primary mechanism

**Concrete mixing patterns that work:**

| Pattern | Approaches | When | Example |
|---------|-----------|------|---------|
| Tailwind + CSS Modules | Tailwind for layout, CSS Modules for complex components | App with standard pages + interactive widgets | Dashboard grid (Tailwind), drag-drop list (CSS Modules) |
| Vanilla Extract + Tailwind | VE for component library, Tailwind for page composition | Design system consumed by Tailwind app | Button/Input library (VE), pages composing them (Tailwind) |
| Plain CSS + CSS Modules | Global foundation + scoped components | Legacy migration, app with heavy global styles | Reset/typography (CSS), product cards (Modules) |
| Zero-runtime + inline styles | Static styles in CSS-in-JS, dynamic values inline | Data visualization, progress bars | Chart container (VE), bar widths (inline style) |

**Pattern 1: Tailwind for layout, CSS Modules for components**

Most common in 2026. Tailwind handles the big structural decisions (grid columns, breakpoints, spacing). CSS Modules handle component-internal states (hover, active, disabled, variants).

```tsx
// Page layout uses Tailwind — fast, visible at a glance
function DashboardPage() {
  return (
    <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 p-6">
      <Sidebar className="lg:col-span-1" />
      <MainContent className="lg:col-span-2" />
    </div>
  );
}

// Complex component uses CSS Modules — isolated, variant-rich
// Sidebar.tsx
import styles from './Sidebar.module.css';
import clsx from 'clsx';

function Sidebar({ className }) {
  const [collapsed, setCollapsed] = useState(false);
  return (
    <aside className={twMerge(styles.sidebar, collapsed && styles.collapsed, className)}>
      <nav>
        {items.map(item => (
          <a
            key={item.href}
            href={item.href}
            className={clsx(styles.navItem, item.active && styles.active)}
          >{item.label}</a>
        ))}
      </nav>
    </aside>
  );
}
```

Why this works: layout classes are few and structural (easy to read as Tailwind). Component classes are complex and stateful (benefit from isolation).

**Pattern 2: Vanilla Extract component library consumed by Tailwind app**

Design system authoring in VE (typed, zero runtime, theme contracts). Page composition in Tailwind (fast, no file switching).

```tsx
// Component library — Vanilla Extract
// Button.css.ts
export const button = recipe({
  base: { display: 'inline-flex', borderRadius: '6px' },
  variants: {
    variant: {
      primary: { background: 'var(--color-primary)', color: 'white' },
      outline: { background: 'transparent', border: '1px solid var(--color-primary)' },
    },
  },
});

// Consumer app — Tailwind
function LandingPage() {
  return (
    <div className="flex flex-col items-center gap-4 p-12">
      <h1 className="text-3xl font-bold">Welcome</h1>
      <Button variant="primary" className="mt-4">Get Started</Button>
    </div>
  );
}
```

**Pattern 3: Legacy Sass + new CSS Modules**

Incremental migration for established Sass codebases. Keep existing Sass styles where they work. Use CSS Modules for all new components. Shared tokens move to CSS custom properties.

```scss
// _tokens.scss → migrated to CSS custom properties
// Legacy: $color-primary: #0366d6;
// New: --color-primary: #0366d6;
```

```tsx
// Legacy component (Sass)
import './legacy-card.scss';
function LegacyCard({ children }) { return <div className="legacy-card">{children}</div>; }

// New component (CSS Modules)
import styles from './NewWidget.module.css';
function NewWidget() { return <div className={styles.widget}>...</div>; }
```

**What NOT to mix:**

| Bad combination | Why |
|----------------|-----|
| Runtime CSS-in-JS + Tailwind in same component | Two different class generation systems fighting for DOM — unpredictable specificity |
| CSS Modules + Sass `@extend` across files | Cross-file coupling that breaks isolation |
| Inline styles as primary styling mechanism | No media queries, no pseudo-classes, no cascade |
| Multiple approaches in one file | Reader must parse two styling paradigms in one component |

**Rule**: One approach per component file. Choose which approach fits the component's role (layout vs interactive vs presentational) and commit to it.

> **Think**: Your team uses Tailwind for everything. You're building a complex data table with sortable columns, resizable headers, row selection, and inline editing. The className string would be 30+ utilities. What do you do?
>
> *Answer: Extract the table into CSS Modules. Keep the page layout in Tailwind. The table component's internal complexity is isolated; the page structure stays fast and visible.*

---

### Use Case Decision Matrix

| App type | Recommended primary | Mix with | Why |
|----------|-------------------|----------|-----|
| SaaS dashboard (Next.js App Router) | Tailwind | CSS Modules for complex widgets | RSC-compatible, fast iteration, design consistency |
| Component library for 5+ apps | Vanilla Extract | CSS custom properties for themes | Zero runtime cost for consumers, type-safe API |
| Legacy Sass SPA migrating to Next.js | CSS Modules for new code | Keep Sass for migrated pages | Incremental migration, preserve existing tokens |
| Marketing site (static, 5 pages) | Tailwind or CSS Modules | Plain CSS for reset/fonts | Small scope, zero complexity overhead |
| Enterprise design system (50+ components) | Vanilla Extract | Sprinkles for atomic utilities | Type safety, theme contracts, zero runtime |
| Electron desktop app | Any | styled-components OK if team prefers | No SSR, no RSC, bundle size less critical |
| Rapid prototype / MVP | Tailwind | Inline styles for dynamic values | Speed > architecture, refactor later |
| Open-source component library | CSS Modules or Vanilla Extract | CSS custom properties for theming | Consumers shouldn't inherit your styling dependencies |

---

## Examples

### Example 1: Choosing for a SaaS dashboard

**Context**: New Next.js App Router app. 3 developers. 6-month timeline. Team knows React but not deep CSS.

Decision process:
1. RSC-first → eliminate runtime CSS-in-JS
2. Team speed → Tailwind gives fast iteration without CSS file management
3. Need custom design later → Tailwind config extensible

**Choice**: Tailwind + small CSS Modules for complex interactive widgets.

### Example 2: Choosing for a component library

**Context**: Shared component library consumed by 5 apps. TypeScript required. Explicit API surface.

Decision process:
1. No runtime — consumers have different app architectures
2. Type safety — typed style contracts
3. Theming — CSS custom properties for consumer customization

**Choice**: Vanilla Extract (zero-runtime, typed, themes as CSS variables).

### Example 3: Choosing for a legacy migration

**Context**: 200-page React SPA using Sass + BEM. Migrating to Next.js gradually.

Decision process:
1. Existing investment in Sass → reuse design tokens
2. Incremental migration → don't rewrite every component
3. New pages use RSC → need compatible approach

**Choice**: Keep Sass for migrated pages, use CSS Modules for new RSC components. Phase out Sass over 1 year.

---

## Key Takeaways
- Six main approaches: plain CSS, CSS Modules, Tailwind, runtime CSS-in-JS, zero-runtime CSS-in-JS, `@scope`
- Six decision axes: runtime cost, RSC compat, DX, scoping, dynamic styling, bundle
- Runtime CSS-in-JS declining for greenfield; RSC compatibility is the main driver
- Tailwind dominates new projects; Vanilla Extract rising for design systems
- Layer model: global → layout → component → override — each layer fits a different approach
- One approach per component file; mix across layers, not within components
- `@scope` (native scoping) is emerging but not yet replacing tooling
- Decision matrix: map app type to recommended approach + mixing strategy

---

## Common Misconception

**"I need CSS-in-JS to do dynamic styles in React."**

Not true. Dynamic styles in React are just class toggles or inline styles, regardless of CSS approach.

```tsx
// No CSS-in-JS needed — just class composition
function Button({ variant }) {
  return (
    <button className={clsx(
      styles.base,
      styles[variant as keyof typeof styles]
    )}>
      Click
    </button>
  );
}
```

CSS Modules + `clsx` achieves identical result to `styled('button')` with zero runtime cost. CSS-in-JS adds convenience (auto-prop-typing, theme access) but not capability.

---

## Feynman Explain
(Explain the six CSS approaches to a teammate who "just writes CSS in a file". Use simple terms. Say when you'd pick each. Don't use "runtime" or "RSC" until you explain what they mean.)


---

## Reframe
(Pause. Judge the decision framework: is "RSC compatibility" really the most important axis? For which apps would bundle size matter more? For which would team speed dominate?)

---

## Drill
Take the quiz. MCQs test approach recognition and tradeoff analysis.

## Quiz: 01-css-landscape-2026

<p class="quiz-question">Which CSS approach for React has ZERO runtime cost in the browser?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> styled-components</p>

<p class="quiz-option"><strong>B.</strong> Emotion</p>

<p class="quiz-option"><strong>C.</strong> CSS Modules</p>

<p class="quiz-option"><strong>D.</strong> Runtime CSS-in-JS</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">CSS Modules are compiled at build time. Generated CSS file is loaded as static asset — no JavaScript runtime executes to apply styles.</p>

<hr/>

<p class="quiz-question">Your Next.js App Router app uses React Server Components. Which approach requires `'use client'` for every styled component?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> CSS Modules</p>

<p class="quiz-option"><strong>B.</strong> Tailwind CSS</p>

<p class="quiz-option"><strong>C.</strong> styled-components</p>

<p class="quiz-option"><strong>D.</strong> Vanilla Extract</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">Runtime CSS-in-JS (styled-components, Emotion) injects styles via JavaScript in browser — incompatible with RSC's server-only execution. Must use 'use client'.</p>

<hr/>

<p class="quiz-question">A teammate says 'I need CSS-in-JS to make styles dynamic based on props.' What's the correct response?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> True — only CSS-in-JS can read React props</p>

<p class="quiz-option"><strong>B.</strong> False — class composition with clsx achieves the same</p>

<p class="quiz-option"><strong>C.</strong> True — but only styled-components supports this</p>

<p class="quiz-option"><strong>D.</strong> False — inline styles are the only alternative</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Dynamic styles in React = conditional class toggling. clsx(styles.base, props.variant &amp;&amp; styles[props.variant]) works with any CSS approach and costs zero runtime.</p>

<hr/>

<p class="quiz-question">A team has 50 React components, Sass + BEM, migrating to Next.js App Router. They want to keep existing investment. Which approach fits best?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Rewrite everything in Tailwind</p>

<p class="quiz-option"><strong>B.</strong> Keep Sass for migrated pages, CSS Modules for new RSC components</p>

<p class="quiz-option"><strong>C.</strong> Switch to styled-components for SSR</p>

<p class="quiz-option"><strong>D.</strong> Convert all Sass to Vanilla Extract</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Incremental migration preserves existing Sass work. New RSC components use CSS Modules (zero-cost, RSC-compatible). Avoids full rewrite risk.</p>

<hr/>

<p class="quiz-question">Which approach is seeing growth in 2026 because it gives CSS-in-JJ syntax with zero runtime?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Styled-components</p>

<p class="quiz-option"><strong>B.</strong> Plain CSS</p>

<p class="quiz-option"><strong>C.</strong> Vanilla Extract</p>

<p class="quiz-option"><strong>D.</strong> Sass</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">Vanilla Extract reads .css.ts files at build time and outputs static CSS. TypeScript-first, zero runtime, RSC-compatible.</p>

<hr/>

<p class="quiz-question">What problem does the native `@scope` CSS rule solve?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Variable scoping in CSS</p>

<p class="quiz-option"><strong>B.</strong> Component-level CSS scoping without tooling</p>

<p class="quiz-option"><strong>C.</strong> Scoped animations</p>

<p class="quiz-option"><strong>D.</strong> Scoped font loading</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">@scope(.card) { ... } limits CSS rules to elements matching the scope root and its descendants — native scoping without CSS Modules or naming conventions.</p>

<hr/>

<p class="quiz-question">Approach A: 0 kB runtime, RSC-compatible, no auto-scoping. Approach B: 0 kB runtime, RSC-compatible, auto-scoped. Identify A and B.</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> A = Plain CSS, B = Tailwind</p>

<p class="quiz-option"><strong>B.</strong> A = Plain CSS, B = CSS Modules</p>

<p class="quiz-option"><strong>C.</strong> A = CSS Modules, B = Plain CSS</p>

<p class="quiz-option"><strong>D.</strong> A = Tailwind, B = Plain CSS</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Both have zero runtime. Plain CSS lacks auto-scoping (global by default). CSS Modules auto-generate unique class names. Tailwind has ~0.5 kB runtime for resets.</p>

<hr/>

<p class="quiz-question">Which decision axis matters MOST for choosing a CSS approach in 2026 React apps?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Syntax preference</p>

<p class="quiz-option"><strong>B.</strong> RSC / Server Component compatibility</p>

<p class="quiz-option"><strong>C.</strong> Number of colors available</p>

<p class="quiz-option"><strong>D.</strong> File extension</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">RSC compatibility cascades into runtime cost, bundle strategy, and component architecture. 2026 React is server-first; approaches that require client JS for styling lose most RSC benefits.</p>

<hr/>

<p class="quiz-question">How does zero-runtime CSS-in-JS differ from runtime CSS-in-JS in bundle impact?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Both add the same runtime</p>

<p class="quiz-option"><strong>B.</strong> Zero-runtime extracts styles to separate CSS files at build time; runtime injects via JS</p>

<p class="quiz-option"><strong>C.</strong> Runtime is smaller because it compresses styles</p>

<p class="quiz-option"><strong>D.</strong> Zero-runtime only works in development</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Runtime CSS-in-JS keeps style strings in JS bundle and injects via script. Zero-runtime generates static .css files during build, loaded separately — styles never touch JS bundle.</p>

<hr/>

<p class="quiz-question">You're building a React component library consumed by 5 internal apps. Which approach is most appropriate?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> styled-components (ThemeProvider for all apps)</p>

<p class="quiz-option"><strong>B.</strong> Tailwind (each app uses same config)</p>

<p class="quiz-option"><strong>C.</strong> Vanilla Extract (zero runtime, typed, CSS custom properties for theming)</p>

<p class="quiz-option"><strong>D.</strong> Global Sass (single stylesheet for all)</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">Component libraries should impose zero runtime cost on consumers. Vanilla Extract extracts at build time, enforces type safety, and CSS custom properties let consumers theme without dependency on a specific JS library.</p>

<hr/>

<p class="quiz-question">What is the recommended boundary rule for mixing CSS approaches in one app?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Use all approaches in every component</p>

<p class="quiz-option"><strong>B.</strong> One approach per component file — mixing happens at file import boundaries</p>

<p class="quiz-option"><strong>C.</strong> Never mix — pick one approach for the whole app</p>

<p class="quiz-option"><strong>D.</strong> Mix freely — build tools handle conflicts automatically</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Each component file uses exactly one CSS approach. Mixing happens at the architecture level: a Tailwind page imports CSS Module components. Never combine styled-components + CSS Modules + inline styles in one file.</p>

<hr/>

<p class="quiz-question">Your team wants to use Tailwind for layout and CSS Modules for complex widgets. Which combination pattern does this represent?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Runtime + zero-runtime hybrid</p>

<p class="quiz-option"><strong>B.</strong> Layer-based hybrid — each layer uses the best-fit approach</p>

<p class="quiz-option"><strong>C.</strong> Single-approach dogma</p>

<p class="quiz-option"><strong>D.</strong> Legacy-first architecture</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Layer model: global foundation (plain CSS) → layout (Tailwind) → component (CSS Modules) → override (className). Each layer's approach is chosen for its specific needs. Tailwind for speed, CSS Modules for isolation.</p>


---

# Module 2: Plain CSS & Sass in React

Est. study time: 2h
Language: en

## Learning Objectives
- Apply plain CSS and Sass in React while managing global namespace
- Design BEM naming that survives component architecture
- Use Sass mixins for React design tokens without runtime cost
- Evaluate when plain CSS/Sass is the right choice vs alternatives

---

## Core Content

### Global CSS in React — The Problem

React components encapsulate JSX and logic. CSS globals don't encapsulate — every rule targets the document.

```css
/* This affects EVERY button on the page */
button { background: blue; }
.card { padding: 16px; }
```

In a component tree, global CSS creates invisible coupling. Component A's `.card` styles affect Component B's `.card`. Fixing B breaks A.

> **Think**: You import a CSS file in ComponentA.tsx. Does ComponentB (sibling, no import) get those styles?
>
> *Answer: Yes. CSS in React is global by default. Import order matters for cascade but any imported CSS affects entire document regardless of which component imports it.*

### BEM as Namespacing Strategy

BEM (Block Element Modifier) is the primary way to namespace plain CSS:

```text
.block {}           /* Component scope */
.block__element {}  /* Child of component */
.block--modifier {} /* Variant of block */
```

In React, BEM block = component name:

```css
/* Button.css */
.button { display: inline-flex; }
.button__icon { margin-right: 8px; }
.button--primary { background: var(--color-primary); }
.button--large { padding: 12px 24px; }
```

```tsx
// Button.tsx
function Button({ variant, size, children }) {
  return (
    <button className={clsx(
      'button',
      variant && `button--${variant}`,
      size && `button--${size}`
    )}>
      {children}
    </button>
  );
}
```

**Tradeoff**: Pure string classes — no TypeScript checking for valid BEM names. Typo in `button--primari` silently applies nothing.

> **Think**: With plain CSS in React, how do you prevent a developer from accidentally using `.card` in a new component?
>
> *Answer: You can't — that's the limitation. Naming conventions (BEM, prefixing) mitigate but don't enforce. Code review catches it. CSS Modules or Tailwind solve this structurally.*

### Sass in React — What Works, What Doesn't

**Sass features that work well in React:**

- **Variables** → design tokens (`$color-primary: #0366d6`)
- **Mixins** → reusable style patterns (`@mixin truncate` → `@include truncate`)
- **Nesting** → component structure (`button { .icon { ... } }`)
- **Functions** → token calculations (`darken($color-primary, 10%)`)

**Sass features that conflict with React component model:**

- `@extend` — creates cross-component coupling. Component A extends B's selector → touching B can break A. Avoid.
- Deep nesting (>3 levels) — generates high-specificity selectors `.header .nav .list .item a`. Component isolation breaks.
- Loop-driven CSS generation — abstracts away what CSS is actually outputted. Debugging becomes guesswork.

> **Think**: Why is Sass `@extend` dangerous in a React component library?
>
> *Answer: @extend moves the selector to wherever the extended rule is defined. If Component A extends Component B's placeholder, now A depends on B's presence in the cascade. Removing B breaks A unexpectedly. Copy-paste the styles instead.*

### Design Tokens as Sass Variables

Sass variables make excellent design tokens because they compile to static values — zero runtime.

```scss
// _tokens.scss
$color-primary: #0366d6;
$color-danger: #d73a49;
$space-xs: 4px;
$space-sm: 8px;
$space-md: 16px;
$radius-sm: 4px;
$radius-md: 8px;
$font-body: 16px;
$font-heading: 24px;
```

```scss
// Button.scss
@use 'tokens' as t;

.button {
  padding: t.$space-sm t.$space-md;
  font-size: t.$font-body;
  border-radius: t.$radius-sm;
}
```

This compiles to static CSS — same as writing `padding: 8px 16px`. No variables in output, no JS needed.

**Limitation**: Tokens are compile-time only. Runtime theme switching requires CSS custom properties (Module 8).

> **Think**: You have Sass variables for colors. User clicks "dark mode". How do you change all `$color-bg` values?
>
> *Answer: You can't — Sass compiles away. Runtime theme switching needs CSS custom properties (`var(--color-bg)`) which are live in the browser. Sass for static tokens + CSS custom properties for dynamic.*

### When Plain CSS/Sass Fits React

**Good fit:**
- Legacy app with established Sass codebase
- Global styles (reset, typography, fonts)
- Animation keyframes (shared across components)
- Print stylesheets
- Single-page app with no SSR concerns
- All team members know Sass, don't know CSS Modules

**Bad fit:**
- RSC-first app (import order unpredictable in RSC)
- Large team (20+ devs) — naming collisions inevitable
- Component library consumed externally — consumers get global styles
- Any app where "this CSS affects that component" happens monthly

> **Think**: How would you import a global CSS file in a Next.js App Router app?
>
> *Answer: Only in `layout.tsx` or `app/globals.css`. Next.js App Router restricts global CSS to root layout — no per-page global CSS. Component-level CSS must use CSS Modules or Tailwind.*

---

### Why This Matters

Plain CSS is the simplest setup but doesn't scale in component architecture. Most developers start here and migrate when naming collisions surface. Understanding BEM and Sass integration means you can work in legacy codebases and make deliberate migration decisions rather than fighting the cascade.

---

### Common Questions

**Q: Can I use Sass with Next.js or Vite?**
A: Yes. Next.js has built-in Sass support (`npm install sass`). Vite supports `.scss` files with `sass` dependency. Both compile to CSS at build.

**Q: Should I use Sass in a new React project in 2026?**
A: If team loves Sass and has no RSC concerns, yes. But Tailwind or CSS Modules are more common for new projects. Sass is increasingly a "mature codebase" choice.

**Q: Does CSS custom properties replace Sass variables entirely?**
A: No. Sass variables compile to static values — they ensure final CSS has no variable indirection. Custom properties are dynamic (runtime-evaluated). Use Sass for build-time constants, custom properties for runtime theme values.

---

## Examples

### Example 1: BEM + Sass in a Button Component

```scss
// styles/buttons.scss
@use '../tokens' as *;

.button {
  display: inline-flex;
  align-items: center;
  gap: $space-sm;
  padding: $space-sm $space-md;
  border: 1px solid transparent;
  border-radius: $radius-sm;
  cursor: pointer;

  &__icon {
    width: 16px;
    height: 16px;
  }

  &--primary {
    background: $color-primary;
    color: white;
  }

  &--outline {
    background: transparent;
    border-color: $color-primary;
    color: $color-primary;
  }

  &--large {
    padding: $space-md $space-lg;
    font-size: 18px;
  }
}
```

```tsx
// Button.tsx
import './styles/buttons.scss';

type Variant = 'primary' | 'outline';
type Size = 'default' | 'large';

function Button({ variant = 'primary', size = 'default', children }) {
  const className = clsx(
    'button',
    `button--${variant}`,
    size !== 'default' && `button--${size}`
  );
  return <button className={className}>{children}</button>;
}
```

### Example 2: Global Stylesheet Layout

```scss
// styles/global.scss
@use 'tokens' as *;

*, *::before, *::after { box-sizing: border-box; }

body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: $font-body;
  color: $color-text;
  background: $color-bg;
}

h1, h2, h3 { margin: 0; line-height: 1.2; }
```

```tsx
// app/layout.tsx (Next.js App Router)
import './styles/global.scss';

export default function RootLayout({ children }) {
  return (
    <html>
      <body>{children}</body>
    </html>
  );
}
```

---

## Key Takeaways
- Plain CSS in React is globally scoped — naming collisions are the main scaling problem
- BEM provides namespacing but no enforcement — typos produce silent failures
- Sass mixins and variables are good for static design tokens
- Avoid Sass `@extend` in React — creates invisible cross-component coupling
- Import global CSS only in root layout (Next.js App Router) or `index.tsx`
- Plain CSS/Sass best for: legacy codebases, global styles, animation keyframes
- Worst for: RSC apps, large teams, external component libraries

---

## Common Misconception

**"Sass nesting mirrors React component nesting, so it's fine to nest deeply."**

```scss
// Bad — 5 levels deep, high specificity
.card {
  .header {
    .title {
      .icon {
        ...  // specificity: .card .header .title .icon
      }
    }
  }
}
```

React component structure should flatten CSS. A `CardHeader` component gets its own styles. Deep nesting creates specificity arms race — later components need `!important` to override.

**Correct approach**: One level of nesting per component. If nesting exceeds 3 levels, extract a child component.

---

## Feynman Explain
(Explain to a junior developer: "Why can't I just write CSS in one big file and import it in React?")


---

## Reframe
(Pause. Judge: Is BEM worth the effort in 2026? CSS Modules and Tailwind solve the same problem structurally. For which apps is BEM still the best answer?)

---

## Drill
Take the quiz to test BEM naming and Sass tradeoffs.

## Quiz: 02-plain-css-sass-react

<p class="quiz-question">In React, importing a CSS file in ComponentA.tsx affects:</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Only ComponentA</p>

<p class="quiz-option"><strong>B.</strong> ComponentA and its children</p>

<p class="quiz-option"><strong>C.</strong> The entire page/document</p>

<p class="quiz-option"><strong>D.</strong> Only sibling components</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">CSS in React is globally scoped regardless of which import triggers the load. Any CSS import affects the entire document.</p>

<hr/>

<p class="quiz-question">What does BEM's double underscore (__) represent?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> A modifier variant</p>

<p class="quiz-option"><strong>B.</strong> An element (child of block)</p>

<p class="quiz-option"><strong>C.</strong> A nested block</p>

<p class="quiz-option"><strong>D.</strong> A CSS pseudo-class</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">BEM convention: block__element. Example: button__icon means 'icon element inside button block'. block--modifier for variants.</p>

<hr/>

<p class="quiz-question">Which Sass feature creates invisible cross-component coupling in React?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Mixins</p>

<p class="quiz-option"><strong>B.</strong> Variables</p>

<p class="quiz-option"><strong>C.</strong> @extend</p>

<p class="quiz-option"><strong>D.</strong> Nesting</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">@extend moves selectors to the extended rule's location. If Component A extends a placeholder from Component B's stylesheet, removing B breaks A. Styles become non-local.</p>

<hr/>

<p class="quiz-question">A Sass variable $color-primary: #0366d6 is defined. How does it appear in the browser's final CSS?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> As $color-primary preserved in CSS</p>

<p class="quiz-option"><strong>B.</strong> As var(--color-primary)</p>

<p class="quiz-option"><strong>C.</strong> As the compiled value #0366d6</p>

<p class="quiz-option"><strong>D.</strong> Undefined — Sass doesn't compile</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">Sass variables are compile-time only. They get replaced with their literal value during build. Browser sees #0366d6, not $color-primary.</p>

<hr/>

<p class="quiz-question">In Next.js App Router, where should global CSS be imported?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Any page.tsx</p>

<p class="quiz-option"><strong>B.</strong> Any component.tsx</p>

<p class="quiz-option"><strong>C.</strong> Only root layout.tsx</p>

<p class="quiz-option"><strong>D.</strong> Only app/global.css</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">App Router restricts global CSS imports to the root layout. Per-page global CSS is not supported — component CSS must be scoped (CSS Modules) or utility-based (Tailwind).</p>

<hr/>

<p class="quiz-question">Which scenario is a GOOD fit for plain CSS/Sass in React?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Component library consumed by 10 external apps</p>

<p class="quiz-option"><strong>B.</strong> Large team (30 devs) building new features daily</p>

<p class="quiz-option"><strong>C.</strong> Legacy codebase with existing Sass design tokens</p>

<p class="quiz-option"><strong>D.</strong> RSC-first greenfield Next.js app</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">Legacy codebases with Sass investment benefit from incremental migration. New apps, large teams, library distribution, and RSC apps benefit from scoped CSS approaches.</p>

<hr/>

<p class="quiz-question">CSS specificity: .card .header .title .icon { color: blue; }. What specificity value is this?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> 0,1,0,0</p>

<p class="quiz-option"><strong>B.</strong> 0,4,0,0</p>

<p class="quiz-option"><strong>C.</strong> 0,0,4,0</p>

<p class="quiz-option"><strong>D.</strong> 0,1,4,0</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">Four classes = 0,0,4,0 (0 inline, 0 IDs, 4 classes, 0 elements). Deep nesting generates high specificity that later rules struggle to override without !important.</p>

<hr/>

<p class="quiz-question">You need runtime theme switching (light/dark). Can Sass variables handle this alone?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Yes — Sass compiles to CSS, browser reads variables</p>

<p class="quiz-option"><strong>B.</strong> No — Sass compiles away, cannot change at runtime</p>

<p class="quiz-option"><strong>C.</strong> Yes — use @media prefers-color-scheme</p>

<p class="quiz-option"><strong>D.</strong> No — Sass only works in development</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Sass variables are replaced with static values at build time. Runtime theme switching needs CSS custom properties (var(--color-bg)) which browser evaluates live.</p>

<hr/>

<p class="quiz-question">A dev writes button { padding: 8px 16px; } in a global stylesheet. Which problem occurs first at scale?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Performance — selector is too specific</p>

<p class="quiz-option"><strong>B.</strong> Naming collision — another .button rule overrides unexpectedly</p>

<p class="quiz-option"><strong>C.</strong> Syntax error — padding shorthand not supported</p>

<p class="quiz-option"><strong>D.</strong> React re-renders on every style change</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Global .button class affects every component rendering a button. Another component's .button style overrides via cascade order. No isolation means collisions are inevitable with scale.</p>

<hr/>

<p class="quiz-question">What's the recommended nesting depth limit for Sass in React components?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> No limit — use as many levels as component tree</p>

<p class="quiz-option"><strong>B.</strong> Maximum 1 level per component</p>

<p class="quiz-option"><strong>C.</strong> Maximum 3 levels per component</p>

<p class="quiz-option"><strong>D.</strong> Maximum 5 levels per component</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Sass nesting reflects CSS specificity, not component hierarchy. One level per component keeps specificity low. Exceeding 3 levels indicates you need a child component, not deeper nesting.</p>


---

# Module 3: CSS Modules in React

Est. study time: 2.5h
Language: en

## Learning Objectives
- Use CSS Modules in React with TypeScript integration
- Compose classes and handle dynamic variants
- Apply CSS Modules in Next.js and Vite

---

## Core Content

### How CSS Modules Work

CSS Modules transform class names at build time. Each file `*.module.css` produces an export object mapping original names to unique generated names.

```css
/* Button.module.css */
.base { padding: 8px 16px; }
.primary { background: blue; }
```

Compiles to:

```css
/* Output */
.Button_base_1a2b3 { padding: 8px 16px; }
.Button_primary_4d5e6 { background: blue; }
```

React imports use the mapping object:

```tsx
import styles from './Button.module.css';

function Button() {
  return <button className={styles.base}>Click</button>;
  // Renders: <button class="Button_base_1a2b3">Click</button>
}
```

> **Think**: What happens if two CSS Module files both define `.base`?
>
> *Answer: No conflict. Each generates unique class names scoped to its file. `.base` in Button.module.css → `.Button_base_1a2b3`. `.base` in Card.module.css → `.Card_base_7f8g9`.*

### TypeScript Integration

CSS Modules aren't TypeScript-aware by default — `styles.base` is typed as `string`, not `'base' | 'primary'`. Enable typed class names:

**Next.js**: built-in. No config.

**Vite**: `vite-plugin-lsc` or TypeScript plugin.

**Manual**: declare module:

```typescript
// src/types/css-modules.d.ts
declare module '*.module.css' {
  const classes: { readonly [key: string]: string };
  export default classes;
}
```

For strict typed modules per file, use `typed-scss-modules` or generate `.module.css.d.ts`:

```typescript
// Button.module.css.d.ts (auto-generated)
export const base: string;
export const primary: string;
export const disabled: string;
```

Then `styles.base` is typed as `string`, but if the key doesn't exist, TypeScript errors.

> **Think**: Why would you want strict typing on CSS Module imports?
>
> *Answer: Catch typos at compile time instead of runtime. `styles.primari` → TypeScript error. Without typing, it's `undefined` → no class applied → silent visual bug.*

### Dynamic Classes with CSS Modules

CSS Modules return strings. Dynamic variants use class composition:

```tsx
import styles from './Button.module.css';
import clsx from 'clsx';

function Button({ variant, disabled }) {
  return (
    <button className={clsx(
      styles.base,
      variant === 'primary' && styles.primary,
      variant === 'outline' && styles.outline,
      disabled && styles.disabled
    )}>
      Click
    </button>
  );
}
```

Pattern: base class always present + conditional variant classes.

**Inline styles for truly dynamic values**:

```tsx
function ProgressBar({ percent }) {
  return (
    <div className={styles.track}>
      <div
        className={styles.fill}
        style={{ width: `${percent}%` }}
      />
    </div>
  );
}
```

Static styles → CSS Module. Dynamic runtime values (position, dimension, color from data) → inline `style` prop.

> **Think**: When should you NOT use CSS Modules for dynamic styles?
>
> *Answer: When the value is runtime-computed (API response, user input, animation progress). CSS Modules are build-time static. For truly dynamic values, inline `style` prop or CSS custom properties are correct.*

### Composition Pattern

CSS Modules support `composes` to reuse styles within the same file:

```css
/* Typography.module.css */
.heading {
  font-weight: 700;
  line-height: 1.2;
}
.headingLarge {
  composes: heading;
  font-size: 24px;
}
```

In React, `composes` is transparent — both class names appear in the DOM:

```tsx
<h1 className={styles.headingLarge}>
  {/* Renders: class="Typography_headingLarge_abc Typography_heading_123" */}
</h1>
```

**When to use `composes`**: Shared base styles within a component file. Avoid cross-file `composes` — it creates coupling similar to Sass `@extend`.

### CSS Modules in Next.js

Next.js App Router uses CSS Modules by default:

```tsx
// app/page.tsx
import styles from './page.module.css';

export default function Page() {
  return <main className={styles.main}>...</main>;
}
```

**Rules:**
- Global CSS only in `app/globals.css` (imported via `layout.tsx`)
- Component CSS always `*.module.css`
- `app/page.module.css` is scoped to `app/page.tsx`
- CSS Modules work in both Server and Client components

```tsx
// Works in RSC — no JavaScript dependency
import styles from './Card.module.css';

export default function Card({ title }) {
  return <div className={styles.card}>{title}</div>;
}
```

### CSS Modules in Vite

Vite supports CSS Modules natively — file naming `*.module.css` triggers module mode.

```tsx
// Vite — same API as Next.js
import styles from './Button.module.css';

// Vite-specific: CSS Modules + PostCSS
// postcss.config.js works with CSS Modules for nesting, autoprefixer
```

Vite also supports `.module.scss` and `.module.less` (Out of the box for Sass). Same scoping mechanism.

### Limitations

1. **Dynamic style computation** — requires inline styles or CSS custom properties
2. **No runtime theme access** — can't read `props.theme` like styled-components
3. **File per component** — 1 CSS file per React component (convention, not requirement)
4. **No prop-driven style logic** — conditions handled via `clsx` in JSX
5. **Global class interop** — third-party CSS (e.g., animation library) requires `:global` directive

```css
/* Apply global class from animation library */
.card {
  composes: animate__fadeIn from global;
}
```

> **Think**: CSS Modules are often called "the boring choice" for React styling. Why is boring a strength?
>
> *Answer: Zero runtime, zero dependencies, works with every React paradigm (RSC, SSR, SPA), standard CSS syntax, no vendor lock-in. Boring = stable, well-understood, always works.*

---

### Why This Matters

CSS Modules are the default in both Next.js and Vite — the two dominant React frameworks. Understanding them means understanding the default styling mechanism for most React apps in 2026. They're also the foundation that Tailwind and zero-runtime CSS-in-JS build on (both generate CSS Modules under the hood in many setups).

---

### Common Questions

**Q: Can I use Sass syntax with CSS Modules?**
A: Yes. `.module.scss` files work identically — compile Sass with scoped class names.

**Q: How do I style a child component from a parent?**
A: Pass the class name as a prop or use `:global`:

```tsx
// Parent passes class
<Child className={styles.childOverride} />

// Or in CSS Module: target child class globally
.parent :global(.child-class) { ... }
```

**Q: Do CSS Modules affect SSR or hydration?**
A: No. Class names are deterministic based on build. Server and client generate identical class names.

---

## Examples

### Example 1: Multi-Variant Button

```css
/* Button.module.css */
.button {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border: 1px solid transparent;
  border-radius: 6px;
  cursor: pointer;
  transition: background 0.15s;
}
.primary { background: #0366d6; color: white; }
.outline { background: transparent; border-color: #0366d6; color: #0366d6; }
.small { padding: 4px 8px; font-size: 14px; }
.large { padding: 12px 24px; font-size: 18px; }
.disabled { opacity: 0.5; pointer-events: none; }
```

```tsx
// Button.tsx
import styles from './Button.module.css';
import clsx from 'clsx';

type ButtonProps = {
  variant?: 'primary' | 'outline';
  size?: 'small' | 'default' | 'large';
  disabled?: boolean;
};

function Button({ variant = 'primary', size = 'default', disabled, children }: ButtonProps) {
  return (
    <button className={clsx(
      styles.button,
      styles[variant],
      size !== 'default' && styles[size],
      disabled && styles.disabled
    )}>
      {children}
    </button>
  );
}
```

### Example 2: Themed Card via CSS Custom Properties

```css
/* Card.module.css */
.card {
  background: var(--card-bg, white);
  border: 1px solid var(--card-border, #e1e4e8);
  border-radius: 8px;
  padding: 16px;
}
.title {
  font-size: 18px;
  color: var(--card-title, #24292f);
}
```

```tsx
// Card.tsx
import styles from './Card.module.css';

function Card({ title, children, themeClass }) {
  return (
    <div className={clsx(styles.card, themeClass)}>
      <h3 className={styles.title}>{title}</h3>
      {children}
    </div>
  );
}

// Consumer:
<div className="dark-theme">
  <Card title="Hello" />
</div>
```

---

## Key Takeaways
- CSS Modules generate unique class names per file — zero specificity conflicts
- Import as object: `import styles from './Component.module.css'`
- Dynamic variants via `clsx(styles.base, condition && styles.variant)`
- TypeScript typing available via `.d.ts` generation
- Build-time only — no runtime cost, RSC-compatible
- CSS Modules are the default styling mechanism in Next.js and Vite
- Limitations: no dynamic style computation, no prop-driven theming (use CSS custom properties)

---

## Common Misconception

**"CSS Modules are just like plain CSS with extra build steps."**

They look like plain CSS but behave differently:
- Class names are local by default, not global
- `:global(.selector)` explicitly escapes to global scope
- `composes` provides style reuse without Sass `@extend`
- File naming convention (`*.module.css`) activates module behavior
- Build tools generate unique hashes per class

They feel like plain CSS but provide component isolation.

---

## Feynman Explain
(Explain CSS Modules to someone who only knows global CSS. Focus on: why class names get hashed, how imports map, why this prevents conflicts.)

---

## Reframe
(Pause. Judge: CSS Modules are the "default path" in 2026. When would you deliberately NOT use them? What gaps force you to reach for another approach?)

---

## Drill
Take the quiz. Questions cover imports, composition, dynamic classes, and integration.

## Quiz: 03-css-modules-react

<p class="quiz-question">What does importing a CSS Module file produce?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> A string of CSS</p>

<p class="quiz-option"><strong>B.</strong> An object mapping original class names to unique generated names</p>

<p class="quiz-option"><strong>C.</strong> A StyleSheet object</p>

<p class="quiz-option"><strong>D.</strong> Nothing — CSS Modules have no import value</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">CSS Modules compile each file to an exports object: { originalName: 'File_originalName_hash' }. React uses this object for scoped class references.</p>

<hr/>

<p class="quiz-question">How do you apply a conditional variant in CSS Modules?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Inline style — style={{ variant: 'primary' }}</p>

<p class="quiz-option"><strong>B.</strong> clsx(styles.base, isPrimary &amp;&amp; styles.primary)</p>

<p class="quiz-option"><strong>C.</strong> styles['variant-primary']</p>

<p class="quiz-option"><strong>D.</strong> CSS Module object spread</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">CSS Modules export strings. Combine with clsx for conditional class composition — same pattern as plain CSS but using scoped class names.</p>

<hr/>

<p class="quiz-question">In Next.js App Router, where can you import a CSS Module?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Only in layout.tsx</p>

<p class="quiz-option"><strong>B.</strong> Any Server or Client component</p>

<p class="quiz-option"><strong>C.</strong> Only Client components</p>

<p class="quiz-option"><strong>D.</strong> Only page.tsx files</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">CSS Modules work in both Server and Client components because they are build-time only — no JavaScript runtime needed, no 'use client' required.</p>

<hr/>

<p class="quiz-question">Two files — Button.module.css and Card.module.css — both define class .base. What happens?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Build error — duplicate class names</p>

<p class="quiz-option"><strong>B.</strong> Last imported wins (cascade)</p>

<p class="quiz-option"><strong>C.</strong> No conflict — each gets unique hashed name</p>

<p class="quiz-option"><strong>D.</strong> Runtime error when both render</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">CSS Modules generate unique class names per file. .base in Button → .Button_base_hash1. .base in Card → .Card_base_hash2. No cascade conflict.</p>

<hr/>

<p class="quiz-question">How do you apply a truly dynamic value (e.g., progress bar width from API) with CSS Modules?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Generate CSS Module at runtime</p>

<p class="quiz-option"><strong>B.</strong> Use inline style prop: style={{ width: `${percent}%` }}</p>

<p class="quiz-option"><strong>C.</strong> Use composes with dynamic value</p>

<p class="quiz-option"><strong>D.</strong> CSS Modules cannot handle this — switch to CSS-in-JS</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">CSS Modules are build-time static. Dynamic runtime values (position, size, color from data) belong in inline style prop. CSS Modules for structural/static classes.</p>

<hr/>

<p class="quiz-question">What does CSS Modules `composes` do?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Compiles multiple CSS files into one</p>

<p class="quiz-option"><strong>B.</strong> Applies another class from the same file alongside the current one</p>

<p class="quiz-option"><strong>C.</strong> Combines two components' styles</p>

<p class="quiz-option"><strong>D.</strong> Creates a CSS variable reference</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">composes: heading; in .headingLarge adds .heading class alongside .headingLarge in the DOM. In-file reuse only — avoid cross-file composes.</p>

<hr/>

<p class="quiz-question">What's the difference between `import './styles.css'` and `import styles from './Component.module.css'`?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> First imports globally, second imports scoped with object mapping</p>

<p class="quiz-option"><strong>B.</strong> Both import the same — just different file extension</p>

<p class="quiz-option"><strong>C.</strong> First is for CSS Modules, second for plain CSS</p>

<p class="quiz-option"><strong>D.</strong> No difference — both are global</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">Plain CSS import adds global rules. CSS Module import returns scoped class mapping object. Different syntax, different scoping behavior.</p>

<hr/>

<p class="quiz-question">You need to style a child that's rendered by a different component. Which CSS Modules approach works?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Parent targets child's CSS Module class via :global</p>

<p class="quiz-option"><strong>B.</strong> Parent passes className prop to child</p>

<p class="quiz-option"><strong>C.</strong> Use composes from parent's module</p>

<p class="quiz-option"><strong>D.</strong> All of the above are valid approaches</p>

<p class="quiz-answer"><strong>Answer:</strong> D</p>

<p class="quiz-explanation">(A) :global(.child-class) targets child's class globally. (B) Passing className as prop is the React-recommended composition approach. (C) composes only works within same file. A and B are practical.</p>

<hr/>

<p class="quiz-question">A large app uses CSS Modules. Team finds .module.css files growing repetitive. Which solution aligns with CSS Modules philosophy?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Switch to styled-components</p>

<p class="quiz-option"><strong>B.</strong> Extract shared styles into base CSS Module files and use composes</p>

<p class="quiz-option"><strong>C.</strong> Use Sass @mixin across modules</p>

<p class="quiz-option"><strong>D.</strong> Inline all styles</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Shared CSS Module base files with composes for reuse — keeps zero runtime, stays within CSS Modules paradigm. Avoids dependency on CSS-in-JS runtime.</p>

<hr/>

<p class="quiz-question">True or False: CSS Modules cannot be used with React Server Components because they need client-side JavaScript.</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> True — CSS Modules require JS to resolve</p>

<p class="quiz-option"><strong>B.</strong> False — CSS Modules are build-time only, work in RSC</p>

<p class="quiz-option"><strong>C.</strong> True — only Tailwind works in RSC</p>

<p class="quiz-option"><strong>D.</strong> False — but only in Next.js</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">CSS Modules compile to static CSS at build time. No JavaScript executes for style resolution. Fully compatible with RSC in any framework.</p>


---

# Module 4: Runtime CSS-in-JS (styled-components) in React

Est. study time: 2.5h
Language: en

## Learning Objectives
- Understand runtime CSS-in-JS mechanism and bundle cost
- Implement ThemeProvider pattern in React
- Evaluate RSC compatibility and SSR hydration
- Make informed 2026 decision about runtime CSS-in-JS

---

## Core Content

### How Runtime CSS-in-JS Works

Runtime CSS-in-JS (styled-components, Emotion) generates `<style>` elements at runtime. Every component render that changes styles triggers re-parsing.

Flow:
1. `styled.button` called — parses template literal CSS string
2. Generates unique class name (e.g., `sc-bdVaJa`)
3. Creates CSS rule string
4. Injects `<style>` tag into `<head>` (or appends to existing style tag)
5. Returns component with generated class

```tsx
// What you write:
const Button = styled.button`
  padding: 8px 16px;
  color: ${p => p.$variant === 'danger' ? 'red' : 'blue'};
`;

// What runs:
// 1. Parse template string with interpolated values
// 2. Hash to class name: sc-bdVaJa
// 3. Inject: <style>[data-styled="active"] .sc-bdVaJa { padding: 8px 16px; color: red; }</style>
// 4. Render: <button class="sc-bdVaJa">
```

> **Think**: Every time `$variant` changes, what happens to the injected styles?
>
> *Answer: styled-components generates a new class for each unique prop combination. If variant toggles between 'danger' and 'default', two style rules exist in DOM. CSS is never removed — it accumulates. Over many combinations, the style tag grows unbounded.*

### Bundle Cost Breakdown

Runtime CSS-in-JS adds two cost layers:

**1. Library runtime (~12-15 kB gzip)**

This is the JS engine that parses CSS strings, generates classes, and manages injection. Ships with every bundle — even pages with zero styled components pay for it if tree-shaking fails.

**2. Styled component definitions in JS bundle**

Each `styled.button\`...\`` is a JavaScript tagged template expression. The CSS string lives in the JS bundle:

```text
Component A: "padding: 8px; color: blue;" → ~10kB source → ~3kB gzip in JS bundle
Component B: "padding: 16px; color: red;" → ~10kB source → ~3kB gzip in JS bundle
```

These strings could be in a `.css` file at zero bundle cost. With runtime CSS-in-JS, they ship as JS.

**Comparison for 100-component app:**
- CSS Modules: 0 kB runtime, ~15 kB CSS (separate file)
- styled-components: ~14 kB runtime + ~30 kB CSS strings in JS = ~44 kB

> **Think**: What happens to CSS bundle if a component is lazy-loaded with React.lazy?
>
> *Answer: styled-components injects into the global style tag — lazy loading doesn't isolate component styles. All styles merge into one growing style element. CSS Modules naturally code-split: lazy component's CSS loads only when the chunk loads.*

### ThemeProvider in React

styled-components uses React Context for theme propagation:

```tsx
import { ThemeProvider } from 'styled-components';

const theme = {
  colors: {
    primary: '#0366d6',
    background: '#ffffff',
  },
  space: { sm: '8px', md: '16px' },
};

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Button />
    </ThemeProvider>
  );
}

// Button reads theme via props:
const Button = styled.button`
  background: ${p => p.theme.colors.primary};
  padding: ${p => p.theme.space.sm};
`;
```

Theme object is accessible in every styled component via `props.theme`. Theme changes trigger re-render of all consuming components.

**Tradeoff**: ThemeProvider couples every styled component to React Context. Your design system cannot work without a wrapping `<ThemeProvider>`. Consumers of your component library must install styled-components and wrap their app.

### SSR Hydration and RSC

**SSR problem**: styled-components generates class names differently on server vs client unless server-side rendering is configured with `StyleSheetManager` and server-side sheet extraction.

```tsx
// Next.js Pages Router needs:
import { ServerStyleSheet } from 'styled-components';
// Custom _document.tsx to collect and inject styles
// Without this: FOUC (flash of unstyled content) on every page load
```

**RSC incompatibility**: styled-components uses `createContext`, hooks, and DOM API — all unavailable in Server Components. Every styled component needs `"use client"`.

```tsx
"use client"; // Required for RSC
import styled from 'styled-components';

const Button = styled.button`
  padding: 8px;
`;

// This component cannot be a Server Component
// Its entire JS bundle ships to the client
```

> **Think**: In a Next.js App Router app with 80% RSC and 20% client components, where do styled components end up?
>
> *Answer: Forced into the 20% client bundle. You can't use styled components in your server-rendered product listing (80% of the app). They only work inside the "use client" boundary.*

### When Runtime CSS-in-JS Still Makes Sense in 2026

Four specific scenarios where the cost is worth paying:

**1. Existing codebase (500+ styled components)**

Migration cost dominates. Rewriting 500 styled components to CSS Modules saves ~14 kB runtime but costs weeks of engineering. For a mature app with no bundle size crisis, the ROI is negative. Strategy: stop using styled-components for new components (use CSS Modules/Tailwind). Replace old components opportunistically during feature work.

**2. Electron / desktop apps**

No SSR, no RSC, no slow networks. The runtime tax (14 kB in a 50 MB Electron bundle) is noise. Dynamic theming via prop interpolation is genuinely convenient. styled-components performs fine here.

**3. Design system with extreme variant counts (100+ variants)**

When a component has 100+ variant combinations (icon + size + color + state + density + border), runtime CSS-in-JS's dynamic class generation is simpler than maintaining CSS Modules with clsx chains. Evaluate Vanilla Extract recipes first — only fall back to runtime if the variant composability needs exceed what recipe() provides.

**4. Rapid prototype → production path where team already owns the cost**

If the prototype was built in styled-components and the team understands the tradeoffs (no RSC, SSR config needed), shipping as-is beats a rewrite. Accept the runtime cost as a known liability — document it for future migration.

**Scenarios where runtime CSS-in-JS is the WRONG choice:**

| Scenario | Why it fails |
|----------|-------------|
| New Next.js App Router app with RSC | Every styled component forces `"use client"` — defeats server components |
| Component library for external consumers | Forces all consumers to install styled-components as peer dependency |
| Performance-sensitive public-facing app | 14 kB runtime + CSS strings in JS bundle delays FCP on slow networks |
| Team doesn't know CSS-in-JS | Learning curve + legacy lock-in — team will be stuck maintaining it |
| SSR-heavy app without SSR config | FOUC on every page load until ServerStyleSheet is configured |

> **Think**: The CTO says "we use styled-components company-wide." You're starting a new product. Do you use it?
>
> *Answer: Depends. If the product uses App Router / RSC: push back — runtime CSS-in-JS forces client components, defeating RSC benefits. If SPA with no SSR: acceptable, bundle cost is the main concern.*

### Cost-Benefit Analysis for Legacy Migration

When deciding whether to migrate away from runtime CSS-in-JS:

| Factor | Favor migration | Favor staying |
|--------|---------------|--------------|
| Component count | <200 components | >500 components |
| RSC adoption | Planning to use App Router | Staying on Pages Router |
| Bundle size pain | CSS strings inflating JS bundle | Bundle is within budget |
| Team size | Small team, can refactor | Large team, coordination cost high |
| Performance budget | Sub-100kB FCP target | No strict performance budget |

**Incremental migration strategy:**
1. Stop using runtime CSS-in-JS for new components
2. Extract design tokens → CSS custom properties
3. Replace one leaf component at a time (leaf → parent → grandparent)
4. Remove runtime library when zero imports remain

This avoids the "big bang" rewrite while gradually eliminating the runtime cost.

### Emotion vs styled-components

| Aspect | styled-components | Emotion |
|--------|------------------|---------|
| Bundle | ~14 kB gzip | ~11 kB gzip |
| API | `styled.tag` only | `styled.tag` + `css` prop |
| SSR | Requires config | Better out-of-box |
| RSC | Incompatible | Incompatible |
| Community | Larger, more resources | Smaller, but actively maintained |
| 2026 trend | Declining new usage | Declining new usage |

Both face same fundamental limitation: runtime style injection is antithetical to React's RSC direction.

---

### Why This Matters

Runtime CSS-in-JS was the dominant approach from 2018-2022. Many existing codebases use it. Understanding its internals and costs helps you maintain legacy apps, evaluate migration, and defend decisions against "but styled-components is what we've always used."

---

### Common Questions

**Q: Does styled-components tree-shake unused components?**
A: Partially. The runtime library (~14 kB) tree-shakes poorly because it's a single module. Individual styled components tree-shake if not imported — but the runtime stays.

**Q: Can I use styled-components with Tailwind?**
A: You *can*, but mixing patterns is confusing. Each component uses one approach. Don't combine within one file.

**Q: What's the migration path from styled-components to zero-cost CSS?**
A: Incremental: new components use CSS Modules or Tailwind. Extract shared design tokens as CSS custom properties. Replace one component at a time. No rewrite.

---

## Examples

### Example 1: Themed Button

```tsx
import styled, { css } from 'styled-components';

const variants = {
  primary: css`background: #0366d6; color: white;`,
  danger: css`background: #d73a49; color: white;`,
  ghost: css`background: transparent; color: #0366d6;`,
};

const sizes = {
  small: css`padding: 4px 8px; font-size: 14px;`,
  large: css`padding: 12px 24px; font-size: 18px;`,
};

const Button = styled.button<{
  $variant?: keyof typeof variants;
  $size?: keyof typeof sizes;
}>`
  display: inline-flex;
  align-items: center;
  border: 1px solid transparent;
  border-radius: 6px;
  cursor: pointer;
  ${p => p.$variant && variants[p.$variant]}
  ${p => p.$size && sizes[p.$size]}
`;

function App() {
  return (
    <ThemeProvider theme={appTheme}>
      <Button $variant="primary" $size="large">Submit</Button>
      <Button $variant="ghost">Cancel</Button>
    </ThemeProvider>
  );
}
```

### Example 2: Migration Pattern (styled → CSS Module)

**Before:**
```tsx
const Card = styled.div`
  padding: 16px;
  background: ${p => p.theme.colors.surface};
  border-radius: 8px;
`;
```

**After:**
```tsx
import styles from './Card.module.css';

// Theme tokens → CSS custom properties on root (handled once)
function Card({ children }) {
  return <div className={styles.card}>{children}</div>;
}
```

Theming moves from ThemeProvider to CSS custom properties — same runtime cost, zero library dependency.

---

## Key Takeaways
- Runtime CSS-in-JS injects `<style>` at runtime — ~12-15 kB library + CSS strings in JS bundle
- ThemeProvider uses React Context — couples library to consumers
- RSC incompatible — every styled component needs `"use client"`
- SSR requires extra configuration to prevent FOUC
- Declining for greenfield 2026 — replaced by zero-runtime, CSS Modules, Tailwind
- Valid for: legacy codebases (500+ components), electron apps, extreme variants (100+)
- Wrong for: new RSC apps, component libraries, perf-sensitive public apps
- Migration: incremental — new components use zero-cost approach, replace leaf components first

---

## Common Misconception

**"styled-components has zero runtime cost because it generates static CSS at build."**

False. styled-components and Emotion are runtime engines.
- Tagged template literal `styled.button\`...\`` executes in browser
- CSS string parsing happens on every mount
- Style injection manipulates DOM
- Library runtime ships to every client

Zero-runtime CSS-in-JS (Vanilla Extract, Linaria) is the build-time approach. The names are confusing — distinguish by "does it execute in the browser?"

---

## Feynman Explain
(Explain why runtime CSS-in-JS costs more than it seems. Include: bundle size, SSR setup, RSC restriction, DOM injection.)

---

## Reframe
(Pause. Judge: would you start a new React project with styled-components in 2026? What would convince you otherwise?)

---

## Drill
Take the quiz to test runtime cost and compatibility understanding.

## Quiz: 04-runtime-css-in-js-react

<p class="quiz-question">How does runtime CSS-in-JS apply styles to the DOM?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Generates inline styles on each element</p>

<p class="quiz-option"><strong>B.</strong> Injects &lt;style&gt; tags at runtime with generated class names</p>

<p class="quiz-option"><strong>C.</strong> Modifies external stylesheet files</p>

<p class="quiz-option"><strong>D.</strong> Uses CSS Shadow DOM</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Runtime CSS-in-JS parses template literals, generates unique class names, and injects corresponding &lt;style&gt; rules into the document head.</p>

<hr/>

<p class="quiz-question">Approximately how large is the styled-components runtime library (gzip)?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> 1-2 kB</p>

<p class="quiz-option"><strong>B.</strong> 5-8 kB</p>

<p class="quiz-option"><strong>C.</strong> 12-15 kB</p>

<p class="quiz-option"><strong>D.</strong> 50+ kB</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">styled-components runtime is ~14 kB gzip. This is the style injection engine — not styles themselves. Ships with the app regardless of how many styled components exist.</p>

<hr/>

<p class="quiz-question">In Next.js App Router, a styled-components component needs:</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Nothing special — works automatically</p>

<p class="quiz-option"><strong>B.</strong> 'use client' directive at the top</p>

<p class="quiz-option"><strong>C.</strong> A babel plugin only</p>

<p class="quiz-option"><strong>D.</strong> Custom webpack config only</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Runtime CSS-in-JS uses createContext, hooks, and DOM APIs — unavailable in RSC. Every styled component requires 'use client', forcing it into the client bundle.</p>

<hr/>

<p class="quiz-question">What problem occurs when runtime CSS-in-JS is used without SSR configuration?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Styles fail to render entirely</p>

<p class="quiz-option"><strong>B.</strong> FOUC — Flash of Unstyled Content</p>

<p class="quiz-option"><strong>C.</strong> Server crashes</p>

<p class="quiz-option"><strong>D.</strong> Reduced TypeScript type checking</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Server generates different class names than client (no StyleSheetManager). Initial HTML has no styles → flash until client JS injects them.</p>

<hr/>

<p class="quiz-question">How does ThemeProvider pass theme to components?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> CSS custom properties on root</p>

<p class="quiz-option"><strong>B.</strong> React Context</p>

<p class="quiz-option"><strong>C.</strong> Global singleton</p>

<p class="quiz-option"><strong>D.</strong> Prop drilling</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">ThemeProvider wraps React Context. Theme object accessible via props.theme in styled components. Changing theme re-renders all consumers via Context.</p>

<hr/>

<p class="quiz-question">Why does runtime CSS-in-JS's style tag grow unbounded with prop combinations?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Each unique props combination generates a new CSS rule</p>

<p class="quiz-option"><strong>B.</strong> Old rules are never garbage collected</p>

<p class="quiz-option"><strong>C.</strong> Styles are duplicated on every render</p>

<p class="quiz-option"><strong>D.</strong> A and B</p>

<p class="quiz-answer"><strong>Answer:</strong> D</p>

<p class="quiz-explanation">styled-components creates new classes per unique prop combination. Old classes remain in the style tag — never removed or deduplicated. Accumulates over session.</p>

<hr/>

<p class="quiz-question">A team uses styled-components for 200 components. Approximately how much of their JS bundle is the CSS runtime?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> 0 kB — all styles are extracted</p>

<p class="quiz-option"><strong>B.</strong> ~14 kB (library) + CSS strings in JS</p>

<p class="quiz-option"><strong>C.</strong> ~200 kB (2 kB per component)</p>

<p class="quiz-option"><strong>D.</strong> CSS is never in the JS bundle</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">~14 kB for runtime library. CSS strings per component add more. With CSS Modules, those strings would be in separate CSS files at zero JS cost.</p>

<hr/>

<p class="quiz-question">When would runtime CSS-in-JS still be the right choice in 2026?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Greenfield RSC-first Next.js app</p>

<p class="quiz-option"><strong>B.</strong> Existing 500-component codebase with styled-components</p>

<p class="quiz-option"><strong>C.</strong> New component library for 10 external apps</p>

<p class="quiz-option"><strong>D.</strong> Static site with no dynamic theming</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Migration cost of rewriting 500 components outweighs runtime tax. New projects (A, C, D) benefit from zero-cost approaches (CSS Modules, Tailwind, Vanilla Extract).</p>

<hr/>

<p class="quiz-question">What is the RUNTIME bundle cost of Emotion vs styled-components?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Identical</p>

<p class="quiz-option"><strong>B.</strong> Emotion ~11 kB, styled-components ~14 kB</p>

<p class="quiz-option"><strong>C.</strong> styled-components ~7 kB, Emotion ~20 kB</p>

<p class="quiz-option"><strong>D.</strong> Both ~5 kB</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Emotion is slightly smaller (~11 kB gzip) than styled-components (~14 kB). Both face same fundamental runtime cost and RSC incompatibility.</p>

<hr/>

<p class="quiz-question">Can a React component library built with styled-components be used without styled-components as a dependency?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Yes — styles are self-contained</p>

<p class="quiz-option"><strong>B.</strong> No — ThemeProvider and styled runtime required</p>

<p class="quiz-option"><strong>C.</strong> Yes — but only in development</p>

<p class="quiz-option"><strong>D.</strong> No — but Emotion can substitute</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Library consumers must install styled-components as a peer dependency. ThemeProvider must wrap their app. This is the main argument against runtime CSS-in-JS for shared libraries.</p>

<hr/>

<p class="quiz-question">A team has 800 styled-components. The CTO wants to migrate to CSS Modules. What's the recommended approach?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Full rewrite — convert all 800 in one sprint</p>

<p class="quiz-option"><strong>B.</strong> Incremental — new components use CSS Modules, replace old components during feature work</p>

<p class="quiz-option"><strong>C.</strong> Keep styled-components — migration cost outweighs benefit at 800 components</p>

<p class="quiz-option"><strong>D.</strong> Convert to Tailwind instead — it's faster to write</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">At 800 components, incremental migration is the only practical path. Stop new styled-components usage. Replace leaf components first during feature work. Extract design tokens to CSS custom properties as a bridge.</p>

<hr/>

<p class="quiz-question">In which scenario is runtime CSS-in-JS the WRONG choice?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Existing 500-component codebase using styled-components</p>

<p class="quiz-option"><strong>B.</strong> Electron desktop app with no RSC concerns</p>

<p class="quiz-option"><strong>C.</strong> New Next.js App Router app with RSC as primary architecture</p>

<p class="quiz-option"><strong>D.</strong> Rapid prototype with no performance constraints</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">Runtime CSS-in-JS forces 'use client' on every styled component, defeating RSC benefits. In a new App Router app, choose zero-runtime approaches (Tailwind, CSS Modules, Vanilla Extract).</p>


---

# Module 5: Zero-Runtime CSS-in-JS (Vanilla Extract)

Est. study time: 2h
Language: en

## Learning Objectives
- Understand build-time extraction mechanism
- Create typed styles with Vanilla Extract recipes and sprinkles
- Use zero-runtime CSS-in-JS for RSC components and design systems

---

## Core Content

### Build-Time Extraction

Zero-runtime CSS-in-JS (Vanilla Extract, Linaria, PandaCSS, StyleX) reads CSS-in-JS files during build and outputs static `.css` files. No style injection at runtime.

```typescript
// Button.css.ts — Vanilla Extract
import { style } from '@vanilla-extract/css';

export const button = style({
  display: 'inline-flex',
  padding: '8px 16px',
  borderRadius: '6px',
  backgroundColor: '#0366d6',
  color: 'white',
});
```

At build time, Vanilla Extract reads every `.css.ts` file:
1. Executes the module in Node.js (build-time context)
2. Collects style objects
3. Generates scoped class names
4. Writes static CSS file
5. Replaces imports with generated class names

```css
/* Generated output */
.Button_button_1a2b3c {
  display: inline-flex;
  padding: 8px 16px;
  border-radius: 6px;
  background-color: #0366d6;
  color: white;
}
```

**Result**: Browser receives CSS file + JS without any CSS strings. Same zero-cost as CSS Modules, with CSS-in-JS syntax.

> **Think**: If the .css.ts file runs at build time in Node.js, what can't you use inside it?
>
> *Answer: Browser APIs, React runtime, hooks, context, props. Build-time execution means you only have access to Node.js APIs and static values. Dynamic values via CSS custom properties only.*

### TypeScript-First Design

Vanilla Extract's key advantage over CSS Modules: **styles are typed**.

```typescript
// CSS Modules — styles[key] typed as string, not validated
import styles from './Button.module.css';
styles.primary // OK at TS level even if primary doesn't exist

// Vanilla Extract — style returns typed string
import { button, primary } from './Button.css.ts';
button // typed as string, but must exist in source file
primary // TS error if not exported from .css.ts
```

No manual `.d.ts` generation needed — types flow from the export.

**Recipes** — type-safe variant system:

```typescript
import { recipe } from '@vanilla-extract/recipes';

export const button = recipe({
  base: { display: 'inline-flex', padding: '8px 16px' },
  variants: {
    variant: {
      primary: { background: '#0366d6', color: 'white' },
      danger: { background: '#d73a49', color: 'white' },
      ghost: { background: 'transparent' },
    },
    size: {
      small: { padding: '4px 8px', fontSize: '14px' },
      large: { padding: '12px 24px', fontSize: '18px' },
    },
  },
  defaultVariants: {
    variant: 'primary',
    size: 'small',
  },
});
```

In React:

```tsx
import { button } from './Button.css.ts';

function Button({ variant, size }: ButtonProps) {
  return (
    <button className={button({ variant, size })}>
      Click
    </button>
  );
  // result: button() returns combined class string based on variant/size
  // button({ variant: 'primary', size: 'large' }) → "Button_button_1a2b3 primary_large_4d5e6"
}
```

Recipes give type-safe variants — invalid variant name = TypeScript error.

### RSC Compatibility

Zero-runtime CSS-in-JS is fully RSC-compatible:

```tsx
// Server Component — no 'use client' needed
import { card } from './Card.css.ts';

export default function Card({ title, children }) {
  return (
    <div className={card}>
      <h2>{title}</h2>
      {children}
    </div>
  );
}
```

Why it works: `.css.ts` files execute at build time, not at request time. The output is a className string — same as CSS Modules. No runtime, no hooks, no Context.

### Sprinkles — Atomic CSS Generation

Vanilla Extract Sprinkles generates type-safe atomic utility classes (like Tailwind but typed):

```typescript
// sprinkles.css.ts
import { defineProperties, createSprinkles } from '@vanilla-extract/sprinkles';

const space = { none: 0, sm: '8px', md: '16px', lg: '24px' };
const colors = { primary: '#0366d6', danger: '#d73a49', surface: '#f6f8fa' };

const responsiveProperties = defineProperties({
  conditions: {
    mobile: {},
    tablet: { '@media': '(min-width: 768px)' },
    desktop: { '@media': '(min-width: 1024px)' },
  },
  defaultCondition: 'mobile',
  properties: {
    padding: space,
    margin: space,
    backgroundColor: colors,
    color: colors,
    gap: space,
  },
});

export const sprinkles = createSprinkles(responsiveProperties);
```

```tsx
// Usage — typed responsive utilities
function Card() {
  return (
    <div className={sprinkles({
      padding: { mobile: 'sm', tablet: 'md', desktop: 'lg' },
      backgroundColor: 'surface',
    })}>
      ...
    </div>
  );
}
// Generates atomic classes for each property+breakpoint combination
// Only classes actually used are generated (build-time)
```

### Vanilla Extract vs PandaCSS vs StyleX

| | Vanilla Extract | PandaCSS | StyleX (Meta) |
|--|----------------|----------|--------------|
| Maker | Seek | Chakra UI team | Meta (Facebook) |
| Approach | `.css.ts` files | `.css.ts` or config-based | Babel plugin |
| Recipes | Built-in | Built-in (sva) | Pattern-based |
| Sprinkles | Built-in (separate) | Built-in (patterns) | N/A |
| RSC | Yes | Yes | Yes |
| Bundle | 0 kB runtime | 0 kB runtime | 0 kB runtime |
| Community | Largest 2026 | Growing | Niche (Meta ecosystem) |

> **Think**: PandaCSS and Vanilla Extract both claim "zero runtime." What's the meaningful difference?
>
> *Answer: API style. Vanilla Extract forces `.css.ts` files (explicit file per style). PandaCSS supports `.css.ts` AND a config-based approach via panda.config.ts with design token definitions and generated JSX patterns. Vanilla Extract is more TypeScript-native; PandaCSS is more config-driven with codegen.*

### Tradeoffs vs CSS Modules

| Aspect | CSS Modules | Vanilla Extract |
|--------|-------------|-----------------|
| Syntax | Standard CSS | JS/TS objects |
| Typing | Manual `.d.ts` | Built-in (TS files) |
| Variant system | clsx in JSX | recipe() |
| Theming | CSS custom properties | CSS custom properties + theme contracts |
| Learning curve | Low (standard CSS) | Medium (new API) |
| Build tool | Any bundler | Requires Vite/Webpack plugin |
| Error messages | Raw CSS parser | TypeScript errors |

---

### Why This Matters

Zero-runtime CSS-in-JS is the fastest-growing React CSS approach in 2026. It combines the developer experience of CSS-in-JS (type safety, component colocation, dynamic variants) with the zero-cost output of CSS Modules. For design systems and type-safe styling, it's the most complete option.

---

### Common Questions

**Q: Can I use Vanilla Extract with Next.js?**
A: Yes. Next.js plugin (`@vanilla-extract/next-plugin`) integrates with both Pages Router and App Router.

**Q: Does zero-runtime CSS-in-JS support dynamic styles?**
A: Via CSS custom properties. Compile-time styles in `.css.ts`, runtime-dynamic values via `var(--prop)` or inline `style`.

**Q: Is zero-runtime CSS-in-JS overkill for a simple app?**
A: Yes. For a 5-page marketing site, CSS Modules or Tailwind suffice. Zero-runtime shines in design systems, multi-theme apps, and TypeScript-heavy codebases.

---

## Examples

### Example 1: Button with Recipes

See recipe example above. Type-safe, zero runtime, RSC-compatible button in ~20 lines.

### Example 2: Themed Design System Contract

```typescript
// theme.css.ts
import { createThemeContract, createTheme } from '@vanilla-extract/css';

export const themeVars = createThemeContract({
  color: { primary: null, surface: null, text: null },
  space: { sm: null, md: null, lg: null },
  radius: { sm: null, md: null },
});

export const lightTheme = createTheme(themeVars, {
  color: { primary: '#0366d6', surface: '#ffffff', text: '#24292f' },
  space: { sm: '8px', md: '16px', lg: '24px' },
  radius: { sm: '4px', md: '8px' },
});

export const darkTheme = createTheme(themeVars, {
  color: { primary: '#58a6ff', surface: '#0d1117', text: '#c9d1d9' },
  space: { sm: '8px', md: '16px', lg: '24px' },
  radius: { sm: '4px', md: '8px' },
});
```

```tsx
// App.tsx
import { lightTheme, darkTheme } from './theme.css.ts';

function App() {
  const [theme, setTheme] = useState(lightTheme);
  return (
    <div className={theme}>
      <Button>...</Button>
    </div>
  );
}

// Button.css.ts uses themeVars — same variables, different values per theme
export const button = style({
  backgroundColor: themeVars.color.primary,
  padding: themeVars.space.md,
});
```

---

## Key Takeaways
- Zero-runtime CSS-in-JS extracts styles at build time — 0 kB runtime, RSC-compatible
- TypeScript-native — no `.d.ts` generation needed
- Recipes for type-safe variants, Sprinkles for typed atomic CSS
- Vanilla Extract, PandaCSS, StyleX — different APIs, same zero-cost principle
- Best for: design systems, typed styling, RSC apps, multi-theme
- Overkill for: simple marketing sites, small teams, rapid prototypes

---

## Common Misconception

**"Zero-runtime CSS-in-JS is just CSS Modules with extra steps."**

Similar output (static CSS files, scoped classes), different DX:
- Type safety: CSS Modules = string map; Vanilla Extract = typed exports
- Variants: CSS Modules = clsx; Vanilla Extract = recipe()
- Theming: CSS Modules = manual CSS vars; Vanilla Extract = typed theme contracts
- Atomic CSS: CSS Modules = none; Vanilla Extract = Sprinkles

Same result layer (scoped CSS), different authoring layer (typed JS objects vs CSS syntax).

---

## Feynman Explain
(Explain how Vanilla Extract differs from styled-components. Key: "build time vs runtime." Why does "running at build time" matter for bundle size and RSC?)

---

## Reframe
(Pause. Judge: would you use Vanilla Extract for your next React project? Which team factors make it a good or bad fit?)

---

## Drill
Take the quiz. Questions contrast zero-runtime with runtime CSS-in-JS and CSS Modules.

## Quiz: 05-zero-runtime-css-in-js

<p class="quiz-question">When does Vanilla Extract process .css.ts files?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> At runtime in the browser</p>

<p class="quiz-option"><strong>B.</strong> At build time during compilation</p>

<p class="quiz-option"><strong>C.</strong> On every React render</p>

<p class="quiz-option"><strong>D.</strong> During SSR only</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Vanilla Extract reads .css.ts files at build time in Node.js, extracts style objects, and generates static CSS files. No processing happens in the browser.</p>

<hr/>

<p class="quiz-question">Can Vanilla Extract components be used in React Server Components?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> No — needs client-side JS</p>

<p class="quiz-option"><strong>B.</strong> Yes — styles extracted at build, no runtime needed</p>

<p class="quiz-option"><strong>C.</strong> Yes — but only with 'use client'</p>

<p class="quiz-option"><strong>D.</strong> No — only works with Pages Router</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Vanilla Extract class names are static strings at build time. No hooks, no context, no runtime — fully compatible with RSC without 'use client'.</p>

<hr/>

<p class="quiz-question">How does Vanilla Extract handle dynamic variant props vs styled-components?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Cannot handle variants — use inline styles</p>

<p class="quiz-option"><strong>B.</strong> Uses recipe() which returns class names based on variant object</p>

<p class="quiz-option"><strong>C.</strong> Same API as styled-components — template literals with prop interpolation</p>

<p class="quiz-option"><strong>D.</strong> Generates a separate CSS file per variant at runtime</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">recipe() defines variants as static style objects. At build time, it generates class names for each variant combination. Runtime: recipe({ variant: 'primary' }) returns the pre-generated class string.</p>

<hr/>

<p class="quiz-question">How do you apply truly dynamic runtime values (e.g., progress percentage) in Vanilla Extract?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Inline style prop — style={{ width: `${percent}%` }}</p>

<p class="quiz-option"><strong>B.</strong> Dynamic recipe variant</p>

<p class="quiz-option"><strong>C.</strong> Runtime .css.ts re-execution</p>

<p class="quiz-option"><strong>D.</strong> Cannot — Vanilla Extract is static only</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">Build-time CSS handles static styles. Runtime-dynamic values (position, dimensions from API) use inline style prop. Same pattern as CSS Modules.</p>

<hr/>

<p class="quiz-question">What is Vanilla Extract Sprinkles?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> A CSS framework like Bootstrap</p>

<p class="quiz-option"><strong>B.</strong> A runtime animation library</p>

<p class="quiz-option"><strong>C.</strong> A type-safe atomic CSS generation system</p>

<p class="quiz-option"><strong>D.</strong> A CSS reset tool</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">Sprinkles generates typed utility classes for properties like padding, margin, colors — like Tailwind utilities but with TypeScript validation and custom design tokens.</p>

<hr/>

<p class="quiz-question">What advantage does Vanilla Extract have over CSS Modules for TypeScript codebases?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Smaller bundle size</p>

<p class="quiz-option"><strong>B.</strong> Typed exports — invalid class names are compile errors</p>

<p class="quiz-option"><strong>C.</strong> Faster build times</p>

<p class="quiz-option"><strong>D.</strong> No advantage — they are identical</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">CSS Modules export { [key: string]: string } — any key is valid at TS level. Vanilla Extract exports typed class name strings — missing export = compile error.</p>

<hr/>

<p class="quiz-question">What happens at build time when Vanilla Extract encounters recipe({ variants: { color: { red: { background: 'red' }, blue: { background: 'blue' } } } })?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Nothing — recipes are runtime-only</p>

<p class="quiz-option"><strong>B.</strong> Generates two CSS classes: red/blue variants</p>

<p class="quiz-option"><strong>C.</strong> Generates one class with CSS variable</p>

<p class="quiz-option"><strong>D.</strong> Throws error — recipes not supported</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Build time: Vanilla Extract reads recipe definition, generates one unique class per variant value ({ red → .recipe_red_hash, blue → .recipe_blue_hash }). Runtime: recipe({ color: 'red' }) returns combined class string.</p>

<hr/>

<p class="quiz-question">Which zero-runtime CSS-in-JS library was created by Meta (Facebook)?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Vanilla Extract</p>

<p class="quiz-option"><strong>B.</strong> PandaCSS</p>

<p class="quiz-option"><strong>C.</strong> StyleX</p>

<p class="quiz-option"><strong>D.</strong> Linaria</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">StyleX was created by Meta (Facebook) for their own use. It uses a Babel plugin for build-time extraction. Less community adoption than Vanilla Extract or PandaCSS.</p>

<hr/>

<p class="quiz-question">What is the bundle size impact of Vanilla Extract at runtime?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> ~14 kB (same as styled-components)</p>

<p class="quiz-option"><strong>B.</strong> ~5 kB (minimal runtime)</p>

<p class="quiz-option"><strong>C.</strong> 0 kB — all styles extracted to CSS files</p>

<p class="quiz-option"><strong>D.</strong> Depends on number of components</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">Zero runtime. All styles are extracted to static .css files at build time. No JavaScript executes for style resolution in the browser.</p>

<hr/>

<p class="quiz-question">A team building a shared React component library needs: type safety, zero dependency, RSC compatibility, and multi-theme support. Which approach fits?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> styled-components (ThemeProvider)</p>

<p class="quiz-option"><strong>B.</strong> Plain CSS (BEM)</p>

<p class="quiz-option"><strong>C.</strong> Vanilla Extract (theme contracts + recipes)</p>

<p class="quiz-option"><strong>D.</strong> Inline styles everywhere</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">Vanilla Extract meets all requirements: typed (TS files), zero runtime (consumers install no JS), RSC-compatible (static class names), and theme contracts with createThemeContract/createTheme.</p>


---

# Module 6: Tailwind CSS with React

Est. study time: 3h
Language: en

## Learning Objectives
- Configure Tailwind with Next.js and Vite
- Apply conditional Tailwind classes in JSX with clsx/tailwind-merge
- Abstract Tailwind into reusable React component patterns
- Understand Tailwind's tradeoffs at scale

---

## Core Content

### Tailwind JIT Engine

Tailwind v4 (2025+) uses a JIT (Just-In-Time) engine that scans source files and generates only the classes actually used.

```text
Input: className="flex items-center gap-4 p-4 bg-blue-500"
Output CSS: only .flex, .items-center, .gap-4, .p-4, .bg-blue-500 (and their variants)
```

No unused CSS purge configuration needed — JIT is the default in v4.

**Key config file** (`tailwind.config.ts` or `app.css` in v4):

```css
/* app.css — Tailwind v4 */
@import "tailwindcss";

@theme {
  --color-primary: #0366d6;
  --color-danger: #d73a49;
}
```

This defines custom design tokens that become Tailwind utility classes: `bg-primary`, `text-primary`, `border-danger`.

```tsx
function Button() {
  return (
    <button className="bg-primary text-white px-4 py-2 rounded-md">
      Click
    </button>
  );
}
```

> **Think**: How does Tailwind JIT know which classes to generate?
>
> *Answer: It scans all source files for className strings matching utility patterns. If you construct class names dynamically (className={`bg-${color}`}), JIT can't see the full string → class may be missing. Use `safeList` or full class names.*

### Conditional Classes in JSX

In React, Tailwind classes are just strings in `className`. Conditionals use standard JavaScript:

```tsx
// Ternary
<button className={`px-4 py-2 ${isActive ? 'bg-blue-500' : 'bg-gray-200'}`}>
  Click
</button>

// clsx (preferred for readability)
<button className={clsx(
  'px-4 py-2 rounded-md',
  variant === 'primary' && 'bg-blue-500 text-white',
  variant === 'outline' && 'border border-blue-500 text-blue-500',
  disabled && 'opacity-50 cursor-not-allowed'
)}>
  Click
</button>
```

**Problem**: Tailwind classes conflict when combined. `px-4` and `px-6` both define `padding-left`/`padding-right`. The last one in the CSS file wins, which may not match your intent.

**Solution**: `tailwind-merge` resolves conflicting Tailwind classes:

```tsx
import { twMerge } from 'tailwind-merge';

function Button({ className, variant }) {
  return (
    <button className={twMerge(
      'px-4 py-2 rounded-md',
      variant === 'primary' && 'bg-blue-500 text-white',
      className  // Consumer's overrides win correctly
    )}>
      Click
    </button>
  );
}
```

Without `twMerge`: `className="px-4 px-6"` → whichever CSS rule appears last in the stylesheet wins (unpredictable).
With `twMerge`: `px-6` replaces `px-4` predictably.

> **Think**: Why can't CSS cascade handle conflicting Tailwind classes like it does in plain CSS?
>
> *Answer: Because all Tailwind utilities have equal specificity (each is one class). `px-4` and `px-6` have identical specificity → whichever appears later in the CSS file wins. CSS source order depends on JIT generation order, not your className string order.*

### Component Abstraction Patterns

Raw Tailwind in every JSX creates repetition. Three patterns extract reusable components:

**1. Simple wrapper (no abstraction)**

```tsx
function Button({ children }) {
  return (
    <button className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600">
      {children}
    </button>
  );
}
```

Pro: explicit, easy to see all styles. Con: duplicates for every variant.

**2. Variant map**

```tsx
const variants = {
  primary: 'bg-blue-500 text-white hover:bg-blue-600',
  danger: 'bg-red-500 text-white hover:bg-red-600',
  ghost: 'bg-transparent text-blue-500 hover:bg-gray-100',
};

const sizes = {
  sm: 'px-3 py-1 text-sm',
  md: 'px-4 py-2 text-base',
  lg: 'px-6 py-3 text-lg',
};

function Button({ variant = 'primary', size = 'md', className, children }) {
  return (
    <button className={twMerge(
      'rounded-md font-medium transition-colors',
      variants[variant],
      sizes[size],
      className
    )}>
      {children}
    </button>
  );
}
```

**3. cva (class-variance-authority)** — variant factory:

```tsx
import { cva } from 'class-variance-authority';

const button = cva('rounded-md font-medium transition-colors', {
  variants: {
    variant: {
      primary: 'bg-blue-500 text-white hover:bg-blue-600',
      danger: 'bg-red-500 text-white hover:bg-red-600',
      ghost: 'bg-transparent text-blue-500 hover:bg-gray-100',
    },
    size: {
      sm: 'px-3 py-1 text-sm',
      md: 'px-4 py-2 text-base',
      lg: 'px-6 py-3 text-lg',
    },
  },
  defaultVariants: { variant: 'primary', size: 'md' },
});

function Button({ variant, size, className, children }) {
  return (
    <button className={twMerge(button({ variant, size }), className)}>
      {children}
    </button>
  );
}
```

`cva` gives type-safe variant props automatically.

### Custom Design Tokens

Tailwind's `@theme` directive (v4) maps to CSS custom properties internally:

```css
/* app.css */
@import "tailwindcss";
@theme {
  --color-brand: #6366f1;
  --color-brand-hover: #4f46e5;
  --font-display: "Inter", sans-serif;
  --radius-card: 12px;
}
```

These become: `bg-brand`, `text-brand`, `hover:bg-brand-hover`, `font-display`, `rounded-card`.

To extend rather than replace, use `--default-*`:

```css
@theme {
  --color-brand: #6366f1;
  --color-gray-50: #f8fafc;  /* Override default gray */
}
```

### RSC Compatibility

Tailwind is fully RSC-compatible. Class name strings are static — no runtime, no hooks.

```tsx
// Server component — works natively
export default function ProductList({ products }) {
  return (
    <div className="grid grid-cols-3 gap-4">
      {products.map(p => (
        <ProductCard key={p.id} product={p} />
      ))}
    </div>
  );
}
```

Next.js App Router has first-class Tailwind integration. Vite requires the Tailwind plugin.

### Tradeoffs at Scale

**Pro:**
- Zero runtime, RSC-compatible, small bundle (purged)
- Design consistency via constraint system
- Fast prototyping — no file switching
- Largest ecosystem (plugins, components, templates)

**Con:**
- Long `className` strings — readability suffers beyond ~5 utilities
- HTML/CSS coupling — separating concerns is impossible
- Custom designs limited to config-defined tokens
- Debugging: which utility causes this style? Check each in order
- Team must memorize utility names (or use autocomplete)

> **Think**: At what team size or component count does Tailwind become a readability problem?
>
> *Answer: Not team size — component complexity. A `<header>` with 15 utility classes is readable. A `<TableHeader>` with conditional sorting, resizing, sticky columns, and 8 interactive states in a single className string is not. Extract sub-components or use cva for complex states.*

### When NOT to Use Tailwind

Tailwind is dominant but not universal. These scenarios suggest a different approach:

**1. Complex interactive components (30+ className utilities)**

A data table with sortable columns, resizable headers, row selection, inline editing, and pagination produces className strings that are unreadable:

```tsx
// Realistic table header — unmaintainable as pure Tailwind
<th className={twMerge(
  'sticky top-0 z-10 bg-gray-50 px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer select-none hover:bg-gray-100 transition-colors',
  sortable && 'cursor-pointer select-none',
  sorted === 'asc' && 'text-indigo-600 bg-indigo-50',
  sorted === 'desc' && 'text-indigo-600 bg-indigo-50',
  resizing && 'border-r-2 border-indigo-500',
  className
)}>
```

Solution: Extract into CSS Modules for the component's internal states. Keep page layout in Tailwind.

**2. Design systems distributed to external consumers**

If your component library ships to 5+ apps that use different styling approaches (Tailwind, CSS Modules, Vanilla Extract), Tailwind locks consumers into Tailwind. They must:
- Install Tailwind as a dependency
- Use Tailwind's config/theme system
- Accept Tailwind's purge/JIT pipeline

For distributed design systems, Vanilla Extract or CSS Modules are better — zero runtime, no framework lock-in.

**3. Heavy pseudo-element reliance (`::before`, `::after`)**

Tailwind's pseudo-element support is limited. Complex decorative elements (tooltip arrows, custom checkmarks, gradient overlays) are easier in CSS Modules or plain CSS.

**4. App with third-party CSS that Tailwind can't control**

If your app integrates a third-party UI kit (calendar, rich text editor, map) with its own CSS, Tailwind's reset may conflict. You need scoped CSS approaches to isolate third-party styles.

**5. Performance-critical animation sequences**

Tailwind's transition utilities cover simple cases (hover, focus). For cinematic animations with complex keyframes, staggered delays, and orchestrated sequences, writing raw CSS in CSS Modules or Vanilla Extract is more direct.

**Summary: Tailwind fits page-level composition best. Component-level complexity should use scoped CSS approaches.**

### Performance Concerns at Scale

**CSS file size growth:**

Tailwind JIT generates one CSS file. In a large app (200+ pages), this file contains all utilities used across the entire app — even if each page only uses 10% of them.

| App size | Tailwind CSS output | Per-page CSS (CSS Modules) |
|----------|-------------------|---------------------------|
| 10 pages | ~8 kB gzip | ~3-5 kB per page |
| 50 pages | ~15 kB gzip | ~3-5 kB per page |
| 200 pages | ~25-40 kB gzip | ~3-5 kB per page |

For small apps, Tailwind wins (one small CSS file). For large apps, CSS Modules win (per-page CSS smaller than Tailwind's cumulative file).

**Solution for large apps**: Split Tailwind into multiple entry points per route:

```css
/* app/page.css — per-route Tailwind */
@import "tailwindcss" source("./app/dashboard/");
```

Or combine: Tailwind for global design system, route-specific CSS Modules for per-page styles.

**Runtime class computation cost:**

In a React component, `twMerge(clsx(...))` runs on every render. For 1000 components on a page, that's 1000 function calls computing class strings. This is negligible (<1ms) but worth knowing for animation-heavy components (60fps).

```tsx
// Avoid in animation-heavy components:
function AnimatedItem({ active }) {
  // twMerge runs on every animation frame if parent re-renders
  return <div className={twMerge('transition-all', active && 'scale-110')} />;
}

// Better: compute class at state change, not during animation
function AnimatedItem({ active }) {
  const className = useMemo(
    () => twMerge('transition-all', active && 'scale-110'),
    [active]
  );
  return <div className={className} />;
}
```

**Readability breaking point:**

Empirical team reports suggest the breaking point for Tailwind readability is:
- **<10 utilities** per className: fine
- **10-20 utilities**: acceptable with twMerge + clsx
- **20+ utilities**: extract sub-component or switch to CSS Modules

If you find yourself writing className strings that span 3+ lines with conditional logic, the component is too complex for inline Tailwind.

> **Think**: Your app has 100 pages. Tailwind CSS output is 28 kB gzip. Each page uses ~8 kB of that. What's the performance optimization?
>
> *Answer: Split Tailwind generation per route segment. Or combine: use Tailwind for layout/global (10 kB), CSS Modules for page-specific components (5 kB/page). This way each page loads 10 kB (Tailwind) + 5 kB (page CSS) = 15 kB vs 28 kB.*

---

### Why This Matters

Tailwind is the dominant CSS approach for new React projects in 2026. Understanding its patterns (conditional classes, abstraction, twMerge, cva) is essential for working on modern React codebases. Its tradeoffs — readability at scale, debugging difficulty, coupling — determine whether it stays productive as the app grows.

---

### Common Questions

**Q: Can I mix Tailwind with CSS Modules?**
A: Yes. Tailwind for layout/utilities, CSS Modules for complex component states (animations, pseudo-elements). Next.js and Vite support both.

**Q: Does Tailwind work with Vanilla Extract or styled-components?**
A: Mixing approaches per-component. Not per-file. A component uses Tailwind OR Vanilla Extract, not both.

**Q: How do I handle responsive design in Tailwind?**
A: Prefix utilities: `md:flex`, `lg:grid-cols-3`, `xl:p-8`. Tailwind's breakpoints work via media queries, same as CSS Modules but inline.

---

## Examples

### Example 1: Responsive Card Grid

```tsx
function Dashboard() {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 p-4">
      {cards.map(card => (
        <div key={card.id} className="bg-white rounded-lg shadow-sm p-6 border border-gray-200">
          <h3 className="text-lg font-semibold text-gray-900">{card.title}</h3>
          <p className="mt-2 text-sm text-gray-600">{card.description}</p>
        </div>
      ))}
    </div>
  );
}
```

### Example 2: Themed Button with cva

```tsx
import { cva, type VariantProps } from 'class-variance-authority';
import { twMerge } from 'tailwind-merge';

const button = cva(
  'inline-flex items-center justify-center rounded-md font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50',
  {
    variants: {
      variant: {
        default: 'bg-slate-900 text-white hover:bg-slate-800',
        destructive: 'bg-red-500 text-white hover:bg-red-600',
        outline: 'border border-slate-200 bg-white hover:bg-slate-100',
        ghost: 'hover:bg-slate-100',
      },
      size: {
        sm: 'h-9 px-3 text-sm',
        md: 'h-10 px-4 py-2',
        lg: 'h-11 px-8 text-lg',
      },
    },
    defaultVariants: { variant: 'default', size: 'md' },
  }
);

type ButtonProps = VariantProps<typeof button> & {
  className?: string;
  children: React.ReactNode;
};

function Button({ variant, size, className, children, ...props }: ButtonProps) {
  return (
    <button className={twMerge(button({ variant, size }), className)} {...props}>
      {children}
    </button>
  );
}
```

---

## Key Takeaways
- Tailwind JIT generates only used classes — minimal CSS bundle
- Conditional classes via clsx; conflict resolution via tailwind-merge
- Abstract reusable components with variant maps or cva
- Custom tokens via `@theme` directive map to Tailwind utilities
- Fully RSC-compatible — class strings, zero runtime
- Scale challenge: long className strings reduce readability; extract sub-components
- NOT for: complex interactive components (30+ utilities), distributed design systems, third-party CSS integration
- Performance: single CSS file grows with app pages — consider per-route CSS splitting above 50 pages
- Breaking point: 20+ utilities per className → extract or switch to CSS Modules

---

## Common Misconception

**"Tailwind produces bloated HTML with lots of class names."**

The HTML is larger, but the CSS is much smaller. A Tailwind site's CSS is typically 5-15 kB gzip vs 50-100 kB for hand-written CSS with similar coverage. The HTML size increase is negligible compared to the CSS reduction. Total page weight (HTML + CSS) is usually lower.

---

## Feynman Explain
(Explain Tailwind JIT to a traditional CSS developer. Why "writing styles in className" is different from inline styles. How purging works. Why utility classes produce smaller CSS.)

---

## Reframe
(Pause. Judge: Tailwind dominates new projects. Is this because it's genuinely better, or because of network effects? When does it fail?)

---

## Drill
Take the quiz. Questions cover JIT, conditional classes, cva, and tradeoffs.

## Quiz: 06-tailwind-css-react

<p class="quiz-question">How does Tailwind JIT engine decide which CSS classes to generate?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Generates all possible Tailwind utilities</p>

<p class="quiz-option"><strong>B.</strong> Scans source files for complete utility class name strings</p>

<p class="quiz-option"><strong>C.</strong> User manually lists classes in config</p>

<p class="quiz-option"><strong>D.</strong> Generates classes on every HTTP request</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">JIT scans source files for full class name strings (e.g., 'bg-blue-500 px-4'). Dynamically constructed strings (bg-${color}) may miss detection.</p>

<hr/>

<p class="quiz-question">What problem does tailwind-merge solve?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Merges Tailwind configs from multiple files</p>

<p class="quiz-option"><strong>B.</strong> Resolves conflicting Tailwind utility classes predictably</p>

<p class="quiz-option"><strong>C.</strong> Combines Tailwind with CSS Modules</p>

<p class="quiz-option"><strong>D.</strong> Minifies Tailwind class names</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Tailwind utilities have equal specificity. 'px-4 px-6' — CSS source order determines winner. twMerge intelligently resolves conflicts: later explicit override wins.</p>

<hr/>

<p class="quiz-question">What is the bundle size impact of Tailwind CSS (gzip, typical app)?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> 50-100 kB</p>

<p class="quiz-option"><strong>B.</strong> 5-15 kB (purged, JIT-generated)</p>

<p class="quiz-option"><strong>C.</strong> 0 kB — Tailwind has no output</p>

<p class="quiz-option"><strong>D.</strong> Depends on Tailwind version only</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">JIT generates only used utilities. Typical Tailwind app outputs 5-15 kB gzip CSS. Plus ~0.5 kB for reset/base styles.</p>

<hr/>

<p class="quiz-question">Which library provides type-safe variant definitions for Tailwind components?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> clsx</p>

<p class="quiz-option"><strong>B.</strong> tailwind-merge</p>

<p class="quiz-option"><strong>C.</strong> cva (class-variance-authority)</p>

<p class="quiz-option"><strong>D.</strong> tailwind-variants</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">cva defines variants with TypeScript types. button({ variant: 'primary', size: 'lg' }) returns class string. Invalid variant name = TS error.</p>

<hr/>

<p class="quiz-question">How do you add custom brand colors in Tailwind v4?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> tailwind.config.ts → colors</p>

<p class="quiz-option"><strong>B.</strong> app.css → @theme { --color-brand: #6366f1; }</p>

<p class="quiz-option"><strong>C.</strong> Inline style prop</p>

<p class="quiz-option"><strong>D.</strong> Cannot add custom colors — Tailwind only has defaults</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Tailwind v4 uses @theme directive in CSS. --color-brand: #6366f1 becomes bg-brand, text-brand, border-brand utilities.</p>

<hr/>

<p class="quiz-question">Tailwind classes: 'px-4 py-2 bg-blue-500 text-white rounded-md'. How many CSS rules does JIT generate?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> 1 combined rule</p>

<p class="quiz-option"><strong>B.</strong> 5 separate utility rules (padding-x, padding-y, background, color, border-radius)</p>

<p class="quiz-option"><strong>C.</strong> Generated per component instance</p>

<p class="quiz-option"><strong>D.</strong> At least 10 rules</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Each Tailwind utility is a separate CSS rule with a single declaration. px-4 = .px-4 { padding-left: 1rem; padding-right: 1rem; }. They compose via multiple classes on one element.</p>

<hr/>

<p class="quiz-question">What's the main readability concern with Tailwind at scale?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> File size too large</p>

<p class="quiz-option"><strong>B.</strong> className strings exceeding 10+ utilities become hard to scan</p>

<p class="quiz-option"><strong>C.</strong> Tailwind has no CSS equivalent</p>

<p class="quiz-option"><strong>D.</strong> Cannot write media queries</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">A className string with 15+ utilities (including responsive variants, states, dark mode) becomes visually noisy. Pattern: extract into sub-components or use cva for complex states.</p>

<hr/>

<p class="quiz-question">Can Tailwind be used in React Server Components?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> No — requires client-side JS</p>

<p class="quiz-option"><strong>B.</strong> Yes — class strings are static, zero runtime needed</p>

<p class="quiz-option"><strong>C.</strong> Yes — but only with 'use client'</p>

<p class="quiz-option"><strong>D.</strong> No — only works with Pages Router</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Tailwind classes are string literals — no runtime, no hooks, no JavaScript execution needed. Fully RSC-compatible in any framework.</p>

<hr/>

<p class="quiz-question">A component has 20+ Tailwind classes with responsive prefixes, dark mode, and hover states. Best refactoring approach?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Switch to CSS Modules</p>

<p class="quiz-option"><strong>B.</strong> Extract sub-components for each section</p>

<p class="quiz-option"><strong>C.</strong> Add more Tailwind classes</p>

<p class="quiz-option"><strong>D.</strong> Use inline styles</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Extract logical sub-components. Each gets its own className with fewer classes. Also consider cva for variant-heavy components. Not an either/or with Tailwind.</p>

<hr/>

<p class="quiz-question">What happens when you dynamically construct a class name: className={`bg-${color}-500`}?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Always works — Tailwind supports dynamic classes</p>

<p class="quiz-option"><strong>B.</strong> May fail — JIT can't scan dynamic expressions, class may not be generated</p>

<p class="quiz-option"><strong>C.</strong> Throws compile error</p>

<p class="quiz-option"><strong>D.</strong> Generates all possible color variants</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">JIT scans source files as strings. It reads className='bg-blue-500' but can't evaluate bg-${color}-500. If color='blue' at runtime, the class may not exist. Use full class names or safelist.</p>

<hr/>

<p class="quiz-question">When does Tailwind become a WORSE choice than CSS Modules for a component?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Always — CSS Modules are better for everything</p>

<p class="quiz-option"><strong>B.</strong> When a component's className string exceeds 20+ utilities with conditional logic</p>

<p class="quiz-option"><strong>C.</strong> When the app has fewer than 10 pages</p>

<p class="quiz-option"><strong>D.</strong> When using TypeScript</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">At 20+ utilities in one className string, readability breaks. The component is too complex for inline Tailwind. Extract to CSS Modules or split into sub-components. Tailwind excels at simple to moderate complexity.</p>

<hr/>

<p class="quiz-question">At what app size does Tailwind's single CSS file become a performance concern compared to per-page CSS Modules?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> 5 pages</p>

<p class="quiz-option"><strong>B.</strong> 50+ pages (single file contains utilities from all pages)</p>

<p class="quiz-option"><strong>C.</strong> Never — Tailwind always produces the smallest CSS</p>

<p class="quiz-option"><strong>D.</strong> 1000+ pages</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">At 50+ pages, Tailwind generates a single file containing utilities from every page. Each page loads the full file but uses ~10%. Per-page CSS Modules would be smaller per route. Mitigation: per-route entry points.</p>


---

# Module 7: Anti-Patterns — Override in React Component Model

Est. study time: 2.5h
Language: en

## Learning Objectives
- Identify specificity wars and cascade anti-patterns in React
- Replace override-driven styling with composition patterns
- Use prop-based styling and `styled(Component)` correctly

---

## Core Content

### The Override Problem

React component model is composable — components wrap other components, props pass down, styles cascade.

CSS cascade + React composition = conflict.

```tsx
// Parent tries to customize child:
function Page() {
  return (
    <div className="page">
      <Button className="page__submit" />  {/* Intent: override Button styles */}
    </div>
  );
}
```

**Problem**: How does `page__submit` override Button's internal styles?

**Three approaches, all problematic:**
1. **High-specificity selector** (`.page .page__submit`) — specificity arms race
2. **`!important`** — breaks all cascade rules, impossible to override further
3. **Deep nesting / `:where()` hacks** — fragile, tooling-dependent

> **Think**: Why does "override the button's padding" seem simple but cascade into problems?
>
> *Answer: Because each override adds specificity or !important. Next dev needs to override your override. Three components deep, you have .parent .child .grandchild .button.submit.with-special-margin. One CSS change cascades through 10+ files.*

### Specificity Wars

CSS specificity determines which rule wins when multiple target the same element.

```css
/* Specificity: 0,1,0,0 (one class) */
.button { padding: 8px; }

/* Specificity: 0,2,0,0 (two classes) */
.parent .button { padding: 12px; }

/* Specificity: 0,3,0,0 */
.grandparent .parent .button { padding: 16px; }

/* Eventually: !important */
.button { padding: 8px !important; }

/* Counter-!important... */
.parent .button { padding: 12px !important; }
```

With CSS Modules or Tailwind, specificity is always equal (one class per rule). With plain CSS/Sass, specificity stacking is inevitable.

**When specificity wars happen in React:**
1. Parent imports a component's CSS module and tries `:global(.button)`
2. Sass nesting creates `.card .header .title` — override needs `.something .card .header .title`
3. Multiple theme layers (base → app → feature → component) each add specificity

> **Think**: A developer adds .page .button to override Button padding. Later, another dev can't override it. Who's at fault?
>
> *Answer: The first dev. Override via specificity is borrowing from the cascade — it doesn't compose. The component should expose a `size` prop or accept `className` that merges correctly.*

### `!important` — Last Resort That Becomes First Resort

`!important` should be extremely rare in component CSS. When it appears:
- It overrides specificity by fiat
- It cannot be overridden except by another `!important` with same/higher specificity
- It breaks the cascade contract

```css
/* Somewhere in component library: */
.button { padding: 8px !important; }

/* Consumer: */
// Can't override — className="p-4" has no effect
// Need: !important in consumer too, or style prop
```

**The only valid uses of `!important`:**
- Utility classes that MUST win (Tailwind's `!` prefix)
- User preference overrides (accessibility: forced colors)
- Third-party widget styles where you lack control

In component CSS: never. Use props or composition.

### Composition Over Inheritance

React's component model already has the right pattern: **props over override**.

**Bad** — override by targeting internal elements:
```tsx
// Button.tsx
function Button({ className }) {
  return <button className={`btn ${className}`}>Click</button>;
}

// Page.tsx — overrides via specificity
<Button className="page-submit" />
/* CSS: .page-submit { padding: 20px !important; } */
```

**Good** — explicit prop API:
```tsx
// Button.tsx
function Button({ size = 'md', className }) {
  return <button className={twMerge(btn({ size }), className)}>Click</button>;
}

// Page.tsx — uses prop, not CSS override
<Button size="lg" />
```

**Best** — compound components:
```tsx
// Button exposes styled sub-components
const Button = { Root, Icon, Label };

function Page() {
  return (
    <Button.Root size="lg">
      <Button.Icon name="check" />
      <Button.Label>Submit</Button.Label>
    </Button.Root>
  );
}
```

> **Think**: What's the difference between "override via CSS" and "override via prop" in terms of maintenance?
>
> *Answer: CSS override is invisible in the component API — it lives in a stylesheet file, not in the component signature. Prop override is explicit — the component declares "I accept a size prop" and TypeScript validates it.*

### styled(Component) — The Right Way to Extend

styled-components and Emotion have `styled(ExistingComponent)` which generates a new component with merged styles:

```tsx
const BaseButton = styled.button`
  padding: 8px 16px;
  background: blue;
  color: white;
`;

const LargeButton = styled(BaseButton)`
  padding: 16px 32px;
  font-size: 18px;
`;
```

**How this works**: `styled(BaseButton)` creates a new component that renders `BaseButton` and passes a generated class name to it. `BaseButton` must pass `className` to its DOM element.

```tsx
// BaseButton must forward className:
function BaseButton({ className, children }) {
  return <button className={className}>{children}</button>;
}

const LargeButton = styled(BaseButton)`
  padding: 16px;
`;
```

**This pattern is composition, not override.** The new component doesn't fight specificity — it adds its own class, and the CSS cascade within generated classes is controlled by build tools, not by selector specificity.

### Override Patterns by CSS Approach

| Approach | Override mechanism | Correct pattern |
|----------|-------------------|-----------------|
| Plain CSS | Specificity, `!important` | Avoid. Use composition or BEM modifier |
| CSS Modules | `:global` or `composes` | Avoid. Accept `className` prop, merge with clsx |
| Tailwind | `className` prop with twMerge | Accept className, twMerge with defaults |
| styled-components | `styled(Component)` | Use styled composition or variant props |
| Vanilla Extract | Recipe variant override | Props that select recipe variants |
| Inline styles | Direct assignment | `style` prop merge |

**Universal rule**: A component should never require CSS knowledge to customize. Every visual dimension the consumer might change should be a prop.

### CSS Override vs Prop-Based Design

| Aspect | CSS Override | Prop-based |
|--------|-------------|------------|
| API surface | Implicit (class names) | Explicit (prop types) |
| TypeScript validation | None | Full |
| Discoverability | Check CSS file | Autocomplete on component |
| Specificity | Accumulates | None (prop = value) |
| Testability | Visual regression only | Unit test prop values |
| Maintenance | "Where does this style come from?" | "Change the prop" |

---

### Why This Matters

CSS override in React is the #1 source of style bugs in component systems. It creates invisible coupling between components, accumulates specificity that makes later changes expensive, and produces "where is this style coming from?" debugging sessions. Understanding prop-based composition over CSS override is the difference between a maintainable design system and a css-specificity nightmare.

---

### Common Questions

**Q: How do I change a child component's color from parent without override?**
A: Add a `color` prop to the child. `Button color="danger"` — not `.parent .button { color: red; }`.

**Q: What if I need to override a third-party component that doesn't accept props?**
A: Wrap it. Your wrapper adds the missing prop API:

```tsx
function ThemedDatePicker(props) {
  return (
    <ThirdPartyDatePicker
      className="themed-datepicker"
      {...props}
    />
  );
}
// CSS: .themed-datepicker { ... } — one override, centrally managed
```

**Q: Is it OK to use className prop for occasional overrides?**
A: Yes, with twMerge. The component controls defaults; className provides escape hatch. It's when className becomes the primary customization mechanism that problems arise.

---

## Examples

### Example 1: Refactoring Override to Props

**Before** — parent overrides child via CSS:
```tsx
// Card.tsx
function Card({ children }) {
  return <div className="card">{children}</div>;
}

// Page.tsx
<Card>
  <p className="card-text">...</p>  {/* CSS: .card-text overrides card's p styles */}
</Card>
```

**After** — Card accepts props for visual variants:
```tsx
function Card({ variant = 'default', padding = 'md', children }) {
  return (
    <div className={clsx(
      'card',
      `card--${variant}`,
      `card--pad-${padding}`
    )}>
      {children}
    </div>
  );
}

// Page.tsx
<Card variant="elevated" padding="lg">...</Card>
```

### Example 2: Specificity Meltdown

```scss
// Base component
.button { padding: 8px; }

// Feature override
.feature-page .button { padding: 12px; }

// Dashboard override within feature
.feature-page .dashboard-panel .button { padding: 16px; }

// Now a new section needs its own padding:
.admin-section .feature-page .dashboard-panel .button {
  padding: 20px !important;  // Breaking point reached
}
```

Each override adds specificity. At 4+ levels, the cascade is unmanageable.

**Fix**: Prop-based. Each context passes `size` prop to Button.

---

## Key Takeaways
- CSS override in React creates specificity wars and invisible coupling
- `!important` breaks cascade — never use in component CSS
- Props over CSS overrides — every visual dimension should be a prop
- `styled(Component)` is composition, not override — works correctly
- `twMerge` resolves conflicting utility classes predictably
- Universal rule: consumer should not need CSS to customize a component

---

## Common Misconception

**"I need to override component styles because the component doesn't support my use case."**

Correct response: extend the component's prop API or create a variant. If the component is third-party, wrap it. Override via CSS means the component's styling contract is broken — fix the contract, not the CSS.

---

## Feynman Explain
(Explain to a junior: "Why is overriding CSS in a component library bad? I just want to change the padding.")

---

## Reframe
(Pause. Judge: Are there cases where CSS override is acceptable? Utility-first CSS (Tailwind) is all about composing classes in className — is that "override" too?)

---

## Drill
Take the quiz. Questions identify override anti-patterns and propose prop-based alternatives.

## Quiz: 07-anti-patterns-override

<p class="quiz-question">What is the primary problem with CSS override in React component composition?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Performance — multiple class names are slow</p>

<p class="quiz-option"><strong>B.</strong> Specificity accumulation → later overrides need more specificity</p>

<p class="quiz-option"><strong>C.</strong> Components don't accept className in React</p>

<p class="quiz-option"><strong>D.</strong> CSS override causes re-renders</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Each override adds specificity (or !important). Deep nesting eventually produces unchangeable rules or !important wars. Props avoid this entirely.</p>

<hr/>

<p class="quiz-question">Where is !important in CSS actually acceptable?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Component base styles</p>

<p class="quiz-option"><strong>B.</strong> Component variant styles</p>

<p class="quiz-option"><strong>C.</strong> Utility classes that must always win (Tailwind ! prefix)</p>

<p class="quiz-option"><strong>D.</strong> Every component override</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">!important is acceptable for utility classes, accessibility overrides, and third-party widget overrides. Never in component CSS intended to be overridden.</p>

<hr/>

<p class="quiz-question">What's the correct way to customize a component's padding in React?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> CSS: .parent .component { padding: 20px; }</p>

<p class="quiz-option"><strong>B.</strong> Component prop: &lt;Button padding="lg" /&gt;</p>

<p class="quiz-option"><strong>C.</strong> Inline style override: style={{ padding: '20px' }}</p>

<p class="quiz-option"><strong>D.</strong> BEM modifier class</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Explicit prop API communicates available options. TypeScript validates. No specificity involved. Autocomplete discovers available padding values.</p>

<hr/>

<p class="quiz-question">Two components deep: grandparent .page, parent .card, child .button. CSS: .card .button { padding: 12px; } .page .card .button { padding: 16px; }. What's the problem?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Nothing — specificity correctly cascades</p>

<p class="quiz-option"><strong>B.</strong> Grandparent override relies on intermediate DOM structure</p>

<p class="quiz-option"><strong>C.</strong> Padding values should be in JavaScript</p>

<p class="quiz-option"><strong>D.</strong> Both rules have same specificity</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Override is coupled to DOM nesting depth. If .card stops containing .button, both overrides break. Prop-based: &lt;Button size="md"&gt; is decoupled from DOM structure.</p>

<hr/>

<p class="quiz-question">How does styled(Component) avoid the specificity problem?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> It adds !important to all rules</p>

<p class="quiz-option"><strong>B.</strong> It generates a new unique class — no specificity fight with base class</p>

<p class="quiz-option"><strong>C.</strong> It removes the base component's styles</p>

<p class="quiz-option"><strong>D.</strong> It only works with inline styles</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">styled(Component) generates a new CSS class for the extension. Both base and extension classes apply to the element. CSS cascade resolves by source order within generated stylesheet, not by selector specificity.</p>

<hr/>

<p class="quiz-question">A team adds .page .submit-btn { background: red !important; } to override Button. Next dev can't change it. What's the fix?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Add another !important with higher specificity</p>

<p class="quiz-option"><strong>B.</strong> Add variant prop to Button and remove CSS override</p>

<p class="quiz-option"><strong>C.</strong> Use inline style</p>

<p class="quiz-option"><strong>D.</strong> Remove Button's CSS file</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Prop variant removes the need for CSS override entirely. Button declares its API; consumers choose variant. No specificity war.</p>

<hr/>

<p class="quiz-question">Which customization method preserves component encapsulation?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> .parent .component { ... }</p>

<p class="quiz-option"><strong>B.</strong> !important override</p>

<p class="quiz-option"><strong>C.</strong> Component prop API</p>

<p class="quiz-option"><strong>D.</strong> Deep nesting with :where()</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">Props are the public API. CSS selectors reaching into a component's internal structure violate encapsulation — the component owns its DOM, not the consumer.</p>

<hr/>

<p class="quiz-question">What's the Tailwind equivalent of CSS override antipattern?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Using twMerge to combine classes</p>

<p class="quiz-option"><strong>B.</strong> Stacking conflicting utilities in className without twMerge</p>

<p class="quiz-option"><strong>C.</strong> Using @apply in component CSS</p>

<p class="quiz-option"><strong>D.</strong> Using variant props</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">className="px-4 px-6" produces CSS source-order-dependent behavior. One "overrides" the other unpredictably. twMerge resolves this.</p>

<hr/>

<p class="quiz-question">A component library's Button uses CSS Modules. Consumers need to change padding. Correct approach?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Consumer adds :global(.button) { padding: 20px !important; }</p>

<p class="quiz-option"><strong>B.</strong> Consumer passes className prop; component merges via clsx</p>

<p class="quiz-option"><strong>C.</strong> Consumer edits the component's .module.css file</p>

<p class="quiz-option"><strong>D.</strong> Consumer copies the Button code and modifies</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Button should accept className and merge: className={clsx(styles.button, className)}. Consumer passes className with twMerge for conflict resolution.</p>

<hr/>

<p class="quiz-question">What's the test that reveals CSS override problems?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Unit test — component renders without error</p>

<p class="quiz-option"><strong>B.</strong> Visual regression — component looks different in different contexts</p>

<p class="quiz-option"><strong>C.</strong> TypeScript — prop types validate</p>

<p class="quiz-option"><strong>D.</strong> Bundle analysis — CSS file size</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Visual regression tests catch unintended style changes caused by cascade. If Button looks different in Page vs Popup due to cascade, VRT reveals it.</p>


---

# Module 8: Theming React Components with CSS

Est. study time: 3h
Language: en

## Learning Objectives
- Design CSS custom property architecture for multi-theme React apps
- Implement theme propagation via React Context + CSS custom properties
- Apply `@scope` for isolated component theming
- Build theme system without runtime CSS-in-JS

---

## Core Content

### CSS Custom Properties — The Runtime Theme Engine

CSS custom properties (`var(--name)`) are the foundation of runtime theming in React. Unlike Sass variables (compile-time), custom properties resolve in the browser:

```css
:root {
  --color-primary: #0366d6;
  --color-surface: #ffffff;
  --color-text: #24292f;
}

.button {
  background: var(--color-primary);
  color: white;
}
```

Change the property value at a higher DOM level → all descendants re-resolve instantly. No re-render, no JavaScript:

```css
.theme-dark {
  --color-primary: #58a6ff;
  --color-surface: #0d1117;
  --color-text: #c9d1d9;
}
```

```tsx
function App() {
  const [theme, setTheme] = useState<'light' | 'dark'>('light');
  return (
    <div className={theme === 'dark' ? 'theme-dark' : ''}>
      <Button /> {/* automatically re-themes */}
    </div>
  );
}
```

> **Think**: How does `var(--color-primary)` resolve when `.theme-dark` sets `--color-primary` to a different value?
>
> *Answer: CSS custom properties cascade like inherited properties. `.theme-dark` sets a new value on that element. All children see the new value because they inherit from the parent. No JavaScript mutation needed — pure CSS cascade.*

### Theme Architecture Layers

A scalable theme system has 4 layers:

**Layer 1: Base definitions** (CSS custom properties on `:root`)

```css
:root {
  --color-primary: #0366d6;
  --color-primary-hover: #0256b3;
  --color-surface: #ffffff;
  --color-surface-secondary: #f6f8fa;
  --color-text: #24292f;
  --color-text-secondary: #57606a;
  --color-border: #d0d7de;

  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;

  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;

  --font-body: 16px;
  --font-heading: 24px;
}
```

**Layer 2: Theme variants**

```css
.theme-dark {
  --color-primary: #58a6ff;
  --color-primary-hover: #79c0ff;
  --color-surface: #0d1117;
  --color-surface-secondary: #161b22;
  --color-text: #c9d1d9;
  --color-text-secondary: #8b949e;
  --color-border: #30363d;
}

.theme-high-contrast {
  --color-primary: #0044cc;
  --color-surface: #ffffff;
  --color-text: #000000;
  /* Increased contrast ratios */
}
```

**Layer 3: Component tokens** (optional — map semantic tokens to concrete values)

```css
:root {
  --button-bg: var(--color-primary);
  --button-text: white;
  --button-border-color: transparent;
  --card-bg: var(--color-surface);
  --card-border-color: var(--color-border);
}
```

**Layer 4: Component implementation**

```css
/* Button.module.css */
.button {
  background: var(--button-bg);
  color: var(--button-text);
  border: 1px solid var(--button-border-color, transparent);
  padding: var(--space-sm) var(--space-md);
  border-radius: var(--radius-md);
}
```

This architecture means you can re-theme an entire app by changing one CSS class — no component code changes.

### Theme Propagation via React Context

React Context + CSS custom properties = theming without runtime CSS-in-JS:

```tsx
// ThemeContext.tsx
type Theme = 'light' | 'dark' | 'high-contrast';

const ThemeContext = createContext<{
  theme: Theme;
  setTheme: (t: Theme) => void;
}>({
  theme: 'light',
  setTheme: () => {},
});

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState<Theme>('light');
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <div className={`theme-${theme}`}>
        {children}
      </div>
    </ThemeContext.Provider>
  );
}

export function useTheme() {
  return useContext(ThemeContext);
}
```

```tsx
// App.tsx
function App() {
  return (
    <ThemeProvider>
      <Header />
      <Dashboard />
    </ThemeProvider>
  );
}

// Header.tsx — toggle button
function Header() {
  const { theme, setTheme } = useTheme();
  return (
    <header>
      <span>App</span>
      <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
        Toggle theme
      </button>
    </header>
  );
}
```

**Contrast with styled-components ThemeProvider**: Same Context-based API, but without the runtime JS library. CSS custom properties handle the actual value resolution.

> **Think**: When React state changes theme, what actually re-renders vs re-styles?
>
> *Answer: Only the ThemeProvider's div className changes (re-render). Every component using var(--color-*) does NOT re-render — CSS custom properties cascade natively. This is the performance advantage over runtime CSS-in-JS theme injection.*

### `@scope` — Native CSS Scoping for Components

`@scope` (Chrome 118+, Safari 17.4+, Firefox 128+) limits CSS rules to a DOM subtree:

```css
@scope(.card) {
  :scope { border: 1px solid var(--color-border); padding: 16px; }
  .title { font-size: 18px; font-weight: 600; }
  .body { font-size: 14px; color: var(--color-text-secondary); }
}
```

Rules inside `@scope(.card)` only match elements inside `class="card"`. No BEM, no CSS Modules needed for basic scoping.

**In React**:

```tsx
function Card({ title, children }) {
  return (
    <div className="card">
      <h2 className="title">{title}</h2>
      <div className="body">{children}</div>
    </div>
  );
}
```

`.title` inside a `@scope(.card)` won't affect `<h2 class="title">` outside `.card`.

**Comparison**:

| Feature | CSS Modules | @scope |
|---------|-------------|--------|
| Browser support | All | Modern browsers only |
| Scoping mechanism | Build-time class rename | Runtime cascade boundary |
| Dynamic scoping | Not possible | `@scope(.card.highlighted)` |
| Tooling required | Build plugin | None |
| Conflicts with other libs | None | None |
| SSR | Yes | Yes |

`@scope` is not a CSS Modules replacement (different guarantee model — runtime vs build-time) but reduces the need for it in simple components.

### Theme Switching Without Re-Render

CSS custom properties cascade without triggering React re-renders. This is critical for performance:

```tsx
// BAD — causes re-render of entire tree:
function BadThemeToggle({ theme }) {
  return (
    <div style={{ backgroundColor: theme === 'dark' ? '#000' : '#fff' }}>
      {/* Every child re-renders when theme changes */}
      <ExpensiveComponent />
    </div>
  );
}

// GOOD — only className changes, CSS handles rest:
function GoodThemeToggle({ theme }) {
  return (
    <div className={`theme-${theme}`}>
      {/* No re-render cascade — CSS custom properties update natively */}
      <ExpensiveComponent />
    </div>
  );
}
```

With CSS custom properties, `ExpensiveComponent` doesn't re-render. The browser's style engine updates colors without JavaScript involvement.

### Multi-Theme Architecture for Component Libraries

Component libraries should provide theme variables, not enforce a theme engine:

```css
/* Library provides CSS custom properties with defaults */
:root {
  --lib-button-bg: #0366d6;
  --lib-button-text: white;
  --lib-button-radius: 6px;
}

.lib-button {
  background: var(--lib-button-bg);
  color: var(--lib-button-text);
  border-radius: var(--lib-button-radius);
}
```

Consumers customize by overriding at their root:

```css
/* Consumer app */
:root {
  --lib-button-bg: #7c3aed;
  --lib-button-radius: 9999px;
}
```

**No React Context, no ThemeProvider, no runtime library required.** Pure CSS contract.

> **Think**: How does this compare to styled-components ThemeProvider for a shared component library?
>
> *Answer: ThemeProvider requires all consumers to wrap their app in a Context provider from the library. CSS custom properties require nothing — just standard CSS. Zero dependency, zero runtime. This is why CSS variables are the standard for library theming in 2026.*

### Theme Breakpoints and Media Queries

```css
:root {
  --color-primary: #0366d6;
}

.theme-dark {
  --color-primary: #58a6ff;
}

/* OS preference as default (no JS) */
@media (prefers-color-scheme: dark) {
  :root {
    --color-primary: #58a6ff;
  }
}
```

Combine media queries with class-based themes:

```css
/* Respect OS preference unless user explicitly chose */
:root:not(.theme-light):not(.theme-dark) {
  --color-primary: #0366d6;
}

@media (prefers-color-scheme: dark) {
  :root:not(.theme-light):not(.theme-dark) {
    --color-primary: #58a6ff;
  }
}
```

---

### Why This Matters

Theming is where most React CSS approaches fail. Runtime CSS-in-JS couples theme to a JS library. Plain CSS has no scoping. CSS Modules can't switch variables at runtime. Combining CSS custom properties (for runtime values) with CSS Modules/`@scope` (for scoping) gives the best of all approaches: zero-runtime, natively themed, scoped styles.

---

### Common Questions

**Q: Can I animate theme transitions with CSS custom properties?**
A: Yes. `transition: background-color 0.3s, color 0.3s;` on components will animate between theme values since the browser sees actual color changes.

**Q: How many CSS custom properties is too many?**
A: Design token scale. 50-100 tokens for colors, spacing, typography is normal. 500+ suggests over-engineering. Each token should map to a design decision element.

**Q: Can CSS custom properties do dynamic calculations?**
A: Yes, with `calc()`: `padding: calc(var(--space-md) * 1.5);`. Complex logic (if/else) is not possible — use JavaScript for that.

---

## Examples

### Example 1: Complete Theme System

```css
/* tokens.css */
:root {
  --color-primary: #6366f1;
  --color-primary-hover: #4f46e5;
  --color-surface: #ffffff;
  --color-surface-hover: #f8fafc;
  --color-text: #0f172a;
  --color-text-muted: #64748b;
  --color-border: #e2e8f0;
  --color-danger: #ef4444;
  --shadow-sm: 0 1px 2px rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px rgb(0 0 0 / 0.1);
}

.theme-dark {
  --color-primary: #818cf8;
  --color-primary-hover: #6366f1;
  --color-surface: #0f172a;
  --color-surface-hover: #1e293b;
  --color-text: #f1f5f9;
  --color-text-muted: #94a3b8;
  --color-border: #334155;
  --color-danger: #f87171;
  --shadow-sm: 0 1px 2px rgb(0 0 0 / 0.3);
  --shadow-md: 0 4px 6px rgb(0 0 0 / 0.4);
}
```

```tsx
// ThemeToggle.tsx
function ThemeToggle() {
  const [dark, setDark] = useState(
    () => window.matchMedia('(prefers-color-scheme: dark)').matches
  );

  useEffect(() => {
    document.documentElement.className = dark ? 'theme-dark' : '';
  }, [dark]);

  return (
    <button onClick={() => setDark(d => !d)}>
      {dark ? 'Light' : 'Dark'} mode
    </button>
  );
}
```

### Example 2: Component with Theme-Breakpoint Awareness

```css
/* ProductCard.module.css */
.card {
  background: var(--color-surface);
  color: var(--color-text);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: var(--space-md);
  transition: background 0.2s, box-shadow 0.2s;
}
.card:hover {
  background: var(--color-surface-hover);
  box-shadow: var(--shadow-md);
}
.title {
  font-size: var(--font-heading);
  color: var(--color-text);
  margin-bottom: var(--space-xs);
}
.price {
  color: var(--color-primary);
  font-weight: 600;
}
```

```tsx
function ProductCard({ product }) {
  return (
    <div className={styles.card}>
      <h3 className={styles.title}>{product.name}</h3>
      <p className={styles.price}>${product.price}</p>
    </div>
  );
}
```

Themes work automatically — no prop drilling, no Context reading in ProductCard.

---

## Key Takeaways
- CSS custom properties (`var(--name)`) enable runtime theming without JS libraries
- Theme architecture: base values → theme variants → component tokens → components
- React Context manages theme state; CSS custom properties handle style propagation
- `@scope` provides native CSS scoping — no tooling needed (modern browsers)
- Theme switching via CSS class change does NOT re-render child components
- Component libraries should expose CSS custom properties, not React Context
- Combine: CSS custom properties (runtime values) + CSS Modules/`@scope` (scoping)

---

## Common Misconception

**"CSS custom properties are slow compared to hardcoded values."**

Negligible difference. CSS custom properties are resolved during the browser's style calculation phase. The performance cost is a single property lookup per `var()` — microseconds. Hardware-accelerated compositing (transforms, opacity) is unaffected. The real performance cost comes from unnecessary React re-renders (avoided by CSS custom properties).

---

## Feynman Explain
(Explain CSS custom properties as "theme variables that the browser understands." Why they cascade like font-size. Why changing one variable re-colors hundreds of components without JavaScript.)

---

## Reframe
(Pause. Judge: Is the CSS custom property + Context pattern better than styled-components ThemeProvider? For which apps would the difference matter?)

---

## Drill
Take the quiz. Questions test theme architecture, custom property cascade, and implementation.

## Quiz: 08-theming-react-components

<p class="quiz-question">CSS custom property var(--color-primary) resolves at:</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Build time (same as Sass)</p>

<p class="quiz-option"><strong>B.</strong> Component mount time</p>

<p class="quiz-option"><strong>C.</strong> Browser runtime — resolves per element via cascade</p>

<p class="quiz-option"><strong>D.</strong> JavaScript evaluation time</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">CSS custom properties resolve in the browser via cascade. The value depends on the nearest ancestor that sets the property. No build step or JS needed.</p>

<hr/>

<p class="quiz-question">When ThemeProvider changes theme state, what actually re-renders?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Every component consuming CSS custom properties</p>

<p class="quiz-option"><strong>B.</strong> Only the element whose className changes (wrapping div)</p>

<p class="quiz-option"><strong>C.</strong> All components in the app</p>

<p class="quiz-option"><strong>D.</strong> Nothing — CSS custom properties cannot re-theme</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Only the wrapping div's className re-renders. CSS custom properties cascade natively — child components see new values without re-rendering. This is the performance advantage over runtime CSS-in-JS.</p>

<hr/>

<p class="quiz-question">What is the recommended theme architecture for a React component library consumed by external apps?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> ThemeProvider from styled-components</p>

<p class="quiz-option"><strong>B.</strong> A React Context provider from the library</p>

<p class="quiz-option"><strong>C.</strong> CSS custom properties documented in README</p>

<p class="quiz-option"><strong>D.</strong> Inline styles with JavaScript objects</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">CSS custom properties impose zero dependencies. Consumers override them in their own CSS. No Context wrapping, no library import — just CSS. Standard for library theming in 2026.</p>

<hr/>

<p class="quiz-question">What does `@scope(.card) { .title { font-size: 18px; } }` do?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Creates a CSS Module scoped to .card</p>

<p class="quiz-option"><strong>B.</strong> Limits .title rule to elements within .card</p>

<p class="quiz-option"><strong>C.</strong> Makes .title inherit from .card global scope</p>

<p class="quiz-option"><strong>D.</strong> Restricts .title to first child only</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">`@scope(.card)` creates a cascade boundary. `.title` inside only matches elements descendant from an element with class `card`. No tooling involved — native CSS feature.</p>

<hr/>

<p class="quiz-question">Which CSS custom property layer should change when applying a dark theme?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Component implementation layer</p>

<p class="quiz-option"><strong>B.</strong> Theme variant layer (--color-*)</p>

<p class="quiz-option"><strong>C.</strong> Base definition layer (:root)</p>

<p class="quiz-option"><strong>D.</strong> Space token layer</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Theme variant (.theme-dark) overrides base color variables. Component styles reference var(--color-*) and update automatically. Don't change component CSS per theme.</p>

<hr/>

<p class="quiz-question">.card { background: var(--card-bg, var(--color-surface, white)); } What does this resolve to?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> First tries --card-bg, then --color-surface, then white</p>

<p class="quiz-option"><strong>B.</strong> Always white</p>

<p class="quiz-option"><strong>C.</strong> --card-bg if set, else the browser default</p>

<p class="quiz-option"><strong>D.</strong> Only --card-bg — fallbacks not supported</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">var(--card-bg, var(--color-surface, white)) uses nested fallbacks. If --card-bg is not set, tries --color-surface. If neither is set, uses white.</p>

<hr/>

<p class="quiz-question">A button's background uses var(--button-bg). Toggling .theme-dark on root changes it instantly. Why no React re-render?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> React batch-updates style changes</p>

<p class="quiz-option"><strong>B.</strong> CSS custom properties are inherited — browser recalculates without JS</p>

<p class="quiz-option"><strong>C.</strong> JavaScript is not involved in style resolution</p>

<p class="quiz-option"><strong>D.</strong> theme-dark forces a full page reflow but not re-render</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">CSS variables cascade: .theme-dark sets --button-bg on root, all children inherit the new value. Browser's style engine updates without React reconciliation.</p>

<hr/>

<p class="quiz-question">How should a design system expose theme tokens to consumers?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Export theme as JS object and provide merge function</p>

<p class="quiz-option"><strong>B.</strong> Document CSS custom property names and expected values</p>

<p class="quiz-option"><strong>C.</strong> Provide ThemeProvider wrapper component</p>

<p class="quiz-option"><strong>D.</strong> Publish an npm package with variable injection</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">CSS custom properties are the API. Consumers override --ds-color-primary: #purple; in their CSS. No import, no Context, no build step.</p>

<hr/>

<p class="quiz-question">What is `@scope`'s main limitation in 2026?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Doesn't work with any CSS framework</p>

<p class="quiz-option"><strong>B.</strong> Browser support — requires modern Chrome/Safari/Firefox</p>

<p class="quiz-option"><strong>C.</strong> Cannot be combined with CSS custom properties</p>

<p class="quiz-option"><strong>D.</strong> Not compatible with React SSR</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">@scope was added in Chrome 118, Safari 17.4, Firefox 128 (2024). Widely supported in modern browsers but not in older versions. Safe for internal tools or consumer-facing apps targeting modern browsers.</p>

<hr/>

<p class="quiz-question">A design system uses CSS custom properties for theming. Consumer wants brand-specific border-radius. What do they do?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Write: :root { --ds-radius-md: 4px; }</p>

<p class="quiz-option"><strong>B.</strong> Wrap components in ThemeProvider border-radius prop</p>

<p class="quiz-option"><strong>C.</strong> Pass className prop with border-radius override</p>

<p class="quiz-option"><strong>D.</strong> Modify design system source code</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">Override the CSS custom property. If design system uses --ds-radius-md: 8px, consumer sets :root { --ds-radius-md: 4px; } in their CSS. No component code changes.</p>


---

# Module 9: Layout Components with Flexbox & Grid

Est. study time: 2h
Language: en

## Learning Objectives
- Build reusable React layout primitives (Stack, Flex, Grid)
- Decide when Flexbox vs CSS Grid per layout pattern
- Implement responsive layout props

---

## Core Content

### Layout Primitives vs Ad-Hoc Layout

Most apps repeat the same layout patterns: vertical stack, horizontal row, grid of items. Layout primitives encapsulate these:

```tsx
// Without primitive — repeated flex classes:
<section className="flex flex-col gap-4">
  <div className="flex items-center gap-2">
    <span>Label</span>
    <input />
  </div>
</section>

// With primitive — intent clear:
<Stack gap="md">
  <Flex gap="sm" align="center">
    <Label>Name</Label>
    <Input />
  </Flex>
</Stack>
```

> **Think**: What's the difference between `className="flex gap-4"` and `<Stack gap="md">`?
>
> *Answer: Same CSS output. The difference is API intent. `<Stack>` communicates "children arranged vertically." `flex gap-4` communicates implementation details. Primitives make layout choices visible in component name.*

### Stack Component

Vertical layout. The most common layout primitive.

```tsx
// Stack.tsx
type StackProps = {
  gap?: 'xs' | 'sm' | 'md' | 'lg' | 'xl';
  align?: 'start' | 'center' | 'end' | 'stretch';
  as?: 'div' | 'section' | 'main' | 'form';
  children: React.ReactNode;
};

function Stack({ gap = 'md', align = 'stretch', as: Tag = 'div', children }: StackProps) {
  return (
    <Tag className={clsx('stack', `stack--gap-${gap}`, `stack--align-${align}`)}>
      {children}
    </Tag>
  );
}
```

```css
/* Stack.module.css */
.stack { display: flex; flex-direction: column; }
.stack--gap-xs { gap: var(--space-xs); }
.stack--gap-sm { gap: var(--space-sm); }
.stack--gap-md { gap: var(--space-md); }
.stack--gap-lg { gap: var(--space-lg); }
.stack--gap-xl { gap: var(--space-xl); }
.stack--align-start { align-items: flex-start; }
.stack--align-center { align-items: center; }
.stack--align-end { align-items: flex-end; }
.stack--align-stretch { align-items: stretch; }
```

### Flex Component (Horizontal Row)

```tsx
type FlexProps = {
  gap?: Spacing;
  align?: 'start' | 'center' | 'end' | 'baseline' | 'stretch';
  justify?: 'start' | 'center' | 'end' | 'between' | 'around' | 'evenly';
  wrap?: boolean;
  as?: ElementType;
  children: React.ReactNode;
};

function Flex({ gap = 'sm', align = 'center', justify = 'start', wrap, as: Tag = 'div', children }: FlexProps) {
  return (
    <Tag className={clsx(
      'flex',
      `flex--gap-${gap}`,
      `flex--align-${align}`,
      `flex--justify-${justify}`,
      wrap && 'flex--wrap'
    )}>
      {children}
    </Tag>
  );
}
```

```css
.flex { display: flex; }
.flex--wrap { flex-wrap: wrap; }
.flex--align-start { align-items: flex-start; }
.flex--align-center { align-items: center; }
.flex--justify-between { justify-content: space-between; }
```

> **Think**: Should Flex and Stack be separate components or one component with a `direction` prop?
>
> *Answer: Tradeoff. Separate components are more explicit (`direction` can't be wrong). One component is fewer imports. In practice, most uses are vertical (Stack) or horizontal (Flex) — separate reads clearer.*

### Grid Component

```tsx
type GridProps = {
  columns: number | { base?: number; sm?: number; md?: number; lg?: number };
  gap?: Spacing;
  children: React.ReactNode;
};

function Grid({ columns = 1, gap = 'md', children }: GridProps) {
  return (
    <div className={clsx(
      'grid',
      `grid--gap-${gap}`,
      typeof columns === 'number' && `grid--cols-${columns}`
    )}>
      {children}
    </div>
  );
}
```

```css
.grid { display: grid; }
.grid--cols-1 { grid-template-columns: repeat(1, 1fr); }
.grid--cols-2 { grid-template-columns: repeat(2, 1fr); }
.grid--cols-3 { grid-template-columns: repeat(3, 1fr); }
.grid--cols-4 { grid-template-columns: repeat(4, 1fr); }
.grid--gap-sm { gap: var(--space-sm); }
.grid--gap-md { gap: var(--space-md); }
```

### When Flexbox vs Grid

| Pattern | Use | Example |
|---------|-----|---------|
| 1D row/column alignment | Flexbox | Nav bar, toolbar, form field + label |
| 2D grid of equal cells | Grid | Product grid, photo gallery, card layout |
| Content-first (size by content) | Flexbox | Button groups, badge clusters |
| Layout-first (fill available) | Grid | Page layout (sidebar + main), dashboard panels |
| Wrapping items | Flexbox (wrap) | Tag list, filter chips |
| Complex spanning | Grid | Magazine layout, heterogeneous cards |

**Rule of thumb**: If you need alignment in one direction, use Flexbox. If you need both rows and columns simultaneously, use Grid.

> **Think**: Dashboard layout with sidebar, header, main content, and footer — Flexbox or Grid?
>
> *Answer: Grid. Two-dimensional layout (sidebar spans full height, header spans full width, main fills remaining). Grid's template areas make this explicit. Flexbox would need nested containers.*

### Responsive Layout Props

Responsive layout = different column counts or gaps at breakpoints:

```tsx
type ResponsiveValue<T> = T | { base: T; sm?: T; md?: T; lg?: T };

function Grid({ columns, gap, children }: { columns: ResponsiveValue<number> }) {
  const breakpoints = ['sm', 'md', 'lg'] as const;
  return (
    <div className={clsx(
      'grid',
      typeof columns === 'number' && `grid--cols-${columns}`,
      typeof columns === 'object' && breakpoints.map(bp =>
        columns[bp] && `grid--${bp}--cols-${columns[bp]}`
      )
    )}>
      {children}
    </div>
  );
}
```

```css
/* Base */
.grid--cols-2 { grid-template-columns: repeat(2, 1fr); }
/* Responsive */
@media (min-width: 640px) { .grid--sm--cols-3 { grid-template-columns: repeat(3, 1fr); } }
@media (min-width: 768px) { .grid--md--cols-4 { grid-template-columns: repeat(4, 1fr); } }
```

Usage:

```tsx
<Grid columns={{ base: 1, sm: 2, md: 3, lg: 4 }}>
  {products.map(p => <ProductCard key={p.id} product={p} />)}
</Grid>
```

> **Think**: How does Tailwind handle this vs CSS Modules?
>
> *Answer: Tailwind: className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4". Same CSS, different DX. Tailwind puts breakpoint logic in className; CSS Modules put it in CSS file.*

---

### Why This Matters

Layout primitives eliminate repetitive flex/grid patterns and make layout intent explicit. A `<Stack gap="lg">` communicates vertical arrangement. `className="flex flex-col gap-4"` communicates implementation. In large codebases, primitives reduce layout bugs and make responsive changes centralized.

---

### Common Questions

**Q: Should I use a layout primitive library like Radix UI or build my own?**
A: Build if layout needs are simple (Stack, Flex, Grid). Use library if you need advanced features (auto-grid, aspect-ratio containers, masonry).

**Q: Do layout primitives cause performance issues?**
A: No. They render a single DOM element with classes. No state, no effects, no context.

---

## Examples

### Example: Dashboard Layout

```tsx
function Dashboard() {
  return (
    <Grid columns={{ base: 1, lg: 4 }} gap="lg" className="p-6">
      <Sidebar className="lg:col-span-1" /> {/* CSS: grid-column: span 1 on lg */}
      <Stack gap="md" className="lg:col-span-3">
        <Flex justify="between" align="center">
          <h1>Dashboard</h1>
          <Button>Export</Button>
        </Flex>
        <Grid columns={{ base: 1, sm: 2, md: 3 }} gap="md">
          {stats.map(s => <StatCard key={s.label} stat={s} />)}
        </Grid>
        <Chart />
      </Stack>
    </Grid>
  );
}
```

---

## Key Takeaways
- Layout primitives (Stack, Flex, Grid) encapsulate repeated flex/grid patterns
- Flexbox: 1D alignment. Grid: 2D layout. Choose accordingly
- Responsive props with breakpoint objects give explicit control
- Primitives reduce layout bugs and make intent clear

---

## Common Misconception

**"I don't need layout components — I just use flex/grid classes inline."**

Both work. Layout components add: named intent (Stack vs flex-col), prop validation (gap values restricted to tokens), and centralized responsive logic. Tradeoff is abstraction layer to learn.

---

## Feynman Explain
(Explain difference between Flexbox and Grid to a junior dev. When would you use each for a React app?)

---

## Drill
Take the quiz.

## Quiz: 09-layout-components-flexbox-grid

<p class="quiz-question">What is a layout primitive component?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> A CSS framework like Tailwind</p>

<p class="quiz-option"><strong>B.</strong> A reusable component that encapsulates flex/grid layout patterns</p>

<p class="quiz-option"><strong>C.</strong> A React hook for responsive design</p>

<p class="quiz-option"><strong>D.</strong> A build tool for CSS</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Layout primitives (Stack, Flex, Grid) encapsulate repeated CSS layout patterns into explicit component APIs.</p>

<hr/>

<p class="quiz-question">Which layout approach for: a nav bar with logo left, links center, profile right?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> CSS Grid (3-column template)</p>

<p class="quiz-option"><strong>B.</strong> Flexbox (justify-content: space-between)</p>

<p class="quiz-option"><strong>C.</strong> Float layout</p>

<p class="quiz-option"><strong>D.</strong> Table layout</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">One-dimensional alignment across main axis. Flexbox with space-between handles this naturally. Grid would also work but overkill.</p>

<hr/>

<p class="quiz-question">Which layout approach for: sidebar (fixed width) + main content + header spanning both?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Flexbox wrapping</p>

<p class="quiz-option"><strong>B.</strong> CSS Grid (template areas)</p>

<p class="quiz-option"><strong>C.</strong> Inline-block elements</p>

<p class="quiz-option"><strong>D.</strong> Position absolute</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Two-dimensional layout needing both rows and columns. Grid template areas map regions explicitly. Flexbox would need nested containers.</p>

<hr/>

<p class="quiz-question">What does a responsive Grid columns prop look like?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> columns="responsive"</p>

<p class="quiz-option"><strong>B.</strong> columns={{ base: 1, md: 2, lg: 3 }}</p>

<p class="quiz-option"><strong>C.</strong> columns={[1, 2, 3]}</p>

<p class="quiz-option"><strong>D.</strong> columns="auto"</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Responsive prop maps breakpoints to column count. Base = mobile default, md = tablet, lg = desktop. Generated CSS uses media queries.</p>

<hr/>

<p class="quiz-question">Stack component vs div with className='flex flex-col gap-4' — key advantage?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Stack is faster to render</p>

<p class="quiz-option"><strong>B.</strong> Stack communicates intent (vertical layout) at component level</p>

<p class="quiz-option"><strong>C.</strong> Stack supports more CSS properties</p>

<p class="quiz-option"><strong>D.</strong> Stack works without CSS</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Both produce same HTML. Stack makes layout intent explicit in component name. `flex flex-col gap-4` communicates implementation, not intent.</p>

<hr/>

<p class="quiz-question">How should layout primitives handle spacing?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Accept any CSS value string</p>

<p class="quiz-option"><strong>B.</strong> Accept only predefined spacing tokens (sm, md, lg)</p>

<p class="quiz-option"><strong>C.</strong> Never accept gap — use wrapper components</p>

<p class="quiz-option"><strong>D.</strong> Always use 16px default</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Restricted token values enforce design system consistency. 'gap-12px' bypasses tokens. 'gap-lg' references design system spacing.</p>

<hr/>

<p class="quiz-question">Grid component with 12 items: columns={3} renders how many rows?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> 3</p>

<p class="quiz-option"><strong>B.</strong> 4</p>

<p class="quiz-option"><strong>C.</strong> 12</p>

<p class="quiz-option"><strong>D.</strong> Depends on content height</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">12 items ÷ 3 columns = 4 rows (assuming grid auto-flow row). The component sets grid-template-columns: repeat(3, 1fr).</p>

<hr/>

<p class="quiz-question">A filter chip list wraps when screen narrows. Which component?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Grid with columns={1}</p>

<p class="quiz-option"><strong>B.</strong> Flex with wrap={true}</p>

<p class="quiz-option"><strong>C.</strong> Stack</p>

<p class="quiz-option"><strong>D.</strong> Absolute positioned divs</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Flex with flex-wrap: wrap lets items naturally flow to next line when container narrows. Grid requires explicit breakpoint column changes.</p>


---

# Module 10: Container Queries & Responsive React Components

Est. study time: 2h
Language: en

## Learning Objectives
- Apply container queries for component-level responsiveness
- Distinguish container queries from viewport media queries
- Build responsive React components independent of page layout

---

## Core Content

### Viewport vs Container Queries

Media queries respond to viewport size. Container queries respond to parent element size.

```css
/* Media query — responds to viewport */
@media (max-width: 768px) {
  .card { flex-direction: column; }
}

/* Container query — responds to parent container */
@container (max-width: 400px) {
  .card { flex-direction: column; }
}
```

**Why container queries matter in React**: A `<ProductCard>` might render in a 4-column grid (wide) or a sidebar (narrow). Media queries can't distinguish these contexts — they only know viewport width. Container queries let the component adapt to its actual available space.

> **Think**: A ProductCard appears in a 4-column grid on desktop AND in a slide-out panel. With media queries, how do you style both contexts?
>
> *Answer: You can't with viewport alone. You'd add a modifier class or prop— `<ProductCard variant="compact" />`. Container queries eliminate the prop: the card detects its own container width.*

### Setting Up Containers

```css
/* Parent establishes a containment context */
.card-grid {
  container-type: inline-size;
  container-name: card-container;
}

.sidebar {
  container-type: inline-size;
  container-name: sidebar;
}
```

`container-type: inline-size` creates a containment context based on inline (width) size. `container-name` optional — names the context for `@container` references.

**In React**:

```tsx
function ProductGrid({ products }) {
  return (
    <div className="card-grid"> {/* container established here */}
      {products.map(p => <ProductCard key={p.id} product={p} />)}
    </div>
  );
}

function Sidebar() {
  return (
    <aside className="sidebar"> {/* different container context */}
      <ProductCard product={featured} />
    </aside>
  );
}
```

### Component Responds to Its Container

```css
/* ProductCard.module.css */
.card {
  container-type: inline-size;
  display: flex;
  flex-direction: row;
  gap: 16px;
}

@container (max-width: 300px) {
  .card { flex-direction: column; }
  .image { width: 100%; }
}

@container (min-width: 301px) and (max-width: 500px) {
  .card { flex-direction: row; gap: 12px; }
  .image { width: 120px; }
}

@container (min-width: 501px) {
  .card { flex-direction: row; gap: 24px; }
  .image { width: 200px; }
}
```

**Key**: Container queries use the container's width, not viewport. Same component renders differently in ProductGrid (wide) vs Sidebar (narrow) without props.

### Container Query Units

Container queries also provide units relative to container size:

- `cqw` — 1% of container width
- `cqh` — 1% of container height
- `cqi` — 1% of container inline size
- `cqb` — 1% of container block size
- `cqmin` — smaller of cqi/cqb
- `cqmax` — larger of cqi/cqb

```css
.card {
  container-type: inline-size;
}
.title {
  font-size: clamp(1rem, 5cqi, 2rem);
}
/* Title scales from 1rem to 2rem based on container width */
```

### Container Queries + Media Queries Combined

```css
/* Outer layout responds to viewport */
@media (max-width: 768px) {
  .grid { grid-template-columns: 1fr; }
}

/* Inner component responds to its container */
.product-card { container-type: inline-size; }

@container (max-width: 350px) {
  .product-card { flex-direction: column; }
}
```

Layers: media queries → page layout. Container queries → component adaptation.

### When Not to Use Container Queries

- Simple responsive: media queries suffice
- Container query performance: containment affects layout — not all elements need it
- If component always renders in one context (e.g., main content only) — media query is simpler

> **Think**: You have a Card component always rendered in a grid that is always 3 columns. Does this need container queries?
>
> *Answer: No. Card always has the same available width. Container query adds complexity without benefit. Use media query to switch grid columns, regular CSS for Card.*

### Browser Support (2026)

Container queries supported in all modern browsers: Chrome 105+, Safari 16+, Firefox 110+. No polyfill needed. Safe for production.

---

### Why This Matters

Container queries are the biggest CSS advancement for component-based architectures since flexbox. They make components truly self-responsive — a `<ProfileCard>` knows how to render based on its actual space, not page context. This eliminates a whole category of "responsive variant" props.

---

### Common Questions

**Q: Can I nest container queries?**
A: Yes. A container inside a container. Each `@container` query responds to its nearest named or anonymous container ancestor.

**Q: Do container queries affect performance?**
A: Minimal. Containment creates a layout boundary — browser recalculates only the container's subtree when its size changes. Performance improvement for large pages.

---

## Examples

### Example: Responsive Dashboard Widget

```tsx
// Widget — adapts to its grid cell size automatically
function Widget({ title, children }) {
  return (
    <div className={styles.widget}>
      <h3 className={styles.title}>{title}</h3>
      <div className={styles.content}>{children}</div>
    </div>
  );
}
```

```css
.widget { container-type: inline-size; }
.title { font-size: clamp(14px, 4cqi, 24px); }
.content { 
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
@container (max-width: 300px) {
  .content { flex-direction: column; }
}
```

---

## Key Takeaways
- Container queries respond to parent element size, not viewport
- `container-type: inline-size` creates containment context
- Container query units (cqw, cqi, cqmin) size elements to container
- Combine: media queries for page layout, container queries for components
- Eliminates responsive variant props — components adapt automatically

---

## Common Misconception

**"Container queries replace media queries."**

Not replace — complement. Media queries handle page-level layout (grid columns, sidebar visibility). Container queries handle component-level adaptation (card layout, font size). Both needed.

---

## Feynman Explain
(Explain: "A card should look different in a 4-column grid vs a sidebar." Why can't media queries handle this? How do container queries fix it?)

---

## Drill
Take the quiz.

## Quiz: 10-container-queries-responsive

<p class="quiz-question">Container query vs media query — what does each respond to?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Media = viewport, Container = parent element size</p>

<p class="quiz-option"><strong>B.</strong> Media = element size, Container = viewport</p>

<p class="quiz-option"><strong>C.</strong> Both respond to viewport but container queries are faster</p>

<p class="quiz-option"><strong>D.</strong> Container queries need JavaScript</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">Media queries check viewport dimensions. Container queries check the nearest container element's size.</p>

<hr/>

<p class="quiz-question">Which CSS property creates a containment context?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> display: contain</p>

<p class="quiz-option"><strong>B.</strong> container-type: inline-size</p>

<p class="quiz-option"><strong>C.</strong> contain: layout</p>

<p class="quiz-option"><strong>D.</strong> isolation: isolate</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">container-type: inline-size creates a containment context on inline (width) size. Children can use @container queries against this context.</p>

<hr/>

<p class="quiz-question">A ProductCard renders in a 4-column grid and a sidebar. How do container queries help?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Card adapts to available width without media query props</p>

<p class="quiz-option"><strong>B.</strong> Card automatically switches to a different component</p>

<p class="quiz-option"><strong>C.</strong> Nothing — use media queries instead</p>

<p class="quiz-option"><strong>D.</strong> Container queries only work on images</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">Card uses @container to detect its own width. In the grid (wide), it renders row layout. In sidebar (narrow), column layout. No variant props needed.</p>

<hr/>

<p class="quiz-question">What does 50cqi represent?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> 50% of container width</p>

<p class="quiz-option"><strong>B.</strong> 50 characters of container text</p>

<p class="quiz-option"><strong>C.</strong> 50% of viewport</p>

<p class="quiz-option"><strong>D.</strong> 50px container inset</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">cqi = container query inline unit. 50cqi = 50% of the container's inline size (width in horizontal writing mode).</p>

<hr/>

<p class="quiz-question">Should container queries replace media queries entirely?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Yes — container queries are superior</p>

<p class="quiz-option"><strong>B.</strong> No — media queries for page layout, container for component adaptation</p>

<p class="quiz-option"><strong>C.</strong> No — media queries are faster</p>

<p class="quiz-option"><strong>D.</strong> Yes — browser vendors recommend this</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Media queries handle page-level layout (sidebar collapse, grid columns). Container queries handle component-level adaptation. Both needed.</p>

<hr/>

<p class="quiz-question">When would container queries add no value?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Component renders in multiple layout contexts</p>

<p class="quiz-option"><strong>B.</strong> Component always renders at same width</p>

<p class="quiz-option"><strong>C.</strong> Component uses flexbox internally</p>

<p class="quiz-option"><strong>D.</strong> Component is a button</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">If component always has the same container width, container query is unnecessary. Media query or static CSS suffices.</p>


---

# Module 11: Animations in React with CSS

Est. study time: 2h
Language: en

## Learning Objectives
- Coordinate CSS animations with React lifecycle
- Use CSS transitions for state-driven UI motion
- Apply View Transitions API in React

---

## Core Content

### CSS Transitions in React

CSS transitions animate between property states. In React, state changes toggle class names → transitions fire:

```css
/* Button.module.css */
.button {
  background: var(--color-primary);
  transition: background 0.2s ease;
}
.button:hover {
  background: var(--color-primary-hover);
}
```

```tsx
// Transition triggered by CSS pseudo-class (hover) — no React state needed
function Button() {
  return <button className={styles.button}>Click</button>;
}
```

**State-driven transitions** toggle via className:

```css
.panel {
  max-height: 0;
  opacity: 0;
  overflow: hidden;
  transition: max-height 0.3s ease, opacity 0.2s ease;
}
.panel.open {
  max-height: 500px;  /* Must be known or use auto — see note */
  opacity: 1;
}
```

```tsx
function Accordion() {
  const [open, setOpen] = useState(false);
  return (
    <div>
      <button onClick={() => setOpen(o => !o)}>Toggle</button>
      <div className={clsx(styles.panel, open && styles.open)}>
        Content
      </div>
    </div>
  );
}
```

> **Think**: What's the problem with transitioning max-height from 0 to auto?
>
> *Answer: CSS can't transition to auto. You must use a specific max-height value (larger than actual content). Alternative: use grid-template-rows transition (row 0 → 1fr) which works in modern browsers.*

### Keyframe Animations

For multi-step or repeating animations, use `@keyframes`:

```css
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.enter { animation: fadeIn 0.3s ease-out; }
.spinner { animation: spin 1s linear infinite; }
```

```tsx
function Toast({ message, onClose }) {
  return (
    <div className={styles.enter}>
      {message}
      <button onClick={onClose}>×</button>
    </div>
  );
}
```

### React Lifecycle + Animation

Mount → enter animation. Unmount → exit animation (needs coordination).

**Problem**: React removes elements immediately. CSS animation on unmount never plays.

**Solution**: Track "closing" state, delay removal:

```tsx
function ToastContainer({ toasts, removeToast }) {
  return (
    <div className={styles.container}>
      {toasts.map(t => (
        <ToastItem key={t.id} toast={t} onRemove={removeToast} />
      ))}
    </div>
  );
}

function ToastItem({ toast, onRemove }) {
  const [exiting, setExiting] = useState(false);

  useEffect(() => {
    if (exiting) {
      const timer = setTimeout(() => onRemove(toast.id), 300); // match CSS animation duration
      return () => clearTimeout(timer);
    }
  }, [exiting]);

  return (
    <div className={clsx(styles.toast, exiting && styles.exit)}>
      <span>{toast.message}</span>
      <button onClick={() => setExiting(true)}>×</button>
    </div>
  );
}
```

```css
.toast {
  animation: slideIn 0.3s ease-out;
}
.exit {
  animation: slideOut 0.3s ease-in forwards;
}
@keyframes slideIn {
  from { transform: translateX(100%); opacity: 0; }
  to { transform: translateX(0); opacity: 1; }
}
@keyframes slideOut {
  from { transform: translateX(0); opacity: 1; }
  to { transform: translateX(100%); opacity: 0; }
}
```

**Pattern**: `exiting` state → apply exit animation class → after animation duration, actually remove.

> **Think**: What happens if the animation duration is 500ms but setTimeout uses 300ms?
>
> *Answer: Component unmounts before animation finishes — visible cut. Always match setTimeout to the CSS animation duration. Better: use onAnimationEnd event.*

### onAnimationEnd Event

```tsx
function ToastItem({ toast, onRemove }) {
  const [exiting, setExiting] = useState(false);

  return (
    <div
      className={clsx(styles.toast, exiting && styles.exit)}
      onAnimationEnd={() => exiting && onRemove(toast.id)}
    >
      ...
    </div>
  );
}
```

No timer needed. Browser fires `onAnimationEnd` when CSS animation completes.

### View Transitions API

View Transitions API (2024+) provides smooth transitions between page/document states:

```tsx
function TabView() {
  const [tab, setTab] = useState('list');

  const switchTab = (newTab: string) => {
    if (document.startViewTransition) {
      document.startViewTransition(() => setTab(newTab));
    } else {
      setTab(newTab); // fallback
    }
  };

  return (
    <div>
      <button onClick={() => switchTab('list')}>List</button>
      <button onClick={() => switchTab('grid')}>Grid</button>
      <div className="view-transition-main">
        {tab === 'list' ? <ListView /> : <GridView />}
      </div>
    </div>
  );
}
```

```css
::view-transition-old(view-transition-main) {
  animation: fadeOut 0.2s ease;
}
::view-transition-new(view-transition-main) {
  animation: fadeIn 0.2s ease;
}
```

React 19+ has built-in support via `<ViewTransition>` component (experimental).

### Performance Considerations

- **`transform` and `opacity` only**: These are composited on GPU. Animating `width`, `height`, `top`, `left` triggers layout reflow.
- **`will-change`**: Hint browser about animating properties. Use sparingly — overuse consumes GPU memory.

```css
.animated-element {
  will-change: transform, opacity;
}
```

- **`content-visibility: auto`**: Skip rendering for off-screen elements. Improves initial render performance.

---

### Why This Matters

CSS animations in React require coordinating two systems: React's component lifecycle and CSS's animation lifecycle. Mount = easy (class applies on render). Unmount = requires exiting state + delayed removal. View Transitions API is the future of page transition in React.

---

### Common Questions

**Q: Should I use Framer Motion instead of CSS animations?**
A: CSS for simple transitions/keyframes. Framer Motion for complex gesture-driven animations (drag, spring physics, layout animations). CSS is zero-dependency, Framer Motion is ~30 kB.

**Q: Can I animate CSS custom properties?**
A: Yes, with `@property` for registered custom properties (tells browser how to interpolate). Otherwise, animate a wrapper property (e.g., opacity), not the variable itself.

---

## Key Takeaways
- CSS transitions for state-driven (class toggle). Keyframes for multi-step/repeating.
- Unmount animations need exiting state + timer or onAnimationEnd
- Transition only `transform` and `opacity` for GPU-composited performance
- View Transitions API for page-level transitions (newer, React 19+)
- CSS animations are zero-dependency, Framer Motion for complex motion

---

## Common Misconception

**"CSS animations are always better than JS animations."**

Not true. CSS animations are better for simple declarative motion. JS animation libraries (Framer Motion, GSAP) handle: spring physics, gesture-driven drag, sequencing, shared layout animations, SVG morphing. Choose by complexity.

---

## Feynman Explain
(Explain: why does a toast need "exiting" state? Why doesn't React handle unmount animations automatically?)

---

## Drill
Take the quiz.

## Quiz: 11-animations-react-css

<p class="quiz-question">How do you trigger a CSS transition in React when state changes?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Call animate() function in useEffect</p>

<p class="quiz-option"><strong>B.</strong> Toggle a CSS class based on state</p>

<p class="quiz-option"><strong>C.</strong> CSS transitions fire automatically on state change</p>

<p class="quiz-option"><strong>D.</strong> Use setTimeout to apply styles</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">State change → conditional className → element gets new class → CSS transition interpolates between old/new property values.</p>

<hr/>

<p class="quiz-question">Why can't CSS animate max-height from 0 to auto?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> auto is not a numeric value — CSS can't interpolate</p>

<p class="quiz-option"><strong>B.</strong> Transitions don't work with max-height</p>

<p class="quiz-option"><strong>C.</strong> CSS only animates opacity</p>

<p class="quiz-option"><strong>D.</strong> It works — statement is false</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">CSS transitions require numeric start/end values. auto is not numeric. Use max-height: 500px (larger than actual content) or grid-template-rows transition.</p>

<hr/>

<p class="quiz-question">What's needed for unmount animation in React?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Nothing — CSS handles all animations</p>

<p class="quiz-option"><strong>B.</strong> Exiting state to apply exit animation class, then remove after animation</p>

<p class="quiz-option"><strong>C.</strong> Use setTimeout only</p>

<p class="quiz-option"><strong>D.</strong> Use React's onUnmount prop</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">React removes elements immediately — exit animation never plays. Pattern: set 'exiting' state → apply exit className → onAnimationEnd/delayed cleanup removes element.</p>

<hr/>

<p class="quiz-question">Which event fires when a CSS keyframe animation completes?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> onAnimationEnd</p>

<p class="quiz-option"><strong>B.</strong> onTransitionEnd</p>

<p class="quiz-option"><strong>C.</strong> onAnimationComplete</p>

<p class="quiz-option"><strong>D.</strong> onFinish</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">onAnimationEnd fires when a CSS animation (@keyframes) finishes. onTransitionEnd fires for CSS transitions. Don't confuse them.</p>

<hr/>

<p class="quiz-question">Which CSS properties are GPU-composited (safe to animate)?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> width, height</p>

<p class="quiz-option"><strong>B.</strong> transform, opacity</p>

<p class="quiz-option"><strong>C.</strong> margin, padding</p>

<p class="quiz-option"><strong>D.</strong> font-size, line-height</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">transform and opacity are composited on GPU — no layout recalc. Width/height/margin/padding trigger layout reflow every frame.</p>

<hr/>

<p class="quiz-question">When should you use Framer Motion over CSS animations?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> For simple enter/exit transitions</p>

<p class="quiz-option"><strong>B.</strong> For gesture-driven animations (drag, spring physics)</p>

<p class="quiz-option"><strong>C.</strong> For hover effects</p>

<p class="quiz-option"><strong>D.</strong> Never — CSS is always better</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">CSS for declarative motion (transitions, keyframes). Framer Motion for gesture-driven, physics-based, or shared layout animations that need JavaScript coordination.</p>


---

# Module 12: CSS Testing in React Apps

Est. study time: 2.5h
Language: en

## Learning Objectives
- Implement visual regression testing for React components
- Write unit tests for CSS-in-JS and CSS Modules
- Audit CSS for accessibility and layout breakpoints
- Decide what to test vs trust

---

## Core Content

### Testing Pyramid for CSS

CSS testing has distinct layers:

```text
       ┌──────────┐
       │  Visual  │  ← Catch visual bugs humans miss
       │  Regr.   │
      ┌┴──────────┴┐
      │  Layout    │  ← Responsive breakpoints, overflow
      │  Tests     │
     ┌┴────────────┴┐
     │  A11y       │  ← Color contrast, focus indicators
     │  Audit      │
    ┌┴──────────────┴┐
    │  Unit Tests   │  ← Class merging, variant output
    │  (CSS-in-JS)  │
   ┌┴────────────────┴┐
   │ TypeScript/Lint  │  ← Typo prevention at compile time
   └──────────────────┘
```

**What to test:**
- Visual output (screenshot comparisons)
- Responsive behavior at breakpoints
- Color contrast ratios
- CSS-in-JS variant logic (conditional class merging)

**What NOT to test:**
- Fundamental CSS property behavior (does `display: flex` work? — trust the browser)
- Exact pixel values (test visual diff tolerance, not pixel numbers)
- Third-party CSS (reset, Tailwind utilities — trust the library)

> **Think**: You write a unit test: `expect(styles.button).toBe('Button_button_abc123')`. Is this useful?
>
> *Answer: No. The class name is an implementation detail. Test the visual output or behavior, not generated class names.*

### Visual Regression Testing

Compare screenshots of components across commits. If component renders differently, test fails.

**Playwright** (most common 2026):

```tsx
// Button.spec.tsx
import { test, expect } from '@playwright/experimental-ct-react';
import Button from './Button';

test('renders primary variant', async ({ mount }) => {
  const component = await mount(<Button variant="primary">Submit</Button>);
  await expect(component).toHaveScreenshot('button-primary.png');
});

test('renders disabled state', async ({ mount }) => {
  const component = await mount(<Button disabled>Submit</Button>);
  await expect(component).toHaveScreenshot('button-disabled.png');
});
```

**Chromatic** (Storybook-based):

```tsx
// Button.stories.tsx
export default { component: Button };

export const Primary = { args: { variant: 'primary', children: 'Submit' } };
export const Disabled = { args: { disabled: true, children: 'Submit' } };
// Chromatic auto-captures screenshots per story
```

**Setup considerations:**
- Use deterministic font loading (system fonts vary per OS)
- Mock random values (colors, dimensions from data)
- Set viewport size explicitly per test
- Use `--update-snapshots` to update baselines after intentional changes

> **Think**: A button's box-shadow changes from 2px to 4px intentionally. What happens to visual regression tests?
>
> *Answer: They fail. Dev reviews the diff, confirms it's intentional, and updates the golden screenshots. This is correct behavior — VRT should fail on ANY visual change, intentional or not.*

### Layout Breakpoint Tests

Test that components respond correctly at breakpoints:

```tsx
import { test, expect } from '@playwright/test';

test('card grid switches to single column on mobile', async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 800 });
  await page.goto('/products');
  const grid = page.locator('.product-grid');
  await expect(grid).toHaveCSS('grid-template-columns', '1fr');
});

test('card grid shows 3 columns on desktop', async ({ page }) => {
  await page.setViewportSize({ width: 1280, height: 800 });
  await page.goto('/products');
  const grid = page.locator('.product-grid');
  await expect(grid).toHaveCSS('grid-template-columns', 'repeat(3, 1fr)');
});
```

**What to assert**: `grid-template-columns`, `flex-direction`, `display`, `visibility`. Not exact pixel values.

### Accessibility Audit

```tsx
import { test, expect } from '@playwright/test';

test('button has sufficient color contrast', async ({ page }) => {
  await page.goto('/');
  const button = page.locator('button.submit');
  const bg = await button.evaluate(el => getComputedStyle(el).backgroundColor);
  const color = await button.evaluate(el => getComputedStyle(el).color);
  // contrast ratio > 4.5:1 for normal text (AA)
  const ratio = getContrastRatio(bg, color);
  expect(ratio).toBeGreaterThanOrEqual(4.5);
});

test('focus indicator is visible', async ({ page }) => {
  await page.goto('/');
  const button = page.locator('button.submit');
  await button.focus();
  const outline = await button.evaluate(el => getComputedStyle(el).outline);
  expect(outline).not.toBe('none');
});
```

Use `axe-core` for automated a11y audit:

```tsx
import { injectAxe, checkA11y } from 'axe-playwright';

test('page has no a11y violations', async ({ page }) => {
  await page.goto('/');
  await injectAxe(page);
  await checkA11y(page, {
    includedImpacts: ['critical', 'serious'],
  });
});
```

### CSS-in-JS Unit Tests

For styled-components, Emotion, Vanilla Extract recipes — test the variant logic, not the CSS output:

```tsx
// Button.tsx — recipe-based
const button = recipe({
  base: { /* ... */ },
  variants: {
    variant: {
      primary: { background: 'blue' },
      danger: { background: 'red' },
    },
  },
});

// Test variant class resolution (unit test):
test('button recipe returns correct variant classes', () => {
  expect(button({ variant: 'primary' })).toContain('primary');
  expect(button({ variant: 'danger' })).toContain('danger');
});
```

**Do NOT test:**
- That `background: blue` renders as blue (browser renders it)
- That CSS property works (trust the spec)
- Exact class names (they change with hash)

**DO test:**
- Conditional class merging (does `isActive && styles.active` apply correctly?)
- twMerge conflict resolution
- cva variant selection

### Testing Tailwind Components

```tsx
import { render, screen } from '@testing-library/react';
import Button from './Button';

test('applies correct classes for primary variant', () => {
  render(<Button variant="primary">Submit</Button>);
  const btn = screen.getByRole('button');
  // Check rendered className string
  expect(btn.className).toContain('bg-blue-500');
});

test('merges consumer className with twMerge', () => {
  render(<Button className="bg-red-500">Submit</Button>);
  const btn = screen.getByRole('button');
  // bg-red-500 should override — NOT both present
  expect(btn.className).not.toMatch(/bg-blue-500/);
});
```

### What to Skip Testing

| Don't test | Reason |
|-----------|--------|
| Browser rendering of CSS properties | Trust the spec |
| Class name hashes | Implementation detail |
| Tailwind utility behavior | Trust framework |
| Third-party CSS | Out of scope |
| Exact font rendering | OS/device dependent |

---

### Why This Matters

CSS bugs are uniquely hard to debug — they manifest visually, cascade unpredictably, and often don't crash. Testing CSS prevents: "it worked in my browser" regressions, accessibility failures, and responsive breakpoint issues that reach production.

---

### Common Questions

**Q: Do I need visual regression tests for every component?**
A: Critical path components (buttons, inputs, layout) yes. Utility components (Stack, Flex) — less value. Prioritize visual impact.

**Q: How often do visual regression tests break from changes?**
A: Frequently at first. As the baseline stabilizes, most failures are intentional changes that need snapshot updates. The value is catching the UNINTENTIONAL diff.

---

## Key Takeaways
- VRT captures visual regressions — use Playwright or Chromatic
- Layout tests assert grid/flex behavior at breakpoints
- a11y audit with axe-core for automated contrast/role checks
- Unit test variant logic, not CSS property output
- Skip: browser rendering, hash values, third-party CSS

---

## Common Misconception

**"I need to test every CSS property my component uses."**

No. Test behavior, not implementation. "Does the button change color when disabled?" is a test. "Does this CSS class have `opacity: 0.5`?" is brittle. The first catches real bugs; the second breaks on every refactor.

---

## Feynman Explain
(Explain: "CSS testing" sounds like testing the browser. What are we actually testing? The component's visual contract.)

---

## Drill
Take the quiz.

## Quiz: 12-css-testing-react

<p class="quiz-question">What do visual regression tests compare?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> CSS property values</p>

<p class="quiz-option"><strong>B.</strong> Component screenshots against golden baselines</p>

<p class="quiz-option"><strong>C.</strong> Class name strings</p>

<p class="quiz-option"><strong>D.</strong> Bundle size</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">VRT captures screenshots of components and compares to stored baselines. Any pixel difference fails the test.</p>

<hr/>

<p class="quiz-question">When a visual regression test fails, what's the correct response?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Update golden snapshot if the visual change is intentional</p>

<p class="quiz-option"><strong>B.</strong> Revert the code change</p>

<p class="quiz-option"><strong>C.</strong> Ignore — tests are flaky</p>

<p class="quiz-option"><strong>D.</strong> Delete the snapshot</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">Review the diff. If intentional (design change), update baseline. If unintentional (bug caused visual change), fix the code.</p>

<hr/>

<p class="quiz-question">What should you NOT test in CSS unit tests?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Conditional class merging logic</p>

<p class="quiz-option"><strong>B.</strong> Variant selection (correct class for variant)</p>

<p class="quiz-option"><strong>C.</strong> Browser rendering of display: flex</p>

<p class="quiz-option"><strong>D.</strong> twMerge conflict resolution</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">Trust the browser's CSS engine. Testing that display: flex works is testing the browser, not your code. Test your component's variant logic and class merging.</p>

<hr/>

<p class="quiz-question">Which tool provides automated accessibility audits?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Playwright only</p>

<p class="quiz-option"><strong>B.</strong> axe-core</p>

<p class="quiz-option"><strong>C.</strong> Tailwind CSS</p>

<p class="quiz-option"><strong>D.</strong> clsx</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">axe-core automates accessibility checks: contrast ratios, ARIA roles, keyboard navigation, focus indicators. Integrates with Playwright or Cypress.</p>

<hr/>

<p class="quiz-question">How do you test responsive breakpoint behavior?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Assert grid-template-columns at different viewport sizes</p>

<p class="quiz-option"><strong>B.</strong> Take screenshots at every breakpoint</p>

<p class="quiz-option"><strong>C.</strong> Mock window.innerWidth</p>

<p class="quiz-option"><strong>D.</strong> Responsive behavior is untestable</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">Set viewport size with page.setViewportSize(), assert CSS property values like grid-template-columns or flex-direction at each breakpoint.</p>

<hr/>

<p class="quiz-question">A Button changes primary bg from blue to green. What tests catch this?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Unit test — expect(BUTTON.bg).toBe('green')</p>

<p class="quiz-option"><strong>B.</strong> Visual regression — screenshot comparison shows diff</p>

<p class="quiz-option"><strong>C.</strong> TypeScript — color type changed</p>

<p class="quiz-option"><strong>D.</strong> Bundle analysis — CSS file size changed</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">VRT catches the visual change automatically. Unit test testing specific color values would need manual update — VRT surfaces ALL visual diffs regardless of which property changed.</p>

<hr/>

<p class="quiz-question">Why should you NOT test generated CSS Module class names?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Class names are hashed — change with every build</p>

<p class="quiz-option"><strong>B.</strong> They are never visible to users</p>

<p class="quiz-option"><strong>C.</strong> CSS Modules don't generate class names</p>

<p class="quiz-option"><strong>D.</strong> They are not strings</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">CSS Module class names include content hashes that change when CSS changes. Testing the exact hash is brittle. Test behavior or visual output instead.</p>


---

# Module 13: Utility Libraries for React CSS

Est. study time: 2h
Language: en

## Learning Objectives
- Choose between clsx, classnames, tailwind-merge, and cva
- Apply conditional class merging correctly
- Assess bundle cost vs ergonomics per library

---

## Core Content

### The Problem Utility Libraries Solve

React JSX builds className strings from conditions:

```tsx
// Without utility — manual string construction:
className={[
  'btn',
  variant === 'primary' && 'btn-primary',
  size === 'lg' && 'btn-lg',
  disabled && 'btn-disabled',
].filter(Boolean).join(' ')}
```

Each utility library simplifies this differently.

### clsx (Most Popular 2026)

Tiny (~228 B gzip). Handles strings, arrays, objects, booleans:

```tsx
import clsx from 'clsx';

clsx('btn', variant === 'primary' && 'btn-primary', disabled && 'btn-disabled');
// → "btn btn-primary btn-disabled"

clsx(['btn', 'btn-lg'], { 'btn-disabled': disabled });
// → "btn btn-lg btn-disabled" (if disabled true)
```

**When to use**: Any React app. It's the universal conditional class utility. No Tailwind dependency needed.

**Bundle**: ~228 B gzip. Effectively free.

### classnames (Legacy, Still Used)

Older API, slightly larger (~428 B gzip):

```tsx
import classnames from 'classnames';

classnames('btn', { 'btn-primary': variant === 'primary' });
```

**Tradeoff**: Same functionality as clsx, but larger. clsx is the modern replacement. Only use if existing codebase already uses classnames.

### tailwind-merge (Tailwind Conflict Resolution)

Resolves conflicting Tailwind classes:

```tsx
import { twMerge } from 'tailwind-merge';

twMerge('px-4 py-2', 'px-6'); // → "py-2 px-6"
// px-6 overrides px-4 intelligently
```

Without twMerge: `className="px-4 px-6"` → CSS source order determines which padding wins (unpredictable).
With twMerge: later className overrides earlier predictably.

**When to use**: Any app using Tailwind where className overrides happen.

**Bundle**: ~6 kB gzip. Not free, but small relative to Tailwind's CSS output.

### cva (class-variance-authority)

Defines type-safe component variants:

```tsx
import { cva, type VariantProps } from 'class-variance-authority';

const button = cva('rounded-md font-medium', {
  variants: {
    variant: {
      primary: 'bg-blue-500 text-white',
      danger: 'bg-red-500 text-white',
    },
    size: {
      sm: 'px-3 py-1 text-sm',
      lg: 'px-6 py-3 text-lg',
    },
  },
  defaultVariants: { variant: 'primary', size: 'sm' },
});

// VariantProps<typeof button> → TypeScript type for props
type ButtonProps = VariantProps<typeof button> & { children: React.ReactNode };
```

**When to use**: Components with multiple variant dimensions. Co-locates variant definitions with component.

**Bundle**: ~1.3 kB gzip.

### Bundle Cost Summary

| Library | gzip | Purpose | When |
|---------|------|---------|------|
| clsx | 228 B | Conditional class merging | Always |
| classnames | 428 B | Same as clsx | Legacy only |
| tailwind-merge | 6 kB | Tailwind conflict resolution | Tailwind apps with overrides |
| cva | 1.3 kB | Type-safe variant definitions | Multi-variant components |

### Composition Pattern

Combine them:

```tsx
import { twMerge } from 'tailwind-merge';
import { cva, type VariantProps } from 'class-variance-authority';
import clsx from 'clsx';

const button = cva('rounded-md font-medium', {
  variants: {
    variant: {
      primary: 'bg-blue-500 text-white hover:bg-blue-600',
      danger: 'bg-red-500 text-white hover:bg-red-600',
    },
  },
});

function Button({ variant, className, children }: ButtonProps) {
  return (
    <button className={twMerge(button({ variant }), className)}>
      {children}
    </button>
  );
}
```

`cva` handles variant logic. `twMerge` handles consumer overrides. `clsx` handles any additional conditions.

### Condition Merging Pitfalls

```tsx
// BAD — clsx doesn't resolve Tailwind conflicts:
clsx('px-4', 'px-6') // → "px-4 px-6" — both present, browser decides

// GOOD — twMerge resolves:
twMerge('px-4', 'px-6') // → "px-6"
```

```tsx
// BAD — clsx includes false values:
clsx(false && 'hidden') // → "" — but '' is still a class attribute

// GOOD — clsx handles booleans correctly:
clsx(disabled && 'disabled') // → "disabled" or ""
```

> **Think**: When would you NOT use twMerge for Tailwind components?
>
> *Answer: When there's no possibility of conflicting classes. Simple components with one variant dimension don't need twMerge. It adds 6 kB for no benefit.*

---

### Why This Matters

Utility libraries are small but impactful. clsx saves 2 lines of filter/join boilerplate per component. twMerge prevents a class of subtle CSS bugs. cva makes variant props type-safe. The small costs (228 B to 6 kB) are among the best ergonomics-per-byte investments in a React app.

---

### Common Questions

**Q: Should I use clsx or twMerge everywhere?**
A: clsx everywhere. twMerge only in component APIs that accept consumer className overrides (i.e., the component that calls twMerge). Internal components don't need it.

**Q: Is cva only for Tailwind?**
A: No. cva returns class strings — works with CSS Modules, Vanilla Extract, plain CSS. Any approach that uses className.

---

## Key Takeaways
- clsx: universal conditional class merging (228 B). Use everywhere.
- twMerge: Tailwind conflict resolution (6 kB). Use at component API boundary.
- cva: type-safe variant definitions (1.3 kB). Use for multi-variant components.
- classnames: legacy alternative to clsx. Don't choose for new projects.
- Combine: cva(def) → twMerge(cva(), consumerClass)

---

## Common Misconception

**"twMerge replaces clsx."**

Not replacement — different purpose. clsx handles "should this class be in the string?" twMerge handles "which of these conflicting classes wins?" Use both. clsx for conditional logic, twMerge for conflict resolution.

---

## Feynman Explain
(Explain: clsx is for building class strings from conditions. twMerge is for resolving conflicts when multiple classes set the same property. Different tools.)

---

## Drill
Take the quiz.

## Quiz: 13-utility-libraries-react-css

<p class="quiz-question">What does clsx do?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Resolves conflicting Tailwind classes</p>

<p class="quiz-option"><strong>B.</strong> Builds class strings from conditional values</p>

<p class="quiz-option"><strong>C.</strong> Generates CSS Module types</p>

<p class="quiz-option"><strong>D.</strong> Minifies CSS class names</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">clsx takes strings, arrays, objects, and boolean conditions, returning a single className string. 'btn' &amp;&amp; 'active' → 'btn active' or 'btn'.</p>

<hr/>

<p class="quiz-question">clsx vs classnames — which is preferred for new projects?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> classnames — it's older and more stable</p>

<p class="quiz-option"><strong>B.</strong> clsx — smaller (~228 B vs ~428 B), same functionality</p>

<p class="quiz-option"><strong>C.</strong> Both — use interchangeably</p>

<p class="quiz-option"><strong>D.</strong> Neither — always use twMerge</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">clsx is ~200 B smaller with the same API. classnames is legacy. For new projects, clsx is the standard.</p>

<hr/>

<p class="quiz-question">What problem does twMerge solve that clsx doesn't?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Merging objects</p>

<p class="quiz-option"><strong>B.</strong> Resolving conflicting Tailwind utility classes</p>

<p class="quiz-option"><strong>C.</strong> Booleans in class strings</p>

<p class="quiz-option"><strong>D.</strong> Array class inputs</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">clsx concatenates — 'px-4 px-6' remains both classes. twMerge detects conflicts and keeps only the last (intended) value. Different purposes.</p>

<hr/>

<p class="quiz-question">When should twMerge be used?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Every className in the app</p>

<p class="quiz-option"><strong>B.</strong> Component APIs that accept consumer className overrides</p>

<p class="quiz-option"><strong>C.</strong> Only with styled-components</p>

<p class="quiz-option"><strong>D.</strong> Never — clsx is sufficient</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">twMerge at the component boundary where consumer className merges with defaults. Internal components don't need it. Adds 6 kB — don't use without need.</p>

<hr/>

<p class="quiz-question">cva provides what feature?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> CSS variable management</p>

<p class="quiz-option"><strong>B.</strong> Type-safe component variant definitions</p>

<p class="quiz-option"><strong>C.</strong> CSS Module compilation</p>

<p class="quiz-option"><strong>D.</strong> Tailwind config generation</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">cva defines variants with TypeScript types. Invalid variant name → compile error. Useful for multi-variant components.</p>

<hr/>

<p class="quiz-question">A component needs: variant prop (3 values) + size prop (3 values) + consumer className override. What's the tool stack?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> cva + twMerge</p>

<p class="quiz-option"><strong>B.</strong> clsx only</p>

<p class="quiz-option"><strong>C.</strong> classnames + twMerge</p>

<p class="quiz-option"><strong>D.</strong> Inline conditional operators</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">cva defines variants (type-safe). twMerge merges variant class string with consumer className. clsx could also be needed for additional runtime conditions.</p>

<hr/>

<p class="quiz-question">Bundle cost of clsx + twMerge + cva together?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> ~7.5 kB gzip</p>

<p class="quiz-option"><strong>B.</strong> ~30 kB gzip</p>

<p class="quiz-option"><strong>C.</strong> ~1 kB gzip</p>

<p class="quiz-option"><strong>D.</strong> ~15 kB gzip</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">clsx (228 B) + twMerge (6 kB) + cva (1.3 kB) = ~7.5 kB gzip total. Modest cost for significant DX improvement.</p>


---

# Module 14: Performance & CSS Bundle in React

Est. study time: 2h
Language: en

## Learning Objectives
- Implement critical CSS extraction in SSR
- Code-split CSS per lazy-loaded route
- Eliminate unused CSS with tools
- Apply CSS containment for rendering performance

---

## Core Content

### Critical CSS

CSS blocks rendering. Browser must download and parse CSS before painting. For large apps, this delays first paint.

**Critical CSS**: Inline styles needed for above-the-fold content in `<head>`. Defer the rest.

```html
<!-- Inlined critical CSS (first paint) -->
<style>
  header { display: flex; ... }
  .hero { font-size: 2rem; ... }
</style>
<!-- Deferred non-critical CSS -->
<link rel="preload" href="/styles.css" as="style" onload="this.rel='stylesheet'">
```

**In Next.js**: Built-in. Automatic critical CSS extraction. No manual setup.

**In Vite**: Use `vite-plugin-critical` or manual extraction.

**Manual extraction**: Tools like `critical` (Node.js) analyze a page at a viewport, extract used styles, inline them.

> **Think**: A 200 kB CSS file blocks rendering. Critical CSS inlines 15 kB for first viewport. What's the improvement?
>
> *Answer: First paint happens after 15 kB instead of 200 kB. On 3G (2 Mbps), that's ~60ms vs ~800ms. Remaining CSS loads non-blocking (preload → switch).*

### CSS Code Splitting

Route-based CSS splitting: each lazy-loaded page/component loads its CSS only when needed.

**CSS Modules naturally code-split** — each component's CSS is a separate file. Bundlers (Next.js, Vite) extract component CSS into per-chunk files.

```tsx
// Lazy component — its .module.css loads only when this chunk loads
const Dashboard = lazy(() => import('./Dashboard'));
```

**With Tailwind**: JIT generates one CSS file containing all used utilities. No per-component splitting. Solution: split into separate entry points or use multiple CSS files per route.

**With styled-components**: All styles merge into one `<style>` tag. No code-splitting — all styles load with first JS bundle.

### Unused CSS Elimination

- **Tailwind JIT**: Only generates used classes — effectively zero unused CSS
- **PurgeCSS**: For hand-written CSS, scans files and removes unused selectors

```js
// postcss.config.js — manual PurgeCSS
module.exports = {
  plugins: [
    require('@fullhuman/postcss-purgecss')({
      content: ['./src/**/*.{tsx,ts}'],
      defaultExtractor: content => content.match(/[\w-/:]+(?<!:)/g) || [],
    }),
  ],
};
```

**Gains**: Hand-written CSS can be 50-80% unused. PurgeCSS drops unused selectors — typically reduces 100 kB → 20 kB.

### CSS Containment

`content-visibility: auto` skips rendering of off-screen elements:

```css
.product-card {
  content-visibility: auto;
  contain-intrinsic-size: 200px; /* placeholder size before rendering */
}
```

Browser renders only visible cards + a few off-screen. Scrolling triggers progressive rendering.

**In React list**:

```tsx
function ProductList({ products }) {
  return (
    <div className="product-grid">
      {products.map(p => (
        <div key={p.id} className="product-card">
          <ProductCard product={p} />
        </div>
      ))}
    </div>
  );
}
```

For 500 products, content-visibility reduces initial render cost from 500 cards to ~20 (viewport + buffer).

### Bundle Impact by CSS Approach

| Approach | CSS in JS bundle | CSS file size | Code-split |
|----------|-----------------|---------------|------------|
| Plain CSS | 0 kB | Full authored | Manual |
| CSS Modules | 0 kB | Per component | Automatic |
| Tailwind | 0 kB | 5-15 kB total | Manual per page |
| Runtime CSS-in-JS | Library + CSS strings | N/A | No (global style tag) |
| Vanilla Extract | 0 kB | Per component | Automatic |

> **Think**: An app loads 10 screens. Total authored CSS: 200 kB. With CSS Modules/Vite, what loads on first page?
>
> *Answer: Only the CSS for components rendered on the first page (~20-30 kB). Other screens' CSS loads with their JS chunks. Tailwind would load all 10 pages' utilities (~10-15 kB because purged). Runtime CSS-in-JS loads all CSS strings with the initial JS bundle.*

### Avoiding Layout Shifts (CLS)

- Set explicit dimensions on images: `<img width="400" height="300" />`
- Use `aspect-ratio` CSS property for dynamic content
- Avoid injecting dynamic content above static content without placeholder dimensions

### Animation Performance

- **`transform` and `opacity` only**: GPU composited, no layout/reflow
- **Avoid animating**: `width`, `height`, `top`, `left`, `margin`, `padding`
- **`will-change`**: Use sparingly — only for elements that DO animate

```css
.toast {
  transform: translateX(100%);
  transition: transform 0.3s ease; /* GPU composited */
}
```

---

### Why This Matters

CSS performance is often the last optimization. But CSS is a render-blocking resource — a slow CSS load directly delays every user interaction. In React, CSS bundle strategy is determined by your styling approach choice (Module 1). You can't optimize CSS in isolation from architecture.

---

### Key Takeaways
- Critical CSS inlines first-viewport styles — built into Next.js, manual in Vite
- CSS Modules/Vanilla Extract code-split automatically per component/route
- Tailwind JIT eliminates unused CSS by construction
- content-visibility: auto skips off-screen rendering (big gains for long lists)
- Avoid animating layout-triggering properties — use transform/opacity

---

## Common Misconception

**"CSS performance doesn't matter because CSS is small."**

CSS file size is only part. CSS is render-blocking — every kB delays first paint. On slow networks, large CSS files directly increase Time to First Contentful Paint (FCP). An app with 200 kB CSS loads text in ~800ms on 3G vs ~150ms for a critical-CSS-optimized app.

---

## Drill
Take the quiz.

## Quiz: 14-performance-css-bundle

<p class="quiz-question">Why is CSS render-blocking a performance concern?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> CSS files are always large</p>

<p class="quiz-option"><strong>B.</strong> Browser delays first paint until CSS is downloaded and parsed</p>

<p class="quiz-option"><strong>C.</strong> CSS blocks JavaScript execution</p>

<p class="quiz-option"><strong>D.</strong> CSS can't be cached</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">CSS is a render-blocking resource. Browser won't paint until all CSS is loaded and parsed. Delaying first paint directly increases FCP.</p>

<hr/>

<p class="quiz-question">What does critical CSS inlining do?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Puts all CSS in a single file</p>

<p class="quiz-option"><strong>B.</strong> Inlines only above-the-fold styles in &lt;head&gt;, defers the rest</p>

<p class="quiz-option"><strong>C.</strong> Removes all CSS from the page</p>

<p class="quiz-option"><strong>D.</strong> Converts CSS to inline styles</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Extracts styles needed for initial viewport content, inlines them in &lt;head&gt; for immediate paint. Remaining CSS loads asynchronously.</p>

<hr/>

<p class="quiz-question">Which CSS approach automatically code-splits per lazy-loaded component?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Runtime CSS-in-JS</p>

<p class="quiz-option"><strong>B.</strong> CSS Modules</p>

<p class="quiz-option"><strong>C.</strong> Tailwind (single file)</p>

<p class="quiz-option"><strong>D.</strong> Sass (single file)</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">CSS Modules bundle tools generate separate CSS per component/lazy chunk. Loads only when component loads. Runtime CSS-in-JS and Tailwind single file load all at once.</p>

<hr/>

<p class="quiz-question">What does content-visibility: auto do?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Makes content invisible</p>

<p class="quiz-option"><strong>B.</strong> Skips rendering of off-screen elements</p>

<p class="quiz-option"><strong>C.</strong> Hides content for search engines</p>

<p class="quiz-option"><strong>D.</strong> Automatically generates CSS</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Browser only renders elements near viewport. Off-screen elements skip rendering until scrolled near. contain-intrinsic-size reserves placeholder space.</p>

<hr/>

<p class="quiz-question">Which CSS approaches contribute ZERO CSS to the JavaScript bundle?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Plain CSS, CSS Modules, Tailwind, Vanilla Extract</p>

<p class="quiz-option"><strong>B.</strong> Runtime CSS-in-JS only</p>

<p class="quiz-option"><strong>C.</strong> All approaches include CSS in JS bundle</p>

<p class="quiz-option"><strong>D.</strong> Only plain CSS has zero JS bundle</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">Plain CSS, CSS Modules, Tailwind, and Vanilla Extract all output separate .css files. Runtime CSS-in-JS keeps CSS strings in the JS bundle.</p>

<hr/>

<p class="quiz-question">How do you avoid layout shift (CLS) when images load?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Set explicit width/height attributes on &lt;img&gt;</p>

<p class="quiz-option"><strong>B.</strong> Use CSS display: none initially</p>

<p class="quiz-option"><strong>C.</strong> Load images with JavaScript after paint</p>

<p class="quiz-option"><strong>D.</strong> CLS is unavoidable</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">Set width and height attributes or CSS aspect-ratio. Browser reserves the space before image loads, preventing layout shift when image arrives.</p>

<hr/>

<p class="quiz-question">Tailwind JIT output for a 10-page app is typically:</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> 50-100 kB — all utilities ever generated</p>

<p class="quiz-option"><strong>B.</strong> 5-15 kB gzip — only used utilities</p>

<p class="quiz-option"><strong>C.</strong> 0 kB — Tailwind has no CSS output</p>

<p class="quiz-option"><strong>D.</strong> Same as authored Tailwind classes size</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">JIT generates only utilities found in source files. 5-15 kB gzip is typical for most apps. Much smaller than hand-written CSS with similar coverage.</p>


---

# Module 15: Capstone — Production React Component Library

Est. study time: 3h
Language: en

## Learning Objectives
- Integrate CSS approach, theming, testing, and performance decisions
- Build a themed, tested, performant component library
- Document tradeoff decisions made across modules

---

## Core Content

### Capstone Overview

Build a React component library (Button + Card + Layout primitives) that demonstrates:
- CSS approach decision based on tradeoff analysis
- CSS custom property theming
- Container query responsiveness
- Visual regression + a11y testing
- Utility library integration (clsx, twMerge, cva)

You'll make deliberate choices at each step, then justify them.

### Step 1: Choose CSS Approach

**Context**: Shared library consumed by 3 apps (React SPA, Next.js RSC, Vite Vue app — via wrapper). Need: zero dependency, theming, type safety.

**Decision**: CSS Modules + CSS custom properties.
- Rationale: Zero runtime, RSC-compatible, no library dependency for consumers
- CSS Custom properties for theming (override at consumer level)
- `cva` for variant definitions (build + runtime = type-safe variants)

### Step 2: Design Token Architecture

```css
/* tokens.css — published as part of library */
:root {
  --ds-color-primary: #6366f1;
  --ds-color-primary-hover: #4f46e5;
  --ds-color-danger: #ef4444;
  --ds-color-surface: #ffffff;
  --ds-color-text: #0f172a;
  --ds-space-xs: 4px;
  --ds-space-sm: 8px;
  --ds-space-md: 16px;
  --ds-space-lg: 24px;
  --ds-radius-sm: 4px;
  --ds-radius-md: 8px;
  --ds-font-body: 16px;
}
```

Consumers override any token:

```css
/* Consumer app */
:root { --ds-color-primary: #7c3aed; }
```

### Step 3: Button Component

```tsx
// Button.tsx
import { cva, type VariantProps } from 'class-variance-authority';
import { twMerge } from 'tailwind-merge';
import styles from './Button.module.css';

const buttonVariants = cva(styles.base, {
  variants: {
    variant: {
      primary: styles.primary,
      danger: styles.danger,
      outline: styles.outline,
    },
    size: {
      sm: styles.sm,
      md: styles.md,
      lg: styles.lg,
    },
  },
  defaultVariants: { variant: 'primary', size: 'md' },
});

type ButtonProps = VariantProps<typeof buttonVariants> & {
  className?: string;
  children: React.ReactNode;
  disabled?: boolean;
};

export function Button({ variant, size, className, disabled, children }: ButtonProps) {
  return (
    <button
      className={twMerge(buttonVariants({ variant, size }), disabled && styles.disabled, className)}
      disabled={disabled}
    >
      {children}
    </button>
  );
}
```

```css
/* Button.module.css */
.base {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--ds-space-sm);
  border-radius: var(--ds-radius-md);
  font-size: var(--ds-font-body);
  border: 1px solid transparent;
  cursor: pointer;
  transition: background 0.15s, opacity 0.15s;
}
.primary { background: var(--ds-color-primary); color: white; }
.primary:hover { background: var(--ds-color-primary-hover); }
.danger { background: var(--ds-color-danger); color: white; }
.outline { background: transparent; border-color: var(--ds-color-primary); color: var(--ds-color-primary); }
.sm { padding: var(--ds-space-xs) var(--ds-space-sm); font-size: 14px; }
.md { padding: var(--ds-space-sm) var(--ds-space-md); }
.lg { padding: var(--ds-space-md) var(--ds-space-lg); font-size: 18px; }
.disabled { opacity: 0.5; pointer-events: none; }
```

### Step 4: Card with Container Query

```tsx
// Card.tsx
import styles from './Card.module.css';

type CardProps = {
  variant?: 'default' | 'elevated';
  children: React.ReactNode;
  className?: string;
};

export function Card({ variant = 'default', children, className }: CardProps) {
  return (
    <div className={twMerge(styles.card, variant === 'elevated' && styles.elevated, className)}>
      {children}
    </div>
  );
}
```

```css
/* Card.module.css */
.card {
  container-type: inline-size;
  background: var(--ds-color-surface);
  border: 1px solid var(--ds-color-border, #e2e8f0);
  border-radius: var(--ds-radius-md);
  padding: var(--ds-space-md);
  color: var(--ds-color-text);
}
.elevated { box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
@container (max-width: 300px) {
  .card { padding: var(--ds-space-sm); }
}
```

### Step 5: Layout Primitives

```tsx
// Stack.tsx — ${\text{see Module 9}}$
// Flex.tsx
// Grid.tsx
```

Import from a `primitives/` directory. Each uses CSS Modules + CSS custom properties for spacing.

### Step 6: Testing

```tsx
// Button.spec.tsx — Playwright
test('renders primary variant', async ({ mount }) => {
  const component = await mount(<Button>Click</Button>);
  await expect(component).toHaveScreenshot();
});

test('renders disabled state', async ({ mount }) => {
  const component = await mount(<Button disabled>Click</Button>);
  await expect(component).toHaveScreenshot();
});

test('applies consumer className correctly', async ({ mount }) => {
  const component = await mount(<Button className="custom-class">Click</Button>);
  await expect(component).toHaveClass(/custom-class/);
});

// A11y
test('has no a11y violations', async ({ mount }) => {
  const component = await mount(<Button>Click</Button>);
  await expect(component).toPassAxe();
});
```

```tsx
// Card.spec.tsx — responsive
test('adapts padding at narrow container', async ({ mount }) => {
  // Mount inside 200px container
  const component = await mount(
    <div style={{ width: '200px' }}>
      <Card>Content</Card>
    </div>
  );
  await expect(component).toHaveScreenshot('card-narrow.png');
});

test('adapts padding at wide container', async ({ mount }) => {
  const component = await mount(
    <div style={{ width: '500px' }}>
      <Card>Content</Card>
    </div>
  );
  await expect(component).toHaveScreenshot('card-wide.png');
});
```

### Step 7: Performance Verification

```tsx
test('Button component CSS is not render-blocking', async ({ page }) => {
  const metrics = await page.goto('/test-page');
  // Verify CSS is loaded in render-blocking resources
  const criticalCSS = metrics.renderBlockingCSS;
  expect(criticalCSS).toBeLessThan(1024); // < 1 kB critical
});
```

### Step 8: Bundle Analysis

Check build output:
- `dist/Button.module.css` — scoped, per component
- `dist/tokens.css` — theme variables (loaded once)
- No runtime library in JS bundle

Target: each component's CSS < 2 kB gzip (including tokens references).

---

### Why This Matters

The capstone ties every module together. You don't just write a component — you make deliberate architectural decisions: approach choice (CSS Modules + custom properties), variant mechanism (cva), conflict resolution (twMerge), theming (custom properties), responsiveness (container queries), testing (VRT + a11y).

Each decision is a tradeoff. The capstone surfaces those tradeoffs and forces you to justify them.

---

### Key Takeaways
- CSS Modules + CSS custom properties = zero-runtime, themable, RSC-compatible library
- cva + twMerge gives type-safe variants with consumer override
- Container queries make components context-responsive without props
- VRT catches visual regressions in theme variants and responsive states
- Performance: check critical CSS size, per-component CSS file sizes, JS bundle CSS contribution

---

## Feynman Explain
(Explain the architecture decisions for the component library to a teammate. Why CSS Modules and not Tailwind? Why CSS custom properties and not ThemeProvider? Why cva + twMerge?)

---

## Reframe
(Pause. Judge: What would change if the library needed to support Vue AND React? What if it was an internal-only library for one team? How do those contexts change approach decisions?)

---

## Drill
Take the quiz to verify understanding of the integrated architecture.

## Quiz: 15-capstone-component-library

<p class="quiz-question">Which CSS approach is best for a shared component library consumed by apps with different frameworks?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> styled-components (ThemeProvider)</p>

<p class="quiz-option"><strong>B.</strong> CSS Modules + CSS custom properties</p>

<p class="quiz-option"><strong>C.</strong> Tailwind (requires consumer to use Tailwind)</p>

<p class="quiz-option"><strong>D.</strong> Global Sass</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">CSS Modules scope styles, CSS custom properties enable theming. Zero dependencies on consumer. Works with React, Vue, Angular — any framework that supports CSS.</p>

<hr/>

<p class="quiz-question">In the capstone architecture, how do consumers customize component colors?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Pass theme object to ThemeProvider</p>

<p class="quiz-option"><strong>B.</strong> Override CSS custom properties in their stylesheet</p>

<p class="quiz-option"><strong>C.</strong> Pass color prop to every component</p>

<p class="quiz-option"><strong>D.</strong> Modify library source code</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Library exposes --ds-color-* variables. Consumer overrides: :root { --ds-color-primary: #purple; }. No React code changes.</p>

<hr/>

<p class="quiz-question">Why does the capstone use cva + twMerge instead of just cva?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> cva doesn't work without twMerge</p>

<p class="quiz-option"><strong>B.</strong> twMerge lets consumers override variant classes via className prop</p>

<p class="quiz-option"><strong>C.</strong> cva generates conflicting classes</p>

<p class="quiz-option"><strong>D.</strong> twMerge replaces cva entirely</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">cva handles variant selection. twMerge merges variant class string with consumer's className, resolving conflicts predictably.</p>

<hr/>

<p class="quiz-question">How does the capstone Card component respond to narrow containers?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Accepts a variant prop</p>

<p class="quiz-option"><strong>B.</strong> Uses @container query to detect width</p>

<p class="quiz-option"><strong>C.</strong> Uses React Context for width</p>

<p class="quiz-option"><strong>D.</strong> ResizeObserver hook</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">container-type: inline-size on .card + @container (max-width: 300px) reduces padding. No JavaScript, no prop — native CSS responsiveness.</p>

<hr/>

<p class="quiz-question">What would change if the library targeted internal use only (one team, one framework)?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Nothing — same architecture</p>

<p class="quiz-option"><strong>B.</strong> Could use Tailwind — no cross-framework concern</p>

<p class="quiz-option"><strong>C.</strong> Must still avoid all dependencies</p>

<p class="quiz-option"><strong>D.</strong> Switch to inline styles</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Internal single-framework library removes cross-compatibility constraint. Tailwind, Vanilla Extract, or styled-components all viable.</p>

<hr/>

<p class="quiz-question">Capstone testing approach includes:</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Unit tests for variant logic only</p>

<p class="quiz-option"><strong>B.</strong> VRT for visual regression + a11y audit</p>

<p class="quiz-option"><strong>C.</strong> No tests — trust the CSS</p>

<p class="quiz-option"><strong>D.</strong> Only TypeScript compilation checks</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">VRT (Playwright/Chromatic) for visual diffs. axe-core for a11y. Unit tests for variant/class merging. Integration tests for responsive behavior.</p>

<hr/>

<p class="quiz-question">What makes the capstone's CSS approach 'RSC-compatible'?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> It uses 'use client' on every component</p>

<p class="quiz-option"><strong>B.</strong> CSS Modules are build-time — no JavaScript for styles</p>

<p class="quiz-option"><strong>C.</strong> It avoids CSS entirely</p>

<p class="quiz-option"><strong>D.</strong> Components are server-only</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">CSS Modules produce static CSS files. No runtime style injection, no hooks, no context. Components can be Server or Client components freely.</p>

<hr/>

<p class="quiz-question">If you needed Vue AND React support for the library, which approach becomes problematic?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> CSS Modules</p>

<p class="quiz-option"><strong>B.</strong> CSS custom properties</p>

<p class="quiz-option"><strong>C.</strong> cva (class-variance-authority)</p>

<p class="quiz-option"><strong>D.</strong> Container queries</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">cva is a JavaScript library — only available in JS/TS projects. CSS Modules and custom properties work universally. Container queries are CSS-native.</p>


---

# Module 16: Hybrid CSS Architecture — Combining Approaches Without Sacrificing Performance

Est. study time: 3h
Language: en

## Learning Objectives
- Design layer-based hybrid CSS architecture for any React app
- Evaluate compatibility between CSS approaches and avoid conflicting combinations
- Measure and budget CSS bundle cost across hybrid stacks
- Make informed tradeoffs between developer experience and runtime performance

---

## Core Content

### The Problem with Single-Approach Dogma

Every CSS approach optimizes for one dimension:
- **Tailwind**: developer speed and design consistency
- **CSS Modules**: isolation and zero overhead
- **Vanilla Extract**: type safety and theme contracts
- **Runtime CSS-in-JS**: dynamic prop interpolation
- **Plain CSS**: simplicity and no tooling

Pick one approach for everything, and you sacrifice the other dimensions. A Tailwind-only app struggles with complex interactive components. A CSS Modules-only app loses the rapid iteration of utility classes. A Vanilla Extract-only design system has a steeper learning curve for page authors.

**The insight**: Different parts of an app have different styling needs. A page layout needs speed and consistency. A complex widget needs isolation and type safety. Global styles need zero tooling overhead. A hybrid architecture matches approach to need.

> **Think**: Your app has a marketing homepage (mostly layout + text), a dashboard (data-heavy with tables + charts), and a settings panel (complex forms with validation states). Would one CSS approach serve all three equally well?
>
> *Answer: Unlikely. Homepage benefits from Tailwind (fast layout iteration). Dashboard components need scoped CSS (complex state management). Settings forms need type-safe variants (Vanilla Extract or CSS Modules with cva). A hybrid approach picks the right tool per section.*

### The Layer Architecture Model

```text
┌─────────────────────────────────────────────────┐
│ App Shell (root layout, nav, footer)            │
│ ├── Global reset, fonts, CSS custom properties  │  ← Plain CSS
│ └── Layout structure (grid, flex, spacing)      │  ← Tailwind
├─────────────────────────────────────────────────┤
│ Page Layer (route-level composition)            │
│ ├── Page grid, responsive breakpoints           │  ← Tailwind
│ └── Per-page section layout                     │  ← Tailwind
├─────────────────────────────────────────────────┤
│ Component Layer (reusable UI building blocks)   │
│ ├── Simple components (Button, Badge, Tag)      │  ← Tailwind or cva
│ ├── Complex components (Table, Calendar, Chart) │  ← CSS Modules or Vanilla Extract
│ └── Layout components (Card, Grid, Stack)       │  ← Tailwind or CSS Modules
├─────────────────────────────────────────────────┤
│ Override Layer (per-instance customization)     │
│ ├── className prop (with twMerge)               │  ← Escape hatch
│ └── Inline style for truly dynamic values       │  ← Direct
└─────────────────────────────────────────────────┘
```

**Key principle**: Each layer has a primary approach. Switching layers is clean — no single file mixes approaches. A page file uses Tailwind. A component file uses CSS Modules. The boundary is the file import.

### Compatibility Matrix

Not all combinations work well. Some produce specificity conflicts, build complexity, or mental overhead.

| Primary approach | Mix with | Compatible? | Notes |
|-----------------|----------|-------------|-------|
| Tailwind | CSS Modules | ✅ Yes | Most common hybrid. Tailwind for layout, CSS Modules for complex components |
| Tailwind | Vanilla Extract | ✅ Yes | VE component library consumed by Tailwind pages |
| Tailwind | Plain CSS | ✅ Yes | Global styles coexist; Tailwind classes have higher specificity |
| CSS Modules | Vanilla Extract | ✅ Yes | Both zero-runtime, both build-time CSS output |
| CSS Modules | Plain CSS | ✅ Yes | Standard: global CSS + scoped module files |
| Vanilla Extract | Plain CSS | ✅ Yes | VE outputs static CSS alongside authored global CSS |
| Tailwind | Runtime CSS-in-JS | ⚠️ Caution | Different class generation systems — specificity unpredictable |
| CSS Modules | Runtime CSS-in-JS | ⚠️ Caution | Possible but confusing — each component uses one, never both |
| Runtime CSS-in-JS | Any other | ❌ Avoid | Runtime library becomes dependency for everything it touches |
| Tailwind | Tailwind + CSS + inline | ✅ All in one file | Bad practice but technically works — don't do this |

**Golden rule**: Each component file uses exactly one approach. The mixing happens at the file/import level — a page imports components built with different approaches.

> **Think**: A component file imports a CSS Module AND uses styled() AND has inline styles. What problems arise?
>
> *Answer: (1) Reader must understand three styling mechanisms in one file. (2) Specificity order between CSS Module class, generated styled class, and inline style is hard to predict. (3) Build tool must support CSS Modules + styled-components simultaneously. (4) The runtime cost of styled-components is paid even for the CSS Module parts.*

### Performance Budgeting Across a Hybrid Stack

When combining approaches, CSS bundle cost is not simply additive — approaches interact in how CSS is loaded, split, and rendered.

**Budget categories:**

```text
Total CSS cost = Global CSS + Tailwind CSS + Module CSS + Runtime JS (if any)
```

| Cost type | Plain CSS | Tailwind | CSS Modules | Vanilla Extract | Runtime CSS-in-JS |
|-----------|-----------|----------|-------------|-----------------|-------------------|
| Static CSS | Authored size | JIT size (5-15 kB) | Per-component | Per-component | 0 (in JS bundle) |
| JS runtime | 0 kB | 0.5 kB | 0 kB | 0 kB | 12-15 kB |
| Code-split | Manual | Single file | Automatic | Automatic | No (global style tag) |
| Unused CSS | Manual purge | Zero (JIT) | Manual | Manual | N/A |
| RSC cost | None | None | None | None | Forces `"use client"` |

**Building a performance budget:**

```text
For a typical SaaS app (50 pages, 200 components):

Option A: Tailwind-only
  CSS: ~15 kB gzip (single file, all utilities)
  JS runtime: 0.5 kB
  Total: 15.5 kB
  Downside: some components have unreadable className strings

Option B: CSS Modules-only
  CSS: ~5 kB per page (split per chunk)
  JS runtime: 0 kB
  Total: ~5 kB per page
  Downside: no utility system, more CSS file management

Option C: Hybrid (Tailwind + CSS Modules)
  CSS: ~10 kB Tailwind + ~3 kB CSS Modules per page
  JS runtime: 0.5 kB
  Total: ~13.5 kB per page
  Best of both: fast layout + scoped complex components
```

**Decision flow for performance budgeting:**

```text
1. Set target: FCP < 1.5s on 3G, CSS budget < 30 kB
2. Start with Tailwind for layout (~10 kB baseline)
3. Add CSS Modules for complex components (+3-5 kB per page)
4. If budget exceeded: move more components to route-level CSS splitting
5. Never add runtime CSS-in-JS unless legacy
```

> **Think**: Your CSS budget is 20 kB. Tailwind uses 10 kB. Complex components add 12 kB. What's the optimization?
>
> *Answer: (1) Check if Tailwind includes unused utilities across all pages — split into per-route Tailwind entry points to reduce shared CSS. (2) Lazy-load complex components so their CSS loads on demand. (3) If still over budget, evaluate if some Tailwind-using pages can use CSS Modules instead, reducing the shared Tailwind baseline.*

### CSS Libraries at Scale — Why They Get Slow and Large

CSS utility libraries (Tailwind, UnoCSS, Windi) and runtime CSS-in-JS libraries both have scaling limits:

**Tailwind scaling limits:**

- **Single CSS file grows with app size**: JIT scans all source files → generates all used utilities → outputs one file. At 200+ pages, this file contains utilities from every page, even though each page only needs ~10%.
- **Impact**: 200-page app Tailwind CSS ~25-40 kB gzip. A single-page app Tailwind ~5-10 kB. The difference is the intersection of utilities across all pages.
- **Mitigation**: Split Tailwind generation per route segment using `@import "tailwindcss" source("./app/dashboard/");`

**Runtime CSS-in-JS scaling limits:**

- **Style tag accumulation**: Each unique prop combination creates a new class that never gets garbage collected. A data table with 50 rows × 10 interaction states = 500 unique class combinations accumulated in the style tag over a session.
- **Impact**: Memory grows unbounded. Long-running SPAs (dashboards kept open for hours) accumulate thousands of unused CSS rules.
- **Mitigation**: Not possible with runtime CSS-in-JS — it's architectural. Zero-runtime approaches don't have this problem.

**Vanilla Extract scaling limits:**

- **Build time**: Each `.css.ts` file executes in Node.js during build. At 500+ component files, build time increases. VE uses caching but cold builds are slower.
- **Output size**: Per-component CSS files mean more HTTP requests. Mitigation: extract shared styles into theme contracts and sprinkles to reduce duplication.
- **Mitigation**: Theme contracts reduce duplication by centralizing design tokens. Sprinkles generate shared atomic classes (like Tailwind but typed).

**CSS Libraries (clsx, twMerge, cva) at scale:**

These are tiny utility libraries but their usage adds call overhead:

| Library | Size | Per-render cost | Scale concern |
|---------|------|----------------|---------------|
| clsx | ~200 B | ~0.001ms | None at any scale |
| twMerge | ~4 kB | ~0.01ms | Call on every render of every component |
| cva | ~2 kB | ~0.005ms | Creates variant resolution on each call |

At 1000 components rendering, twMerge adds ~10ms total — negligible. But in animation frames (60fps = 16ms budget), avoid twMerge in hot paths. Use `useMemo` for computed class strings in animation-heavy components.

> **Think**: A developer says "twMerge adds 4 kB to our bundle — let's remove it." Is this a good argument?
>
> *Answer: No. 4 kB gzip for twMerge is a rounding error in a typical React bundle (200-500 kB). twMerge solves a real problem (predictable Tailwind class conflict resolution). Without it, className override behavior is undefined. The 4 kB is insurance, not bloat.*

### Case Study 1: SaaS Dashboard (Next.js App Router)

**Context**: 30-page dashboard app. 3 devs. 6-month timeline. Team knows React, varied CSS experience.

**Architecture decision:**

```text
Layer 1 (Global): Plain CSS — reset, @font-face, CSS custom properties for theme
Layer 2 (Layout): Tailwind — page grids, responsive breakpoints, spacing
Layer 3 (Components): CSS Modules for complex; Tailwind + cva for simple
Layer 4 (Overrides): className prop with twMerge
```

**Why this works:**
- Page layouts use Tailwind → fast iteration, responsive variants inline
- Charts, data tables, filter panels use CSS Modules → isolated, state-rich, animations
- Simple widgets (Button, Badge, Card) use Tailwind + cva → type-safe variants, no extra CSS files
- Global theme tokens as CSS custom properties → runtime theme switching, no JS library

**CSS budget:**
- Tailwind: 12 kB (shared across all pages)
- CSS Modules per page: 3-8 kB (loaded on demand)
- Global CSS: 2 kB (reset + tokens)
- Total per page: ~14-20 kB

**Tradeoff accepted**: Tailwind file larger than needed for each page, but developer speed justifies it. If performance becomes critical, split Tailwind per route.

### Case Study 2: Enterprise Design System (NPM Package)

**Context**: 50-component library consumed by 10 internal apps. TypeScript required. Theme support (light/dark/custom).

**Architecture decision:**

```text
Layer 1 (Global): Plain CSS — CSS custom properties for theme contracts
Layer 2 (Layout): Vanilla Extract sprinkles — typed atomic utilities
Layer 3 (Components): Vanilla Extract recipes — type-safe variants, theme-variable-aware
Layer 4 (Overrides): className prop (consumer brings own CSS approach)
```

**Why this works:**
- Zero runtime cost for consumers — no JS dependency
- TypeScript-native — invalid variant name = compile error
- Theme contracts enforce consistent token usage across components
- Consumers can style with Tailwind, CSS Modules, or anything — VE output is just CSS class names

**CSS budget:**
- Theme contract CSS: 1 kB
- Component styles: 15-25 kB (all components, single CSS file)
- Sprinkles: 5 kB (atomic utilities matching design space)
- Total: ~21-31 kB

**Tradeoff accepted**: Steeper learning curve for library authors (VE API). But consumers get a turnkey design system with zero styling dependency.

### Case Study 3: E-commerce Platform (Legacy Sass Migration)

**Context**: 200-page site using Sass + BEM. Migrating to Next.js App Router. 5-year-old codebase.

**Architecture decision:**

```text
Layer 1 (Global): Sass → migrated to CSS custom properties (incremental)
Layer 2 (Layout): New pages use Tailwind; old pages keep Sass
Layer 3 (Components): New components use CSS Modules; old components stay Sass
Layer 4 (Overrides): twMerge for new; BEM modifiers for legacy
```

**Why this works:**
- No rewrite — old Sass continues working during migration
- Shared tokens move to CSS custom properties (one-time work, benefits both old and new)
- New code uses modern approaches (Tailwind, CSS Modules)
- Migration happens at natural boundary (page or component rewrite during feature work)

**CSS budget (after migration):**
- Legacy Sass: 50 kB (gradually shrinking)
- Tailwind: 10 kB (new pages)
- CSS Modules: 5 kB per new page (on demand)
- Global CSS custom properties: 2 kB

**Tradeoff accepted**: Dual CSS pipeline (Sass build + Tailwind + CSS Modules) adds build complexity. Worth it to avoid a 200-page rewrite.

---

### Common Questions

**Q: Does a hybrid approach increase build complexity?**
A: Yes — multiple plugins, multiple configs. But most frameworks already support the common combinations:
- Next.js: supports CSS Modules + Tailwind + Sass + global CSS out of the box
- Vite: supports CSS Modules + Tailwind + Sass + PostCSS
- The only additional setup is Vanilla Extract (needs plugin) or runtime CSS-in-JS (needs SSR config)

The build complexity cost is paid once (setup). The wrong CSS approach cost is paid every sprint.

**Q: How do I enforce the hybrid architecture across a team?**
A: Three mechanisms:
1. **Directory conventions**: `/components/ui/` for simple Tailwind components. `/components/complex/` for CSS Modules. `/lib/design-system/` for Vanilla Extract
2. **Linting**: ESLint rule forbidding CSS Module imports in page files (pages should use Tailwind only)
3. **Code review**: Check that one component file doesn't mix approaches

**Q: How do themes work across a hybrid stack?**
A: CSS custom properties are the bridge. Define tokens as CSS variables at the root — every approach reads them:
- Tailwind: `@theme { --color-primary: #0366d6; }` → `bg-primary`
- CSS Modules: `background: var(--color-primary)`
- Vanilla Extract: `backgroundColor: themeVars.color.primary`
- Plain CSS: `background: var(--color-primary)`
- styled-components: `background: ${p => p.theme.colors.primary}` (convert to CSS var during migration)

One theme definition, all approaches consume it.

**Q: What's the minimum viable hybrid approach?**
A: CSS Modules + Plain CSS. Every React project needs global CSS (reset, fonts) and component styles. CSS Modules handle components. This gives you zero runtime, RSC compatibility, automatic code splitting, and standard CSS syntax. Add Tailwind only when layout iteration speed becomes the bottleneck.

---

## Examples

### Example 1: Page with Hybrid Stack

```tsx
// app/dashboard/page.tsx — Tailwind for layout
import DashboardChart from './DashboardChart';
import StatsGrid from './StatsGrid';

export default function DashboardPage() {
  return (
    <div className="grid grid-cols-1 lg:grid-cols-4 gap-6 p-6">
      <header className="lg:col-span-4 flex items-center justify-between">
        <h1 className="text-2xl font-bold">Dashboard</h1>
        <div className="flex gap-2">
          <button className="px-4 py-2 bg-blue-600 text-white rounded-lg text-sm">
            Export
          </button>
        </div>
      </header>
      <StatsGrid className="lg:col-span-4" />
      <div className="lg:col-span-3">
        <DashboardChart />
      </div>
      <aside className="lg:col-span-1">
        <ActivityFeed />
      </aside>
    </div>
  );
}
```

```tsx
// DashboardChart.tsx — CSS Modules for complex component
import styles from './DashboardChart.module.css';
import clsx from 'clsx';

export default function DashboardChart() {
  const [view, setView] = useState<'day' | 'week' | 'month'>('week');
  return (
    <div className={styles.chart}>
      <div className={styles.toolbar}>
        {(['day', 'week', 'month'] as const).map(v => (
          <button
            key={v}
            className={clsx(styles.tab, view === v && styles.activeTab)}
            onClick={() => setView(v)}
          >
            {v}
          </button>
        ))}
      </div>
      <div className={styles.chartArea}>
        {/* Chart content with complex CSS (grid lines, axes, tooltips) */}
      </div>
    </div>
  );
}
```

### Example 2: Theme Token Bridge

```css
/* globals.css — single source of truth for theme tokens */
:root {
  --color-primary: #6366f1;
  --color-primary-hover: #4f46e5;
  --color-surface: #ffffff;
  --color-text: #1e293b;
  --space-sm: 8px;
  --space-md: 16px;
  --radius-sm: 6px;
  --radius-md: 12px;
  --font-body: 'Inter', system-ui, sans-serif;
}
```

```css
/* app.css — Tailwind v4 reads CSS vars */
@import "tailwindcss";
@theme {
  --color-primary: var(--color-primary);
  --color-surface: var(--color-surface);
  --color-text: var(--color-text);
}
```

```css
/* Card.module.css — reads same vars */
.card {
  background: var(--color-surface);
  color: var(--color-text);
  border-radius: var(--radius-md);
  padding: var(--space-md);
}
```

```typescript
// theme.css.ts — Vanilla Extract reads same vars (for VE components)
export const themeVars = createThemeContract({
  color: { primary: null, surface: null, text: null },
});
```

One set of CSS custom properties serves all approaches. Theme switching (dark mode) changes the property values at the root, and every component — regardless of styling approach — updates automatically.

---

## Key Takeaways
- No single CSS approach fits every app layer — hybrid architecture matches approach to need
- Layer model: global (plain CSS) → layout (Tailwind) → component (CSS Modules/VE) → override (className)
- One approach per component file — mixing happens at import boundaries, not within files
- Compatibility matrix: Tailwind + CSS Modules is the most common and safest hybrid
- Performance budget: Tailwind baseline (~10 kB) + CSS Modules on top (~3-5 kB per page)
- CSS libraries at scale: twMerge/cva negligible cost; Tailwind single file grows with app routes
- Theme tokens as CSS custom properties bridge all approaches with zero runtime
- Case studies: SaaS dashboard (hybrid), enterprise DS (VE-only), legacy migration (incremental)

---

## Common Misconception

**"Hybrid CSS architecture means every file uses multiple approaches."**

Wrong. Hybrid architecture means different files use different approaches, each chosen for its layer. A single file should use exactly one approach. The hybrid is in the project's composability — a Tailwind-layout page imports CSS-Module components that use CSS-custom-property tokens.

Think of it like programming languages: your backend might be Rust, your frontend TypeScript, your config files YAML. They don't mix in one file. The hybrid is at the project architecture level, not the file level.

---

## Feynman Explain
(Explain hybrid CSS architecture to a teammate who says "just pick one approach and stick with it." Why does picking one create problems? How does the layer model solve this?)

---

## Reframe
(Pause. Judge: Is there a case where a single approach IS better than hybrid? Small apps? Single-developer projects? Where does hybrid add unnecessary complexity?)

---

## Drill
Take the quiz. Questions cover layer model, compatibility matrix, performance budgeting, and case study analysis.

## Quiz: 16-hybrid-css-architecture

<p class="quiz-question">What is the primary design principle of hybrid CSS architecture?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Use all CSS approaches in every component file</p>

<p class="quiz-option"><strong>B.</strong> Each file uses one approach; different files serve different layers</p>

<p class="quiz-option"><strong>C.</strong> Always use the newest CSS approach for everything</p>

<p class="quiz-option"><strong>D.</strong> Avoid CSS Modules entirely</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Hybrid architecture means different files use different approaches, each chosen for its layer. No single file mixes approaches. The hybrid is at the project architecture level.</p>

<hr/>

<p class="quiz-question">In the layer architecture model, which approach is recommended for global foundation (reset, fonts, CSS variables)?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> styled-components with ThemeProvider</p>

<p class="quiz-option"><strong>B.</strong> Vanilla Extract recipes</p>

<p class="quiz-option"><strong>C.</strong> Plain CSS</p>

<p class="quiz-option"><strong>D.</strong> Tailwind utility classes</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">Global foundation (reset, @font-face, CSS custom properties, keyframes) needs zero tooling. Plain CSS is the simplest, most compatible choice for this layer.</p>

<hr/>

<p class="quiz-question">Which combination of CSS approaches is MOST compatible and recommended?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Runtime CSS-in-JS + Tailwind in the same component</p>

<p class="quiz-option"><strong>B.</strong> Tailwind for layout + CSS Modules for complex components</p>

<p class="quiz-option"><strong>C.</strong> Inline styles for everything + CSS Modules</p>

<p class="quiz-option"><strong>D.</strong> Sass @extend across CSS Modules</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Tailwind for layout + CSS Modules for complex components is the most common and safest hybrid. Tailwind handles structure fast; CSS Modules isolate component complexity.</p>

<hr/>

<p class="quiz-question">Tailwind generates one CSS file containing all utilities used across the app. At what app size does this become a performance concern?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> 5 pages</p>

<p class="quiz-option"><strong>B.</strong> 50+ pages (single CSS file grows larger than per-page CSS would be)</p>

<p class="quiz-option"><strong>C.</strong> Only affects development builds</p>

<p class="quiz-option"><strong>D.</strong> Never — Tailwind's output is always optimal</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">At 50+ pages, Tailwind's single CSS file contains utilities from every page. Each page loads the full file but only uses ~10%. Per-page CSS Modules would be smaller. Solution: per-route Tailwind entry points.</p>

<hr/>

<p class="quiz-question">How should design tokens (colors, spacing, fonts) be shared across a hybrid CSS stack?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Each approach defines its own tokens independently</p>

<p class="quiz-option"><strong>B.</strong> CSS custom properties defined once, consumed by all approaches</p>

<p class="quiz-option"><strong>C.</strong> JavaScript constants exported to every styling system</p>

<p class="quiz-option"><strong>D.</strong> Duplicate values in each approach's config file</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">CSS custom properties on :root are the single source of truth. Tailwind references them via @theme. CSS Modules use var(). Vanilla Extract creates theme contracts from the same CSS vars. One source, all approaches consume.</p>

<hr/>

<p class="quiz-question">A SaaS dashboard uses Tailwind for layout and CSS Modules for complex widgets. A new developer asks: 'Can I use Tailwind in my Chart component too?' What's the right response?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Yes — use whatever approach you prefer</p>

<p class="quiz-option"><strong>B.</strong> No — Chart is a complex component with many states; CSS Modules isolate that complexity better</p>

<p class="quiz-option"><strong>C.</strong> Yes — but only for hover effects</p>

<p class="quiz-option"><strong>D.</strong> No — Tailwind can't be used with CSS Modules in the same app</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">The architecture decision is intentional: layout = Tailwind (fast iteration), complex components = CSS Modules (isolation). Chart with sorting, filtering, and animations benefits from scoped CSS. Keep the boundary clean.</p>

<hr/>

<p class="quiz-question">What is the total CSS cost for a hybrid app using Tailwind (12 kB) + CSS Modules (5 kB per page) + global CSS (2 kB), on a 3-page load?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> 19 kB</p>

<p class="quiz-option"><strong>B.</strong> 12 kB + 5 kB (only current page's CSS Modules) + 2 kB = 19 kB for first page</p>

<p class="quiz-option"><strong>C.</strong> 12 kB + 15 kB + 2 kB = 29 kB</p>

<p class="quiz-option"><strong>D.</strong> 5 kB per page, no baseline</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Tailwind (12 kB) and global CSS (2 kB) load once. CSS Modules code-split per page — only current page's modules (5 kB) load. Total first page: ~19 kB. Other pages' CSS loads with their JS chunks.</p>

<hr/>

<p class="quiz-question">An enterprise design system ships as an NPM package consumed by 10 apps. Which hybrid approach is most appropriate?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Tailwind — all consumers must use Tailwind too</p>

<p class="quiz-option"><strong>B.</strong> Vanilla Extract for components + CSS custom properties for theming</p>

<p class="quiz-option"><strong>C.</strong> styled-components with ThemeProvider</p>

<p class="quiz-option"><strong>D.</strong> Inline styles for everything</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Vanilla Extract produces zero-runtime static CSS — consumers don't need VE installed. CSS custom properties for theming don't require a JS library. Consumers can override tokens regardless of their own CSS approach.</p>

<hr/>

<p class="quiz-question">How does runtime CSS-in-JS's style tag grow unbounded in a hybrid stack?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> It doesn't — all hybrid approaches prevent this</p>

<p class="quiz-option"><strong>B.</strong> Each unique prop combination generates a new class that never garbage collects</p>

<p class="quiz-option"><strong>C.</strong> It only happens during development</p>

<p class="quiz-option"><strong>D.</strong> Tailwind automatically cleans it up</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Runtime CSS-in-JS creates new class names for unique prop combinations. These accumulate in the style tag over a session. Zero-runtime approaches (CSS Modules, Tailwind, VE) don't have this problem.</p>

<hr/>

<p class="quiz-question">What is the golden rule of file-level approach mixing?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Always use at least two approaches per file</p>

<p class="quiz-option"><strong>B.</strong> Each component file uses exactly one CSS approach</p>

<p class="quiz-option"><strong>C.</strong> Put all CSS in one file for consistency</p>

<p class="quiz-option"><strong>D.</strong> Use inline styles as the primary approach</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Each component file uses exactly one approach. The mixing happens at file/import level — a page (Tailwind) imports complex components (CSS Modules) that use shared tokens (CSS custom properties). Never mix within one file.</p>


---

# Module 17: Migration & Gradual Adoption Strategies

Est. study time: 2h
Language: en

## Learning Objectives
- Plan incremental migration between CSS approaches
- Implement coexistence patterns for dual CSS pipelines
- Extract design tokens into framework-agnostic CSS custom properties
- Manage team workflow during multi-phase CSS transitions

---

## Core Content

### Why Big-Bang CSS Rewrites Fail

Every "rewrite all styles in X" project shares the same failure pattern:

1. **Month 1**: Enthusiasm. Migration planned for "6 weeks."
2. **Month 3**: 30% done. Original estimate was wrong — every component has edge cases.
3. **Month 6**: 60% done. Business needs new features — now maintaining two CSS approaches indefinitely.
4. **Month 12**: Project abandoned. Old CSS still exists alongside new. Team morale down.

**Root cause**: CSS is coupled to component logic. You can't swap a component's styling approach without touching its JSX and testing its behavior. A "CSS migration" is actually a component migration.

> **Think**: Your team maintains 300 components using styled-components. The CTO wants to switch to Tailwind. What's the realistic timeline?
>
> *Answer: 6-12 months minimum. Each component needs: (1) rewrite CSS string to Tailwind classes, (2) remove styled() wrapper, (3) update any prop-based style logic, (4) remove ThemeProvider usage, (5) test visual regression. At 5 components per week with 1 dedicated dev, that's 60 weeks. Plan for 6-12 months with 2-3 devs part-time.*

### Incremental Migration: The Strangler Fig Pattern

The strangler fig pattern grows new architecture alongside old, gradually replacing pieces until nothing of the original remains.

```text
Phase 1: Coexistence
┌─────────────────┬─────────────────┐
│   Old approach  │   New approach  │
│  (styled-comps) │  (CSS Modules)  │
│                 │                 │
│  Button.tsx     │  Dashboard.tsx  │  ← Old and new files coexist
│  Card.tsx       │  Chart.tsx      │
│  Nav.tsx        │  Settings.tsx   │
└─────────────────┴─────────────────┘

Phase 2: Replacement (opportunistic)
┌─────────────────┬─────────────────┐
│   Old approach  │   New approach  │
│                 │                 │
│  Button.tsx ──► │  Button.tsx     │  ← Replaced during feature work
│  Card.tsx       │  Dashboard.tsx  │
│  Nav.tsx        │  Chart.tsx      │
│                 │  Settings.tsx   │
└─────────────────┴─────────────────┘

Phase 3: Cleanup
┌──────────────────────────────────┐
│          New approach            │
│                                  │
│  Button.tsx    Dashboard.tsx     │  ← Zero old imports
│  Card.tsx      Chart.tsx         │
│  Nav.tsx       Settings.tsx      │
└──────────────────────────────────┘
```

**Rule**: Never migrate a component unless you're already touching it for a feature or bug fix. "Style-only" migrations create work with zero user-facing value.

> **Think**: A component hasn't been touched in 2 years. It still uses styled-components. Should you migrate it?
>
> *Answer: No. If it works and no feature requires changing it, the migration has negative ROI. The runtime cost of one component is negligible. Migrate it when you add a feature or fix a bug.*

### Coexistence Patterns

When two CSS approaches run in the same app, they must coexist without conflict:

**Pattern 1: Side-by-side file imports**

Old and new components coexist in the same app. Old components import their approach independently. New components use the modern approach. No file mixes them.

```tsx
// Old component — unchanged
import styled from 'styled-components';
const Button = styled.button`padding: 8px;`;

// New component — uses different approach
import styles from './Card.module.css';
function Card() { return <div className={styles.card}>...</div>; }
```

**Pattern 2: Wrapper boundaries**

When old component is inside new component (or vice versa), use CSS custom properties as the boundary layer:

```tsx
// New layout component (Tailwind) wraps old component (styled-components)
function DashboardPage() {
  return (
    <div className="grid grid-cols-3 gap-4 p-6">
      {/* Old styled-components chart — works inside Tailwind grid */}
      <LegacyChart />
    </div>
  );
}
```

Tailwind sets layout. Old component handles its own internal styles. No conflict because Tailwind targets layout divs, not chart internals.

**Pattern 3: Shared design tokens via CSS custom properties**

Both old and new read from the same CSS custom properties:

```css
/* Global tokens — both approaches read these */
:root {
  --color-primary: #6366f1;
  --space-md: 16px;
}
```

```tsx
// Old styled-components
const Button = styled.button`
  background: var(--color-primary);
  padding: var(--space-md);
`;

// New CSS Modules
.button { background: var(--color-primary); padding: var(--space-md); }
```

Same tokens, different approaches. Changes flow through CSS custom properties.

**Pattern 4: Build pipeline coexistence**

Both approaches must compile simultaneously:

| Combination | Build setup | Complexity |
|-------------|-------------|------------|
| styled-components + CSS Modules | Both supported by default in Next.js/Vite | Low |
| styled-components + Tailwind | Both supported; Tailwind JIT scans all files | Low |
| CSS Modules + Sass | Next.js/Vite support both natively | Low |
| Vanilla Extract + Tailwind | VE plugin + Tailwind plugin | Medium |
| All four above | Multiple plugins, potential conflict | High |

Most frameworks support the common combinations. Test that both produce correct output in dev and production builds.

> **Think**: You add Vanilla Extract to an existing Next.js app using CSS Modules. What could break?
>
> *Answer: (1) VE requires a webpack/Vite plugin — ensure it doesn't conflict with existing CSS handling. (2) VE's class name generation might collide with CSS Module hashes (unlikely but test). (3) Build time increases because VE executes .css.ts files in Node. (4) Production CSS output now contains both VE-generated and CSS Module-generated files — verify ordering.*

### Design Token Extraction Strategy

Before migrating any component, extract shared design tokens from the old approach. This decouples visual values from implementation.

**Step 1: Audit existing tokens**

Search the old codebase for repeated values:

```typescript
// Find all hardcoded colors, spacing, fonts in styled-components:
// background: '#0366d6' appears in 47 components
// padding: '16px' appears in 89 components
// border-radius: '8px' appears in 32 components
```

**Step 2: Define as CSS custom properties**

```css
/* globals.css — new token system */
:root {
  --color-primary: #0366d6;
  --color-primary-hover: #0256b3;
  --color-danger: #d73a49;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --radius-sm: 4px;
  --radius-md: 8px;
  --font-size-body: 16px;
  --font-size-heading: 24px;
}
```

**Step 3: Update old components to use CSS vars (optional)**

Old styled-components can reference the same vars:

```tsx
// Before: hardcoded value
const Button = styled.button`background: #0366d6;`;

// After: reads from CSS custom property
const Button = styled.button`background: var(--color-primary);`;
```

This step is optional — only do it if you plan to keep old components long-term. Otherwise, wait until migration to update.

**Step 4: New components use tokens via their approach**

```tsx
// Tailwind: @theme { --color-primary: var(--color-primary); }
// Then: bg-primary

// CSS Modules: background: var(--color-primary);

// Vanilla Extract: backgroundColor: themeVars.color.primary
```

> **Think**: What's the single most important migration step?
>
> *Answer: Extract design tokens to CSS custom properties FIRST. This decouples visual values from implementation. Once tokens are in CSS vars, old and new approaches read from the same source. Changing a color value updates both systems simultaneously. Everything else (component migration) is mechanical.*

### Migration Paths: Common Scenarios

**Path A: styled-components → CSS Modules**

```text
Timeline: 6-12 months for 300 components

1. Month 1: Extract tokens to CSS custom properties
2. Month 1-3: New components use CSS Modules (stop growth of old system)
3. Month 3-9: Replace leaf components during feature work
   a. Convert styled.button → CSS Module + JSX button
   b. Move variant logic from ${p => ...} to clsx()
   c. Replace ThemeProvider references with CSS var references
4. Month 9-12: Replace parent components
5. Month 12: Remove styled-components dependency when zero imports remain
```

**Path B: Sass/plain CSS → Tailwind**

```text
Timeline: 3-6 months for 200-page site

1. Month 1: Set up Tailwind alongside existing Sass
2. Month 1-3: New pages use Tailwind only
3. Month 3-6: During redesigns, convert old Sass pages to Tailwind
4. Month 6: Remove Sass dependency when zero .scss files remain
```

**Path C: Sass → CSS Modules (with Tailwind optional)**

```text
Timeline: 4-8 months for 100 components

1. Month 1: Convert global Sass tokens to CSS custom properties
2. Month 1-2: New components use CSS Modules
3. Month 2-6: Rewrite active components to CSS Modules during features
4. Month 6-8: Clean up dead Sass files
5. Optionally add Tailwind for layout components
```

**Path D: Vanilla Extract → Tailwind (rare)**

```text
Timeline: 2-4 months for 50 components

1. Month 1: New layout components use Tailwind
2. Month 1-3: Rewrite VE components that benefit from faster iteration
3. Keep VE for design system / typed components — Tailwind for pages
4. Result is often hybrid, not full migration
```

> **Think**: Your team chooses Path A (styled-components → CSS Modules). What's the first component you migrate?
>
> *Answer: A leaf component (no children) with simple styles and no ThemeProvider usage. A Button or Badge component. Success gives confidence, and the risk is low. Never start with a complex parent component like a Table or Form.*

### Team Workflow During Migration

**Rules for a smooth migration:**

1. **No "CSS migration" tickets** — always pair migration with feature work: "Add export button (and while touching Button, convert to CSS Modules)"
2. **Track percentage, not deadlines** — "70% of components converted" (measurable) vs "Done by June" (guess)
3. **One person, one approach** — don't let a dev learn two new CSS approaches simultaneously
4. **Visual regression testing** — before/after screenshots for every migrated component
5. **Acres of diamonds** — look at what the old approach does WELL before replacing. If styled-components' dynamic theming is genuinely useful, keep it until you have a CSS custom property alternative

**Migration readiness checklist:**

```text
Before migration sprint:
□ Design tokens extracted to CSS custom properties
□ New approach build pipeline proven in production
□ Team trained on new approach (2-5 small components)
□ Visual regression testing in place
□ Leaf components identified (low-risk starters)
□ "No new old-approach components" rule enforced

During migration:
□ One component per ticket (never batch)
□ Before/after screenshot in PR
□ Remove old import when zero references remain
□ Track converted/total ratio weekly
```

---

### Common Questions

**Q: Should I ever do a full rewrite of all CSS?**
A: Almost never. CSS rewrites are like moving your house by rebuilding it while living in it — possible but painful. The strangler fig pattern (gradual replacement) has lower risk and delivers value incrementally.

**Q: How do I prevent new components from using the old approach during migration?**
A: Enforce via linting. Add an ESLint rule that warns on `import from 'styled-components'` in new files. Document the new approach with code examples. In code review, reject new old-approach usage.

**Q: What about the old approach's build pipeline?**
A: Keep it running during migration. Remove it when:
- Zero imports of the old approach remain in the source
- Zero CI scripts reference it
- Zero documentation references it
- Zero team members still use it for new work

Removing too early blocks migration. Removing too late creates confusion.

**Q: Can I use codemods for migration?**
A: For simple cases (rename `styled.button` → CSS Module), yes. For anything involving variant logic prop interpolation, codemods produce fragile output. Manual migration is safer for complex components.

---

## Examples

### Example 1: Incremental styled-components → CSS Modules

**Before:**
```tsx
// Button.tsx — styled-components
import styled, { css } from 'styled-components';

const variants = {
  primary: css`background: #0366d6; color: white;`,
  outline: css`background: transparent; border-color: #0366d6;`,
};

const StyledButton = styled.button<{ $variant?: keyof typeof variants }>`
  display: inline-flex;
  padding: 8px 16px;
  border-radius: 6px;
  ${p => p.$variant && variants[p.$variant]}
`;

function Button({ variant, children }) {
  return <StyledButton $variant={variant}>{children}</StyledButton>;
}
```

**After:**
```tsx
// Button.tsx — CSS Modules
import styles from './Button.module.css';
import clsx from 'clsx';

function Button({ variant = 'primary', children }) {
  return (
    <button className={clsx(
      styles.button,
      variant === 'primary' && styles.primary,
      variant === 'outline' && styles.outline,
    )}>
      {children}
    </button>
  );
}
```

```css
/* Button.module.css */
.button {
  display: inline-flex;
  padding: 8px 16px;
  border-radius: 6px;
}
.primary { background: var(--color-primary); color: white; }
.outline { background: transparent; border-color: var(--color-primary); }
```

**Migration steps:**
1. Create `Button.module.css` with the same styles (using CSS vars)
2. Rewrite `Button.tsx` to import CSS Module, remove styled imports
3. Test visual regression
4. Remove old imports (none if Button was the last styled-components user)

### Example 2: Dual Build Pipeline

```tsx
// next.config.ts — supporting styled-components + CSS Modules during migration
const nextConfig = {
  compiler: {
    styledComponents: true,  // Keep for old components
  },
};

// tailwind.config.ts — adding Tailwind alongside existing stack
export default {
  content: ['./src/**/*.{tsx,ts}'],
  plugins: [],
};
```

No conflict — Next.js handles CSS Modules natively, styled-components via compiler option, and Tailwind via content scanning. All three coexist.

---

## Key Takeaways
- Big-bang CSS rewrites fail — use the strangler fig pattern (incremental replacement)
- Never migrate a component unless touching it for a feature or bug fix
- Extract design tokens to CSS custom properties FIRST — this decouples values from implementation
- Coexistence patterns: side-by-side files, wrapper boundaries, shared tokens, dual build pipeline
- Visual regression testing before/after every migrated component
- Track percentage, not deadlines — "70% converted" over "done by June"
- Lint against new old-approach usage during migration
- Remove old approach when zero imports remain

---

## Common Misconception

**"We need to finish the migration before shipping new features."**

False. You can (and should) ship features while migrating. The strangler fig pattern adds new-feature components in the new approach. Old components stay until they need changes. This means:
- New features use modern CSS
- Old features stay stable
- Migration costs are amortized over feature work
- Business value is delivered continuously

Stop the migration if it's blocking features. Resume when it can be paired with feature work again. Incomplete migration with zero new old-style components is a success state, not a failure.

---

## Feynman Explain
(Explain the strangler fig migration pattern to a product manager. Why is gradual replacement safer than a rewrite? How does it deliver value during migration, not just after?)

---

## Reframe
(Pause. Judge: When WOULD a full rewrite of CSS be justified? Are there cases where the old approach is so broken that incremental migration is impossible? What makes a codebase "un-strangler-able"?)

---

## Drill
Take the quiz. Questions cover migration phases, coexistence patterns, token extraction strategy, and team workflow.

## Quiz: 17-migration-strategies

<p class="quiz-question">What is the recommended pattern for migrating CSS approaches in a large React app?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Full rewrite over one weekend</p>

<p class="quiz-option"><strong>B.</strong> Strangler fig — gradual replacement during feature work</p>

<p class="quiz-option"><strong>C.</strong> Rewrite all CSS first, then migrate components</p>

<p class="quiz-option"><strong>D.</strong> Only migrate when the library is deprecated</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">The strangler fig pattern grows new architecture alongside old, replacing pieces during feature work. No big-bang rewrite. Each component migrates when it's already being touched.</p>

<hr/>

<p class="quiz-question">A component hasn't been modified in 3 years and uses an old CSS approach. Should you migrate it?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Yes — all components must use the same approach</p>

<p class="quiz-option"><strong>B.</strong> No — if it works and no feature requires changes, migration has negative ROI</p>

<p class="quiz-option"><strong>C.</strong> Yes — but only if it's a leaf component</p>

<p class="quiz-option"><strong>D.</strong> No — old components should be deleted</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Never migrate a component unless touching it for a feature or bug fix. 'Style-only' migrations create work with zero user-facing value. Migrate when you add a feature.</p>

<hr/>

<p class="quiz-question">What's the FIRST step in any CSS migration?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Install the new CSS tool</p>

<p class="quiz-option"><strong>B.</strong> Extract design tokens to CSS custom properties</p>

<p class="quiz-option"><strong>C.</strong> Rewrite the first component</p>

<p class="quiz-option"><strong>D.</strong> Notify all developers</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Extract design tokens (colors, spacing, fonts) to CSS custom properties FIRST. This decouples visual values from implementation. Both old and new approaches read from the same source. Changing a value updates both systems.</p>

<hr/>

<p class="quiz-question">What is the risk of creating 'CSS migration' tickets that don't include feature work?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> No risk — pure CSS tickets are efficient</p>

<p class="quiz-option"><strong>B.</strong> They create work with zero user-facing value, reducing business buy-in</p>

<p class="quiz-option"><strong>C.</strong> CSS cannot be migrated without feature changes</p>

<p class="quiz-option"><strong>D.</strong> They're the only way to ensure consistency</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Pure CSS migration tickets have no user-visible outcome. Management sees 'two sprints, zero features.' Pair migration with feature work: 'Add search bar (and convert related component to CSS Modules).'</p>

<hr/>

<p class="quiz-question">During migration from styled-components to CSS Modules, an old component wraps a new component. How do they coexist?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Convert both at the same time</p>

<p class="quiz-option"><strong>B.</strong> They coexist naturally — each file uses its own approach, CSS custom properties bridge theming</p>

<p class="quiz-option"><strong>C.</strong> Wrap the new component in ThemeProvider</p>

<p class="quiz-option"><strong>D.</strong> Convert the parent first</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Old and new components coexist in the same tree. Each uses its own styling approach. CSS custom properties bridge theming. The old component reads var(--color-primary), the new component reads the same var.</p>

<hr/>

<p class="quiz-question">A team of 10 starts migrating 300 styled-components to CSS Modules. What's the best progress metric?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Deadline-based — 'done by June'</p>

<p class="quiz-option"><strong>B.</strong> Percentage-based — '70% of components converted'</p>

<p class="quiz-option"><strong>C.</strong> Time-based — '3 sprints for migration'</p>

<p class="quiz-option"><strong>D.</strong> No tracking — just work on it when possible</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Percentage of converted components is measurable and objective. 'Done by June' is a guess. Track converted/total weekly. Adjust timeline based on actual velocity, not estimates.</p>

<hr/>

<p class="quiz-question">What's the first component type you should migrate in a CSS transition?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> The most complex component (Table)</p>

<p class="quiz-option"><strong>B.</strong> A leaf component with simple styles (Button, Badge)</p>

<p class="quiz-option"><strong>C.</strong> The root App component</p>

<p class="quiz-option"><strong>D.</strong> Any component with !important</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Start with leaf components (no children, simple styles). Low risk, fast success. Confidence builds. Complex components come later when the team is comfortable with the new approach.</p>

<hr/>

<p class="quiz-question">How should you prevent new components from using the old approach during migration?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Verbally remind developers in standup</p>

<p class="quiz-option"><strong>B.</strong> ESLint rule that warns on old approach imports in new files</p>

<p class="quiz-option"><strong>C.</strong> Delete the old library immediately</p>

<p class="quiz-option"><strong>D.</strong> Don't worry — it'll sort itself out</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">ESLint rules enforce the constraint automatically. 'No new imports from styled-components after migration start date.' Combined with code review, this prevents old-approach usage in new files.</p>

<hr/>

<p class="quiz-question">When should you remove the old approach's build pipeline?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Immediately after starting migration</p>

<p class="quiz-option"><strong>B.</strong> When zero imports of the old approach remain in source</p>

<p class="quiz-option"><strong>C.</strong> When 50% of components are converted</p>

<p class="quiz-option"><strong>D.</strong> Never — keep both forever</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Remove old dependencies and build config when zero imports reference them. Removing too early blocks migration. Removing too late creates confusion. Verify: zero source imports, zero CI references, zero docs.</p>

<hr/>

<p class="quiz-question">A team has 6 months to migrate 200 components. Their velocity is 5 components per week. What should they do?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Work overtime to meet deadline</p>

<p class="quiz-option"><strong>B.</strong> Prioritize: migrate highest-traffic components first, accept incomplete migration at month 6</p>

<p class="quiz-option"><strong>C.</strong> Cancel all features until migration is complete</p>

<p class="quiz-option"><strong>D.</strong> Hire 3 more developers for the migration</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">At 5/week for 24 weeks = 120 components in 6 months. Realistically 80-90% completion. Prioritize high-traffic components. '90% converted, no new old-style components' is a success state. Ship features alongside migration.</p>
