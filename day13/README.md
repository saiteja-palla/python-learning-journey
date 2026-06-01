# Day 13 — Debugging, Docstring Structure & Conditional Operators

---

## 📚 Concepts Learned

| Concept | Description |
|---|---|
| Debugging — `print()` | Insert print statements to inspect variable values at runtime |
| Debugging — breakpoints | Pause execution at a line and inspect state in IDE |
| Debugging — rubber duck | Explain code line by line out loud to spot logic errors |
| Docstring structure | `"""One-line summary.\n\nExtended description if needed."""` — right after `def` |
| `help(func)` | Prints the docstring of any function in terminal |
| Conditional operator `==` | Compares value — `name == 'teja'` checks equality, not assignment |
| `=` vs `==` | `=` assigns, `==` compares — common bug source |
| `in` operator in conditions | `if name in list` — cleaner than chaining multiple `==` checks |

---

## 🧮 Exercises — Debugging Practice

Three debugging exercises — identifying and fixing logic, syntax and runtime errors.
- No standalone files — concept practice only

### Types of Errors Fixed
- **Syntax errors** — missing colons, incorrect indentation
- **Runtime errors** — wrong variable names, index out of range
- **Logic errors** — off-by-one in loops, wrong comparison operator

---

## 💡 Key Takeaways

- **`==` not `=` in conditions** — `if name == 'teja'` is comparison, `name = 'teja'` is assignment — easy to miss
- **`in` operator** — `if user in ['admin', 'guest']` is cleaner than `if user == 'admin' or user == 'guest'`
- **Describe the bug before fixing it** — rubber duck debugging forces clear thinking before touching code
- **Docstrings are for humans** — write what the function does, not how — `help()` surfaces it instantly
- **Print-driven debugging** — fastest way to catch unexpected values mid-execution before reaching for a debugger

---