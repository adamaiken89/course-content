# Module 1: Agentic Mindset & Session Lifecycle

Est. study time: 1.5h
Language: en

## Learning Objectives
- Distinguish agentic coding from chat-based LLM usage
- Decide when to use an agent vs code manually
- Manage session lifecycle: start, continue, restart
- Detect context pollution and diminishing returns

---

## Core Content

### What is Agentic Software Engineering

Traditional LLM chat: you paste code, ask question, get answer. You drive every step.

Agentic: you set goal and constraints. Agent explores codebase, plans, implements, verifies. Agent drives subtasks. You review and redirect.

Shift: **operator → orchestrator**. You don't write every line. You decide direction, inspect output, correct course.

```text
Chat LLM:   You: "write a function to sort users" → LLM: outputs code
Agentic:    You: "add user sorting to the admin panel, follow existing patterns"
            Agent: reads current code → identifies patterns → writes code → runs tests → fixes → presents diff
```

> **Think**: What mental shift is hardest for developers switching from chat to agentic? Why?
> *Answer: Trust. Developers are used to controlling every character. Agentic requires trusting output, reviewing intelligently, not micromanaging.*

### When to Use Agents

| Good for Agent | Bad for Agent | Best Manual |
|---------------|---------------|-------------|
| Boilerplate generation | Novel algorithm design | Architecture decisions |
| Cross-file refactoring | High-security code | Production hotfixes |
| Test writing | Cryptography | Sensitive data handling |
| Documentation | Performance-critical kernels | Legal/compliance code |
| Bug hunting (explore) | System-level programming | Creative design |
| Code review | Domain you don't understand | Reviewing agent's work |

Rule: agent for **mechanical, well-defined, explorable** tasks. Manual for **creative, high-stakes, underspecified** tasks.

> **Think**: You need to implement a new payment provider integration. Agent or manual? Why?
> *Answer: Agent if existing provider integrations exist (pattern to follow). Manual if first integration or security-critical financial logic.*

### Session Lifecycle

```text
START → EXPLORE/PLAN → IMPLEMENT → VERIFY → REVIEW → [CONTINUE or RESTART]
```

**New session** triggers:
- Context exceeds ~90% capacity (agent starts forgetting early instructions)
- Task domain fundamentally changes (e.g., backend → infrastructure)
- Agent shows confusion (repeats questions, contradicts itself)
- After major failure (agent spiraling on wrong approach)

**Continue session** triggers:
- Same-file edits
- Same-feature continuation
- Same bug investigation
- Context still under ~70% full

**Restart** protocol:
1. Compress current session into summary
2. Copy key decisions to AGENTS.md or CLAUDE.md
3. Start fresh session with compressed summary + instructions
4. Cost: ~15s overhead, saves thousands of tokens

> **Think**: You've been working on authentication for 3 hours. Agent is generating good code but responses are slowing and it forgot the project structure. What do you do?
> *Answer: Compress session → restart fresh with compressed summary. Don't push through degradation.*

### Context Pollution Signals

Symptoms of degraded context:
- Agent asks questions already answered
- Agent writes code that violates earlier decisions
- Agent repeats itself
- Response latency increases (more tokens to process)
- Agent "forgets" tools it used successfully earlier

**Prevention**: compress proactively (not just when full). Every 30-50 turns, or when topic closes.

---

## Why This Matters

Most agent failures aren't technical. They're **context management failures**. Wrong session choice, wrong task delegation, wrong trust level. This module's concepts prevent 80% of common agent frustrations.

---

## Common Questions

**Q: Should I let agent explore freely or guide tightly?**
A: Depends on task maturity. New codebase: guide tightly. Established codebase: let agent explore patterns first (discovery-first, covered in M6).

**Q: What if agent wastes tokens exploring too much?**
A: Set budget in prompt: "Spend max 3 tool calls exploring, then propose plan." Bounded exploration.

**Q: Should I restart session daily?**
A: Not necessarily. Restart when context degrades, not on calendar. Some sessions last 100+ turns if topic stays tight.

---

## Examples

### Example 1: Session Lifecycle Management

Problem: Building a feature across 2 days. End of day 1, context ~80% full.

Bad: Start day 2 fresh without context. Agent re-explores codebase, misses yesterday's design decisions.

Good: Compress day 1 → write key decisions to AGENTS.md → start fresh with compressed summary. Day 2 agent picks up where you left off.

### Example 2: Recognizing Wrong Tool for Task

Problem: Need to implement custom sorting algorithm for novel data structure.

Bad: Ask agent to implement from scratch. Agent writes plausible-looking but incorrect algorithm. You don't catch bug. Production fails.

Good: Write algorithm yourself (manual). Ask agent to write tests, benchmark, review for edge cases. Agent helps without being trusted with core logic.

---

## Key Takeaways
- Agentic = orchestrator, not operator. Set goal, review output, redirect.
- Use agents for mechanical/explorable tasks. Manual for creative/high-stakes.
- New session when context degraded, domain shifted, or after failure.
- Compress before restart. Preserve decisions in AGENTS.md.
- Detect context pollution: repetition, forgetting, contradictions.

---

## Common Misconception

**"Agent should do everything."** No. Agent is a force multiplier, not a replacement. Best results come from strategic delegation: agent handles mechanical work, you handle decisions the agent cannot make. The best agentic developers are those who know what NOT to delegate.

---

## Feynman Explain

(Explain "session lifecycle" to a developer who only uses chat LLMs. Why not just keep one chat open forever? What's different about agent sessions?)

---

## Reframe

(Judge: "always start new session for each task" vs "never restart unless forced." Which extreme is more dangerous? What's the cost of each? When would each be right?)

---

## Drill

Take the quiz. Run: `learn.sh quiz agentic-engineering 1`

## Quiz: 01-agentic-mindset

<p class="quiz-question">What is the primary mental shift from chat-based LLM to agentic coding?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Writing more code yourself</p>

<p class="quiz-option"><strong>B.</strong> Moving from operator to orchestrator</p>

<p class="quiz-option"><strong>C.</strong> Using a different programming language</p>

<p class="quiz-option"><strong>D.</strong> Eliminating code review entirely</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Chat LLM: you drive every step. Agentic: you set goals and constraints, agent drives subtasks. You become orchestrator, not operator.</p>

<hr/>

<p class="quiz-question">Which task is BEST suited for an agent?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Designing a novel cryptographic algorithm</p>

<p class="quiz-option"><strong>B.</strong> Writing cross-file refactoring following existing patterns</p>

<p class="quiz-option"><strong>C.</strong> Making high-level architecture decisions for a new system</p>

<p class="quiz-option"><strong>D.</strong> Debugging a production hotfix under time pressure</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Mechanical, well-defined tasks with existing patterns are ideal for agents. Novel algorithms, architecture decisions, and hotfixes are better done manually.</p>

<hr/>

<p class="quiz-question">Which signal indicates you should start a NEW session (not continue)?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Agent generates working code on first try</p>

<p class="quiz-option"><strong>B.</strong> Agent asks a question already answered 10 turns ago</p>

<p class="quiz-option"><strong>C.</strong> You see a minor typo in agent's output</p>

<p class="quiz-option"><strong>D.</strong> Agent completes a subtask successfully</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Forgetting already-answered questions is a sign of context degradation. Minor typos or successful completions are not restart signals.</p>

<hr/>

<p class="quiz-question">Before restarting a session, what should you do?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Delete all files the agent created</p>

<p class="quiz-option"><strong>B.</strong> Compress session and save key decisions to AGENTS.md</p>

<p class="quiz-option"><strong>C.</strong> Ask agent to rewrite everything from scratch</p>

<p class="quiz-option"><strong>D.</strong> Nothing - just close and reopen</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Compress preserves decisions. Starting fresh without context means agent re-explores and misses design rationale.</p>

<hr/>

<p class="quiz-question">Context budget is at 85%. Agent is working well on the same feature. What should you do?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Restart immediately before context gets worse</p>

<p class="quiz-option"><strong>B.</strong> Continue until context is 100% full</p>

<p class="quiz-option"><strong>C.</strong> Compress proactively, continue same session</p>

<p class="quiz-option"><strong>D.</strong> Switch to a different project</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">Proactive compression is better than waiting until full degradation or restarting prematurely. Compress now, continue working.</p>

<hr/>

<p class="quiz-question">Why is 'agent should do everything' a misconception?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Agents are too slow for any real work</p>

<p class="quiz-option"><strong>B.</strong> Best results come from strategic delegation, not full replacement</p>

<p class="quiz-option"><strong>C.</strong> Agents cannot write any useful code</p>

<p class="quiz-option"><strong>D.</strong> Manual coding is always faster</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Agent is a force multiplier. Delegate mechanical work, keep creative and high-stakes decisions for yourself. Knowing what NOT to delegate is key.</p>

<hr/>

<p class="quiz-question">You need to implement a search feature. The codebase has 3 existing search implementations. Agent or manual?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Agent - pattern exists to follow</p>

<p class="quiz-option"><strong>B.</strong> Manual - search is too complex for agents</p>

<p class="quiz-option"><strong>C.</strong> Neither - this cannot be done with current tools</p>

<p class="quiz-option"><strong>D.</strong> Always manual for any feature</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">Existing patterns make this ideal for agents. Agent can read existing implementations, extract the pattern, and replicate for new use case.</p>

<hr/>

<p class="quiz-question">A session has been running 4 hours on authentication. Agent now suggests approaches already rejected. What happened?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Agent is learning and reconsidering</p>

<p class="quiz-option"><strong>B.</strong> Context pollution - agent is forgetting earlier decisions</p>

<p class="quiz-option"><strong>C.</strong> This is normal agent behavior</p>

<p class="quiz-option"><strong>D.</strong> The authentication system changed</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Revisiting already-rejected approaches is a clear sign of context degradation. Compress and restart.</p>

<hr/>

<p class="quiz-question">What is the cost of NOT compressing before restart?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Zero - agent remembers across sessions</p>

<p class="quiz-option"><strong>B.</strong> Agent re-explores codebase and misses previous decisions</p>

<p class="quiz-option"><strong>C.</strong> Files get corrupted</p>

<p class="quiz-option"><strong>D.</strong> Token costs increase by 10x</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Without compressed summary, fresh session has no memory of design decisions. Agent wastes tokens re-discovering what was already settled.</p>

<hr/>

<p class="quiz-question">Which pair is correctly matched?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Test writing → Manual; Cryptography → Agent</p>

<p class="quiz-option"><strong>B.</strong> Boilerplate → Agent; Architecture decisions → Manual</p>

<p class="quiz-option"><strong>C.</strong> Code review → Manual; Bug hunting → Manual</p>

<p class="quiz-option"><strong>D.</strong> Hotfixes → Agent; Documentation → Manual</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Boilerplate is mechanical (good for agent). Architecture decisions require human judgment (good for manual).</p>


---

# Module 2: opencode Architecture & Modes

Est. study time: 1.5h
Language: en

## Learning Objectives
- Map opencode tool system and permission model
- Distinguish Plan, Build, and Custom modes
- Design custom modes with tool-permission tables
- Build a multi-mode workflow pipeline

---

## Core Content

### Tool System Overview

opencode agents access filesystem via tools. Each tool has specific capability:

| Tool | Does | Permission needed |
|------|------|-------------------|
| Read | Read any file | Read |
| Write | Write/create files | Write |
| Edit | Modify existing files | Write |
| Glob | Pattern-match file paths | Read |
| Grep | Search file contents | Read |
| Bash | Run shell commands | Write |
| Task | Spawn subagent | Varies by subagent mode |
| Compress | Summarize context | Always allowed |
| Question | Ask user | Always allowed |

> **Think**: Which tool would you block in a mode meant only for code review?
> *Answer: Write, Edit, Bash (all can modify system). Read + Glob + Grep + Question are sufficient for review.*

### Permission Model

Modes restrict tool access at system level. This is **not a prompt** — agent physically cannot call disallowed tools.

```text
Plan mode: Read + Glob + Grep + Task + Compress + Question
           NO: Write, Edit, Bash, tool deletion

Build mode: ALL tools available

Custom mode: YOUR rules
```

> **Think**: Why enforce at system level instead of just telling agent "don't write files"?
> *Answer: Prompts can be ignored or forgotten. System-level enforcement is absolute. Agent CANNOT write even if it tries.*

### Plan / Build / Custom Modes

| Mode | Use Case | Safety |
|------|----------|--------|
| **Plan** | Design, explore, ask questions before committing | Zero risk of unwanted changes |
| **Build** | Implementation with full power | Full trust, full responsibility |
| **Custom** | Create role-specific guardrails | Configurable per role |

> **Think**: A junior dev on your team wants to use opencode. Which mode do you give them?
> *Answer: Custom "junior" mode: Read + Write tests only. No modify source, no bash. Promotes safety while they learn.*

### Custom Mode Catalog

| Mode | Tools Allowed | Tools Blocked | Use Case |
|------|--------------|---------------|----------|
| **Researcher** | Read, Glob, Grep, Task (explore), Write (.md only) | Write (src), Edit, Bash | Investigate issues, write design docs. Cannot touch source. |
| **Reviewer** | Read, Glob, Grep, Question, Write (review output) | Write (src), Edit, Bash | PR review, code audit, style check. |
| **Tester** | Read, Glob, Grep, Write (test/ only) | Write (src/), Edit (src/), Bash | Write test coverage without risk to source. |
| **Commiter** | Read, Glob, Grep, Bash (git only) | Write, Edit | Stage, commit, push. No code changes. |
| **Linter** | Read, Glob, Grep, Bash (lint tools only) | Write, Edit | Enforce style, report violations. |
| **Architect** | Read, Glob, Grep, Write (docs/ only) | Write (src/), Edit, Bash | RFCs, ADRs, architecture documents. |
| **Scaffolder** | Write (new files only), Read, Glob, Grep | Edit (existing files), Bash | Generate boilerplate, new components. |
| **Security Scout** | Read, Glob, Grep, Bash (security tools) | Write, Edit | Vulnerability scan, dependency audit. |
| **Janitor** | Read, Glob, Grep, Edit, Bash (delete/rename) | Write (new features) | Clean dead code, rename, restructure. |
| **Deployer** | Read (configs), Bash (deploy commands) | Write, Edit (src) | Production deployments, rollbacks. |

> **Think**: Why does Scaffolder allow Write but block Edit? What risk does this prevent?
> *Answer: Can create new files but cannot modify existing ones. Prevents accidental edits to stable code during generation.*

### Multi-Mode Workflow Pipeline

Chain modes across development phases:

```text
Phase 1: RESEARCHER
    Agent investigates bug/feature request. Writes findings as .md.
    You review and approve direction.

Phase 2: ARCHITECT
    Agent designs solution. Writes RFC/ADR.
    You review design.

Phase 3: BUILD (default mode)
    Agent implements. Full tool access.
    You review code as it comes.

Phase 4: TESTER
    Agent writes tests for new code.
    Cannot touch source. Safe coverage.

Phase 5: REVIEWER
    Agent audits full diff. Read-only.
    Produces review report.

Phase 6: COMMITER
    You stage files manually.
    Agent writes commit message, commits, pushes.
```

Each phase locks agent to appropriate capabilities. Prevents jumping ahead.

> **Think**: What happens if you skip RESEARCHER and go straight to BUILD for a complex feature?
> *Answer: Agent may implement wrong approach because it didn't fully investigate. Researcher phase catches misunderstandings before code is written.*

---

## Why This Matters

Modes are the safety system of agentic development. Without them, agent has full filesystem access all the time. Custom modes let you match capability to task — reducing risk, improving focus, and enabling multi-phase workflows that catch errors early.

---

## Common Questions

**Q: Can I switch modes mid-session?**
A: Yes. Open a new session with desired mode. Or use mode-switching if supported by your opencode setup.

**Q: How many custom modes should I create?**
A: Start with 3-4 (Researcher, Reviewer, Tester, Commiter). Add more as you identify specific needs. Quality over quantity.

**Q: Can a mode be "read-only but can run tests"?**
A: Yes. Custom mode can allow specific Bash commands (e.g., `npm test`, `pytest`) while blocking Write/Edit.

**Q: Do custom modes work with subagents?**
A: Yes. When you spawn a task subagent, it inherits the current mode's permission set (or can be assigned its own mode).

---

## Examples

### Example 1: Researcher Mode Configuration

```text
Mode: Researcher
Read: ✅ (all files)
Write: ✅ (.md files only)
  - pattern: "**/*.md"
  - pattern: "docs/**"
Edit: ❌
Bash: ❌ (except read-only commands like `ls`, `cat`)
Task: ✅ (explore subagent only)
```

Best for: "Investigate why the login page is slow. Don't change anything."

### Example 2: Multi-Mode Bug Fix

Scenario: Production bug in payment processing.

1. **Researcher** mode: Agent investigates error logs, traces code path, writes findings.md
2. You review → confirm root cause
3. **Build** mode: Agent implements fix
4. **Tester** mode: Agent writes regression tests
5. **Reviewer** mode: Agent reviews full diff
6. **Commiter** mode: Agent writes commit message, commits

Each phase has safety rails. No premature commits. No untested changes.

---

## Key Takeaways
- Modes restrict tool access at system level (not just prompts)
- Plan = read-only. Build = full access. Custom = your rules.
- Custom mode catalog: Researcher, Reviewer, Tester, Commiter, Linter, Architect, Scaffolder, Security Scout, Janitor, Deployer
- Each mode has specific allowed/blocked tools
- Chain modes across dev lifecycle for safety and focus
- Start with 3-4 custom modes, grow as needed

---

## Common Misconception

**"Custom modes are just system prompts with different instructions."** No. Mode enforcement is at the **tool permission level**. You cannot prompt your way around a blocked tool. If a mode denies Write, the agent cannot write a single byte — no matter how cleverly it's prompted.

---

## Feynman Explain

(Explain custom modes to a developer who uses one editor for everything. Why would you want different "editors" for researching vs coding vs committing? Use an analogy from physical tools.)

---

## Reframe

(Judge: "All team members should use the same build mode" vs "each person should have custom modes." When would shared modes cause problems? When would custom modes create confusion?)

---

## Drill

Take the quiz. Run: `learn.sh quiz agentic-engineering 2`

## Quiz: 02-opencode-architecture

<p class="quiz-question">What is the key difference between Plan mode and Build mode?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Plan mode is faster; Build mode is slower</p>

<p class="quiz-option"><strong>B.</strong> Plan mode cannot write or edit files; Build mode can</p>

<p class="quiz-option"><strong>C.</strong> Plan mode uses a different AI model</p>

<p class="quiz-option"><strong>D.</strong> Build mode cannot read files</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Plan mode is read-only at system level. Agent physically cannot write or edit files. Build mode has full tool access.</p>

<hr/>

<p class="quiz-question">What does a mode restrict at the system level?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Which prompts the agent receives</p>

<p class="quiz-option"><strong>B.</strong> Which tools the agent can call</p>

<p class="quiz-option"><strong>C.</strong> Which files are visible in the filesystem</p>

<p class="quiz-option"><strong>D.</strong> Which programming languages are available</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Modes restrict tool access permissions. This is enforced at system level, not via prompting.</p>

<hr/>

<p class="quiz-question">Which mode should you use to investigate a bug without risking any file changes?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Build mode</p>

<p class="quiz-option"><strong>B.</strong> Researcher mode</p>

<p class="quiz-option"><strong>C.</strong> Commiter mode</p>

<p class="quiz-option"><strong>D.</strong> Scaffolder mode</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Researcher mode allows reading all files and writing only .md reports. Cannot touch source code.</p>

<hr/>

<p class="quiz-question">Which tools should a Reviewer mode allow?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Read, Glob, Grep, Question</p>

<p class="quiz-option"><strong>B.</strong> Write, Edit, Bash</p>

<p class="quiz-option"><strong>C.</strong> All tools including delete</p>

<p class="quiz-option"><strong>D.</strong> Bash only</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">Reviewer needs read-only access plus ability to produce review output. Write/Edit/Bash are unnecessary and risky.</p>

<hr/>

<p class="quiz-question">Why is system-level enforcement better than prompting 'don't write files'?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> System enforcement is cheaper</p>

<p class="quiz-option"><strong>B.</strong> Prompts can be ignored or forgotten; system enforcement cannot be bypassed</p>

<p class="quiz-option"><strong>C.</strong> System enforcement is faster</p>

<p class="quiz-option"><strong>D.</strong> System enforcement uses less tokens</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">No amount of prompting can override a blocked tool. System-level enforcement is absolute.</p>

<hr/>

<p class="quiz-question">What is the correct sequence for a safe multi-mode workflow?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Build → Researcher → Commiter → Reviewer</p>

<p class="quiz-option"><strong>B.</strong> Researcher → Build → Tester → Reviewer → Commiter</p>

<p class="quiz-option"><strong>C.</strong> Commiter → Tester → Build → Reviewer</p>

<p class="quiz-option"><strong>D.</strong> Reviewer → Build → Researcher → Tester</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Research first (understand problem), build (implement), test (verify), review (audit), commit (ship). Each phase has appropriate restrictions.</p>

<hr/>

<p class="quiz-question">Which mode allows creating new files but prevents editing existing ones?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Janitor</p>

<p class="quiz-option"><strong>B.</strong> Build</p>

<p class="quiz-option"><strong>C.</strong> Scaffolder</p>

<p class="quiz-option"><strong>D.</strong> Deployer</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">Scaffolder allows Write (new files) but blocks Edit (existing files). Safe for generating boilerplate.</p>

<hr/>

<p class="quiz-question">A junior developer needs to write tests without risk to source code. Which custom mode?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Build mode - they need full access</p>

<p class="quiz-option"><strong>B.</strong> Tester mode - read + write test files only</p>

<p class="quiz-option"><strong>C.</strong> Commiter mode - git only</p>

<p class="quiz-option"><strong>D.</strong> Plan mode - read only</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Tester mode allows reading source and writing to test directories only. Source code is safe from accidental modification.</p>

<hr/>

<p class="quiz-question">When would the Janitor mode be most useful?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Writing new features</p>

<p class="quiz-option"><strong>B.</strong> Cleaning dead code, renaming, restructuring</p>

<p class="quiz-option"><strong>C.</strong> Production deployments</p>

<p class="quiz-option"><strong>D.</strong> Code review</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Janitor mode allows delete/rename operations but blocks new feature code. Purpose-built for cleanup tasks.</p>

<hr/>

<p class="quiz-question">Which statement about custom modes is FALSE?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Custom modes can allow specific Bash commands while blocking others</p>

<p class="quiz-option"><strong>B.</strong> Custom modes are just system prompts with different instructions</p>

<p class="quiz-option"><strong>C.</strong> Custom modes can restrict Write to specific file patterns</p>

<p class="quiz-option"><strong>D.</strong> Custom modes can be used with subagents</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Custom modes are tool-permission configurations, not prompts. System-level enforcement is fundamentally different from instruction-based control.</p>


---

# Module 3: Instructions & Knowledge Persistence

Est. study time: 1.5h
Language: en

## Learning Objectives
- Write effective AGENTS.md instructions per project
- Use CLAUDE.md for cross-session memory
- Apply knowledge re-use tiers: session → project → global
- Compress context strategically between sessions

---

## Core Content

### The Memory Problem

Agent sessions are stateless. Each new session starts blank. Without persistence, agent re-explores codebase, re-learns conventions, repeats mistakes every session.

Solution: **layered memory system**.

```text
Session Memory (compress tool)    → lasts one session
Project Memory (AGENTS.md)        → lasts per repo, persists across sessions
Global Memory (CLAUDE.md)         → lasts per repo, long-term facts
Skills (custom skills)            → lasts across all repos, reusable workflows
```

> **Think**: A project has specific naming conventions. Where should you document them so every agent session uses them?
> *Answer: AGENTS.md. It's loaded at session start for that repo. CLAUDE.md is for facts learned, not static conventions.*

### AGENTS.md: Per-Project Instructions

AGENTS.md sits in project root. Loaded automatically at session start. Contains:

```text
What to put in AGENTS.md:
- Project conventions (naming, imports, folder structure)
- Framework choices (React 19 + Next.js + Tailwind)
- Testing approach (vitest + testing-library, minimum 80% coverage)
- Common commands (dev server, test suite, lint)
- Agent boundaries (what NOT to do: delete files, modify configs)
- Project-specific patterns (component structure, data flow)
```

Good AGENTS.md:

```text
# Project: course-content
# Framework: Next.js 14 + React 19 + Tailwind CSS
# Testing: vitest + @testing-library/react
# State: Zustand stores in src/stores/
# Conventions: kebab-case for files, PascalCase for components
# Do NOT modify: next.config.js, tailwind.config.ts, package.json
# Commands: npm run dev | npm test | npm run lint
```

Bad AGENTS.md:

```text
# Be careful with the code
# Write good tests
# Follow the project style
```

> **Think**: Why is "Write good tests" a bad AGENTS.md instruction?
> *Answer: Too vague. Agent doesn't know what "good" means. Specify: "Write vitest + testing-library tests. One test per component. Mock API calls."*

### CLAUDE.md: Learned Facts

CLAUDE.md stores facts the agent discovers during work. Updated by agent or you.

Examples of what goes in CLAUDE.md:

```text
# Learned during session 2024-01-15
# Auth token refresh occurs in middleware.ts, not API route
# User cache uses Redis with 5min TTL
# The legacy sort function in utils/sort.ts is deprecated, use lodash orderBy
```

CLAUDE.md is read at session start. Agent can suggest updates as it learns.

Rule: AGENTS.md = **static instructions you write**. CLAUDE.md = **dynamic facts discovered during work**.

> **Think**: You discover the CI pipeline runs tests in a specific order. Where to record this?
> *Answer: CLAUDE.md. It's a fact discovered during work, not a static instruction.*

### Knowledge Re-Use Tiers

| Tier | File | Scope | Updated by | Example |
|------|------|-------|------------|---------|
| Session | Compress tool | Current session | You (compress) | "We decided on PostgreSQL, rejected MongoDB" |
| Project | AGENTS.md | Per repo | You (manually) | "Test with vitest, coverage ≥80%" |
| Project | CLAUDE.md | Per repo | Agent + You | "Auth middleware at middleware.ts, not routes" |
| Global | Custom skills | All repos | You (manually) | "create-react-component skill for any React project" |

Promotion path: Session → noticed pattern → add to AGENTS.md → pattern generalizes → elevate to skill.

> **Think**: Session noticed the agent always writes tests after implementation. This is useful. Where to promote?
> *Answer: If specific to this project → AGENTS.md. If you want it in every project → custom skill or global AGENTS.md config.*

### Compression Strategy

Compression collapses conversation history into dense summary. Preserve:

```text
KEEP in compression:
- Design decisions made (with rationale)
- Rejected alternatives (so agent doesn't revisit)
- File paths created/modified
- Patterns established
- Current state (what's done, what's pending)

DROP from compression:
- Failed attempts that led nowhere
- Verbose tool outputs (long error logs, stack traces)
- Back-and-forth exploration noise
- Already-compressed segments that are superseded
```

Pattern: compress every 30-50 turns or when topic closes. Don't wait until context 100% full.

```text
Compress timing:
< 30 turns:  probably premature
30-50 turns:  good cadence for complex topics
50+ turns:    context likely degrading
> 70% budget: compress immediately
```

> **Think**: You have a long error trace from a failed build. Should you include it in compression summary?
> *Answer: No. Include the root cause conclusion, not the raw trace. "Build failed due to missing @types/react" not 200 lines of build output.*

---

## Why This Matters

Without memory persistence, every session is Groundhog Day. Agent re-discovers what it already learned. Knowledge tiers let you build institutional memory that compounds across sessions — each session starts smarter than the last.

---

## Common Questions

**Q: Should I commit AGENTS.md to version control?**
A: Yes. It's project configuration, like .eslintrc or tsconfig.json. CLAUDE.md is optional — commit if you want shared team memory.

**Q: What if AGENTS.md contradicts CLAUDE.md?**
A: AGENTS.md wins. It's explicit instructions. CLAUDE.md is discovered facts that may be stale.

**Q: Can I have multiple AGENTS.md files?**
A: Yes. Some setups support per-directory AGENTS.md. Check your opencode version's documentation.

**Q: Does compression lose information?**
A: Yes — deliberately. You lose noise, keep signal. If uncertain, keep the detail. Conservative compression is safer than aggressive.

---

## Examples

### Example 1: Compression Before Restart

Bad compression: "We worked on auth and made progress."

Good compression: "Auth system: implemented JWT refresh token flow. Token stored in httpOnly cookie. Refresh endpoint at POST /api/auth/refresh. Rejected approach of storing in localStorage (XSS vulnerability). Next: implement token rotation on refresh to prevent replay attacks. Files created: middleware.ts, lib/auth.ts, tests/auth.test.ts."

### Example 2: Knowledge Promotion

Session observation (3x): Agent always asks "what test framework do you use?"

Session 4 answer → add to AGENTS.md: `Testing: vitest + @testing-library/react`

After 3 projects with same setup → promote to custom skill `react-test-setup` with full instructions.

---

## Key Takeaways
- AGENTS.md = static instructions you write. CLAUDE.md = dynamic facts agent discovers.
- Knowledge tiers: session → project (AGENTS.md) → global (skills)
- Compress every 30-50 turns or when context >70%. Keep decisions, drop noise.
- Promote patterns noticed 3+ times to higher tier.
- Commit AGENTS.md. CLAUDE.md optional.

---

## Common Misconception

**"The agent will remember across sessions automatically."** No. Agent sessions are stateless. Without AGENTS.md, CLAUDE.md, or compression carryover, each session starts fresh. Memory persistence is your responsibility.

---

## Feynman Explain

(Explain the three knowledge tiers to a teammate who keeps everything in their head. Why write things down when you could just tell the agent each time?)

---

## Reframe

(Judge: "compress aggressively and restart often" vs "never compress, ride one session." Compare token costs, memory quality, and developer time tradeoffs.)

---

## Drill

Take the quiz. Run: `learn.sh quiz agentic-engineering 3`

## Quiz: 03-instructions-knowledge

<p class="quiz-question">What is the purpose of AGENTS.md?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Logging agent activity during sessions</p>

<p class="quiz-option"><strong>B.</strong> Providing per-project static instructions loaded at session start</p>

<p class="quiz-option"><strong>C.</strong> Storing authentication tokens</p>

<p class="quiz-option"><strong>D.</strong> Configuring the AI model parameters</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">AGENTS.md contains project conventions, testing approaches, and boundaries. Loaded automatically at session start.</p>

<hr/>

<p class="quiz-question">Where should you document a fact discovered during work (e.g., 'auth middleware is in middleware.ts')?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> AGENTS.md</p>

<p class="quiz-option"><strong>B.</strong> CLAUDE.md</p>

<p class="quiz-option"><strong>C.</strong> package.json</p>

<p class="quiz-option"><strong>D.</strong> README.md</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">CLAUDE.md stores dynamic facts discovered during sessions. AGENTS.md is for static instructions you write upfront.</p>

<hr/>

<p class="quiz-question">How often should you compress a session for complex tasks?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Every 5 turns</p>

<p class="quiz-option"><strong>B.</strong> Every 30-50 turns or when context exceeds 70%</p>

<p class="quiz-option"><strong>C.</strong> Only at end of day</p>

<p class="quiz-option"><strong>D.</strong> Never - compression loses information</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">30-50 turns or &gt;70% context is good cadence. Too early (5 turns) is premature. Too late degrades quality.</p>

<hr/>

<p class="quiz-question">What should you INCLUDE when compressing a session?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Full error traces from failed builds</p>

<p class="quiz-option"><strong>B.</strong> Design decisions made and rejected alternatives</p>

<p class="quiz-option"><strong>C.</strong> Every tool output verbatim</p>

<p class="quiz-option"><strong>D.</strong> Git commit history</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Keep design decisions, rejected alternatives, file paths created, patterns established. Drop raw error traces and noise.</p>

<hr/>

<p class="quiz-question">A pattern appears in 3+ projects. Where should it live?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> CLAUDE.md of each project</p>

<p class="quiz-option"><strong>B.</strong> Custom skill (global, all repos)</p>

<p class="quiz-option"><strong>C.</strong> A readme file</p>

<p class="quiz-option"><strong>D.</strong> Screenshot for reference</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Patterns generalizing across projects should be elevated to custom skills. Per-project files require duplication.</p>

<hr/>

<p class="quiz-question">Which is an example of a GOOD AGENTS.md instruction?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Write good code</p>

<p class="quiz-option"><strong>B.</strong> Test: vitest + @testing-library/react. Coverage ≥80%. One test per component.</p>

<p class="quiz-option"><strong>C.</strong> Be careful with dependencies</p>

<p class="quiz-option"><strong>D.</strong> Try your best</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Specific, actionable instructions beat vague encouragement. Name the framework, threshold, and pattern.</p>

<hr/>

<p class="quiz-question">What wins if AGENTS.md contradicts CLAUDE.md?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> CLAUDE.md - it's more recent</p>

<p class="quiz-option"><strong>B.</strong> AGENTS.md - it's explicit instructions</p>

<p class="quiz-option"><strong>C.</strong> Neither - ask the user</p>

<p class="quiz-option"><strong>D.</strong> Whichever has more detail</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">AGENTS.md is authoritative static instructions. CLAUDE.md is discovered facts that may be stale.</p>

<hr/>

<p class="quiz-question">What should you do when you notice the agent repeatedly asking the same question?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Ignore - it will learn eventually</p>

<p class="quiz-option"><strong>B.</strong> Add the answer to AGENTS.md</p>

<p class="quiz-option"><strong>C.</strong> Restart the session</p>

<p class="quiz-option"><strong>D.</strong> Switch to a different AI model</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Repeated questions indicate missing context. Add answer to AGENTS.md so every future session benefits.</p>

<hr/>

<p class="quiz-question">What is the promotion path for knowledge discovered in a session?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Keep it only in that session</p>

<p class="quiz-option"><strong>B.</strong> Session → noticed pattern → AGENTS.md → if general → skill</p>

<p class="quiz-option"><strong>C.</strong> Directly to publication</p>

<p class="quiz-option"><strong>D.</strong> Discard after session ends</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Pattern elevates from session memory to project config to global skill as it proves generalizable.</p>

<hr/>

<p class="quiz-question">Context is at 90%. You have 10 more minutes on this task. What should you do?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Keep working - task almost done</p>

<p class="quiz-option"><strong>B.</strong> Compress now, finish in same session</p>

<p class="quiz-option"><strong>C.</strong> Restart fresh, lose last decisions</p>

<p class="quiz-option"><strong>D.</strong> Ignore context - it adjusts automatically</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Compress proactively before context degrades. Finish task in same session. Don't push through near-empty context.</p>


---

# Module 4: Skills System Deep Dive

Est. study time: 2h
Language: en

## Learning Objectives
- Use built-in skills (caveman, review, commit, cavecrew, learn-anything)
- Decide when to create custom skills vs use inline instructions
- Choose between flexible (description-only) and scripted (deterministic) skill designs
- Map available hooks and events for automation
- Manage skill lifecycle: create, test, publish, maintain

---

## Core Content

### What Skills Are

Skills package instructions + optional scripts into reusable units. Loaded when triggered by name or automatically.

```text
Skill = Instructions (what agent should do)
      + Optional scripts (deterministic behavior)
      + Metadata (name, description, trigger)
      + Trigger conditions (keyword, event, file change)
```

> **Think**: How is a skill different from AGENTS.md?
> *Answer: AGENTS.md loads every session. Skills load only when triggered. Skills can contain executable scripts. AGENTS.md is pure instructions.*

### Built-in Skills Catalog

| Skill | Trigger | What it does |
|-------|---------|--------------|
| **caveman** | `caveman` keyword | Ultra-compressed communication. Drops articles/filler/pleasantries. |
| **caveman-help** | `caveman help` | Quick reference for all caveman modes. |
| **caveman-review** | `caveman review` | Ultra-compressed code review comments: location, problem, fix. |
| **caveman-commit** | `/commit` or `write commit` | Compressed Conventional Commits messages. Subject ≤50 chars. |
| **caveman-compress** | `compress memory file` | Compress CLAUDE.md/memory files into caveman format. |
| **caveman-stats** | `caveman stats` | Show token usage and estimated savings for session. |
| **cavecrew** | `delegate`, `use cavecrew` | Subagent delegation: Investigator (locate), Builder (1-2 file edit), Reviewer (diff review). |
| **learn-anything** | `learn X` | Structured curriculum builder + MCQ + spaced repetition. |
| **customize-opencode** | opencode config editing | Safe editing of opencode configuration files. |

> **Think**: Which skill would you use to save tokens when writing commit messages?
> *Answer: caveman-commit. Compressed Conventional Commits with ≤50 char subject. Cuts commit message tokens ~70%.*

### When to Create Custom Skills

Create skill when pattern appears **3+ times**:

| Scenario | Skill or not? |
|----------|--------------|
| "Create React component with tests" done 3x | ✅ Create skill |
| "Deploy to production" happens weekly | ✅ Create skill |
| One-time database migration script | ❌ Inline instruction |
| Project-specific ESLint rule | ❌ AGENTS.md (not general) |
| "Review PR for security issues" repeated task | ✅ Create skill |
| Team onboarding workflow with 5+ steps | ✅ Create skill |

> **Think**: Why wait for 3 repetitions? Why not create skill on first occurrence?
> *Answer: First occurrence may be one-off. Skill creation has overhead (authoring, testing, maintaining). 3x rule prevents premature abstraction.*

### Flexible vs Scripted Skill Design

**Flexible** (description-only):

```text
Skill: "code-reviewer"
Description: "Review code for correctness, style, security, performance.
Be thorough but concise. Tag issues as critical/major/minor.
Suggest fixes for each issue."
```

- Cheap to create. LLM interprets freely.
- Inconsistent output. Varies by model state.
- Handles edge cases naturally.
- Best for: creative tasks, strategy, nuanced review.

**Scripted** (deterministic steps):

```text
Skill: "deploy-check"
Script:
  1. Run `npm run typecheck` → fail if errors
  2. Run `npm run lint` → fail if warnings
  3. Run `npm test` → fail if any test fails
  4. Run `npm run build` → fail if errors
  5. If all pass: print "✅ Deploy ready"
  6. If any fail: print error report, exit 1
```

- Deterministic. Same input → same output.
- Expensive to write/maintain. Breaks on unexpected input.
- Best for: build steps, CI, mechanical transforms.

**Hybrid** (recommended):

```text
Skill: "feature-implementer"
Script: Run lint + typecheck + test
Instructions: "Implement feature per spec. Follow existing patterns.
After implementation, run verification script. Fix until green."
```

Script for mechanical gates. LLM for judgment.

| Aspect | Flexible | Scripted | Hybrid |
|--------|----------|----------|--------|
| Consistency | Low | High | Medium |
| Maintenance | Low | High | Medium |
| Edge cases | Handles well | Breaks loudly | Handles with script fallback |
| Token cost | Medium | Low | Low (script gates save tokens) |
| Best for | Strategy, review | Build, deploy | Full workflows |

> **Think**: Should a code review skill be flexible or scripted?
> *Answer: Flexible. Code review requires judgment. Scripted can't assess "is this logic correct?" Hybrid: script runs lint/typecheck (mechanical), LLM reviews logic (judgment).*

### Hooks and Events

Skills can attach to lifecycle events:

| Hook | Fires when | Use case |
|------|-----------|----------|
| `pre-message` | Before each message processed | Inject context, check permissions |
| `post-message` | After each message processed | Log decisions, update CLAUDE.md |
| `pre-tool` | Before specific tool call | Validate inputs, prevent destructive ops |
| `post-tool` | After specific tool call | Verify output, save results |
| `pre-commit` | Before git commit | Run pre-commit checks |
| `post-commit` | After git commit | Update changelog, notify |
| File watcher | On file change | Regenerate, retest |

Example: hook `pre-tool` for Write to block writing to config files.

```text
Skill: "config-guard"
Hook: pre-tool (Write)
Condition: file matches next.config.js or package.json
Action: block with message "Config files are read-only. Edit manually."
```

> **Think**: You want to ensure agent never deletes the package.json. Which hook + condition?
> *Answer: pre-tool for Delete/Bash(rm) with condition file = package.json. Block access.*

### Skill Lifecycle

```text
1. IDENTIFY need (3x repetition or critical workflow)
2. PROTOTYPE as inline instructions (verify it works)
3. FORMALIZE as skill (write description/script)
4. TEST in isolation (dry-run mode)
5. PUBLISH to skills directory
6. MONITOR usage (any failures? confusion?)
7. UPDATE as patterns evolve
8. RETIRE when no longer needed
```

Testing checklist before publishing:
- [ ] Run in dry-run mode → verify output
- [ ] Run on edge cases (empty input, missing files)
- [ ] Error messages readable without domain knowledge
- [ ] Token cost acceptable (skill shouldn't burn 5000 tokens to save 10s)
- [ ] Idempotent (running twice same result, or safe to re-run)
- [ ] Has human escape hatch (override flag)

> **Think**: Why test skill in dry-run mode before publishing?
> *Answer: Catches logical errors without risk. Scripted skills may have path errors, missing dependencies, or incorrect assumptions that are cheap to fix before production use.*

---

## Why This Matters

Skills are your most reusable asset. A good skill saves tokens, ensures consistency, and encodes hard-won patterns. Bad skills waste tokens and produce unreliable output. Understanding flexible vs scripted tradeoffs is what separates novice from expert skill authors.

---

## Common Questions

**Q: Can skills call other skills?**
A: Yes. A deploy skill can call test skill and lint skill internally. Composition reduces duplication.

**Q: How do I share skills with my team?**
A: Put skills in version control. Or use opencode's skill distribution mechanism if available.

**Q: What if a skill doesn't work as expected?**
A: Check logs. Run in isolation with minimal input. Add debugging output. Iterate.

**Q: Can I write skills in any language?**
A: Scripts can be any executable (bash, python, node). Instructions are plaintext/markdown.

---

## Examples

### Example 1: Hybrid Security Review Skill

```text
Name: security-review
Type: hybrid
Script: run `npm audit`, `snyk test`, `grep -r "apiKey\|secret\|password" src/`
Instructions: "Review code for security issues.
Check: hardcoded secrets, SQL injection, XSS, CSRF, auth bypass.
For each finding: tag severity (critical/major/minor), location, suggested fix.
Start with script output, then review code logic."
```

Script finds low-hanging fruit (known vulns, hardcoded secrets). LLM reviews logic (auth flaws, injection points).

### Example 2: Avoid Premature Skills

Bad: Create skill for "write a README.md" after doing it once. Next task is different.

Good: After 3rd time writing READMEs for different projects, notice pattern (sections: description, install, usage, API, contributing). Create skill with template and style guide.

---

## Key Takeaways
- Skills = instructions + optional scripts + triggers
- Built-in: caveman, review, commit, cavecrew, learn-anything, customize-opencode
- Create skill when pattern repeats 3+ times
- Flexible (LLM judges) vs Scripted (deterministic) vs Hybrid (best of both)
- Hooks: pre/post message, pre/post tool, file watchers, git hooks
- Lifecycle: identify → prototype → formalize → test → publish → monitor → update → retire

---

## Common Misconception

**"Every task should have a skill."** Skills have overhead: creation, testing, maintenance, token cost at trigger. Not every task benefits from skill-ification. The 3x repetition rule prevents premature abstraction. A one-off task is cheaper with inline instructions than a skill that'll never be used again.

---

## Feynman Explain

(Explain the difference between flexible and scripted skills using a cooking analogy. When would you follow a recipe exactly vs cook by taste?)

---

## Reframe

(Judge: "always make hybrid skills" vs "flexible first, add scripts when consistency fails." Which approach leads to better skills over time? What's the cost of over-engineering a skill?)

---

## Drill

Take the quiz. Run: `learn.sh quiz agentic-engineering 4`

## Quiz: 04-skills-system

<p class="quiz-question">How is a skill different from AGENTS.md?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Skills are shorter than AGENTS.md</p>

<p class="quiz-option"><strong>B.</strong> Skills load on trigger, can include scripts. AGENTS.md loads every session.</p>

<p class="quiz-option"><strong>C.</strong> AGENTS.md is for the user, skills are for the agent</p>

<p class="quiz-option"><strong>D.</strong> There is no difference</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">AGENTS.md loads automatically per session. Skills load only when triggered and can contain executable scripts.</p>

<hr/>

<p class="quiz-question">Which built-in skill saves tokens when writing commit messages?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> learn-anything</p>

<p class="quiz-option"><strong>B.</strong> caveman-commit</p>

<p class="quiz-option"><strong>C.</strong> cavecrew</p>

<p class="quiz-option"><strong>D.</strong> caveman-compress</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">caveman-commit produces compressed Conventional Commits messages with ≤50 char subjects.</p>

<hr/>

<p class="quiz-question">When should you create a custom skill?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> The first time you do any task</p>

<p class="quiz-option"><strong>B.</strong> After noticing the same pattern 3+ times</p>

<p class="quiz-option"><strong>C.</strong> Only when requested by a teammate</p>

<p class="quiz-option"><strong>D.</strong> Never - built-in skills cover everything</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">3x repetition rule prevents premature abstraction. First occurrence may be one-off.</p>

<hr/>

<p class="quiz-question">Which skill type is best for a code review task?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Scripted - deterministic output</p>

<p class="quiz-option"><strong>B.</strong> Flexible - requires judgment</p>

<p class="quiz-option"><strong>C.</strong> No skill needed</p>

<p class="quiz-option"><strong>D.</strong> AGENTS.md only</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Code review requires judgment about correctness, architecture, and design. Flexible (LLM-driven) is appropriate.</p>

<hr/>

<p class="quiz-question">What is the advantage of a hybrid skill?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Only uses scripts</p>

<p class="quiz-option"><strong>B.</strong> Script handles mechanical gates, LLM handles judgment</p>

<p class="quiz-option"><strong>C.</strong> No LLM calls needed</p>

<p class="quiz-option"><strong>D.</strong> Faster than any other approach</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Hybrid splits work: script runs deterministic checks (lint, typecheck), LLM handles nuanced decisions.</p>

<hr/>

<p class="quiz-question">Which hook would you use to block agent from modifying package.json?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> post-message</p>

<p class="quiz-option"><strong>B.</strong> pre-tool (Write) with condition matching package.json</p>

<p class="quiz-option"><strong>C.</strong> file-watcher</p>

<p class="quiz-option"><strong>D.</strong> pre-commit</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">pre-tool hook fires before tool execution. Condition on file path blocks Write to protected files.</p>

<hr/>

<p class="quiz-question">What is the correct skill lifecycle order?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Publish → Test → Prototype → Identify</p>

<p class="quiz-option"><strong>B.</strong> Identify → Prototype → Formalize → Test → Publish → Monitor → Update → Retire</p>

<p class="quiz-option"><strong>C.</strong> Formalize → Test → Identify → Publish</p>

<p class="quiz-option"><strong>D.</strong> Prototype → Publish → Identify → Test</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Identify need first, then prototype, formalize, test, publish, monitor, update, retire.</p>

<hr/>

<p class="quiz-question">A team member proposes creating a skill for 'start the dev server.' Should you?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Yes - every repeated action needs a skill</p>

<p class="quiz-option"><strong>B.</strong> No - this is a one-command action. Inline or alias is fine.</p>

<p class="quiz-option"><strong>C.</strong> Yes - but make it scripted</p>

<p class="quiz-option"><strong>D.</strong> No - skills can't run shell commands</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Starting a server is a single command. Skill overhead (creation, trigger) unnecessary. Shell alias or package.json script is better.</p>

<hr/>

<p class="quiz-question">Which is TRUE about scripted skills?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> They handle edge cases better than flexible skills</p>

<p class="quiz-option"><strong>B.</strong> They produce deterministic output but break on unexpected input</p>

<p class="quiz-option"><strong>C.</strong> They cost more tokens than flexible skills</p>

<p class="quiz-option"><strong>D.</strong> They cannot run bash commands</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Scripted skills are deterministic (same input → same output) but break on unexpected input. Flexible skills handle edge cases better.</p>

<hr/>

<p class="quiz-question">What should you check before publishing a skill?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Only that it works on happy path</p>

<p class="quiz-option"><strong>B.</strong> Dry-run + edge cases + readable errors + acceptable token cost + idempotent + human escape hatch</p>

<p class="quiz-option"><strong>C.</strong> That the skill name is memorable</p>

<p class="quiz-option"><strong>D.</strong> That it matches AGENTS.md</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Quality checklist: dry-run, edge cases, error clarity, token cost, idempotency, override capability. Happy path alone is insufficient.</p>


---

# Module 5: Spec Crafting for Agent Execution

Est. study time: 1.5h
Language: en

## Learning Objectives
- Write specs agents execute reliably without over-specifying
- Choose right granularity for different task types
- Include acceptance criteria the agent can self-verify
- Provide effective technical context

---

## Core Content

### The Specification Problem

Humans fill gaps from context. Agents don't. What's "obvious" to you is invisible to agent.

```text
Human spec: "Add search to the user list page"
Human reads: add search bar, filter results, handle empty state, debounce input

Agent reads: "add search" → what search? which field? API? client-side? debounce? pagination?
```

Write with **explicit gap-filling**. Assume agent knows nothing beyond what's in the spec + codebase.

> **Think**: Why does "add search" fail as agent spec?
> *Answer: Too many unknowns. Agent must guess: search field, API endpoint, debounce timing, UI placement, empty state, error handling. Each guess may be wrong.*

### Good vs Bad Specs

| Bad | Good |
|-----|------|
| "Fix the login bug" | "Login returns 500 when email contains '+' character. Fix input sanitization in POST /api/auth/login. Add test for email with '+'." |
| "Add sorting to table" | "Add sort by name and date to UserTable component. Click header to toggle asc/desc. Default: sort by name asc. Use existing useSort hook in hooks/useSort.ts." |
| "Improve performance" | "Profile shows UserList re-renders on every keystroke in search input. Memoize UserList with React.memo. Memoize filter function with useMemo." |
| "Write tests" | "Write vitest tests for useAuth hook: 1) returns null when not authenticated 2) returns user object when authenticated 3) throws on expired token 4) clears user on logout" |

> **Think**: What's common in all "good" columns?
> *Answer: Specific file paths, concrete behavior, existing patterns referenced, acceptance criteria that can be verified.*

### Spec Template

```text
Task: [One-line summary]
Scope: [Files to create/modify. Be specific.]
Acceptance:
  - [Measurable criteria 1]
  - [Measurable criteria 2]
Context:
  - [Existing pattern to follow]
  - [Rejected approaches (don't explore again)]
  - [Constraints or boundaries]
Verification:
  - [How to confirm it works: test command, manual check]
```

Example:

```text
Task: Add email uniqueness validation to user registration
Scope: modify src/api/auth/register.ts
Acceptance:
  - 409 response when email exists (case-insensitive)
  - 201 response when email unique
  - Test covers both cases
Context:
  - Follow existing validation pattern in src/api/users/create.ts
  - DB query: User.findByEmail(email) already exists
  - Do NOT add client-side validation (separate task)
Verification:
  - npm test src/api/auth/__tests__/register.test.ts
```

> **Think**: What's the cost of missing "rejected approaches" in spec?
> *Answer: Agent may explore and propose approaches already considered and rejected. Wastes tokens and time. Write down what NOT to do.*

### Granularity: How Big Should Spec Be?

| Task size | Spec detail | Agent autonomy | Best for |
|-----------|-------------|----------------|----------|
| Small (1-2 files) | High precision | Low | Bug fix, refactor, test |
| Medium (3-8 files) | Medium detail + pattern references | Medium | Feature addition |
| Large (8+ files) | Architecture + boundaries + file list | High | New feature, module |

Rule: **Spec scales inversely with agent autonomy**. Smaller tasks = tighter spec. Larger tasks = more room for agent to design.

```text
Small spec: "Fix this specific line. Change === to ==. Test passes."
Medium spec: "Add sort to table. Follow useSort pattern in hooks/. Files: UserTable.tsx, types.ts"
Large spec: "Add payment flow. Architecture: [diagram]. Files: [list]. Implement in order: 1) types 2) API 3) UI 4) tests"
```

> **Think**: A large feature spec with very high precision (every line specified) wastes what?
> *Answer: Agent's exploration ability. Over-specifying defeats purpose of using agent. You might as well write code yourself. Balance: enough direction to avoid wrong direction, enough freedom for agent to leverage codebase patterns.*

### Technical Context

Provide context agent cannot discover from codebase:

```text
Context to provide:
- Business rules not in code (e.g., "free tier users cannot export")
- Rejected approaches (saves agent from re-exploring dead ends)
- External dependencies (e.g., "rate limiter is external service, not in repo")
- Performance requirements (e.g., "must handle 1000 concurrent users")
- Security constraints (e.g., "never log user passwords")
```

Context NOT needed:
- Imports (agent reads existing code)
- Project conventions (should be in AGENTS.md)
- Framework API (agent already knows React, Express, etc.)

> **Think**: Should you specify which React hooks to use for a new feature?
> *Answer: Only if project uses non-standard hooks. Standard hooks (useState, useEffect, useMemo) agent already knows. Let it choose based on codebase patterns.*

---

## Why This Matters

Most agent implementation failures trace back to spec problems — not agent capability. Bad spec → wrong output → frustration. Good spec → right output → trust. Spec quality is the highest-leverage skill in agentic development.

---

## Common Questions

**Q: How do I know if my spec is detailed enough?**
A: Read it as if you're the agent. Would you know exactly what to do? Would you have any questions? If yes, add more.

**Q: What if agent still gets it wrong with good spec?**
A: Check if acceptance criteria are verifiable. If agent can't tell if it succeeded, it can't self-correct.

**Q: Should I write specs in issues/PRDs or in session?**
A: Both. External spec for team alignment. Session spec for agent execution. They may differ in format.

---

## Examples

### Example 1: Bug Fix Spec

Bad: "Fix the broken dropdown"

Good:
```text
Task: Dropdown menu closes immediately after opening on mobile
Scope: modify src/components/Dropdown/Dropdown.tsx
Acceptance:
  - Dropdown stays open on tap
  - Closes on tap outside
  - Same behavior across all breakpoints
Context:
  - Bug introduced in PR #142 (clickOutside handler added)
  - The handler fires on capture phase but should be bubble phase on mobile
  - Do NOT change desktop behavior
Verification: npm test src/components/Dropdown/__tests__/
```

### Example 2: Feature Spec - Right Granularity

```text
Task: Add dark mode toggle to settings page
Scope: new file src/components/Settings/DarkModeToggle.tsx
       modify src/context/ThemeContext.tsx
Acceptance:
  - Toggle switch in settings panel
  - Persists choice to localStorage
  - Applies immediately without page reload
  - Follows system preference on first visit
Context:
  - ThemeContext already has setTheme/getTheme
  - CSS variables for dark mode defined in globals.css
  - Follow existing toggle pattern in NotificationsToggle.tsx
  - Do NOT modify existing CSS variable definitions
Verification: npm test, then toggle manually in browser
```

---

## Key Takeaways
- Agents don't fill gaps. Write explicit specs.
- Include: scope, acceptance criteria, context (patterns, rejected, constraints), verification.
- Granularity: small tasks = tight spec. Large tasks = looser with architecture guide.
- Provide context agent can't discover: business rules, rejected approaches, performance/security constraints.
- Bad spec is #1 cause of agent failures. Spec quality is highest-leverage skill.

---

## Common Misconception

**"More detail is always better."** Over-specifying burns tokens and constrains agent's ability to leverage codebase patterns. The goal is to provide enough direction without writing the code yourself. If spec is longer than implementation, you should write it yourself.

---

## Feynman Explain

(Explain spec granularity to a junior developer. Why is "add search" both too vague and "add search with these 50 specific lines" too detailed? Where's the sweet spot?)

---

## Reframe

(Judge: "write everything in spec" vs "write minimum spec, let agent ask questions." Which leads to better outcomes? When would each approach be better?)

---

## Drill

Take the quiz. Run: `learn.sh quiz agentic-engineering 5`

## Quiz: 05-spec-crafting

<p class="quiz-question">Why does the spec 'Fix the login bug' fail for agent execution?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Agent cannot fix login bugs</p>

<p class="quiz-option"><strong>B.</strong> Too many unknowns: which bug, which file, what behavior</p>

<p class="quiz-option"><strong>C.</strong> Login bugs require manual intervention</p>

<p class="quiz-option"><strong>D.</strong> The spec is too long</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Agent doesn't know which bug, which file, expected behavior, or how to verify fix. Spec must be explicit.</p>

<hr/>

<p class="quiz-question">What should you include in every agent spec?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Full code implementation</p>

<p class="quiz-option"><strong>B.</strong> Scope, acceptance criteria, context, verification method</p>

<p class="quiz-option"><strong>C.</strong> Only the task name</p>

<p class="quiz-option"><strong>D.</strong> Screenshot of expected UI</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Scope (files), acceptance criteria (measurable), context (patterns, constraints), verification (how to confirm).</p>

<hr/>

<p class="quiz-question">A large feature (8+ files) should have what level of spec detail?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Every line specified</p>

<p class="quiz-option"><strong>B.</strong> Architecture guide + boundaries + file list. More agent autonomy.</p>

<p class="quiz-option"><strong>C.</strong> Same as a 1-file bug fix</p>

<p class="quiz-option"><strong>D.</strong> No spec - let agent figure everything out</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Large tasks benefit from architecture direction and boundaries, not line-by-line specs. Agent needs room to explore and implement.</p>

<hr/>

<p class="quiz-question">What information should you include in the 'Context' section of a spec?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Imports that the agent should use</p>

<p class="quiz-option"><strong>B.</strong> Business rules not in code, rejected approaches, constraints</p>

<p class="quiz-option"><strong>C.</strong> Full git history</p>

<p class="quiz-option"><strong>D.</strong> Framework documentation</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Context should include what agent cannot discover: business rules, rejected approaches, performance/security constraints.</p>

<hr/>

<p class="quiz-question">What is the risk of over-specifying a task?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Agent produces better code</p>

<p class="quiz-option"><strong>B.</strong> Wastes tokens, constrains agent's ability to leverage codebase patterns</p>

<p class="quiz-option"><strong>C.</strong> No risk - more detail is always better</p>

<p class="quiz-option"><strong>D.</strong> Agent runs faster</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Over-specifying constrains agent exploration and wastes tokens. If spec is longer than implementation, write the code yourself.</p>

<hr/>

<p class="quiz-question">Which acceptance criterion is MEASURABLE?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> The feature should feel fast</p>

<p class="quiz-option"><strong>B.</strong> Returns 200 with user data. Returns 404 for unknown ID. Test covers both.</p>

<p class="quiz-option"><strong>C.</strong> Make it work well</p>

<p class="quiz-option"><strong>D.</strong> Improve user experience</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Measurable criteria are specific and verifiable. 'Feel fast' and 'work well' cannot be objectively checked.</p>

<hr/>

<p class="quiz-question">What is the key difference between specs for humans vs specs for agents?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> No difference</p>

<p class="quiz-option"><strong>B.</strong> Humans fill gaps from context. Agents need explicit gap-filling.</p>

<p class="quiz-option"><strong>C.</strong> Agent specs should be shorter</p>

<p class="quiz-option"><strong>D.</strong> Human specs should be more detailed</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Humans infer missing details from experience and context. Agents execute literally. Write with explicit gap-filling.</p>

<hr/>

<p class="quiz-question">Your spec includes 'Use the existing pattern.' What else might be needed?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Nothing - agent will find it</p>

<p class="quiz-option"><strong>B.</strong> Reference to which file has the pattern: 'Follow pattern in src/hooks/useSort.ts'</p>

<p class="quiz-option"><strong>C.</strong> Full pattern code</p>

<p class="quiz-option"><strong>D.</strong> Git blame output</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Specify which file contains the pattern. 'Existing pattern' is too vague — agent may look at wrong file.</p>

<hr/>

<p class="quiz-question">Should you include rejected approaches in spec context?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> No - let agent discover them</p>

<p class="quiz-option"><strong>B.</strong> Yes - saves agent from re-exploring dead ends</p>

<p class="quiz-option"><strong>C.</strong> Only if there are more than 3</p>

<p class="quiz-option"><strong>D.</strong> No - it limits creativity</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Rejected approaches save tokens and prevent agent from wasting time on paths already ruled out.</p>

<hr/>

<p class="quiz-question">A medium-size feature (adding sort to a table). Which spec is best?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Add sort to UserTable. Use existing useSort hook. Click header to toggle.</p>

<p class="quiz-option"><strong>B.</strong> Add sort. Make it work.</p>

<p class="quiz-option"><strong>C.</strong> Add sort by implementing sortComparator with merge sort algorithm...</p>

<p class="quiz-option"><strong>D.</strong> npm install sort-table-lib and use it</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">Medium detail: references existing pattern, specifies behavior, doesn't over-specify implementation. Agent can follow useSort hook pattern.</p>


---

# Module 6: Dev Loop Patterns

Est. study time: 1.5h
Language: en

## Learning Objectives
- Apply Plan→Explore→Implement→Verify→Review loop
- Choose between discovery-first and spec-first approaches
- Use agents effectively for debugging
- Detect and break out of loop inefficiencies

---

## Core Content

### The Standard Dev Loop

```text
PLAN → EXPLORE → IMPLEMENT → VERIFY → REVIEW → [iterate or done]

PLAN:      Agent proposes approach. You approve or redirect.
EXPLORE:   Agent reads relevant files, understands patterns.
IMPLEMENT: Agent writes code.
VERIFY:    Agent runs checks (typecheck, lint, test).
REVIEW:    You inspect diff, approve changes or request fixes.
```

Each iteration tightens. First loop may be broad. Subsequent loops narrow.

> **Think**: Which step is most commonly skipped? What happens when it's skipped?
> *Answer: EXPLORE. Skipping leads to agent implementing against wrong patterns or missing context. Fix takes longer than explore would have.*

### Discovery-First vs Spec-First

**Spec-First**: You write detailed spec. Agent implements. Best when:
- Task is well-understood
- Requirements are clear
- Implementation path is obvious
- You know the codebase well

```text
You: "Add email validation to register form. Spec: [detailed]"
Agent: Implements per spec
You: Review → approve
Time: Fast. Single direction.
```

**Discovery-First**: Agent explores first, proposes plan, you refine. Best when:
- Task is fuzzy or complex
- You're unfamiliar with relevant code
- Multiple valid approaches exist
- Requirements need refinement

```text
You: "We need to add 2FA support. Explore options."
Agent: Reads auth code → finds TOTP lib → proposes 3 approaches
You: "Go with approach 2, but use different storage"
Agent: Implements
Time: Slower first loop. Fewer surprises.
```

> **Think**: When would discovery-first be cheaper overall despite slower first loop?
> *Answer: When spec-first would lead to wrong implementation. Discovery catches misunderstandings before code is written. Rework costs more than upfront exploration.*

### Choosing the Right Approach

| Factor | Spec-First | Discovery-First |
|--------|-----------|-----------------|
| Task clarity | High | Low |
| Codebase familiarity | High | Low |
| Number of valid approaches | 1 | 2+ |
| Risk tolerance | Higher | Lower |
| Token budget | Tight | Generous |
| Developer availability | Available to write spec | Busy, trust agent to explore |

Rule: If you can write a complete spec in 5 min → spec-first. If you need 30 min to understand the codebase → discovery-first.

```text
Decision flow:
Can you write a complete, verifiable spec in <5 min?
  YES → Spec-First
  NO  → Can you clearly describe the goal?
         YES → Discovery-First (agent explores, proposes plan)
         NO  → Agent can't help yet. Explore manually first.
```

> **Think**: You need to add a feature to a module you've never read. Approach?
> *Answer: Discovery-first. Let agent read the module, understand patterns, propose approach. Cheaper than you reading it yourself.*

### Debugging with Agents

Debugging is a natural discovery-first task:

```text
1. DESCRIBE symptom → not diagnosis
   Bad: "The bug is in auth middleware"
   Good: "Login returns 500 for users with '+' in email"

2. Let agent explore code path
   Agent reads: route handler → validation → DB query → error handler

3. Agent proposes root cause + fix
   "Found: input sanitization at src/middleware/validate.ts line 45
    doesn't encode '+' character. Fix: use encodeURIComponent."

4. Verify fix (agent proposes or runs test)
5. Apply fix + regression test
```

Debugging rules:
- State symptom, not diagnosis (agent may find different root cause)
- Provide reproduction steps (exact input, exact output)
- Set boundaries ("don't modify DB schema")
- Let agent read full error path before suggesting fix

> **Think**: Why should you state symptom not diagnosis for debugging?
> *Answer: Your diagnosis may be wrong. Agent may find different (correct) root cause if allowed to explore freely.*

### Breaking Out of Inefficient Loops

Signals loop is stuck:
- Agent making same error repeatedly
- Fix introduces new bug in unrelated code
- Agent re-reading same files
- Response length growing without progress

Breakout strategies:

```text
Stuck symptom        →  Breakout action
Same error repeats     Restart session (context poisoned)
Fix creates new bug    Reset to last known good state. Smaller scope.
Re-reading same files  Compress session. Restart fresh.
Growing response       Cut scope. "Only fix this specific line, nothing else."
Agent overconfident    "Run verification after each change. Show me evidence."
```

> **Think**: Agent has fixed the same bug 3 times, each fix breaks something else. What to do?
> *Answer: Reset to last clean state. Restart session fresh. Give much tighter spec: "Change ONE line: X to Y. Run tests. That's it."*

---

## Why This Matters

The dev loop is your core interaction pattern. Getting loop right means efficient, reliable agent output. Bad loop means frustration, rework, and wasted tokens. Discovery-first vs spec-first is the most impactful decision you make per task.

---

## Common Questions

**Q: Can I mix approaches mid-task?**
A: Yes. Start discovery-first for exploration, then spec-first for each subtask. Common pattern: "Explore the payment flow" then "Implement the refund endpoint with this spec."

**Q: How many explore → implement cycles is normal?**
A: 1-3 per task. More means something is wrong (bad spec, wrong approach, context degraded).

**Q: Should I review after every step or batch?**
A: For safety-critical: review after plan and after implementation. For routine: batch review at end. Tradeoff: safety vs momentum.

---

## Examples

### Example 1: Spec-First Success

Task: "Add timestamp to log output" (well-understood, single file)

Spec: "Modify src/utils/logger.ts: add ISO timestamp before each message. Format: `[2024-01-15T10:30:00Z] message`. Use `new Date().toISOString()`. Test: check log output format."

Agent: implement → verify → done. 2 minutes.

### Example 2: Discovery-First Success

Task: "Support WebSocket for real-time updates" (fuzzy, many approaches)

1. Explore: Agent reads current API (REST), checks if Socket.io or ws is installed, reads existing real-time patterns
2. Proposes: "Socket.io already installed. Add to server.ts. Create socket handlers in src/socket/. Connect from client via useSocket hook."
3. Refine: You add "only authenticated users, namespace /updates"
4. Implement: Agent follows approved plan
5. Review: Working, follows patterns

Total: 15 min (5 explore, 2 refine, 5 implement, 3 review). Spec-first would have been 15 min too but 50% chance wrong approach first.

---

## Key Takeaways
- Standard loop: Plan → Explore → Implement → Verify → Review
- Spec-first: detailed spec, fast execution, for well-understood tasks
- Discovery-first: explore then plan, for fuzzy or unfamiliar tasks
- Debugging: state symptom not diagnosis. Let agent explore code path.
- Break stuck loops: restart, smaller scope, tighter spec, verify after each change
- Decision: can you write spec <5 min? → Spec-first. Else → Discovery-first.

---

## Common Misconception

**"Discovery-first wastes tokens on exploration."** Discovery-first catches misunderstandings before code is written. Rework after wrong implementation costs more tokens and time than upfront exploration. The cheapest exploration is the one that prevents wrong code.

---

## Feynman Explain

(Explain the difference between spec-first and discovery-first using a navigation analogy. When do you use a detailed map vs explore and decide as you go?)

---

## Reframe

(Judge: "always discovery-first" vs "always spec-first." What are the hidden costs of each extreme? When would each one fail catastrophically?)

---

## Drill

Take the quiz. Run: `learn.sh quiz agentic-engineering 6`

## Quiz: 06-dev-loop

<p class="quiz-question">What is the correct order of the standard dev loop?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Implement → Plan → Verify → Explore → Review</p>

<p class="quiz-option"><strong>B.</strong> Plan → Explore → Implement → Verify → Review</p>

<p class="quiz-option"><strong>C.</strong> Review → Implement → Plan → Explore → Verify</p>

<p class="quiz-option"><strong>D.</strong> Explore → Review → Plan → Implement → Verify</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Standard loop: Plan (approach), Explore (understand code), Implement (write), Verify (check), Review (human inspect).</p>

<hr/>

<p class="quiz-question">When is spec-first the better approach?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Task is fuzzy with multiple valid approaches</p>

<p class="quiz-option"><strong>B.</strong> Task is well-understood, requirements clear, codebase familiar</p>

<p class="quiz-option"><strong>C.</strong> You have limited time to write spec</p>

<p class="quiz-option"><strong>D.</strong> You don't know the codebase</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Spec-first works when you know exactly what to do. Discovery-first is better for fuzzy or unfamiliar tasks.</p>

<hr/>

<p class="quiz-question">When debugging with an agent, what should you provide?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Your diagnosis of the bug</p>

<p class="quiz-option"><strong>B.</strong> Symptom, reproduction steps, boundaries</p>

<p class="quiz-option"><strong>C.</strong> Full source code of everything</p>

<p class="quiz-option"><strong>D.</strong> Nothing - agent will figure it out</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">State symptom (not diagnosis), exact reproduction steps, and boundaries (what not to change). Let agent explore the code path.</p>

<hr/>

<p class="quiz-question">Agent has fixed the same bug 3 times. Each fix introduces a new bug. What to do?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Let it try again - 4th time might work</p>

<p class="quiz-option"><strong>B.</strong> Reset to last clean state. Restart session. Tighter spec.</p>

<p class="quiz-option"><strong>C.</strong> Fix it yourself completely</p>

<p class="quiz-option"><strong>D.</strong> Ask agent to fix faster</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Context is likely poisoned or approach is fundamentally wrong. Reset, restart, give much tighter scope.</p>

<hr/>

<p class="quiz-question">What is the risk of discovery-first?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Agent will definitely implement wrong thing</p>

<p class="quiz-option"><strong>B.</strong> Slower first loop, uses more tokens upfront</p>

<p class="quiz-option"><strong>C.</strong> Agent cannot explore code</p>

<p class="quiz-option"><strong>D.</strong> Only works for simple tasks</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Discovery-first costs more tokens upfront (exploration). Benefit: prevents wrong implementation. Tradeoff: token cost vs rework cost.</p>

<hr/>

<p class="quiz-question">What is the most commonly skipped loop step and its consequence?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Skip Plan → no direction</p>

<p class="quiz-option"><strong>B.</strong> Skip Explore → agent implements against wrong patterns</p>

<p class="quiz-option"><strong>C.</strong> Skip Verify → undetected bugs</p>

<p class="quiz-option"><strong>D.</strong> Skip Review → no human oversight</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Explore is most skipped. Agent assumes it knows the patterns. Leads to code that doesn't fit the codebase. Fixing takes longer than exploring.</p>

<hr/>

<p class="quiz-question">Agent response length is growing, it keeps re-reading same files, and progress stalls. What's happening?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Agent is being thorough</p>

<p class="quiz-option"><strong>B.</strong> Context is degraded. Restart session.</p>

<p class="quiz-option"><strong>C.</strong> This is normal behavior</p>

<p class="quiz-option"><strong>D.</strong> Files are too complex</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Growing response length and re-reading are signs of context degradation. Compress and restart fresh.</p>

<hr/>

<p class="quiz-question">You're unfamiliar with the codebase. Which approach is best?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Spec-first - you know the feature</p>

<p class="quiz-option"><strong>B.</strong> Discovery-first - agent explores, proposes plan, you refine</p>

<p class="quiz-option"><strong>C.</strong> Ask agent to implement without exploring</p>

<p class="quiz-option"><strong>D.</strong> Write full implementation yourself</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Discovery-first lets agent read code and propose approaches. You refine based on its findings. Cheaper than you reading everything.</p>

<hr/>

<p class="quiz-question">When should you switch from spec-first to discovery-first mid-task?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> When agent implements correctly on first try</p>

<p class="quiz-option"><strong>B.</strong> When agent asks clarifying questions about unclear requirements</p>

<p class="quiz-option"><strong>C.</strong> When spec is very detailed</p>

<p class="quiz-option"><strong>D.</strong> Never - pick one and stick with it</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Agent questions about requirements signal spec gaps. Switch to discovery: let agent explore and propose, then refine spec together.</p>

<hr/>

<p class="quiz-question">What is the best rule of thumb for choosing approach?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Always use spec-first - it's faster</p>

<p class="quiz-option"><strong>B.</strong> Always use discovery-first - it's safer</p>

<p class="quiz-option"><strong>C.</strong> If you can write complete spec &lt;5 min → spec-first. Else → discovery-first.</p>

<p class="quiz-option"><strong>D.</strong> Let the agent decide</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">5-minute rule: if spec fits in 5 min, write it. If not, you don't understand the task well enough → let agent explore first.</p>


---

# Module 7: Context & Compression Strategy

Est. study time: 1h
Language: en

## Learning Objectives
- Track and manage token budget across session
- Distinguish signal from noise in conversation history
- Apply compression at optimal times
- Preserve critical information through compression

---

## Core Content

### Token Budget Mechanics

Each session has finite token capacity. Context window fills with:
- System instructions (AGENTS.md, skills, initial prompt)
- Conversation history (your messages + agent responses)
- Tool outputs (file reads, search results, test output)
- Code snippets (generated or read)

```text
Typical budget breakdown:
~10%  System/instructions
~30%  Your messages + spec
~40%  Tool outputs (biggest consumer)
~20%  Agent responses + code
```

> **Think**: What's the biggest token consumer? How to reduce it?
> *Answer: Tool outputs (40%). Reduce by: limiting file reads (specify exact lines), summarizing search results, avoiding full test output on failure.*

### Signal vs Noise

```text
SIGNAL (keep):                          NOISE (drop):
Design decisions                        Full error traces (keep root cause only)
Rejected alternatives                   Verbose search results
File paths created/modified             Multiple read attempts of same file
Patterns established                    Trial-and-error exploration
Current state (done/pending)            "I'll check that file" statements
User preferences expressed              Speculative output before tool call
Test results (pass/fail summary)        Full test output (unless failed)
```

Compression replaces noise with signal summary.

> **Think**: A file read returns 300 lines. You only need 3 specific functions. What to do?
> *Answer: Don't include full output in spec. Say: "Read src/utils.ts lines 45-60 and 120-135." Or ask agent to extract only relevant portions.*

### When to Compress

| Context used | Action |
|-------------|--------|
| < 30% | No compression needed |
| 30-50% | Monitor. Compress if task phase closes. |
| 50-70% | Compress proactively. Don't wait. |
| 70-90% | Compress immediately if topic allows. |
| > 90% | Restart session. Compress summary for next session. |

Compression triggers (not just by percentage):
- Task phase completes (feature done, bug found, design approved)
- Agent shows confusion (repeating questions, forgetting context)
- Before restarting session
- After long tool output (error trace, search results)

> **Think**: Context is at 60%. Task is mid-implementation. Should you compress?
> *Answer: Probably not yet if task is flowing well. But if next step involves large file reads, compress first to make room.*

### What to Preserve Through Compression

Compression summary must include enough for agent to continue without re-exploring:

```text
Must preserve:
- Current task state ("Implementing auth middleware. Routes done, need token validation.")
- Design decisions made ("We chose JWT over session. Token in httpOnly cookie.")
- Rejected alternatives ("localStorage rejected for XSS reasons.")
- Files modified/created ("src/middleware/auth.ts, src/lib/jwt.ts")
- Patterns established ("Error handling via ApiError class, not thrown strings")
- Pending next steps ("Next: implement token refresh endpoint")
- Known issues ("Refresh endpoint currently has no rate limiting")
```

> **Think**: You're compressing mid-task. How do you decide what to keep about rejected alternatives?
> *Answer: Keep only alternatives agent might reasonably re-propose. Don't keep every passing thought. "Rejected localStorage due to XSS" saves re-debate.*

### Compression Anti-Patterns

```text
Anti-pattern 1: Compressing too aggressively
  Effect: Agent loses context, re-explores, wastes tokens
  Fix: When uncertain, keep more. Conservative compression > aggressive.

Anti-pattern 2: Never compressing until forced
  Effect: Agent quality degrades gradually, hard to notice
  Fix: Set compression timer. Every 30-50 turns, compress.

Anti-pattern 3: Including noise in compression
  Effect: Compression summary is as long as original
  Fix: Use template: state → decisions → files → patterns → next steps → issues

Anti-pattern 4: Compressing without saving decisions externally
  Effect: If session dies before restart, decisions lost
  Fix: Also save key decisions to AGENTS.md or CLAUDE.md
```

> **Think**: Why is "never compressing until forced" worse than compressing too early?
> *Answer: Degradation is gradual. You don't notice agent getting worse until it's unusable. Proactive compression prevents the gradual decline.*

---

## Why This Matters

Context management is the #1 practical constraint on agentic development. Running out of context mid-task is like running out of memory mid-application. Compression is your garbage collector — run it proactively, not when the system crashes.

---

## Common Questions

**Q: How long should compression summary be?**
A: For a 50-turn complex session: 300-500 words. For simple task: 100-200 words. If longer than 500 words, you're including noise.

**Q: Can I automate compression?**
A: Some setups support auto-compression at threshold. But manual compression with judgment is generally better.

**Q: Does compression affect agent quality?**
A: Good compression → no loss. Bad compression (dropping critical decisions) → agent confusion. Conservative is safer.

---

## Examples

### Example 1: Good Compression

Before: 50-turn session implementing payment flow. 2000+ tokens of conversation.

Compression:
```text
State: Payment flow implementation. Stripe integration done.
       Refund endpoint pending.
Decisions: Stripe over Braintree (lower fees for our volume).
           Webhook secret in env, not config file. No DB storage of full card numbers.
Files: src/api/payments/create.ts, src/services/stripe.ts, src/webhooks/stripe.ts
Pattern: All API routes use asyncHandler wrapper. Errors return {error: code, message}.
Pending: POST /api/payments/refund. Must check refund window (90 days from charge date).
Issues: Webhook endpoint not tested locally (Stripe CLI not installed).
```

After: 150 words. Agent can continue immediately without re-exploring.

### Example 2: Bad Compression

"Worked on payments. Stripe integration. Some progress on refund stuff. Need to finish refund endpoint."

90 words but zero usable context. Agent will re-explore everything.

---

## Key Takeaways
- Tool outputs consume ~40% of token budget. Be precise with reads.
- Compress proactively at 50-70%, not when forced at 90%.
- Preserve: state, decisions, rejected alternatives, files, patterns, next steps, issues.
- Drop: raw error traces, verbatim search results, speculative output.
- When uncertain, keep more. Conservative compression > aggressive.
- Set cadence: every 30-50 turns or when topic phase closes.

---

## Common Misconception

**"Compression loses information, so compress as little as possible."** Bad compression loses information. Good compression discards noise, preserves signal. The risk of running out of context (agent degradation) is higher than risk of compressing too much. Compress proactively.

---

## Feynman Explain

(Explain context budget to a developer. Why can't the agent just remember everything? Use working memory analogy: you can hold ~7 items in mind at once. Compression is like writing down the important things so you can forget the rest.)

---

## Reframe

(Judge: "compress at 50% every time" vs "compress only when quality degrades." Which strategy wastes more tokens overall? Which produces better output?)

---

## Drill

Take the quiz. Run: `learn.sh quiz agentic-engineering 7`

## Quiz: 07-context-compression

<p class="quiz-question">What consumes the most token budget in a typical session?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> System instructions</p>

<p class="quiz-option"><strong>B.</strong> Tool outputs</p>

<p class="quiz-option"><strong>C.</strong> User messages</p>

<p class="quiz-option"><strong>D.</strong> Agent greetings</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Tool outputs ~40% of budget. Be precise with file reads and search results.</p>

<hr/>

<p class="quiz-question">At what context usage should you compress proactively?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> 10%</p>

<p class="quiz-option"><strong>B.</strong> 50-70%</p>

<p class="quiz-option"><strong>C.</strong> 90%</p>

<p class="quiz-option"><strong>D.</strong> Only when session ends</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">50-70% is proactive zone. Don't wait until 90% when quality is already degrading.</p>

<hr/>

<p class="quiz-question">Which should you KEEP in a compression summary?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Full error trace from failed build</p>

<p class="quiz-option"><strong>B.</strong> Design decisions and rejected alternatives</p>

<p class="quiz-option"><strong>C.</strong> Every tool output verbatim</p>

<p class="quiz-option"><strong>D.</strong> Agent's greeting message</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Keep design decisions, rejected alternatives, file paths, patterns, pending steps. Drop raw traces and noise.</p>

<hr/>

<p class="quiz-question">What is the risk of compressing too aggressively?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Session ends prematurely</p>

<p class="quiz-option"><strong>B.</strong> Agent loses critical context, re-explores, wastes tokens</p>

<p class="quiz-option"><strong>C.</strong> Files get deleted</p>

<p class="quiz-option"><strong>D.</strong> Token budget increases</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Over-aggressive compression drops signal. Agent re-explores what was lost. When uncertain, keep more.</p>

<hr/>

<p class="quiz-question">Context is at 60% and task is flowing well with no confusion. What should you do?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Compress immediately</p>

<p class="quiz-option"><strong>B.</strong> Monitor, but compress if next step involves large file reads</p>

<p class="quiz-option"><strong>C.</strong> Restart session</p>

<p class="quiz-option"><strong>D.</strong> Ignore compression entirely</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">If flowing well, no need to compress immediately. But if large reads coming, compress first to make room.</p>

<hr/>

<p class="quiz-question">What is the recommended compression cadence for complex sessions?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Every 5 turns</p>

<p class="quiz-option"><strong>B.</strong> Every 30-50 turns or when topic phase closes</p>

<p class="quiz-option"><strong>C.</strong> Only at session end</p>

<p class="quiz-option"><strong>D.</strong> Never for simple tasks</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">30-50 turns or phase boundaries. Not too frequent (waste) and not too rare (degradation).</p>

<hr/>

<p class="quiz-question">What is the compression anti-pattern 'saving without external backup'?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Compressing too early</p>

<p class="quiz-option"><strong>B.</strong> Not saving decisions to AGENTS.md or CLAUDE.md, losing them if session dies</p>

<p class="quiz-option"><strong>C.</strong> Compressing too late</p>

<p class="quiz-option"><strong>D.</strong> Compressing too frequently</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Compression lives in session. If session dies, decisions die. Also save to external memory (AGENTS.md, CLAUDE.md).</p>

<hr/>

<p class="quiz-question">A file read returns 500 lines. You need 2 specific functions. Best approach?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Read full file, agent will filter</p>

<p class="quiz-option"><strong>B.</strong> Specify exact line ranges: 'Read lines 100-130 and 300-320'</p>

<p class="quiz-option"><strong>C.</strong> Ask agent to read entire file three times</p>

<p class="quiz-option"><strong>D.</strong> Skip reading, guess the implementation</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Exact line ranges minimize token waste. Full reads are the biggest token consumer.</p>

<hr/>

<p class="quiz-question">Which compression summary is MORE useful for continuing work?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Worked on search feature. Some progress. Need to finish.</p>

<p class="quiz-option"><strong>B.</strong> Search: implemented full-text search with PostgreSQL tsvector. Query at src/api/search.ts. Next: add pagination. Known: highlight snippet not working for CJK characters.</p>

<p class="quiz-option"><strong>C.</strong> Search feature. 2000 lines of code written.</p>

<p class="quiz-option"><strong>D.</strong> Did search stuff. Agent worked hard.</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Specific state, files, next steps, and known issues. Agent can continue without re-exploring.</p>

<hr/>

<p class="quiz-question">Mid-task, you notice agent re-reading files it already read. What's likely happening?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Agent is being thorough</p>

<p class="quiz-option"><strong>B.</strong> Context is degraded - agent forgot what it read</p>

<p class="quiz-option"><strong>C.</strong> Files changed since last read</p>

<p class="quiz-option"><strong>D.</strong> This is standard behavior</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Re-reading is a sign of context degradation. The content was likely in earlier context that's now compressed or pushed out.</p>


---

# Module 8: Planning & Style Enforcement

Est. study time: 1.5h
Language: en

## Learning Objectives
- Force agent to plan before writing code
- Define and enforce project conventions
- Use style guides effectively in prompts
- Apply safe refactoring patterns with agents

---

## Core Content

### Why Enforce Planning

Agents optimize for immediate task completion. Without planning step, agent starts writing code immediately — often wrong direction.

```text
No plan enforced:
  You: "Add user search"
  Agent: Writes search UI with client-side filtering (wrong for 10k users)
  You: "No, we need server-side search with debounce"
  Agent: Rewrites everything (wasted tokens)

Plan enforced:
  You: "Add user search. Propose approach first."
  Agent: "Client-side or server-side? User count? Search fields?"
  You: "Server-side. 10k users. email + name fields."
  Agent: Implements correctly first time.
```

> **Think**: How many tokens does "plan first" save in typical medium task?
> *Answer: 30-50% of total tokens. Rewriting wrong approach costs more than writing plan upfront.*

### Planning Prompt Templates

**Basic enforcement** (in every task prompt):

```text
Before writing code:
1. Read relevant files to understand existing patterns
2. Propose implementation approach with file list
3. I will review and approve before you begin
```

**Structured planning** (for complex tasks):

```text
Plan format:
- Approach: [one-paragraph summary]
- Files to modify: [list]
- Files to create: [list]
- Key design decisions: [3-5 bullet points]
- Risks/unknowns: [what you're unsure about]
- Estimated verification: [how you'll confirm it works]

Do NOT start implementation until I approve this plan.
```

> **Think**: What happens if you don't include "I will review and approve before you begin"?
> *Answer: Agent may treat plan as suggested direction and start implementing without waiting. Explicit approval gate prevents premature implementation.*

### Planning in AGENTS.md

Make planning default behavior for your project:

```text
## Planning Protocol
For any task beyond 1-file change:
1. Read relevant files (max 5 tool calls)
2. Propose approach with file list
3. Wait for approval before implementing
```

This loads every session, no need to repeat.

> **Think**: Should 1-line bug fixes also require planning?
> *Answer: No. Planning overhead exceeds benefit for trivial fixes. Reserve planning for multi-file or complex tasks.*

### Style Enforcement

Agents write in their own style unless told otherwise. Define style in AGENTS.md or per-task.

**What to specify:**

```text
Styling conventions:
- Import order: React → third-party → internal (absolute) → relative
- Naming: PascalCase components, camelCase functions, SCREAMING_SNAKE constants
- Error handling: Use Result type, not thrown exceptions
- File structure: One component per file. Component + test colocated.
- CSS: Tailwind utility classes. No CSS modules.
- State: Zustand stores in src/stores/. No Redux.
- API: tRPC router in src/server/api/. No REST.
```

**Enforcement methods:**

| Method | Strength | Overhead | Best for |
|--------|----------|----------|----------|
| AGENTS.md conventions | Passive (agent reads) | Low | Established rules |
| Per-task style block | Active (agent follows) | Medium | Task-specific rules |
| Verification gate | Hard (agent must pass) | High | Critical rules |
| Linter auto-fix | Automatic | Zero | Formatting only |

> **Think**: Why is "linter auto-fix" zero overhead but only for formatting?
> *Answer: Linter runs post-hoc, fixes automatically. Agent doesn't need to think about it. But linters can't enforce architectural conventions (file structure, naming patterns).*

### Refactoring with Agents

Safe refactoring pattern:

```text
1. EXPLORE: Agent maps all usages of the code to refactor
2. PLAN: Agent proposes refactor approach + impact analysis
3. APPROVE: You review plan for missed dependencies
4. EXECUTE: Agent performs refactor in small steps
5. VERIFY: Run typecheck + lint + test after each step
6. REVIEW: You inspect diff for correctness

Critical rules:
- One rename/reorg per step
- Verify after each step (not batch)
- Never refactor and add features in same step
- Keep original code until new code verified
```

**Refactoring anti-patterns:**

```text
Anti-pattern: Refactor + add feature in one go
  Problem: Bug could be in refactor OR feature. Hard to diagnose.
  Fix: Separate into two tasks.

Anti-pattern: Rename without checking all references
  Problem: Agent may miss string references, config files, or comments.
  Fix: Ask agent to find ALL usages before renaming.

Anti-pattern: Trust agent's grep results without verification
  Problem: Agent's grep may miss indirect references (dynamic imports, computed keys).
  Fix: Run typecheck after rename to catch missed references.
```

> **Think**: A rename task needs to update 15 files. Should agent batch all in one step?
> *Answer: No. Do 3-5 files per step, verify after each. If something breaks, you know which step caused it. Batching 15 files risks cascade failure.*

---

## Why This Matters

Without enforced planning, agent writes code immediately — often wrong, requiring rewrite. Without style enforcement, agent produces inconsistent code that needs human cleanup. Planning and style are force multipliers: invest upfront tokens, save massive rework.

---

## Common Questions

**Q: How detailed should style enforcement be?**
A: Enough to produce code you'd accept without manual reformatting. If you'd fix it manually, specify it.

**Q: What if AGENTS.md style rules are long?**
A: Keep them. 200 tokens of style rules saves thousands of tokens in rework. One-time cost per session.

**Q: Can agent enforce style automatically?**
A: Formatting → linter. Architecture → prompts. Naming → AGENTS.md. Don't rely on agent alone for style enforcement.

---

## Examples

### Example 1: Planning Gate

Bad: No gate
```text
You: "Add dark mode"
Agent: Writes CSS variables, toggle button, local storage. Uses class-based dark mode.
(Project uses CSS variables with data-theme attribute. Wrong approach.)
```

Good: With gate
```text
You: "Add dark mode. Propose approach first."
Agent: "CSS variables with data-theme? Or class toggle? Or CSS nesting?"
You: "data-theme attribute on html element. Variables in globals.css."
Agent: Implements correctly. First try.
```

### Example 2: Safe Rename

```python
# Step 1: Map usages
Agent: "UserService.findUsers() used in 12 files: routes/users.py, tests/test_users.py..."

# Step 2: Rename
Agent renames UserService.findUsers() → UserService.searchUsers()

# Step 3: Verify
Agent runs typecheck → passes
Agent runs tests → all pass

# Step 4: You review
Diff shows 12 files updated correctly.
```

---

## Key Takeaways
- Enforce plan-before-code with explicit approval gate
- Put planning protocol in AGENTS.md for automatic loading
- Style enforcement: AGENTS.md (low), per-task (medium), verification gate (high)
- Linter handles formatting. Prompts handle architecture.
- Refactor in small steps, verify after each step
- Never refactor + feature in same step
- Planning saves 30-50% tokens by preventing wrong direction

---

## Common Misconception

**"Planning wastes tokens — the agent should just write code."** Planning saves tokens. Wrong-first-direction costs 2-3x of planning overhead. A 100-token plan prevents 1000-token rewrite. Plan is cheap insurance.

---

## Feynman Explain

(Explain "plan first" to a developer who hates writing specs. Why does planning save time even though it feels like slowdown? Use construction analogy: measure twice, cut once.)

---

## Reframe

(Judge: "always enforce planning" vs "plan only for complex tasks." How do you define "complex"? What's the cost of false positive (plan for trivial task)? What's the cost of false negative (no plan for complex task)?)

---

## Drill

Take the quiz. Run: `learn.sh quiz agentic-engineering 8`

## Quiz: 08-planning-style

<p class="quiz-question">What happens when you don't enforce planning before implementation?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Agent works faster with fewer tokens</p>

<p class="quiz-option"><strong>B.</strong> Agent starts writing immediately, often in wrong direction</p>

<p class="quiz-option"><strong>C.</strong> Agent refuses to work</p>

<p class="quiz-option"><strong>D.</strong> Agent plans anyway without being asked</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Without enforcement, agent optimizes for speed → starts writing immediately. Often wrong direction → rework.</p>

<hr/>

<p class="quiz-question">How much token savings does 'plan first' typically provide?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> 10% or less</p>

<p class="quiz-option"><strong>B.</strong> 30-50% by preventing rewrites</p>

<p class="quiz-option"><strong>C.</strong> 100% - no tokens used</p>

<p class="quiz-option"><strong>D.</strong> Token usage increases</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Preventing wrong direction saves 2-3x of planning overhead. A 100-token plan prevents 1000-token rewrite.</p>

<hr/>

<p class="quiz-question">What is the purpose of the 'approval gate' in planning?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Slows down the agent</p>

<p class="quiz-option"><strong>B.</strong> Ensures agent waits for human review before implementing</p>

<p class="quiz-option"><strong>C.</strong> Lets agent decide when to proceed</p>

<p class="quiz-option"><strong>D.</strong> Automatically rejects all plans</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Approval gate ensures agent presents plan and waits for human confirmation before writing code.</p>

<hr/>

<p class="quiz-question">Which style enforcement method has zero overhead?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> AGENTS.md conventions</p>

<p class="quiz-option"><strong>B.</strong> Per-task style block</p>

<p class="quiz-option"><strong>C.</strong> Verification gate</p>

<p class="quiz-option"><strong>D.</strong> Linter auto-fix</p>

<p class="quiz-answer"><strong>Answer:</strong> D</p>

<p class="quiz-explanation">Linter auto-fix runs automatically post-hoc. Agent doesn't need to think about formatting.</p>

<hr/>

<p class="quiz-question">Why should you NOT refactor and add features in same step?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Agent cannot do both at once</p>

<p class="quiz-option"><strong>B.</strong> If bug appears, hard to tell if from refactor or new feature</p>

<p class="quiz-option"><strong>C.</strong> Refactoring is always unnecessary</p>

<p class="quiz-option"><strong>D.</strong> Features should never follow refactoring</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Bug origin becomes ambiguous. Separate refactor (behavior-preserving) from feature (behavior-changing).</p>

<hr/>

<p class="quiz-question">How many files should a rename step typically update at once?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> All files at once</p>

<p class="quiz-option"><strong>B.</strong> 3-5 files per step, verify after each</p>

<p class="quiz-option"><strong>C.</strong> 1 file only</p>

<p class="quiz-option"><strong>D.</strong> As many as possible</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Small batches (3-5) with verification after each. If something breaks, you know which step caused it.</p>

<hr/>

<p class="quiz-question">What should you verify after each refactoring step?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Only that files were saved</p>

<p class="quiz-option"><strong>B.</strong> Typecheck + lint + tests</p>

<p class="quiz-option"><strong>C.</strong> Only the UI looks correct</p>

<p class="quiz-option"><strong>D.</strong> Nothing - verify only at end</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Run typecheck (catches missed references), lint (styling), tests (behavior). Catch issues immediately.</p>

<hr/>

<p class="quiz-question">Where should you put planning protocol to avoid repeating it every session?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> In every task prompt</p>

<p class="quiz-option"><strong>B.</strong> In AGENTS.md</p>

<p class="quiz-option"><strong>C.</strong> In a separate chat</p>

<p class="quiz-option"><strong>D.</strong> In commit messages</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">AGENTS.md loads every session automatically. Write planning protocol once.</p>

<hr/>

<p class="quiz-question">Should a 1-line bug fix require a planning step?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Yes - always plan</p>

<p class="quiz-option"><strong>B.</strong> No - planning overhead exceeds benefit for trivial fixes</p>

<p class="quiz-option"><strong>C.</strong> Only if the bug is in production</p>

<p class="quiz-option"><strong>D.</strong> Only if you don't know the fix</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Planning overhead (reading files, writing proposal) exceeds time saved for trivial fixes. Reserve for complex tasks.</p>

<hr/>

<p class="quiz-question">Agent's grep for 'findUsers' missed files using dynamic import `import(`./services/${name}`)`. What went wrong?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Agent's grep was incorrect</p>

<p class="quiz-option"><strong>B.</strong> Dynamic imports and computed references are invisible to static grep</p>

<p class="quiz-option"><strong>C.</strong> The files didn't exist</p>

<p class="quiz-option"><strong>D.</strong> Agent skipped the search</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Static grep misses dynamic references. Run typecheck after rename to catch these. Don't trust grep alone.</p>


---

# Module 9: Subagent Delegation (Cavecrew)

Est. study time: 1h
Language: en

## Learning Objectives
- Distinguish when to use subagents vs inline work
- Use Cavecrew subagent types: Investigator, Builder, Reviewer
- Structure delegation prompts for subagents
- Manage context across subagent boundaries

---

## Core Content

### Why Subagents

Main agent context is precious. Each tool call and response consumes space. Subagents run in separate context — they explore, build, or review without polluting main thread.

```text
Inline work: Main context fills with exploration noise
    You: "Find all API routes"
    Agent reads 20 files... context now at 60%
    Agent still hasn't started implementation

Subagent delegation: Main context stays clean
    You: "Use investigator to map API routes"
    Subagent explores, returns compressed summary (200 tokens)
    Main agent uses summary → context still at 20%
    Agent starts implementation with full budget
```

> **Think**: Main context is at 70%. You need to research a complex database schema. Should you do it inline or delegate?
> *Answer: Delegate to investigator subagent. Schema exploration will consume 1000s of tokens. Subagent keeps that noise separate, returns only compressed summary.*

### Cavecrew Subagent Types

**Investigator** — Read-only code locator:
```text
Input: "Find all WebSocket connections and their handlers"
Output: File:line table. Compressed. No suggestions, no fixes.

Best for: Codebase mapping, usage analysis, impact assessment
Context saved: ~60% vs inline exploration
```

**Builder** — Surgical 1-2 file edit:
```text
Input: "Change function name X to Y in file Z"
Output: Diff receipt. Refuses 3+ file scope.

Best for: Typo fixes, single-function rewrites, mechanical renames
Context saved: Keeps large diffs out of main thread
```

**Reviewer** — Diff/branch reviewer:
```text
Input: "Review the diff for security issues"
Output: One line per finding. Severity-tagged. No praise, no scope creep.

Best for: PR review, pre-commit audit, post-implementation check
Context saved: Review findings as single summary, not full diff discussion
```

> **Think**: You need to rename a function used across 15 files. Which subagent to use?
> *Answer: Investigator first (map all usages) → You review → Builder (rename in batches, 3-5 files per call) → Reviewer (verify diff).*

### Delegation Structure

Effective subagent prompt:

```text
Task type: [investigate | build | review]
Scope: [exact files, exact question]
Output format: [what you need back]
Constraints: [boundaries, what NOT to do]
Main context: [compressed context so subagent isn't blind]
```

Example:

```text
Task type: investigate
Scope: Find all files importing from 'old-lib'. Check src/ and tests/ recursively.
Output format: File:line. Group by directory.
Constraints: Do NOT modify any files. Do NOT suggest fixes.
Main context: We're migrating from old-lib to new-lib. tracked in AGENTS.md.
```

Subagent returns compressed output (~60% smaller than inline equivalent).

> **Think**: Why include "main context" in delegation prompt? Doesn't subagent run fresh?
> *Answer: Subagent starts blank. Including key context (project goals, constraints, recent decisions) prevents it from making wrong assumptions.*

### When to Delegate vs Inline

| Factor | Delegate | Inline |
|--------|----------|--------|
| Context budget | < 40% remaining | > 60% remaining |
| Task scope | Isolated, bounded | Tightly coupled to main task |
| Output size | Large expected | Small expected |
| Parallel need | Yes (multiple delegations) | No |
| Decision dependency | Low (exploration only) | High (needs your input mid-task) |

Rule: If task would consume >20% of remaining context budget → delegate. If task output is simple "yes/no" or small diff → inline.

> **Think**: Main context is at 50%. You need to check if a function is used anywhere. Delegate or inline?
> *Answer: Delegate. Grep search + reading results consumes tokens. Subagent does it, returns "Used in 3 files: [file:line]." About 50 tokens.*

---

## Why This Matters

Subagent delegation is the most powerful context management technique. It lets you parallelize work (multiple subagents), protect main context from exploration noise, and receive compressed outputs. Cavecrew makes this structured with predefined agent types.

---

## Common Questions

**Q: Can subagents create subagents?**
A: Typically no (one level deep). Subagent complexity is bounded.

**Q: Do subagents share context?**
A: No. Each subagent runs fresh. You must pass relevant context in delegation prompt.

**Q: Can I use subagents for non-coding tasks?**
A: Yes. Investigator for research, Builder for document edits, Reviewer for spec review.

---

## Examples

### Example 1: Parallel Investigation

Task: Add payment method to checkout. Need to understand existing patterns.

1. Delegate investigator A: "Map current checkout flow files and data flow"
2. Delegate investigator B: "Find all payment-related code and config"
3. Delegate investigator C: "List test patterns for checkout tests"

All three run in parallel (separate contexts). Each returns compressed summary. Main agent synthesizes and proposes approach. Total: 1 min, main context barely touched.

### Example 2: Pre-Commit Review

After feature implementation (main context at 75%):

Delegate reviewer: "Review the git diff for: correctness, security, style violations. Return severity-tagged findings."

Reviewer checks diff without polluting main context. Returns 3-5 line summary. If no critical issues → commit. If issues → fix inline with remaining context budget.

---

## Key Takeaways
- Subagents run in separate context. Protect main thread from exploration noise.
- Cavecrew types: Investigator (locate), Builder (1-2 file edit), Reviewer (diff review)
- Subagent output ~60% smaller than inline equivalent
- Delegate when task would consume >20% of remaining context budget
- Pass key context in delegation prompt (subagent starts blank)
- Subagents can run in parallel for independent tasks

---

## Common Misconception

**"Subagents are slower than inline because of overhead."** Subagent overhead (create + return) is ~5 seconds. Exploration inline costs 500+ tokens of context space. Main context budget is finite — protecting it with subagents is faster in practice because you maintain high-quality context longer.

---

## Feynman Explain

(Explain subagent delegation to a manager. Why not have one person do everything? Why split work across team members even though coordination overhead exists?)

---

## Reframe

(Judge: "always delegate exploration" vs "never delegate, keep everything inline." What's the hidden context cost of each choice? When does delegation overhead exceed benefit?)

---

## Drill

Take the quiz. Run: `learn.sh quiz agentic-engineering 9`

## Quiz: 09-subagent-delegation

<p class="quiz-question">What is the primary benefit of subagent delegation?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Faster execution than inline</p>

<p class="quiz-option"><strong>B.</strong> Protects main context from exploration noise</p>

<p class="quiz-option"><strong>C.</strong> Subagents write better code</p>

<p class="quiz-option"><strong>D.</strong> No token cost for subagents</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Subagents run in separate context. Exploration noise doesn't pollute main thread.</p>

<hr/>

<p class="quiz-question">Which Cavecrew subagent type is best for mapping codebase usage?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Builder</p>

<p class="quiz-option"><strong>B.</strong> Investigator</p>

<p class="quiz-option"><strong>C.</strong> Reviewer</p>

<p class="quiz-option"><strong>D.</strong> All three equally</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Investigator is read-only code locator. Finds usages, returns file:line table. No modifications.</p>

<hr/>

<p class="quiz-question">When should you delegate a task to a subagent?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Always delegate everything</p>

<p class="quiz-option"><strong>B.</strong> When task would consume &gt;20% of remaining context budget</p>

<p class="quiz-option"><strong>C.</strong> Only for build tasks</p>

<p class="quiz-option"><strong>D.</strong> Never - always work inline</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">If task consumes &gt;20% remaining context, delegate. Protects budget for main task.</p>

<hr/>

<p class="quiz-question">What context compression ratio does subagent output typically achieve vs inline?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Same size</p>

<p class="quiz-option"><strong>B.</strong> ~60% smaller</p>

<p class="quiz-option"><strong>C.</strong> ~90% smaller</p>

<p class="quiz-option"><strong>D.</strong> ~10% smaller</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Cavecrew output is ~60% smaller than equivalent inline exploration. Compressed summaries, no noise.</p>

<hr/>

<p class="quiz-question">Why include 'main context' in delegation prompt?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Subagent has no access to main session context</p>

<p class="quiz-option"><strong>B.</strong> To make the prompt longer</p>

<p class="quiz-option"><strong>C.</strong> It's optional and rarely needed</p>

<p class="quiz-option"><strong>D.</strong> Subagent reads main context automatically</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">Subagent starts fresh with no context. Pass relevant decisions, goals, and constraints so it doesn't make wrong assumptions.</p>

<hr/>

<p class="quiz-question">Can you run multiple subagents in parallel?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Yes - independent investigations run simultaneously</p>

<p class="quiz-option"><strong>B.</strong> No - only one subagent at a time</p>

<p class="quiz-option"><strong>C.</strong> Yes, but they share context</p>

<p class="quiz-option"><strong>D.</strong> No - subagents cannot run independently</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">Independent subagents can run in parallel. Each in its own context. Results synthesized in main thread.</p>

<hr/>

<p class="quiz-question">Which Cavecrew subagent type would you use for post-implementation diff review?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Investigator</p>

<p class="quiz-option"><strong>B.</strong> Builder</p>

<p class="quiz-option"><strong>C.</strong> Reviewer</p>

<p class="quiz-option"><strong>D.</strong> None - review inline</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">Reviewer is designed for diff/branch review. Returns severity-tagged findings without polluting main context.</p>

<hr/>

<p class="quiz-question">What tool does a Builder subagent refuse?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Read</p>

<p class="quiz-option"><strong>B.</strong> Write new files</p>

<p class="quiz-option"><strong>C.</strong> 3+ file scope edits</p>

<p class="quiz-option"><strong>D.</strong> Running tests</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">Builder is for surgical 1-2 file edits. Refuses 3+ file scope by design.</p>

<hr/>

<p class="quiz-question">Main context is at 30%. Task is checking if a function is used. Delegate or inline?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Delegate - still use subagent for exploration</p>

<p class="quiz-option"><strong>B.</strong> Inline - plenty of context budget remaining</p>

<p class="quiz-option"><strong>C.</strong> Neither - do it manually</p>

<p class="quiz-option"><strong>D.</strong> Hard to say</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">30% remaining is comfortable. Simple grep + result check is fast inline. Subagent overhead not worth it.</p>

<hr/>

<p class="quiz-question">What is the typical overhead time for delegating to a subagent?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> &lt;1 second</p>

<p class="quiz-option"><strong>B.</strong> ~5 seconds</p>

<p class="quiz-option"><strong>C.</strong> ~30 seconds</p>

<p class="quiz-option"><strong>D.</strong> Several minutes</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">~5 seconds for create + return. Worth it when saving hundreds of tokens of main context.</p>


---

# Module 10: Script Management & Quality

Est. study time: 1.5h
Language: en

## Learning Objectives
- Write and test skill scripts effectively
- Apply logging and idempotency to scripts
- Design fallback behavior for edge cases
- Use quality checklist before publishing scripts

---

## Core Content

### What Are Scripts in Skills

Scripts are deterministic executable code attached to a skill. Unlike LLM instructions (flexible, interpreted fresh each time), scripts produce the same output for same input every execution.

```text
Skill with script:
  Name: "test-watcher"
  Trigger: on file change in src/
  Script:
    - Run `npm test -- --changed` (only changed files)
    - If tests pass: print "✅"
    - If tests fail: print first failure + exit 1
    - If no tests match: print "No affected tests"

Without script (instructions only):
  "Watch for file changes and run relevant tests."
  Agent decides how to do this. May work, may not.
```

> **Think**: When is a script better than LLM instructions for the same task?
> *Answer: When task is deterministic and failure is unacceptable. Build steps, CI checks, data validation. LLM for judgment tasks.*

### Script Quality Principles

**Fail fast, fail loud:**

```bash
#!/bin/bash
# Bad: silent failure
npm test || true

# Good: fail loud
npm test || { echo "❌ Tests failed. Aborting."; exit 1; }
```

**Idempotent (safe to re-run):**

```bash
# Bad: destructive, not idempotent
rm -rf dist/
mkdir dist/

# Good: safe to re-run
rm -rf dist/ 2>/dev/null
mkdir -p dist/
```

**Graceful edge cases:**

```bash
# Bad: crashes on empty directory
for file in src/*.ts; do
  npx tsc --noEmit "$file"
done

# Good: handles empty
for file in src/*.ts; do
  [ -f "$file" ] || continue
  npx tsc --noEmit "$file"
done
```

> **Think**: Why is `npm test || true` dangerous?
> *Answer: Silently swallows test failures. Downstream processes think everything passed. Always fail loud when checks fail.*

### Logging and Debugging Scripts

Every script should produce enough output to diagnose failure:

```text
Good log output:
  [test-watcher] Running tests for changed files...
  [test-watcher] Found 3 changed files: auth.ts, user.ts, product.ts
  [test-watcher] Running: npm test -- --changed
  [test-watcher] ✅ All 45 tests passed (12.3s)
  [test-watcher] Done.

Bad log output:
  Running tests...
  Done.
```

Logging rules:
- Prefix with `[skill-name]` to identify source
- Print inputs (which files, what args)
- Print outputs (pass/fail, metrics, duration)
- Print errors with enough context to fix
- Use consistent format (machine+human readable)

> **Think**: A deploy script fails. What should logs contain?
> *Answer: Which environment? What commit? What step failed? What error? Enough info to fix without re-running entire script.*

### Fallback Design

Scripts encounter unexpected situations. Design for failure:

```bash
# Primary path
if npm run build; then
  echo "Build succeeded"
  exit 0
fi

# Fallback: retry with clean cache
echo "Build failed. Retrying with clean cache..."
npm cache clean --force
if npm run build; then
  echo "Build succeeded (clean cache)"
  exit 0
fi

# Final fallback: report
echo "❌ Build failed even after cache clean."
echo "Manual intervention required."
exit 1
```

Fallback patterns:

| Fallback Type | When | Action |
|--------------|------|--------|
| Retry | Transient failure | Try once more |
| Degrade | Non-critical step | Skip, warn, continue |
| Escalate | Unknown error | Log full context, exit, notify |
| Default | Optional value | Use fallback value, log warning |

> **Think**: A script checks if a config file exists. It doesn't. What's the right fallback?
> *Answer: Depends on criticality. Required config → exit with error + expected location. Optional config → use defaults + log warning.*

### Quality Checklist

Before publishing any script-backed skill:

```text
[ ] Dry-run mode: runs without side effects, prints what it WOULD do
[ ] Edge cases tested: empty input, missing files, network errors, permission denied
[ ] Error messages readable without domain knowledge
[ ] Token cost measured: script doesn't burn excessive tokens
[ ] Idempotent: re-running same state produces same result
[ ] Human escape hatch: override flag (--force, --skip)
[ ] Logs sufficient: input + output + errors + duration
[ ] Fallback defined: what happens when primary path fails
[ ] Timeout defined: max execution time
[ ] Dependencies documented: what must be installed
```

> **Think**: Which checklist item is most commonly skipped? What's the consequence?
> *Answer: Edge cases. Script works on happy path, crashes on empty input or missing file. Leading to silent failures or confusing errors.*

---

## Why This Matters

Scripts are the deterministic backbone of your skill system. Bad scripts produce unreliable automation → you stop trusting the skill system. Good scripts — with idempotency, logging, fallbacks — make automation reliable. Quality checklist prevents shipping fragile scripts.

---

## Common Questions

**Q: Should all skills have scripts?**
A: No. Flexible skills (LLM instructions only) are fine for judgment tasks. Add scripts for deterministic steps.

**Q: How do I test a script in isolation?**
A: Create a test directory with sample inputs. Run script against it. Verify output. Automate with CI if critical.

**Q: What language should scripts be in?**
A: Bash for simple. Python/Node for complex. Match your team's expertise.

---

## Examples

### Example 1: Quality Script with Fallbacks

```bash
#!/bin/bash
set -euo pipefail

SKILL_NAME="deploy-check"
ENV="${1:-staging}"
COMMIT="${2:-HEAD}"

echo "[$SKILL_NAME] Environment: $ENV, Commit: $COMMIT"

# Step 1: Typecheck
echo "[$SKILL_NAME] Running typecheck..."
if ! npm run typecheck 2>/dev/null; then
  echo "[$SKILL_NAME] ❌ Typecheck failed. Fix before deploy."
  exit 1
fi
echo "[$SKILL_NAME] ✅ Typecheck passed"

# Step 2: Tests (non-critical, degrade on fail)
echo "[$SKILL_NAME] Running tests..."
if npm test -- --silent; then
  echo "[$SKILL_NAME] ✅ All tests passed"
else
  echo "[$SKILL_NAME] ⚠️ Tests failed. Continuing (non-blocking)..."
fi

# Step 3: Build
echo "[$SKILL_NAME] Building..."
if ! npm run build; then
  echo "[$SKILL_NAME] Build failed. Retrying with clean cache..."
  rm -rf .cache/
  npm run build || {
    echo "[$SKILL_NAME] ❌ Build failed after retry."
    exit 1
  }
fi
echo "[$SKILL_NAME] ✅ Build succeeded"

echo "[$SKILL_NAME] ✅ Deploy check complete. Ready for $ENV."
```

### Example 2: Dry-Run Mode

```bash
DRY_RUN="${DRY_RUN:-false}"

delete_unused_assets() {
  local file="$1"
  if [ "$DRY_RUN" = "true" ]; then
    echo "[dry-run] Would delete: $file"
  else
    rm "$file"
    echo "[deleted] $file"
  fi
}
```

---

## Key Takeaways
- Scripts = deterministic code. Same input → same output.
- Fail fast, fail loud: `exit 1` on failure, never suppress errors.
- Idempotent: safe to re-run. Same state → same result.
- Log: prefix with skill name, print inputs/outputs/errors/duration.
- Fallbacks: retry → degrade → escalate → default.
- Quality checklist: dry-run, edge cases, readable errors, token cost, idempotent, escape hatch, logs, fallback, timeout, dependencies.
- Not every skill needs a script. Judgment tasks → flexible. Deterministic tasks → script.

---

## Common Misconception

**"A script that works once is good enough."** Scripts run many times across different states. An empty directory, missing environment variable, or network timeout will expose fragility. Test edge cases before publishing. The cost of fixing a broken script mid-deploy is 100x the cost of testing ahead.

---

## Feynman Explain

(Explain idempotency to a non-programmer. Why can't a script just "do the thing" without worrying about what happened before? Use microwave example: pressing "start" twice doesn't double-cook your food. Good scripts behave like that.)

---

## Reframe

(Judge: "always write scripts for every step" vs "scripts only for critical paths." Where's the line? When does a script cause more problems than it solves?)

---

## Drill

Take the quiz. Run: `learn.sh quiz agentic-engineering 10`

## Quiz: 10-script-management

<p class="quiz-question">What makes scripted skills different from flexible (LLM-only) skills?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Scripted skills are slower</p>

<p class="quiz-option"><strong>B.</strong> Scripted skills produce deterministic output, same input → same output</p>

<p class="quiz-option"><strong>C.</strong> Scripted skills cannot run bash commands</p>

<p class="quiz-option"><strong>D.</strong> Scripted skills use more tokens</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Scripts are deterministic. LLM instructions are interpreted fresh each time. Scripts for reliability, LLM for judgment.</p>

<hr/>

<p class="quiz-question">Why is `npm test || true` considered bad practice?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> It runs tests twice</p>

<p class="quiz-option"><strong>B.</strong> It silently swallows test failures</p>

<p class="quiz-option"><strong>C.</strong> True is not a valid command</p>

<p class="quiz-option"><strong>D.</strong> It only runs npm, not tests</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">`|| true` suppresses the exit code. Test failures are hidden from caller. Always fail loud on check failures.</p>

<hr/>

<p class="quiz-question">What does it mean for a script to be idempotent?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Runs exactly once</p>

<p class="quiz-option"><strong>B.</strong> Running multiple times with same state produces same result</p>

<p class="quiz-option"><strong>C.</strong> Cannot be stopped once started</p>

<p class="quiz-option"><strong>D.</strong> Only runs on Fridays</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Idempotent: safe to re-run. Same starting state → same ending state. No cumulative side effects.</p>

<hr/>

<p class="quiz-question">Which is GOOD log output for a deploy script?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Running deploy...</p>

<p class="quiz-option"><strong>B.</strong> [deploy] Env: staging, Commit: abc123. Build: ✅ (34s). Tests: ✅ (142/142). Deploy: ✅.</p>

<p class="quiz-option"><strong>C.</strong> Doing stuff...</p>

<p class="quiz-option"><strong>D.</strong> Command executed</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Good logs: prefix, inputs, step results, metrics, final status. Enables debugging without re-running.</p>

<hr/>

<p class="quiz-question">A script's primary path fails with transient error. What fallback pattern?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Exit immediately</p>

<p class="quiz-option"><strong>B.</strong> Retry once, then escalate if still failing</p>

<p class="quiz-option"><strong>C.</strong> Ignore and continue</p>

<p class="quiz-option"><strong>D.</strong> Delete all files</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Retry once for transient failures. If still fails, escalate (log + exit). Don't silently continue if step is critical.</p>

<hr/>

<p class="quiz-question">What is the purpose of dry-run mode in a script?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Makes script run faster</p>

<p class="quiz-option"><strong>B.</strong> Prints what it WOULD do without side effects</p>

<p class="quiz-option"><strong>C.</strong> Runs in a different programming language</p>

<p class="quiz-option"><strong>D.</strong> Deletes test files</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Dry-run = preview mode. Shows intended changes without executing them. Essential for testing destructive operations.</p>

<hr/>

<p class="quiz-question">Which is MOST commonly skipped in quality checklist?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Dry-run mode</p>

<p class="quiz-option"><strong>B.</strong> Edge case testing (empty input, missing files)</p>

<p class="quiz-option"><strong>C.</strong> Idempotency check</p>

<p class="quiz-option"><strong>D.</strong> Dependency documentation</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Edge cases are most commonly skipped. Script works on happy path but crashes on empty directory, missing file, or network timeout.</p>

<hr/>

<p class="quiz-question">A script running on CI fails with 'file not found.' What should logs contain?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Error occurred</p>

<p class="quiz-option"><strong>B.</strong> Expected file path, search locations tried, current working directory, permissions</p>

<p class="quiz-option"><strong>C.</strong> File not found. Try again.</p>

<p class="quiz-option"><strong>D.</strong> Something went wrong</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Good error logs include what was expected, what was checked, and runtime context (cwd, permissions). Enough info to fix without re-running.</p>

<hr/>

<p class="quiz-question">A config file is optional. Script doesn't find it. What should happen?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Script crashes</p>

<p class="quiz-option"><strong>B.</strong> Use defaults, log warning, continue</p>

<p class="quiz-option"><strong>C.</strong> Create empty config file</p>

<p class="quiz-option"><strong>D.</strong> Ask user for input</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Optional file = fallback to defaults. Log warning so user knows default was used. Don't crash for optional dependencies.</p>

<hr/>

<p class="quiz-question">What does the 'human escape hatch' in quality checklist mean?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Script cannot be stopped by human</p>

<p class="quiz-option"><strong>B.</strong> Override flags (--force, --skip) so human can bypass checks if needed</p>

<p class="quiz-option"><strong>C.</strong> Script notifies human after completion</p>

<p class="quiz-option"><strong>D.</strong> Human must approve each step</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Override flags let humans bypass checks in exceptional situations. Critical for production: sometimes you need to force-deploy despite warnings.</p>


---

# Module 11: Automated Checks & TDD

Est. study time: 1.5h
Language: en

## Learning Objectives
- Integrate typecheck, lint, and test into agent prompts
- Apply test-first workflow with agents
- Design verification gates that auto-fail before review
- Balance verification speed vs thoroughness

---

## Core Content

### The Verification Problem

Agent code looks plausible. Often wrong in subtle ways. Without automated verification, you must manually inspect every line — defeating purpose of agent.

Solution: **verification gates** — automated checks that run after each implementation step.

```text
Without gate: Agent writes code → you review → find bug → agent fixes → you re-review
With gate:    Agent writes code → typecheck + lint + test pass → you review → approve
```

> **Think**: What percentage of common agent bugs are caught by typecheck + lint + test?
> *Answer: ~80%. Typecheck catches type errors, lint catches style/pattern violations, tests catch logic errors. Remaining 20% need human review.*

### Verification Gates in Prompts

Embed verification into task prompt:

```text
Implementation protocol:
1. Write code
2. Run: npm run typecheck (fix until clean)
3. Run: npm run lint (fix until clean)
4. Run: npm test -- --related (affected tests pass)
5. Only then present diff for review

Do NOT skip steps 2-4. If any step fails, fix and re-run before moving on.
```

**In AGENTS.md:**

```text
## Verification Protocol
All code changes must pass before presenting to human:
1. TypeScript check: npm run typecheck
2. Linting: npm run lint (or eslint)
3. Tests: npm test -- --related
4. Build: npm run build (for deployable changes)
```

> **Think**: Why specify `--related` for tests instead of full suite?
> *Answer: Full suite may take 10+ minutes. Related tests take seconds. Run full suite in CI. Fast verification gates keep agent loop tight.*

### Test-First Agentic Workflow

Test-first with agents is powerful but needs structure:

```text
1. SPEC: You write failing test (expresses desired behavior)
2. IMPLEMENT: Agent writes code to pass test
3. VERIFY: Agent runs test → green
4. REFINE: You review test + code, iterate

Benefits:
- Test = executable spec (no ambiguity)
- Agent knows exactly when done (test passes)
- Regression safety (test stays forever)
- You verify intent before implementation
```

Example:

```text
You write test:
  test('POST /api/users returns 201 with valid data and 400 with missing email', ...)

Agent prompt:
  "Implement the endpoint so this test passes.
   Do NOT modify the test file.
   Run test after implementation to confirm."

Agent: reads test → implements → runs → test passes → presents diff
```

> **Think**: Why should YOU write the test, not the agent?
> *Answer: Test encodes YOUR intent. If agent writes test too, it may encode wrong assumptions. You write test = spec. Agent implements to spec.*

### Verification Speed Tradeoffs

| Gate | Speed | Catch Rate | When to skip |
|------|-------|-----------|--------------|
| Typecheck | Fast (<5s) | ~40% of bugs | Never |
| Lint | Fast (<5s) | ~10% of bugs | Initial exploration |
| Unit tests (related) | Medium (10-60s) | ~20% of bugs | Before human review |
| Full test suite | Slow (1-10m) | ~30% of bugs | CI only |
| Build | Medium (30-120s) | ~10% of bugs | Before deploy |
| TypeScript strict | Fast + thorough | ~50% of bugs | If project supports it |

Order: typecheck → lint → related tests → build. Fail fast, fail cheap.

> **Think**: Agent is exploring a large refactor. Should it run full test suite on every change?
> *Answer: No. Related tests only during iteration. Full suite in CI. Speed matters during agent loop.*

### When Gates Fail

Agent hits verification failure. Proper response:

```text
1. Read error message (don't guess)
2. Fix the issue (not the symptom)
3. Re-run gate
4. If stuck 3+ times → stop and tell human

Anti-patterns:
- Agent disabling the gate ("skip typecheck for now")
- Agent patching symptom not cause
- Agent rewriting test instead of fixing code
- Agent ignoring failure ("it's probably fine")
```

**Guard prompt:**

```text
If typecheck/lint/test fails:
1. Read the error. Understand root cause.
2. Fix the actual issue. Not a workaround.
3. Re-run the gate.
4. If still failing after 3 attempts → stop and report to me.
Do NOT: skip the gate, modify test files, or apply workarounds.
```

> **Think**: Agent can't fix a type error after 3 attempts. What's likely wrong?
> *Answer: Wrong approach, misunderstanding of types, or project has unusual type setup. Stop and investigate. Don't keep trying same approach.*

---

## Why This Matters

Without verification gates, agent output quality is unreliable. With gates, 80% of common bugs are caught automatically. Your review time drops from line-by-line to spot-checking. Verification is the difference between trusting and hoping.

---

## Common Questions

**Q: Should I run verification on every code change, even small ones?**
A: Yes. Typecheck and lint are fast (<5s). Run them always. Tests on related files.

**Q: What if project has no tests?**
A: Start with typecheck + lint. Those alone catch ~50% of agent bugs. Add tests gradually.

**Q: Can verification run in parallel with implementation?**
A: Typecheck/lint can be continuous (file watcher). Tests need implementation first.

---

## Examples

### Example 1: Gate-Protected Prompt

```text
Task: Add pagination to user list endpoint.
Protocol:
1. Read current endpoint pattern
2. Implement pagination
3. Run: npm run typecheck (must pass)
4. Run: npm run lint (must pass)
5. Run: npm test -- --related (must pass)
6. Present diff only after steps 3-5 pass
```

Agent implements → typecheck fails (missing type) → fixes → typecheck passes → lint passes → test passes → presents diff. 2 minutes. Clean.

### Example 2: Test-First Workflow

You write:
```typescript
test('search returns results matching query', async () => {
  const results = await searchAPI.query('alice')
  expect(results).toHaveLength(1)
  expect(results[0].name).toBe('Alice')
})

test('search returns empty array for no match', async () => {
  const results = await searchAPI.query('nonexistent')
  expect(results).toEqual([])
})
```

Agent prompt: "Implement searchAPI.query to pass these tests. Tests are correct and final."

Agent implements → runs tests → green. Done.

---

## Key Takeaways
- Verification gates catch ~80% of agent bugs automatically
- Gate order: typecheck → lint → related tests → build
- Embed verification protocol in AGENTS.md (loads every session)
- Test-first: you write test (spec), agent implements to pass
- Run related tests during iteration, full suite in CI
- If gate fails 3+ times → stop and investigate
- Warn agent: do NOT skip gates, modify tests, or apply workarounds

---

## Common Misconception

**"Tests are for CI, not for agent workflow."** Tests are the most efficient feedback mechanism for agents. A failing test tells agent exactly what's wrong — faster than you can describe it in prose. Tests are executable specs that never misinterpret.

---

## Feynman Explain

(Explain verification gates to a junior developer. Why not just trust the agent and check later? Use cooking analogy: taste while cooking, not just at serving.)

---

## Reframe

(Judge: "run full test suite after every change" vs "run only typecheck, trust agent for correctness." Where's the right balance? When does over-verification hurt more than help?)

---

## Drill

Take the quiz. Run: `learn.sh quiz agentic-engineering 11`

## Quiz: 11-automated-checks-tdd

<p class="quiz-question">What percentage of common agent bugs are caught by typecheck + lint + test?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> ~40%</p>

<p class="quiz-option"><strong>B.</strong> ~80%</p>

<p class="quiz-option"><strong>C.</strong> ~100%</p>

<p class="quiz-option"><strong>D.</strong> ~20%</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">About 80%. Typecheck (~40%), lint (~10%), tests (~30%). Remaining 20% need human review (logic errors, design issues).</p>

<hr/>

<p class="quiz-question">What is the recommended verification gate order?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Tests → Lint → Typecheck → Build</p>

<p class="quiz-option"><strong>B.</strong> Typecheck → Lint → Related Tests → Build</p>

<p class="quiz-option"><strong>C.</strong> Build → Tests → Lint → Typecheck</p>

<p class="quiz-option"><strong>D.</strong> All at once</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Fastest gates first. Typecheck (&lt;5s) → Lint (&lt;5s) → Related tests (10-60s) → Build (30-120s). Fail fast, fail cheap.</p>

<hr/>

<p class="quiz-question">Why should you run related tests (not full suite) during agent iteration?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Full suite is run by CI</p>

<p class="quiz-option"><strong>B.</strong> Speed — related tests take seconds, full suite may take minutes</p>

<p class="quiz-option"><strong>C.</strong> Related tests are more accurate</p>

<p class="quiz-option"><strong>D.</strong> Full suite is not available locally</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Fast verification keeps agent loop tight. Full suite runs in CI. Related tests catch relevant regressions quickly.</p>

<hr/>

<p class="quiz-question">In test-first agentic workflow, who writes the test?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Agent — it writes both test and implementation</p>

<p class="quiz-option"><strong>B.</strong> You — test encodes your intent as executable spec</p>

<p class="quiz-option"><strong>C.</strong> CI pipeline</p>

<p class="quiz-option"><strong>D.</strong> Either, doesn't matter</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">You write test. Test = executable spec encoding YOUR intent. Agent implements to spec. If agent writes test too, assumptions may be wrong.</p>

<hr/>

<p class="quiz-question">What should agent do when a gate fails repeatedly (3+ attempts)?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Skip the gate and continue</p>

<p class="quiz-option"><strong>B.</strong> Modify tests to match output</p>

<p class="quiz-option"><strong>C.</strong> Stop and report to human</p>

<p class="quiz-option"><strong>D.</strong> Try the same fix again</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">After 3 failures, something is fundamentally wrong. Wrong approach, misunderstanding, or unusual setup. Investigate, don't brute force.</p>

<hr/>

<p class="quiz-question">Which gate catches the MOST bugs?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Lint</p>

<p class="quiz-option"><strong>B.</strong> Typecheck</p>

<p class="quiz-option"><strong>C.</strong> Build</p>

<p class="quiz-option"><strong>D.</strong> Full test suite</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Typecheck catches ~40% of bugs — type mismatches, missing properties, wrong arguments. Fastest gate with highest catch rate.</p>

<hr/>

<p class="quiz-question">What anti-pattern should you guard against in verification prompts?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Agent running gates automatically</p>

<p class="quiz-option"><strong>B.</strong> Agent disabling gates or applying workarounds</p>

<p class="quiz-option"><strong>C.</strong> Agent reporting gate failures</p>

<p class="quiz-option"><strong>D.</strong> Agent re-running gates after fixing</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Guards needed: prevent agent from skipping gates, modifying tests to match broken code, or applying superficial workarounds.</p>

<hr/>

<p class="quiz-question">Project has no tests. What gates should be used as minimum?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> No gates — project isn't ready</p>

<p class="quiz-option"><strong>B.</strong> Typecheck + Lint — catches ~50% of agent bugs</p>

<p class="quiz-option"><strong>C.</strong> Only build</p>

<p class="quiz-option"><strong>D.</strong> Manual review only</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Typecheck + lint together catch ~50% of common agent bugs. Fast, no setup overhead. Add tests gradually.</p>

<hr/>

<p class="quiz-question">Agent writes code that fails typecheck. Error says 'Property X does not exist on type Y.' What should agent do?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Use // @ts-ignore</p>

<p class="quiz-option"><strong>B.</strong> Read the error, fix the actual type mismatch</p>

<p class="quiz-option"><strong>C.</strong> Ask you what to do</p>

<p class="quiz-option"><strong>D.</strong> Ignore and present diff anyway</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Fix root cause. 'as any' or @ts-ignore treats symptom. Understand the type and fix properly.</p>

<hr/>

<p class="quiz-question">What makes tests better specs than natural language?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Tests are shorter</p>

<p class="quiz-option"><strong>B.</strong> Tests are executable, unambiguous, and permanent (regression safety)</p>

<p class="quiz-option"><strong>C.</strong> Tests run faster than reading</p>

<p class="quiz-option"><strong>D.</strong> Tests don't need review</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Tests = executable specs. They never misinterpret, they verify automatically, and they stay as regression protection.</p>


---

# Module 12: Evidence & Human Review

Est. study time: 1h
Language: en

## Learning Objectives
- Collect reviewable artifacts from agent work
- Structure effective human review process
- Automate review with review checklist skills
- Balance trust vs verification

---

## Core Content

### Why Evidence Matters

Agent works fast. You can't watch every action. Evidence artifacts let you verify after the fact.

```text
No evidence:
  Agent: "Done"
  You: "What did you change?"
  Agent: "The things we discussed"
  You: (must re-read everything)

With evidence:
  Agent: "Done. Files modified: auth.ts, login.tsx. Diff attached. Tests pass."
  You: reviews diff in 30 seconds. Approve.
```

> **Think**: What's the minimum evidence you need to approve an agent's work?
> *Answer: Diff (what changed), test results (it works), decisions made (why this approach). 30-second review.*

### Evidence Artifacts

| Artifact | Format | What it proves |
|----------|--------|---------------|
| Diff/patch | git diff | Exactly what changed |
| Test results | stdout log | Behaviors preserved/added |
| Typecheck/lint output | stdout log | Code quality maintained |
| Decision log | Markdown | Design choices and tradeoffs |
| Coffee-scent receipt | Markdown | Compressed summary of what happened |

**Evidence prompt in every task:**

```text
After implementation, provide:
1. Summary of what was done (2-3 sentences)
2. List of files created/modified
3. Key design decisions made (and why)
4. Verification results (typecheck ✅ lint ✅ test ✅)
5. Any risks or tradeoffs worth noting
```

> **Think**: When is a decision log more important than the diff?
> *Answer: When approach is contentious or has tradeoffs. "Chose X over Y because Z" helps you evaluate if right call was made without re-analyzing the problem.*

### Human Review Strategy

Review in layers, not single pass:

```text
Layer 1: Evidence check (30s)
  - Verify evidence exists and is coherent
  - Check summary matches files modified
  - Confirm verification gates passed

Layer 2: Diff scan (2-5 min)
  - Scan for: logic errors, security issues, unconventional patterns
  - Don't read every line. Trust verification gates for mechanics.
  - Focus on: business logic, data flow, auth/permissions

Layer 3: Spot check (5-10 min for complex)
  - Read critical files fully (core logic, security-sensitive)
  - Run modified feature manually if applicable
  - Check edge cases agent may have missed
```

**When to fully read vs spot check:**

| Situation | Review approach |
|-----------|----------------|
| Bug fix (clear scope) | Spot check diff |
| New feature (complex) | Full read + manual test |
| Refactor (mechanical) | Trust gates, scan diff |
| Security-sensitive | Full read + audit |
| Boilerplate/tests | Trust gates, sample check |

> **Think**: Why scan diff before reading full files?
> *Answer: Diff shows only what changed. Full files include unchanged code — reading them wastes time. Scan diff first, drill into full files only if something looks suspicious.*

### Review Automation with Skills

Create a review skill that enforces review checklist:

```text
Skill: "review-check"
Type: flexible
Instructions:
  Review this diff for:
  1. Correctness: Logic errors, off-by-one, wrong conditions
  2. Security: Injections, auth bypass, data exposure
  3. Conventions: Follows project patterns from AGENTS.md
  4. Edge cases: What happens on empty/null/unexpected input
  5. Testing: Are there tests? Do they cover edge cases?

  For each finding: tag severity (critical/major/minor), file:line, suggested fix.
  No praise. No "looks good" without specific verification.
```

Run after agent implementation to get structured review before your human review.

> **Think**: Why "no praise" in review skill instructions?
> *Answer: Praise wastes tokens. Review is for finding issues. Agent-generated praise ("good work!") adds no value. Output only actionable findings.*

### Trust Calibration

Trust scales with evidence quality, not familiarity:

```text
Low trust (new agent, new codebase):
  - Full diff review
  - Manual test of feature
  - Review all test files
  - Run verification gates yourself

Medium trust (familiar setup, good track record):
  - Scan diff
  - Spot-check critical files
  - Verify test results
  - Trust gates passed

High trust (established patterns, consistent agent):
  - Summary review
  - Security check of changed files
  - Trust gates + agent's own review
```

**Trust degrades** after: incorrect code, missed gate, unexplained changes.

> **Think**: Trust calibrated right. Agent delivers 10 clean PRs. Next PR is complex auth change. What review level?
> *Answer: Escalate trust for high-risk changes regardless of history. Auth/permissions always get full review. Trust applies to routine work, not security boundaries.*

---

## Why This Matters

Without evidence artifacts, you're flying blind. With evidence, review takes 30s-5min instead of 30min. Review automation catches issues before your review, compounding efficiency. Trust calibration ensures you don't miss critical bugs or waste time on routine work.

---

## Common Questions

**Q: Should agent write review of its own code?**
A: Yes—with a review skill. Agent's self-review catches many issues before you see it.

**Q: How do I know if agent is lying about verification results?**
A: If trust is low, run verification yourself. If trust is medium, spot-check one result.

**Q: What if evidence is missing or incomplete?**
A: Ask agent to provide it. If agent can't produce coherent evidence, something is wrong.

---

## Examples

### Example 1: Evidence Receipt

After completing a task, agent provides:

```text
## Summary
Added email uniqueness check to user registration.
Returns 409 for duplicate (case-insensitive). Tests added.

## Files
- src/api/auth/register.ts (modified: added email check)
- src/api/auth/__tests__/register.test.ts (modified: added 2 test cases)

## Decisions
- Case-insensitive check: existing emails "User@Example.com" and "user@example.com" are duplicates
- Used raw SQL `LOWER(email) = LOWER($1)` (existing ORM can't express this efficiently)

## Verification
- typecheck ✅
- lint ✅
- test ✅ (45/45, including 2 new)

## Risks
- Performance: full table scan on email column. Not an issue for <100k users.
```

You review: 30 seconds. Approve.

### Example 2: Trust Calibration Applied

Day 1: Full review of every agent output. 30 min.

Day 5: Agent is consistent. Gates always pass. Review becomes scan + spot check. 5 min.

Week 3: Agent handles routine tasks end-to-end. You review only summary + security-critical files. 2 min.

Month 2: New team member reports a bug agent introduced in authentication. Trust resets for auth-related changes. You now review auth diffs fully.

---

## Key Takeaways
- Collect evidence: diff, test results, decisions, gate outputs
- Prompt agent to provide summary + files + decisions + verification + risks after each task
- Review in layers: evidence check → diff scan → spot check
- Create review skill for structured agent self-review before your review
- Calibrate trust: low = full review, medium = scan, high = summary
- Trust degrades on mistakes. Always escalate for security-critical changes.

---

## Common Misconception

**"If verification gates pass, manual review is unnecessary."** Gates catch ~80% of bugs. The remaining 20% include logic errors, design flaws, and security vulnerabilities. Always review. But review faster when gates pass — scan diff, don't read every line.

---

## Feynman Explain

(Explain evidence collection to a manager. Why can't you just trust the agent and check if it works? Use building contractor analogy: would you pay without inspecting the work first? But would you inspect every nail, or spot-check?)

---

## Reframe

(Judge: "full review every time" vs "trust gates completely." What's the cost of over-reviewing? The risk of under-reviewing? Where's the optimal point?)

---

## Drill

Take the quiz. Run: `learn.sh quiz agentic-engineering 12`

## Quiz: 12-evidence-review

<p class="quiz-question">What is the minimum evidence needed to approve agent work?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Agent says 'done'</p>

<p class="quiz-option"><strong>B.</strong> Diff, test results, design decisions</p>

<p class="quiz-option"><strong>C.</strong> Full log of every tool call</p>

<p class="quiz-option"><strong>D.</strong> Approval from another team member</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Diff (what changed), test results (it works), decisions (why this approach). 30-second review with these artifacts.</p>

<hr/>

<p class="quiz-question">What is the recommended review order?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Read full modified files first</p>

<p class="quiz-option"><strong>B.</strong> Evidence check → Diff scan → Spot check</p>

<p class="quiz-option"><strong>C.</strong> Run tests first</p>

<p class="quiz-option"><strong>D.</strong> Random sampling</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Layers: evidence exists and coherent (30s) → diff scan for issues (2-5m) → deep spot check critical files (5-10m).</p>

<hr/>

<p class="quiz-question">Why should a review skill instruct 'no praise'?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Praise wastes tokens without adding value</p>

<p class="quiz-option"><strong>B.</strong> Praise makes agent overconfident</p>

<p class="quiz-option"><strong>C.</strong> Praise violates policy</p>

<p class="quiz-option"><strong>D.</strong> Agent cannot give genuine praise</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">Review is for finding issues. Agent-generated praise ('good work!') adds no actionable information. Output only findings.</p>

<hr/>

<p class="quiz-question">How should trust calibrate after 10 clean PRs followed by a complex auth change?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> High trust — agent earned it</p>

<p class="quiz-option"><strong>B.</strong> Escalate review for auth (high-risk change)</p>

<p class="quiz-option"><strong>C.</strong> Reset trust to zero</p>

<p class="quiz-option"><strong>D.</strong> Same medium trust as before</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Trust applies to routine work. Security/auth/permissions always get full review regardless of history.</p>

<hr/>

<p class="quiz-question">What causes trust to degrade?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Agent working too fast</p>

<p class="quiz-option"><strong>B.</strong> Incorrect code, missed verification gates, unexplained changes</p>

<p class="quiz-option"><strong>C.</strong> Agent being verbose</p>

<p class="quiz-option"><strong>D.</strong> Agent asking questions</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Trust degrades on: incorrect code, skipped gates, changes to files outside scope, inability to explain decisions.</p>

<hr/>

<p class="quiz-question">For which situation should you perform a FULL read (not scan)?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Bug fix with clear scope</p>

<p class="quiz-option"><strong>B.</strong> Security-sensitive code change</p>

<p class="quiz-option"><strong>C.</strong> Mechanical rename</p>

<p class="quiz-option"><strong>D.</strong> Test file additions</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Security-sensitive code always gets full read + audit. Bug fixes (clear scope), mechanical refactors, tests: scan or spot check.</p>

<hr/>

<p class="quiz-question">What should you do if agent provides incomplete evidence?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Approve anyway — agent earned trust</p>

<p class="quiz-option"><strong>B.</strong> Ask agent to provide complete evidence</p>

<p class="quiz-option"><strong>C.</strong> Assume agent is hiding something</p>

<p class="quiz-option"><strong>D.</strong> Ignore and move on</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Incomplete evidence = request completion. If agent can't produce coherent evidence, investigate before approving.</p>

<hr/>

<p class="quiz-question">What is the purpose of a decision log in evidence?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Makes review longer</p>

<p class="quiz-option"><strong>B.</strong> Shows why agent chose approach X over Y without you re-analyzing</p>

<p class="quiz-option"><strong>C.</strong> Documents which AI model was used</p>

<p class="quiz-option"><strong>D.</strong> Logs all errors during implementation</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Decision log explains tradeoffs. Helps you evaluate if right call was made without re-doing the analysis.</p>

<hr/>

<p class="quiz-question">High trust level should still require what minimum review?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> No review needed</p>

<p class="quiz-option"><strong>B.</strong> Summary + security check of changed files</p>

<p class="quiz-option"><strong>C.</strong> Full diff read</p>

<p class="quiz-option"><strong>D.</strong> Manual testing of all features</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Even high trust: summary check + security scan. Never zero review. Superhuman trust is cargo-culting.</p>

<hr/>

<p class="quiz-question">An agent says 'all tests pass' but you suspect otherwise. What to do?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Trust the agent</p>

<p class="quiz-option"><strong>B.</strong> Run tests yourself or ask agent to show output</p>

<p class="quiz-option"><strong>C.</strong> Ignore suspicion — it's probably fine</p>

<p class="quiz-option"><strong>D.</strong> Reject all changes</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">If trust is low or something feels off, verify. Ask agent to show test command and output. Evidence should be reproducible.</p>


---

# Module 13: Safety, Guardrails, Rollback

Est. study time: 1h
Language: en

## Learning Objectives
- Set token limits and timeout guards for agent sessions
- Detect and prevent infinite loops
- Protect against destructive operations
- Implement rollback strategy

---

## Core Content

### Token Limit Guards

Unbounded agent sessions can burn thousands of tokens on dead ends.

```text
Hard limits to set:
- Max tool calls per task (e.g., 20)
- Max tokens per response (model limit)
- Max session duration (timeout)
- Max file size for reads (prevent reading huge files)

In AGENTS.md:
  ## Safety Limits
  - Max 20 tool calls per task (if exceeded, stop and report)
  - Never read files >1000 lines without specifying line range
  - Never write files >500 lines without checkpoint check
```

> **Think**: Agent used 50 tool calls on one task and isn't done. What happened?
> *Answer: Likely stuck in loop or went too deep without checkpoint. Should have stopped at 20 and reported. Set hard limit.*

### Infinite Loop Detection

Agent loops look like:

```text
- Repeating same file reads
- Making same type of edit repeatedly
- Fix introduces bug → fix bug → introduces new bug → ...
- Re-exploring already-explored code
- Response patterns repeat (same phrasing, same tool sequence)

Prevention:
  - "If you've attempted same fix 3+ times, stop and report"
  - "If you're re-reading same files, compress and restart"
  - "If you've modified same function 3+ times, show me current state"

Detection:
  - Watch for repetitive tool sequences
  - Track "edit count per file" (3+ edits same file → investigate)
  - Notice when responses get longer without progress
```

> **Think**: Agent has edited login.tsx 7 times. Each edit changes approach. What's happening?
> *Answer: Agent is in iteration loop without convergence. Context likely degraded or approach fundamentally wrong. Stop and reassess.*

### Destructive Operation Guards

Agent can delete or overwrite files. Protect critical paths.

```text
Guards to define:
1. Never delete: package.json, tsconfig.json, node_modules (unless authorized)
2. Never modify: CI config, deploy scripts, security configs
3. Read-only zones: /docs, /config (unless explicitly authorized per task)

In AGENTS.md:
  ## Protected Files (READ ONLY unless per-task approval)
  - package.json, package-lock.json
  - tsconfig.json, next.config.js
  - .github/workflows/*
  - Dockerfile, docker-compose.yml
  - Any file matching *.config.*
  
  ## Never Delete
  - Any file in root directory
  - Any lockfile
  - .gitignore
  - README.md
```

> **Think**: Why list protected files in AGENTS.md instead of relying on generic "be careful"?
> *Answer: Generic instructions ignored or forgotten. Specific file paths are unambiguous. Agent checks before writing.*

### Rollback Strategy

When agent makes changes that need reversal:

```text
Rollback plan (prepare before agent starts):
1. Agent changes are in working tree (not committed)
2. `git stash` or `git checkout -- .` to reset
3. If partial: `git diff` to see changes, revert specific files
4. If committed: `git revert <commit>` or `git reset HEAD~1`

Agent-assisted rollback:
  "Undo the changes to auth.ts. Keep changes to login.tsx."
  Agent: reads current state → reverts specific file → keeps other changes

Safeguard: "Before starting, verify git status is clean."
  If not clean → warn user. Don't start on dirty tree.
```

**Rollback tiers:**

| Situation | Action |
|-----------|--------|
| Minor mistake in single file | Agent reverts specific file |
| Feature went wrong direction | `git checkout` affected files |
| Agent corrupted multiple files | `git reset --hard` to last clean state |
| Changes committed incorrectly | `git revert` or interactive rebase |
| Catastrophic failure | `git stash` → restore from backup |

> **Think**: Agent modified 5 files but only 2 changes are good. How to rollback safely?
> *Answer: Revert specific bad files. Don't revert all. Agent can do selective revert: "Revert utils.ts and api.ts to HEAD. Keep test.ts changes."*

### Pre-Flight Check

Before any significant task, run pre-flight:

```text
Pre-flight checklist:
- [ ] Git working tree clean
- [ ] Branch is correct (not main/master unless authorized)
- [ ] Typecheck passes on current state
- [ ] Tests pass on current state
- [ ] Disk space sufficient
- [ ] Required services running (DB, dev server)

If any fails → stop and resolve before proceeding.
```

This ensures agent starts from known good state. Bugs introduced are agent's, not pre-existing.

> **Think**: Why check typecheck + tests pass BEFORE agent starts?
> *Answer: If typecheck/tests fail after agent change, was it agent's fault or pre-existing? Known good state = clear attribution.*

---

## Why This Matters

Agent failures range from token waste to data loss. Safety guardrails prevent catastrophic mistakes. Rollback plan ensures you can recover instantly. Pre-flight ensures clean attribution of issues. Safety is not optional — it's the difference between empowering tool and dangerous one.

---

## Common Questions

**Q: Can I set automatic tool call limits?**
A: Depends on opencode setup. Some support max tool calls. If not, enforce via AGENTS.md prompt.

**Q: Should I commit agent changes before review?**
A: No. Keep changes in working tree until reviewed. If review rejects, revert is trivial.

**Q: What if agent accidentally deletes a file?**
A: `git checkout <deleted-file>` restores it immediately. Git is your safety net.

---

## Examples

### Example 1: Infinite Loop Caught

Agent is fixing a bug in sort function. After 4 edits, function still fails test:

Without guard: Agent keeps trying different approaches. 15 edits later, still failing. 5000 tokens wasted.

With guard: "If 3+ attempts fail → stop and report." After 3 fails, agent reports: "Tried 3 approaches. All fail. Need human guidance." You investigate: it's a data issue, not code issue.

### Example 2: Destructive Operation Blocked

Agent tries to modify `next.config.js` (in protected list):

```text
Agent: "I need to add an environment variable to next.config.js"
(Checks AGENTS.md: "README ONLY unless per-task approval")
Agent: "next.config.js is in protected files. Cannot modify.
       Please approve: add PUBLIC_API_URL to next.config.js?"
You: "Yes, approved."
Agent: modifies file.
```

Without guard: Agent silently modifies config. May break build.

---

## Key Takeaways
- Set hard limits: max tool calls, token budget, timeout
- Detect loops: repeated reads, repeated edits, no convergence
- Protect critical files: list in AGENTS.md with clear rules
- Rollback plan: git revert, selective revert, reset
- Pre-flight: clean git, typecheck passes, tests pass before agent starts
- Guardrails prevent catastrophe. Rollback ensures recovery.

---

## Common Misconception

**"Guardrails slow down the agent."** 50 tokens of safety rules at start of session save 5000 tokens of damage control. Guardrails don't slow successful work — they prevent expensive failures. Speed without safety is recklessness, not efficiency.

---

## Feynman Explain

(Explain guardrails and rollback to a non-technical stakeholder. Use car analogy: guardrails are seatbelts, rollback is airbag. You don't need them most of the time, but when you do, nothing else substitutes.)

---

## Reframe

(Judge: "maximum guardrails on every task" vs "minimum guardrails, trust the agent." Where do guardrails create false security? When do they prevent useful work?)

---

## Drill

Take the quiz. Run: `learn.sh quiz agentic-engineering 13`

## Quiz: 13-safety-guardrails

<p class="quiz-question">What is the first safety measure to set for agent sessions?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Disable internet access</p>

<p class="quiz-option"><strong>B.</strong> Hard limits on max tool calls per task</p>

<p class="quiz-option"><strong>C.</strong> Use a different AI model</p>

<p class="quiz-option"><strong>D.</strong> No measures needed</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Hard limits (e.g., 20 tool calls per task) prevent infinite loops and runaway token burn.</p>

<hr/>

<p class="quiz-question">What indicates an agent is in an infinite loop?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Agent produces correct code quickly</p>

<p class="quiz-option"><strong>B.</strong> Repeated file reads, same edits without convergence, no progress</p>

<p class="quiz-option"><strong>C.</strong> Agent asks one clarifying question</p>

<p class="quiz-option"><strong>D.</strong> Agent completes task and stops</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Repeated reads of same files, same type of edit without convergence, response patterns repeating = loop.</p>

<hr/>

<p class="quiz-question">What should you do when agent has edited the same function 5+ times without fixing it?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Let it keep trying</p>

<p class="quiz-option"><strong>B.</strong> Stop. Context likely degraded or approach wrong. Restart.</p>

<p class="quiz-option"><strong>C.</strong> Delete and rewrite from scratch</p>

<p class="quiz-option"><strong>D.</strong> Ignore — it will converge eventually</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">3+ attempts same issue → stop and reassess. Don't brute force. Context poisoned or approach wrong.</p>

<hr/>

<p class="quiz-question">Where should protected file lists be defined?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> In a separate document</p>

<p class="quiz-option"><strong>B.</strong> In AGENTS.md — loaded every session, unambiguous</p>

<p class="quiz-option"><strong>C.</strong> Verbally agreed with the team</p>

<p class="quiz-option"><strong>D.</strong> In commit messages</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">AGENTS.md loads every session. Specific file paths are unambiguous. Generic 'be careful' is forgotten.</p>

<hr/>

<p class="quiz-question">How should you rollback if agent modified 5 files but only 2 changes are good?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Revert all 5 files</p>

<p class="quiz-option"><strong>B.</strong> Revert only the 2 bad files, keep the 3 good ones</p>

<p class="quiz-option"><strong>C.</strong> Start a new session</p>

<p class="quiz-option"><strong>D.</strong> Manually undo each change</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Selective revert: revert specific bad files. Keep good changes. Agent can do this: 'Revert bad.ts to HEAD.'</p>

<hr/>

<p class="quiz-question">Why should you verify git status is clean BEFORE agent starts?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Makes git history cleaner</p>

<p class="quiz-option"><strong>B.</strong> Known good state = clear attribution of any new issues</p>

<p class="quiz-option"><strong>C.</strong> Agent cannot work on dirty tree</p>

<p class="quiz-option"><strong>D.</strong> Prevents merge conflicts</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Clean state before start means any new bugs are agent's fault, not pre-existing. Clear attribution.</p>

<hr/>

<p class="quiz-question">Agent needs to modify deployment config. Protected list says READ ONLY. What should agent do?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Modify anyway — the task needs it</p>

<p class="quiz-option"><strong>B.</strong> Stop and ask human for per-task approval</p>

<p class="quiz-option"><strong>C.</strong> Ignore the protected list</p>

<p class="quiz-option"><strong>D.</strong> Create a new config file instead</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Protected means read-only unless per-task approval. Agent should request approval specific to this modification.</p>

<hr/>

<p class="quiz-question">What is the recommended guard when agent has tried the same fix 3 times?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Try a 4th time — it might work</p>

<p class="quiz-option"><strong>B.</strong> Stop and report to human</p>

<p class="quiz-option"><strong>C.</strong> Undo all changes and restart</p>

<p class="quiz-option"><strong>D.</strong> Delete affected files</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">3 attempts same approach → wrong approach or context degraded. Stop, report, get guidance.</p>

<hr/>

<p class="quiz-question">Which rollback action is appropriate for catastrophic failure (multiple files corrupted)?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Revert specific files one by one</p>

<p class="quiz-option"><strong>B.</strong> git reset --hard to last known good commit</p>

<p class="quiz-option"><strong>C.</strong> Delete repository and re-clone</p>

<p class="quiz-option"><strong>D.</strong> Manual copy from backup</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Catastrophic = reset to last clean state. `git reset --hard` restores everything. Quick and definitive.</p>

<hr/>

<p class="quiz-question">Pre-flight check reveals typecheck is already failing before agent starts. What to do?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Let agent start — it might fix typecheck</p>

<p class="quiz-option"><strong>B.</strong> Stop. Fix pre-existing issues first. Agent starts from clean state.</p>

<p class="quiz-option"><strong>C.</strong> Ignore — typecheck is optional</p>

<p class="quiz-option"><strong>D.</strong> Ask agent to work around the failures</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Pre-existing failures make attribution impossible. Fix first, then agent starts clean. Any new failures = agent's fault.</p>


---

# Module 14: Token Economy

Est. study time: 1h
Language: en

## Learning Objectives
- Understand token cost structure of agent operations
- Identify and eliminate token waste patterns
- Optimize prompts for minimum token consumption
- Measure and track token efficiency

---

## Core Content

### Token Cost Breakdown

Every agent action costs tokens. Not all actions produce equal value.

```text
Cost per operation (approximate):
  Simple question      50-100 tokens
  Write 20-line file   200-400 tokens
  Read 100-line file   300-500 tokens
  Grep search          100-200 tokens
  Glob pattern         50-100 tokens
  Agent response       200-1000 tokens
  Compression          200-500 tokens (but saves 10x+)

Token waste hot spots:
  - Reading full files when only few lines needed
  - Including full error traces in context
  - Letting agent explore without bounds
  - Repeating same information across messages
  - Long agent responses with praise/summarization of unchanged code
```

> **Think**: What's the highest-ROI token investment?
> *Answer: Spec writing and compression. 200 tokens of spec save 2000+ tokens of wrong direction. 500 tokens of compression save 5000+ of context space.*

### Waste Elimination Patterns

| Pattern | Waste | Fix |
|---------|-------|-----|
| Full file reads | 300-500 tokens each | Specify line ranges. Read only what's needed. |
| Agent summarizing unchanged code | 200-500 tokens | "Show only changes. Skip unchanged code." |
| Repeated exploration | 1000+ tokens | Compress decisions to AGENTS.md after first exploration. |
| Praise/affirmation | 50-100 tokens per response | "Skip praise. Just give me findings." |
| Full test output on success | 100-500 tokens | "Only show test failures, skip passing tests." |
| Multiple small tool calls vs batch | Overhead per call | "Read lines 45-60 and 120-135 in one read call." |

> **Think**: Agent says "Here is the updated file: [full file 200 lines]" when only 5 lines changed. What to do?
> *Answer: Instruct: "Show only the diff/hunk, not full file." 5 lines instead of 200 = 97% token savings.*

### Prompt Optimization for Token Efficiency

```diff
- "Could you please take a look at the function below and let me know what you think might need to be changed? I was wondering if there's anything we should improve. Thanks!"
+ "Review this function. Find bugs and optimization opportunities."

Before: 30 tokens (50% filler)
After:  10 tokens (70% reduction)
```

Optimization rules:
- Drop greetings/polite phrases ("please", "thanks", "could you")
- Use short synonyms ("fix" not "implement a solution for")
- Use one word when enough ("yes" not "yes, that sounds right")
- Combine constraints into single instruction ("Fix bug: X. Follow pattern Y. Verify with Z.")
- Use formatting (headers, lists) to reduce ambiguity (saves re-explanation tokens)

> **Think**: You write "please could you implement the feature for adding user search functionality to the admin panel we discussed yesterday?" How many tokens wasted?
> *Answer: ~15 tokens of filler. "Implement user search in admin panel per yesterday's spec" = same information, half the tokens.*

### Measuring Token Efficiency

Track these metrics across sessions:

```text
Metrics to monitor:
  - Tokens per task completed
  - Tokens per file changed
  - Tokens per bug fixed
  - Context usage at task completion
  - Number of compression events
  - Number of restarts due to context full

Improvement targets:
  - Token waste per task < 20% (80% productive)
  - Context usage at task end < 70% (room to continue)
  - Compressions per session: 1-3 (not 0 = never compress, not 10 = over-compressing)
  - Restarts due to context: < 1 per 5 sessions
```

> **Think**: Your average task consumes 5000 tokens. After applying optimization, it's 3000. What changed?
> *Answer: 40% improvement. Likely from: precise file reads, no praise, no full-file output, spec before implementation.*

---

## Why This Matters

Tokens cost money AND context space. Every wasted token reduces effective capacity. Optimization compounds: shorter prompts → more room for output → better results → fewer iterations → less tokens. Token economy is the meta-skill that amplifies all other skills.

---

## Common Questions

**Q: How many tokens is too many for a single task?**
A: If task takes >10 tool calls or >20 agent responses, scope is too large or something is wrong.

**Q: Should I optimize every prompt?**
A: No. Optimize AGENTS.md (loads every session) and common patterns. One-off prompts don't need micro-optimization.

**Q: Does linter output waste tokens?**
A: Only failures. Configure: "Show only lint errors, not passed rules." Many linters support --quiet.

---

## Examples

### Example 1: Before/After Optimization

Before (prompt):
```text
Hi! I was hoping you could help me implement a feature for our application. It's about adding a search bar to the user management page. I think it would be great if users could search by name or email. Let me know what you think!
```

After (optimized):
```text
Add search bar to user management page. Search by name or email.
Pattern: Follow existing search in ProductList.tsx.
Files: UserManagement.tsx, useSearch.ts
```

Before: 45 tokens → After: 25 tokens. Same information.

### Example 2: File Read Savings

Before: "Read src/api/users.ts" — agent returns 300 lines (800 tokens).

After: "Read lines 45-60 (search function) and 120-135 (sort function)" — agent returns 30 lines (80 tokens).

90% token savings. Exactly the information needed.

---

## Key Takeaways
- Token waste hot spots: full file reads, praise, repeated exploration, full file output on small changes
- Fix 1: specify line ranges for reads
- Fix 2: "show only diff/changes, not full files"
- Fix 3: compress decisions to AGENTS.md (don't re-explore)
- Fix 4: drop filler from prompts
- Measure: tokens per task, context at completion, compression frequency
- Optimization compounds: less tokens → better context → better output → fewer iterations

---

## Common Misconception

**"Token optimization is micro-optimization — not worth the effort."** Token optimization is NOT micro. Full file reads waste 800 tokens vs 80 for targeted reads. Praise/affirmation adds 50-100 tokens per response across 20 responses = 2000 wasted tokens. These add up to significant context space. Token optimization is high-ROI.

---

## Feynman Explain

(Explain token economy to someone who's never thought about LLM costs. Use money budget: you have $100 per session. Every tool action costs $5-50. Do you spend $40 reading a full file when you only need 3 lines?)

---

## Reframe

(Judge: "optimize every interaction" vs "don't optimize at all, token cost is negligible." At what scale does optimization matter? When is a developer's time more valuable than tokens?)

---

## Drill

Take the quiz. Run: `learn.sh quiz agentic-engineering 14`

## Quiz: 14-token-economy

<p class="quiz-question">What is the biggest token waste hot spot?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Agent greeting messages</p>

<p class="quiz-option"><strong>B.</strong> Reading full files when only few lines needed</p>

<p class="quiz-option"><strong>C.</strong> System instructions</p>

<p class="quiz-option"><strong>D.</strong> Compression summaries</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Full file reads 300-800 tokens. Specifying line ranges reduces to 50-100 tokens. Biggest single source of waste.</p>

<hr/>

<p class="quiz-question">How many tokens does 'show only diff, not full file' typically save?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> 10-20%</p>

<p class="quiz-option"><strong>B.</strong> 50-97% depending on file size vs change size</p>

<p class="quiz-option"><strong>C.</strong> 0% — same either way</p>

<p class="quiz-option"><strong>D.</strong> Increases token usage</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">If 5 lines changed in 200-line file, diff = 5 lines vs full file = 200 lines. 97% savings.</p>

<hr/>

<p class="quiz-question">What is the highest-ROI token investment?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Long greetings</p>

<p class="quiz-option"><strong>B.</strong> Spec writing and compression</p>

<p class="quiz-option"><strong>C.</strong> Reading full files</p>

<p class="quiz-option"><strong>D.</strong> Full test output</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">200 tokens of spec prevent 2000+ tokens of wrong direction. 500 tokens of compression save 5000+ context space.</p>

<hr/>

<p class="quiz-question">How can you reduce token waste from file reads?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Read files only once</p>

<p class="quiz-option"><strong>B.</strong> Specify exact line ranges instead of reading entire files</p>

<p class="quiz-option"><strong>C.</strong> Never read files — guess the content</p>

<p class="quiz-option"><strong>D.</strong> Read files in random order</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Exact line ranges (e.g., 'read lines 45-60') vs full file. 90% savings with no information loss.</p>

<hr/>

<p class="quiz-question">What metrics should you track for token efficiency?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Number of files in project</p>

<p class="quiz-option"><strong>B.</strong> Tokens per task, context usage at completion, compression frequency</p>

<p class="quiz-option"><strong>C.</strong> Lines of code written</p>

<p class="quiz-option"><strong>D.</strong> Number of git commits</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Track: tokens per task, context at end, compression events, restarts due to full context.</p>

<hr/>

<p class="quiz-question">Agent output includes 'Here is the updated file:' followed by 200 lines with 3 lines changed. What instruction would fix this?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Write better code</p>

<p class="quiz-option"><strong>B.</strong> Show only the diff/changed lines, not the full file</p>

<p class="quiz-option"><strong>C.</strong> Use fewer lines</p>

<p class="quiz-option"><strong>D.</strong> Nothing — this is optimal</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">'Show only diff' instruction saves 97% of output tokens for this response.</p>

<hr/>

<p class="quiz-question">How much of a typical prompt is filler that can be cut?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> 1-2%</p>

<p class="quiz-option"><strong>B.</strong> 30-50% (greetings, politeness, hedging)</p>

<p class="quiz-option"><strong>C.</strong> 80-90%</p>

<p class="quiz-option"><strong>D.</strong> 0% — every word is essential</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Greetings, please/thanks, hedging, repeated context. 'Fix this bug' instead of 'Could you please help me fix this bug when you get a chance?'</p>

<hr/>

<p class="quiz-question">What is the target for context usage at task completion?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> &lt; 70% (room to continue or iterate)</p>

<p class="quiz-option"><strong>B.</strong> 95%+ (maximize usage)</p>

<p class="quiz-option"><strong>C.</strong> &lt; 10% (never use context)</p>

<p class="quiz-option"><strong>D.</strong> 50% exactly</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">Under 70% means room for iteration, follow-up, or review without hitting full context.</p>

<hr/>

<p class="quiz-question">How many token-waste-free compression events per session is ideal?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> 0 — never compress</p>

<p class="quiz-option"><strong>B.</strong> 1-3</p>

<p class="quiz-option"><strong>C.</strong> 10+ — compress after every message</p>

<p class="quiz-option"><strong>D.</strong> Only at session end</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">1-3 compressions per session balances context preservation vs overhead. 0 = degradation. &gt;3 = over-compressing.</p>

<hr/>

<p class="quiz-question">A task consistently requires 8000 tokens. After optimization, it's 5000. What's the improvement?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> 37.5% reduction</p>

<p class="quiz-option"><strong>B.</strong> 60% reduction</p>

<p class="quiz-option"><strong>C.</strong> Token usage increased</p>

<p class="quiz-option"><strong>D.</strong> No meaningful change</p>

<p class="quiz-answer"><strong>Answer:</strong> A</p>

<p class="quiz-explanation">3000 tokens saved = 37.5% reduction. Compounds across multiple tasks: 10 tasks = 30,000 tokens saved.</p>


---

# Module 15: Prompt Patterns Library

Est. study time: 1.5h
Language: en

## Learning Objectives
- Apply chain-of-thought, few-shot, and role-prompting for code tasks
- Choose the right prompt pattern for each scenario
- Recognize and avoid prompt anti-patterns
- Combine patterns for complex tasks

---

## Core Content

### Why Prompt Patterns Matter

Agent quality depends heavily on prompt structure. The right pattern reduces ambiguity, improves output consistency, and saves iterations.

```text
Bad prompt:
  "Make the login page better"

Good pattern:
  "Role: Security-focused code reviewer.
   Task: Audit login page for vulnerabilities.
   Process: List auth flows → Check each against OWASP top 10 →
            Tag findings as critical/major/minor.
   Output: Table format. Include line numbers and fix suggestion."
```

> **Think**: Why does the bad prompt fail? What does the good prompt add?
> *Answer: Bad = no context, no criteria. Good adds: role (perspective), process (thinking path), output format (structure). Each addition reduces ambiguity.*

### Chain-of-Thought (CoT)

Agent thinks step-by-step before answering. Improves correctness for complex tasks.

```text
Before CoT:
  "Is this code vulnerable?"
  Agent: "Looks fine."

With CoT:
  "Analyze this code step by step:
   1. Identify all user inputs
   2. Trace data flow through the function
   3. Check each input against known vulnerability patterns
   4. Verify sanitization exists before trusted execution
   Then: is it vulnerable? Report findings with evidence."

  Agent: walks through each step → identifies vulnerability → explains why.
```

| Pattern | Effect | Token cost | Best for |
|---------|--------|-----------|----------|
| CoT | +20-40% accuracy | +100-300 tokens | Complex logic, security, math |
| Zero-shot CoT ("let's think step by step") | +15-25% accuracy | +5 tokens | Quick improvement |
| Structured CoT (numbered steps) | +25-35% accuracy | +50-150 tokens | Multi-step analysis |

> **Think**: When is CoT NOT worth the extra tokens?
> *Answer: Simple tasks (rename, typo fix, boilerplate). CoT overhead 100-300 tokens for no benefit on trivial work.*

### Few-Shot Prompting

Provide examples of desired input/output format.

```text
Before few-shot:
  "Write a test for the login function."
  Agent: writes test in its preferred style.

With few-shot:
  "Write tests for the login function.
   Follow this exact test pattern:

   Example:
   test('returns user data for valid credentials', async () => {
     const result = await api.login('valid@user.com', 'password123')
     expect(result).toHaveProperty('token')
     expect(result.user.email).toBe('valid@user.com')
   })

   Now write tests for: wrong password, expired token, rate limiting."
```

| Shot count | Effect | Token cost | Best for |
|-----------|--------|-----------|----------|
| 1 shot | Signals format | +50-200 tokens | Format alignment |
| 2-3 shots | Signals format + edge case pattern | +100-500 tokens | Complex outputs |
| 4+ shots | Diminishing returns | Heavy | Rarely needed |

> **Think**: How many shots are optimal for a code generation task?
> *Answer: 1-3. One shows format. Two show variation. Three show edge case. Beyond 3, agent has enough pattern and extra examples waste tokens.*

### Role Prompting

Assign a persona to the agent. Changes perspective and priorities.

```text
Roles for engineering tasks:
  "Senior Developer"          → Focus on production quality, maintainability
  "Security Auditor"          → Focus on vulnerabilities, edge cases
  "Performance Engineer"      → Focus on bottlenecks, optimization
  "Junior Developer"          → Focus on clear explanation, learning
  "QA Engineer"               → Focus on test coverage, failure modes
  "Code Reviewer"             → Focus on correctness, conventions
  "Technical Writer"          → Focus on documentation, clarity
```

Example: Same code evaluated by different roles:

```text
Security Auditor:
  "Report finds: SQL injection risk at line 45 (raw query),
   XSS vulnerability at line 78 (untrusted innerHTML),
   Auth bypass at line 120 (missing token validation)"

Performance Engineer:
  "Report finds: N+1 query in user list, missing index on email,
   bundle has unused lodash imports"
```

> **Think**: What role would you assign for a refactoring task?
> *Answer: "Senior Developer" (production quality, maintainability) or "Code Reviewer" (correctness, conventions). Depends on refactor goal.*

### Combined Pattern

Complex tasks benefit from combining patterns:

```text
Role: Senior Developer
Task: Implement search with pagination
Process:
  1. Read existing search pattern (ProductSearch.tsx)
  2. Propose approach (wait for approval)
  3. Implement following our conventions
  4. Run typecheck → lint → tests (must pass)
  5. Show diff with summary of changes
  6. Flag any risks or tradeoffs

Examples of our pattern:
  (show 1-2 lines of existing pattern)

Apply step-by-step. Don't skip steps.
```

Combines: role (Senior Dev) + CoT (numbered steps) + few-shot (pattern reference) + verification gate.

> **Think**: What's the token cost of a combined pattern? Worth it?
> *Answer: 200-400 tokens for the pattern setup. If it prevents one wrong-direction iteration (1000+ tokens), worth it. For trivial tasks, use simpler pattern.*

### Anti-Patterns to Avoid

```text
Anti-pattern 1: "Be careful"
  Problem: Vague. No specific actions.
  Fix: "Run typecheck after changes. Don't modify tests."

Anti-pattern 2: Over-constraining
  Problem: Spec is longer than implementation = you should write it yourself.
  Fix: Provide patterns, not line-by-line instructions.

Anti-pattern 3: Task overflow
  Problem: "Implement search, add dark mode, fix login bug, refactor utils"
  Agent: context fills with task list, each gets half attention.
  Fix: One task per session.

Anti-pattern 4: Assuming shared knowledge
  Problem: "Fix the same bug as last time" (agent doesn't remember)
  Fix: Describe the bug. Every time.

Anti-pattern 5: Changing requirements mid-session
  Problem: "Actually, forget the search bar — add filters instead"
  Effect: Agent's half-done search work pollutes context for filter task.
  Fix: Separate tasks. Finish or discard search, then start filters.
```

> **Think**: You notice agent output quality dropping after 3 changes of scope in same session. What happened?
> *Answer: Task overflow + context pollution. Agent has partial context for each requirement. Finish current task, then start new session for new task.*

---

## Why This Matters

Prompt patterns are your most powerful tool for improving agent output. A well-structured prompt can double output quality at zero extra cost. A bad prompt guarantees poor results regardless of agent capability. Pattern library lets you pick the right tool for each job.

---

## Common Questions

**Q: Should I use the same pattern for every task?**
A: No. Match pattern to task complexity. Simple task → simple prompt. Complex task → combined pattern.

**Q: How do I know which pattern to use?**
A: Classification: Is task analysis-heavy? → CoT. Is format critical? → Few-shot. Is perspective important? → Role. Is it complex? → Combined.

**Q: Can patterns hurt performance?**
A: Yes. Over-constraining limits agent. Wrong role gives wrong perspective. Too many shots waste tokens. Match pattern to need.

---

## Examples

### Example 1: Security Audit with Combined Pattern

```text
Role: Security Auditor (OWASP Top 10 expert)
Task: Audit src/api/auth/login.ts for vulnerabilities
Process:
  1. List all user-controlled inputs
  2. Trace each input's full data flow
  3. Check each path against: injection, auth bypass, data exposure, rate limiting
  4. Report findings as table: Risk | Location | Description | Fix
Examples of security issues we've fixed:
  (2 examples of past vulnerabilities)
```

Agent finds: no rate limiting on login, verbose error messages (e.g., "user not found" vs "wrong password"), no account lockout. Each tagged with fix suggestion.

### Example 2: Complex Feature with Combined Pattern

```text
Role: Senior Full-Stack Developer
Task: Add file upload to user profile
Process:
  1. Read existing upload pattern (src/api/files/upload.ts)
  2. Propose approach: file size limit? format validation? storage backend?
  3. Wait for approval
  4. Implement with typecheck + test after each step
  5. Present diff with summary + risks

Our conventions:
  - Express routes in src/api/
  - Services in src/services/
  - Error handling: next(err) with ApiError class
```

Agent reads upload pattern → proposes: "Use multer with 5MB limit, validate image/jpeg + image/png, store in S3, save URL in Postgres" → You: "Add webp support" → Agent implements.

---

## Key Takeaways
- CoT: step-by-step thinking. Best for complex analysis. +20-40% accuracy.
- Few-shot: examples. Best for format alignment. 1-3 shots optimal.
- Role prompting: changes agent's perspective. Match role to task type.
- Combined patterns for complex tasks. Cost: 200-400 token setup.
- Anti-patterns: vague instructions, over-constraining, task overflow, assumption of shared knowledge, mid-session scope changes.
- Match pattern to task complexity. Don't over-engineer simple prompts.

---

## Common Misconception

**"A single perfect prompt template works for everything."** No universal prompt. Analysis tasks need CoT. Format-critical tasks need few-shot. Perspective-sensitive tasks need role. Complex tasks need combination. Build a library, pick the right tool.

---

## Feynman Explain

(Explain prompt patterns to a beginner. Why can't you just ask nicely? Use cooking analogy: "make dinner" vs "make pasta with tomato sauce, instructions: boil water, add pasta, drain after 10 min" vs "cook like a chef making carbonara.")

---

## Reframe

(Judge: "always use CoT + few-shot + role combined" vs "always use minimal prompt." What does each approach optimize for? When does each fail?)

---

## Drill

Take the quiz. Run: `learn.sh quiz agentic-engineering 15`

## Quiz: 15-prompt-patterns

<p class="quiz-question">Which prompt pattern is best for complex analysis tasks (e.g., security audit)?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Minimal prompt ('is this secure?')</p>

<p class="quiz-option"><strong>B.</strong> Chain-of-Thought (step-by-step analysis)</p>

<p class="quiz-option"><strong>C.</strong> Few-shot with irrelevant examples</p>

<p class="quiz-option"><strong>D.</strong> Role prompting as Junior Developer</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">CoT forces step-by-step analysis. +20-40% accuracy for complex tasks. 'Minimal prompt' leads to superficial answers.</p>

<hr/>

<p class="quiz-question">How many examples (shots) are optimal for code generation tasks?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> 10+</p>

<p class="quiz-option"><strong>B.</strong> 1-3</p>

<p class="quiz-option"><strong>C.</strong> 0 — examples hurt performance</p>

<p class="quiz-option"><strong>D.</strong> Exactly 5</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">1 shows format. 2 shows variation. 3 shows edge cases. Beyond 3 = diminishing returns and token waste.</p>

<hr/>

<p class="quiz-question">What role would you assign for finding performance bottlenecks?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Security Auditor</p>

<p class="quiz-option"><strong>B.</strong> Performance Engineer</p>

<p class="quiz-option"><strong>C.</strong> Technical Writer</p>

<p class="quiz-option"><strong>D.</strong> Junior Developer</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Performance Engineer focuses on bottlenecks, optimization, profiling. Right role → right perspective.</p>

<hr/>

<p class="quiz-question">What is 'task overflow' anti-pattern?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> One task per session — best practice</p>

<p class="quiz-option"><strong>B.</strong> Multiple unrelated tasks in same prompt — each gets half attention</p>

<p class="quiz-option"><strong>C.</strong> Giving agent too few tasks</p>

<p class="quiz-option"><strong>D.</strong> Agent completing tasks too quickly</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Multiple tasks in one session = context pollution. Each task gets partial attention. Separate into sequential sessions.</p>

<hr/>

<p class="quiz-question">When is Chain-of-Thought NOT worth the extra tokens?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Security audit</p>

<p class="quiz-option"><strong>B.</strong> Simple tasks (rename, typo fix, boilerplate)</p>

<p class="quiz-option"><strong>C.</strong> Complex logic</p>

<p class="quiz-option"><strong>D.</strong> Multi-step analysis</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">CoT overhead 100-300 tokens. No benefit for trivial work where answer is obvious.</p>

<hr/>

<p class="quiz-question">What is the token cost of a combined pattern (role + CoT + few-shot + verification)?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> 50-100 tokens</p>

<p class="quiz-option"><strong>B.</strong> 200-400 tokens — saves 1000+ by preventing wrong direction</p>

<p class="quiz-option"><strong>C.</strong> 2000+ tokens — not worth it</p>

<p class="quiz-option"><strong>D.</strong> 0 tokens — free</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">200-400 tokens setup cost. Prevents one wrong-direction iteration (1000+ tokens). Net positive for complex tasks.</p>

<hr/>

<p class="quiz-question">What's the problem with 'Fix the same bug as last time'?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Agent remembers last session — redundant</p>

<p class="quiz-option"><strong>B.</strong> Agent doesn't have memory across sessions without context</p>

<p class="quiz-option"><strong>C.</strong> Bug was already fixed</p>

<p class="quiz-option"><strong>D.</strong> Too specific</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Agent sessions are stateless. 'Same as last time' = no information. Always describe the bug.</p>

<hr/>

<p class="quiz-question">What happens when you change task scope mid-session (e.g., 'forget search, add filters')?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Agent smoothly switches focus</p>

<p class="quiz-option"><strong>B.</strong> Half-done search work pollutes context for filter task</p>

<p class="quiz-option"><strong>C.</strong> Nothing — agent handles scope changes well</p>

<p class="quiz-option"><strong>D.</strong> Agent resets automatically</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Previous task's context (partial code, decisions, mess) stays in context. Pollution degrades new task quality.</p>

<hr/>

<p class="quiz-question">Which pattern combination is best for: 'Audit this API endpoint and write tests for vulnerabilities'?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Minimal: 'Write tests'</p>

<p class="quiz-option"><strong>B.</strong> Role (Security Auditor) + CoT (trace inputs → check vulnerabilities → write tests)</p>

<p class="quiz-option"><strong>C.</strong> Only few-shot (test examples)</p>

<p class="quiz-option"><strong>D.</strong> Role (Junior Developer) for simple tests</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Security Auditor role gives right perspective. CoT ensures thorough analysis before writing tests. Two patterns for two subtasks (audit + test).</p>

<hr/>

<p class="quiz-question">What's the effect of 'over-constraining' a prompt?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Agent produces more creative solutions</p>

<p class="quiz-option"><strong>B.</strong> Agent has no room to apply judgment or leverage codebase patterns</p>

<p class="quiz-option"><strong>C.</strong> Agent works faster</p>

<p class="quiz-option"><strong>D.</strong> No effect — more constraints always better</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Over-constraining: spec is longer than you'd write = wasted tokens + agent can't use its strengths. Provide patterns, not line-by-line.</p>


---

# Module 16: Production Pipeline & MCPs

Est. study time: 1h
Language: en

## Learning Objectives
- Integrate agent workflow with CI/CD pipeline
- Use agents for PR review automation
- Understand MCP server integration
- Design custom hooks for automation

---

## Core Content

### Agent + CI/CD Integration

Agent development doesn't replace CI/CD — it changes where agent output enters the pipeline.

```text
Without agent:
  Dev writes code → commit → PR → CI runs (typecheck, lint, test, build) → review → merge

With agent:
  Agent writes code → (typecheck → lint → test) already passed before commit
  → commit → PR → CI runs (full suite) → agent reviews → human spot-checks → merge

Key: verification gates run BEFORE commit. CI should never catch what agent already verified.
```

**Pre-commit agent checks (run by agent before presenting diff):**

```text
1. Typecheck → pass
2. Lint → pass (auto-fix if project allows)
3. Related tests → pass
4. Build → pass (for deployable changes)
5. Evidence receipt generated (summary + diff + decisions + gate results)
```

If any fail → agent fixes and re-runs. Only passes to you when all green.

> **Think**: CI catches a type error that agent should have caught. What went wrong?
> *Answer: Agent skipped pre-commit verification gate. Either not instructed to run it, or gate was disabled. Fix: enforce verification in AGENTS.md.*

### PR Review Automation

Agent can automate PR review. Integration options:

**As PR reviewer (agent comments on PR):**
- Agent reads PR diff
- Applies review skill (correctness, security, conventions)
- Posts review comments on PR
- Human reviews agent's review + spot-checks code

**As PR author (agent writes PR for you):**
- Requires: feature branch, changes already reviewed
- Agent writes PR description, summarizes changes, tags reviewers
- Agent may create PR via GitHub API

```text
Agent PR review checklist:
1. Verify all acceptance criteria met (from spec)
2. Check diff matches intended scope (no unrelated changes)
3. Run mental review: correctness, security, conventions
4. Check test coverage (are new behaviors tested?)
5. Flag any risks or tradeoffs
6. Output: structured review report + per-line comments if needed
```

> **Think**: Should agent have write access to merge PRs?
> *Answer: No. Agent reviews and comments. Human merges. Merge is human responsibility.*

### MCP Server Integration

MCP (Model Context Protocol) servers extend agent capabilities. Think of them as "tools plugins."

**Common MCP servers:**

| MCP Server | What it provides | Use case |
|-----------|-----------------|----------|
| GitHub | PR, issues, repos, commits | PR review automation, issue triage |
| Git | Clone, branch, commit, push | Automated git operations |
| Filesystem | Read/write outside project | Config files, logs |
| PostgreSQL | Query DB | Database exploration, migrations |
| SQLite | Query local DB | Local development data |
| Puppeteer | Browser automation | Visual testing, screenshots |
| Brave Search | Web search | Research, documentation lookup |

**Installing MCP servers:**

```text
In opencode.json or equivalent config:
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/dir"]
    }
  }
}
```

> **Think**: You want agent to create PRs automatically. Which MCP server needed?
> *Answer: GitHub MCP server. Provides PR creation, commenting, merging capabilities. Agent can run `gh` commands through it.*

### Custom Hooks

Hooks trigger automated actions on events.

**Common hook triggers:**

```text
Pre-commit hook:
  Before allowing commit → run typecheck + lint + tests
  If any fail → block commit, report failures

Post-merge hook:
  After merge → update CLAUDE.md, clear merged branch

Post-deploy hook:
  After deploy → run smoke tests, notify team

File change hook:
  On package.json change → run `npm install`, report new dependencies
  On config change → validate config format
```

**Hook design principles:**
- Fail open (hooks shouldn't block if they error)
- Log all actions (so you can debug hook failures)
- Keep fast (<1s for typical hook)
- Have escape hatch (`--no-verify` for git hooks)

> **Think**: You hook pre-commit to run full test suite. Tests take 15 minutes. Everyone hates this hook. What's wrong?
> *Answer: Hook is too slow. Full suite is for CI. Hook should run related tests only, or only typecheck + lint. Speed matters for adoption.*

### Multi-Repo Workflows

Agent managing multiple repos needs structured approach:

```text
Scenario: Microservice architecture with 5+ repos.
Challenge: Agent context can't hold all repos simultaneously.

Approach:
1. AGENTS.md per repo (conventions, patterns)
2. Common patterns in shared skill (accessible across repos)
3. Per-session scope: one repo per session
4. Cross-repo changes: coordinate via issue/PR, not agent context

For changes spanning repos:
1. Session A: change shared library repo → publish new version
2. Session B: update consumer repos to use new version
```

> **Think**: Why one-repo-per-session for multi-repo work?
> *Answer: Context can't hold all repos. Splitting per-session keeps focus clean. Cross-repo coordination happens via version bumps, not simultaneous edits.*

---

## Why This Matters

Agent development doesn't exist in isolation. It integrates with CI/CD, PR workflows, MCP-extended capabilities, and custom automation hooks. Production pipeline ensures agent output flows smoothly into existing development infrastructure — not disrupting it.

---

## Common Questions

**Q: Should CI run same checks as agent verification?**
A: Yes — but CI runs full suite (slower, more thorough). Agent runs related checks (fast, frequent). Both catch different things.

**Q: Can MCP servers be security risks?**
A: Yes. Filesystem MCP grants file access. Database MCP grants query access. Restrict MCP server permissions to minimum needed.

**Q: What's the most useful MCP server for daily development?**
A: GitHub (PR management) and Filesystem (access outside project). Start with these.

---

## Examples

### Example 1: Full Production Pipeline

```text
1. Agent implements feature (with pre-commit verification)
2. Agent produces evidence receipt
3. You review → approve
4. Agent creates branch + PR (via GitHub MCP)
5. PR triggers CI (full test suite, build, deploy preview)
6. CI passes
7. Agent reviews own PR (review skill)
8. Human spot-checks → merges
9. Post-merge hook: deploys to staging
10. Post-deploy hook: runs smoke tests
```

Total human time: 5-10 min per PR. Agent does everything else.

### Example 2: Hook for Safety

```text
Hook: pre-tool guard for Write
  If destination matches "src/config/*.ts" or "*.config.*":
    - Log: "Protected file. Needs approval."
    - Block write
    - Ask: "Approve write to [file]?"
```

Prevents accidental config modifications. Agent learns to ask before touching protected files.

---

## Key Takeaways
- Agent verification gates run BEFORE commit. CI should never catch what agent already checked.
- Agent can review PRs (structured comments) or author PRs (description + summary).
- MCP servers extend capabilities: GitHub, Filesystem, Database, Browser, Search.
- Custom hooks automate: pre-commit checks, post-merge updates, post-deploy tests.
- Multi-repo: one repo per session. Shared patterns in cross-repo skills.
- Hooks should be fast, log actions, and have escape hatches.
- MCP servers need permission restriction (security).

---

## Common Misconception

**"Agent replaces CI/CD."** Agent complements CI/CD. Agent handles pre-commit verification (fast, focused). CI handles full suite (thorough, independent). Agent is the first gate, CI is the last gate. Both needed.

---

## Feynman Explain

(Explain agent + CI/CD integration to a DevOps engineer. Why not just have agent commit directly to production? What value does the pipeline add if agent already verified?)

---

## Reframe

(Judge: "let agent create and merge PRs autonomously" vs "agent only reviews, human always merges." Where's the right balance? When would full autonomy be acceptable?)

---

## Drill

Take the quiz. Run: `learn.sh quiz agentic-engineering 16`

## Quiz: 16-production-pipeline

<p class="quiz-question">When should agent verification gates run relative to commit?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> After commit — CI catches everything</p>

<p class="quiz-option"><strong>B.</strong> Before commit — gates pass before agent presents diff</p>

<p class="quiz-option"><strong>C.</strong> Never — verification is human responsibility</p>

<p class="quiz-option"><strong>D.</strong> Only on Fridays</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Pre-commit verification. Agent runs typecheck → lint → tests → only then presents diff. CI should never catch what agent already verified.</p>

<hr/>

<p class="quiz-question">What should agent's role be in PR workflow?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Full write access to merge PRs autonomously</p>

<p class="quiz-option"><strong>B.</strong> Review and comment. Human merges.</p>

<p class="quiz-option"><strong>C.</strong> No involvement in PRs</p>

<p class="quiz-option"><strong>D.</strong> Only write PR descriptions, no review</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Agent reviews, comments, authors PRs. But merge is human responsibility. Safety boundary.</p>

<hr/>

<p class="quiz-question">What does MCP (Model Context Protocol) provide?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Faster agent responses</p>

<p class="quiz-option"><strong>B.</strong> Extended tool capabilities via server plugins</p>

<p class="quiz-option"><strong>C.</strong> Better AI models</p>

<p class="quiz-option"><strong>D.</strong> Automatic code generation</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">MCP servers add tool capabilities: GitHub API, filesystem access, database queries, browser automation.</p>

<hr/>

<p class="quiz-question">Which MCP server enables agent to create PRs automatically?</p>

<p class="quiz-difficulty">★☆☆</p>

<p class="quiz-option"><strong>A.</strong> Filesystem server</p>

<p class="quiz-option"><strong>B.</strong> GitHub server</p>

<p class="quiz-option"><strong>C.</strong> SQLite server</p>

<p class="quiz-option"><strong>D.</strong> Puppeteer server</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">GitHub MCP provides PR creation, commenting, issue management, repo operations.</p>

<hr/>

<p class="quiz-question">What's a common anti-pattern for hooks?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Hooks run fast (&lt;1s)</p>

<p class="quiz-option"><strong>B.</strong> Hooks have escape hatches</p>

<p class="quiz-option"><strong>C.</strong> Hook runs full test suite (15 min) on every pre-commit</p>

<p class="quiz-option"><strong>D.</strong> Hooks log all actions</p>

<p class="quiz-answer"><strong>Answer:</strong> C</p>

<p class="quiz-explanation">Slow hooks frustrate developers and get bypassed. Full suite is for CI. Pre-commit hook should be fast (typecheck + lint + related tests).</p>

<hr/>

<p class="quiz-question">What is the recommended approach for multi-repo agent workflow?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Load all repos in one session</p>

<p class="quiz-option"><strong>B.</strong> One repo per session. Shared patterns in cross-repo skill.</p>

<p class="quiz-option"><strong>C.</strong> Agent handles repos independently without coordination</p>

<p class="quiz-option"><strong>D.</strong> Manual only — agents can't handle multi-repo</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Context can't hold all repos. One per session keeps focus. Shared skill for cross-repo patterns.</p>

<hr/>

<p class="quiz-question">CI catches a type error after agent's PR. What went wrong?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Normal — CI catches things agent misses</p>

<p class="quiz-option"><strong>B.</strong> Agent skipped pre-commit typecheck gate</p>

<p class="quiz-option"><strong>C.</strong> Typecheck cannot be automated</p>

<p class="quiz-option"><strong>D.</strong> CI is misconfigured</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Agent should have caught this with pre-commit typecheck. Either gate not enforced or skipped. Fix: enforce in AGENTS.md.</p>

<hr/>

<p class="quiz-question">When designing a pre-commit hook, what is most important?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Comprehensive — check everything</p>

<p class="quiz-option"><strong>B.</strong> Fast — developers won't use slow hooks</p>

<p class="quiz-option"><strong>C.</strong> Silent — no output unless error</p>

<p class="quiz-option"><strong>D.</strong> Random — vary checks each time</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Speed is most important for hooks developers actually use. Fast (&lt;1s) typecheck + lint is better than 15-min full suite that gets bypassed.</p>

<hr/>

<p class="quiz-question">What is the purpose of a post-deploy hook?</p>

<p class="quiz-difficulty">★★☆</p>

<p class="quiz-option"><strong>A.</strong> Revert deploy if issues found</p>

<p class="quiz-option"><strong>B.</strong> Run smoke tests and notify team after deployment</p>

<p class="quiz-option"><strong>C.</strong> Prevent deploy during business hours</p>

<p class="quiz-option"><strong>D.</strong> Delete old deploy artifacts</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Post-deploy: verify deployment succeeded (smoke tests), notify team, update deployment tracking.</p>

<hr/>

<p class="quiz-question">Agent has GitHub MCP configured. What's a reasonable permission boundary?</p>

<p class="quiz-difficulty">★★★</p>

<p class="quiz-option"><strong>A.</strong> Full repo admin access</p>

<p class="quiz-option"><strong>B.</strong> Read + comment + PR creation. No merge. No admin.</p>

<p class="quiz-option"><strong>C.</strong> Only read access</p>

<p class="quiz-option"><strong>D.</strong> Only write access to main branch</p>

<p class="quiz-answer"><strong>Answer:</strong> B</p>

<p class="quiz-explanation">Agent needs read (analyze), comment (review), PR create (author). Merge and admin are human responsibilities. Restrict to minimum permissions.</p>
