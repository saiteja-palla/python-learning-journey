# Day 4 — Randomization & Lists

## 📚 Concepts Learned

| Concept | Description |
|---|---|
| `random` module | Built-in module for generating random values |
| `random.randint(a, b)` | Returns a random integer between a and b (inclusive) |
| `random.choice(list)` | Picks a random element from a list |
| Lists `[]` | Ordered collection of items, accessed by index |
| Nested lists | Lists inside lists — `[[1,2], [3,4]]` |
| List indexing | Access elements via `list[0]`, `list[1]` etc. |
| Input validation | Check invalid input and `exit()` early |

---

## 📝 Task

#### Coin Flip Simulator
Simulates a random coin toss and prints the result.
- 📄 [coin_flip_simulator.py](./coin_flip_simulator.py)

**Rules**
- Randomly pick either `Heads` or `Tails`
- Print the result to the user


#### Rock Paper Scissors Game

A 1-player game where the user plays against the computer with ASCII art output.
- 📄 [rock_paper_scissors_game.py](./rock_paper_scissors_game.py)

**Rules**
- User chooses `0` for Rock, `1` for Paper, `2` for Scissors
- Computer randomly picks one of the three
- Winner decided by:
  - Rock beats Scissors
  - Scissors beats Paper
  - Paper beats Rock
- Same choice → Draw
- Input outside `0–2` → Error message + exit


## 💡 Key Takeaways

- Always `import` modules at the **top** of the file
- `random.choice(list)` is cleaner than `randint` for picking from fixed options
- Lists + indexing make code shorter and more readable than separate variables
- Validate user input **before** running any game logic — fail fast with `exit()`
- Multi-line strings `"""..."""` are useful for storing ASCII art

---
