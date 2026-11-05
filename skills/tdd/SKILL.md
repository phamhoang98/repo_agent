---
name: tdd
description: "Test-driven development loop (red, green, refactor). Use when the user asks for TDD or when fixing logic that has clear expected inputs and outputs."
---

Follow a strict red-green-refactor loop:

1. **Red**: write one small failing test that describes the next behavior. Run it and confirm it fails for the expected reason.
2. **Green**: write the minimum production code to make it pass. Run the test.
3. **Refactor**: clean up names and duplication with all tests green. Run the suite again.
4. Repeat until the behavior is complete. Then run the full relevant suite.

Rules:
- Never write production code without a failing test that needs it.
- One behavior per test; test public behavior, not internals.
- Keep each cycle small (minutes, not hours).
- Report each cycle briefly: test added, result before, result after.
