# Module 12: Feedback & Error-Driven Learning

Est. study time: 2.5h
Language: en
Description: Why errors are essential for learning — and how to give/receive feedback that actually improves performance.

```mermaid
mindmap
  root((Feedback))
    Learning from Errors
    Types of Feedback
    Immediate vs Delayed
    Feedback Sandwich Myth
    Self-Feedback
    Receiving Feedback
```

## Learning Objectives
- Distinguish outcome feedback, corrective feedback, and elaborative feedback
- Explain how prediction errors drive learning
- Apply feedback principles to self-study (self-feedback)
- Avoid common feedback mistakes (sandwich, delayed too long)

---

## Real-World Example

You solve a practice problem. You check the answer. Wrong.

Three possible responses:
- "Wrong. Score: 0." (outcome only)
- "Wrong. The correct answer is X." (corrective)
- "Wrong. Here's why: you misinterpreted step 3. Step 3 should be Y because Z." (elaborative)

Each gives you different information. Each produces different learning. The third one is best — but even corrective beats outcome-only.

> **Think**: If you get a practice problem wrong but don't find out WHY until tomorrow, how much do you learn?
>
> *Answer: Less than if you got immediate explanation. The error trace fades. Immediate feedback links the error to its correction most strongly.*

---

## Core Content

### The Learning Function of Errors

Errors are not failures — they are **learning signals**.

```mermaid
graph LR
    Act[Action] --> Pred[Prediction]
    Pred --> Outcome[Actual Outcome]
    Outcome --> Match{Match?}
    Match -->|Yes| Nothing[No update]
    Match -->|No| Error[Prediction error signal]
    Error --> Update[Update mental model]
    Update --> Better[Better prediction next time]
    style Error fill:#b86a4a
    style Update fill:#5c8a6a
```

**Prediction error**: The gap between expected outcome and actual outcome. The brain uses this gap to update its model. Larger gap = stronger learning signal — IF you receive feedback.

**Without feedback**: No error signal. No update. Same mistake repeated.

> **Cloze**: "Learning occurs when there is a gap between {prediction} and {outcome}. This {prediction error} drives updates to the mental model."
>
> *Answer: prediction, outcome, prediction error*

### Types of Feedback

| Type | Content | Learning effect |
|------|---------|----------------|
| **Outcome** | Right/wrong only | Weak — confirms but doesn't explain |
| **Corrective** | Right/wrong + correct answer | Medium — provides target |
| **Elaborative** | + explanation of WHY | Strong — fixes mental model |
| **Metacognitive** | + strategy guidance | Strongest — builds self-regulation |

**Elaborative feedback is best**: It tells you not just what was wrong, but why, and how to fix it.

> **Think**: Why does outcome-only feedback (score, no explanation) produce weak learning?
>
> *Answer: It signals error but not the cause. Without knowing WHY you were wrong, you can't update the specific faulty reasoning. You might change the right thing or miss the real issue.*

### Timing: Immediate vs Delayed

| Timing | Best for | Why |
|--------|----------|-----|
| **Immediate** | Procedural skills, novices | Prevents error reinforcement |
| **Delayed** | Conceptual understanding, experts | Allows error detection practice |
| **Self-paced** | Most learning | Learner sees feedback when ready |

**The guidance hypothesis**: Immediate feedback helps initial skill acquisition (prevents practicing errors). Delayed feedback helps transfer (learner must detect their own errors).

> **Predict**: A student is learning to solve physics problems. Should they get immediate feedback after each step or delayed feedback after the full problem?
>
> *Answer: Immediate at first (builds correct procedure), then shift to delayed (forces self-checking). Novices benefit more from immediate feedback.*

### The Feedback Sandwich Myth

The "feedback sandwich" (positive → criticism → positive) is widely taught but empirically weak.

**Problems with the sandwich:**
1. Learner focuses on the positive (reinforcement) and misses the criticism
2. Positive framing dilutes the error signal
3. Feels patronizing
4. Doesn't improve learning outcomes compared to direct corrective feedback

**Better approach**: Direct, specific, actionable feedback about the error, separated from general encouragement.

> **Spot the Mistake**: "You did great on the first section! But the second section had errors. Overall, your effort is commendable!"
>
> What's wrong?
>
> *Answer: Feedback sandwich. The error signal is buried between compliments. Learner may not process the correction. Direct: "Section 2 had errors in steps 3-4. Here's why and how to fix."*

### Self-Feedback: How to Give Yourself Feedback When Studying Solo

You can't always get a teacher. But you can create your own feedback loops.

**Self-feedback techniques:**

| Technique | How | What it trains |
|-----------|-----|----------------|
| **Answer-check** | Solve → check → analyze error | Detection |
| **Self-explanation** | Explain why answer is wrong | Understanding |
| **Error log** | Track error types over time | Pattern recognition |
| **Compare methods** | Solve with method A, then method B | Strategy selection |
| **Generate distractors** | Create wrong answers + explain why wrong | Deep understanding |

**Example error log:**

| Date | Topic | Error type | Cause | Fix |
|------|-------|-----------|-------|-----|
| Jan 5 | Quadratic eq | Wrong formula | Confused with linear | Write comparison table |
| Jan 6 | Quadratic eq | Sign error | Rushed | Slow down step 3 |

> **Think**: A student misses a problem but doesn't analyze why. They just move on. How much do they learn from the error?
>
> *Answer: Almost nothing. The error signal fired but wasn't processed. Analyzing the error converts the signal into a model update.*

### Error-Driven Learning in Action

The effective learning cycle:

```mermaid
graph TD
    A[Attempt task] --> B[Get outcome / feedback]
    B --> C{Correct?}
    C -->|Yes| D[Reinforce current model]
    C -->|No| E[Analyze error type & cause]
    E --> F[Identify specific gap]
    F --> G[Study gap]
    G --> H[Retry similar task]
    H --> A
    style E fill:#b86a4a
    style G fill:#5c8a6a
```

**Key insight**: The error analysis + targeted gap study is the engine of improvement. Without it, errors repeat.

> **Predict**: Two students each make 10 practice test errors. Student A notes "wrong" and moves on. Student B logs each error type, studies the gap, and retests. After 5 such sessions, who improves more?
>
> *Answer: Student B. Error analysis turns each mistake into a learning opportunity. Student A just accumulates errors without fixing root causes.*

### How to Receive Feedback

Receiving feedback is a skill. The best learners:

1. **Seek** feedback proactively (don't wait for tests)
2. **Separate** ego from information (error ≠ personal failure)
3. **Ask** for specifics ("What did I miss?")
4. **Apply** immediately (retry before the feedback fades)
5. **Track** error patterns (notice recurring types)

> **Think**: When someone gives you feedback, what's the most productive first reaction?
>
> *Answer: "What can I learn from this?" — not defense or shame. Feedback is data about your current model, not about your worth.*

---

## Why This Matters

Feedback is how you know if learning is happening. Without it, you're flying blind. Error-driven learning is the mechanism behind:
- Retrieval practice (feedback from correct answers)
- Worked examples (feedback from expert solution)
- Self-testing (feedback from answer key)
- Any practice with comparison (feedback from difference)

If you're not getting feedback on your learning, you're guessing.

---

## Key Takeaways
- Prediction errors drive learning — the gap between expected and actual outcome
- Elaborative feedback (why) is better than corrective (what) is better than outcome (score)
- Immediate feedback for novices, delayed for experts
- Feedback sandwich dilutes the error signal — be direct
- Self-feedback loops: solve → check → analyze → restudy → retry
- Error logs reveal patterns and root causes
- Receiving feedback is a skill: seek it, separate ego, apply immediately

---

## Common Misconception

**Misconception**: "Making errors means you're not learning."

**Reality**: Errors ARE learning signals. The question is whether you receive feedback to correct them. Error-free practice (re-reading) produces no prediction errors → no model updates.

**Correct framing**: Make errors early and often — with immediate feedback. Each error is an opportunity to update your mental model.

---

## Spot the Mistake

"I learn best by getting it right the first time. If I make mistakes, I feel like I'm failing."

What's wrong?

*Answer: Error-avoidance mindset. It leads to staying in your comfort zone, avoiding challenge, and missing learning opportunities. Productive error = prediction error signal = learning trigger.*

---

## Feynman Explain
(Explain error-driven learning: your brain is a prediction machine. When your prediction is wrong, your brain says "surprise!" and updates. Errors are like hitting a wrong note while playing piano — painful but the only way your brain knows to adjust your finger position.)

---

## Reframe
(Judge: think of a recent error you made while studying. Did you analyze it or just move on? Design an error log for your current study topic. Track 5 errors and their root causes.)

---

## Drill
Run: `learn.sh quiz learning-theories 12`
