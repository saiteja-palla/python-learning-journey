# Day 12 — Scope, Namespaces, Global Keyword & Constants

---

## 📚 Concepts Learned

| Concept | Description |
|---|---|
| Local Scope | Variable inside a function — only accessible within it |
| Global Scope | Variable outside all functions — accessible everywhere |
| Block Scope | Python has no block scope — variables inside `if`/`for`/`while` leak out |
| `global` keyword | Use inside a function to modify a global variable |
| Constants | `UPPER_SNAKE_CASE` — signals value should not change, Python does not enforce it |
| Namespaces | Each scope has its own namespace — same name in different scopes does not conflict |

---

## 🧮 Exercise — Prime Number Checker

Checks whether a given number is prime.
- 📄 [prime_checker.py](./prime_checker.py)

### Rules
- Numbers less than 2 → not prime
- Divide by every number from `2` to `num - 1`
- Any exact division found → not prime
- No divisor found → prime

---

## 🎮 Project — Number Guessing Game

Terminal-based number guessing game with easy and hard difficulty levels.
- 📄 [number_guessing.py](./number_guessing.py)

### Rules
- Computer picks a random number between 1 and 100
- Player chooses difficulty — `easy` (10 attempts) or `hard` (5 attempts)
- Each guess — told if answer is too high or too low
- Attempts countdown after each wrong guess
- Run out of attempts → lose
---

## 💡 Key Takeaways

- **Python has no block scope** — variables defined inside `if`/`for`/`while` are accessible outside — different from Java/JavaScript
- **Use `global` sparingly** — modifying globals inside functions reduces predictability — better to pass as arguments
- **Constants are convention only** — `UPPER_SNAKE_CASE` signals "do not change this" — Python does not enforce immutability
- **Early return pattern** — in prime checker, return `False` as soon as a divisor is found — avoids unnecessary iterations
- **`range(2, num)` not `range(2, num+1)`** — including `num` itself always gives a false divisor since `num % num == 0`

---