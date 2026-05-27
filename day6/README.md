# Day 6 — Functions, Indentation & While Loops

## 📚 Concepts Learned

| Concept | Description |
|---|---|
| `def` | Define a reusable function |
| Function indentation | Code block inside function must be indented |
| `while` loop | Repeat until condition becomes False |
| `while not` | Loop until something is True |
| Boolean conditions | `not`, `and`, `or` in loop/if conditions |
| Function abstraction | Create your own function when built-in doesn't exist |
| Nested `if/else` | Conditions inside conditions |

---

## 🤖 Project — Reeborg's World (Hurdle 1–4)

Solved all 4 hurdles in Reeborg's World using functions and while loops.

### Hurdle 1 — Fixed steps
Simple move and jump sequence — hardcoded steps.

### Hurdle 2 — Variable hurdle positions
Used `while not at_goal()` loop to handle unknown hurdle positions.

### Hurdle 3 — Variable hurdle heights
Extended logic to handle hurdles of different heights.

### Hurdle 4 — Maze solver (Right-hand rule) ⭐
Most complex — solved a maze using the classic **right-hand wall follower** algorithm.

---

## 🧩 Hurdle 4 — Maze Solver

- 📄 [maize_solver.py](./maize_solver.py)

### Algorithm — Right-hand rule
> Always keep the wall on your right side — a classic maze solving technique used in robotics!

```
wall on right? → No  → turn right + move (hug the wall)
wall on right? → Yes → wall in front? → Yes → turn left
                                       → No  → move forward
Repeat until goal reached!
```

## 💡 Key Takeaways

- `def` creates a reusable block of code — call it as many times as needed
- **Indentation is not optional in Python** — it defines the code block
- `while` loop runs **as long as condition is True** — use carefully to avoid infinite loops
- When a built-in function doesn't exist → **create your own** (`turn_right()` from 3x `turn_left()`)
- Right-hand rule is a **real algorithm** used in robotics and maze solving 🤖

---
