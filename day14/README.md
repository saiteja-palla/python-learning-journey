# Day 14 — Higher Lower Game

---

## 📚 Concepts Learned

| Concept | Description |
|---|---|
| Higher order functions | Functions that take or return other functions |
| `choice()` from `random` | Pick a random item from a list |
| `dict.get(key)` | Safely retrieve a value from a dictionary |
| `global` keyword | Modify a global variable (`guess_count`) from inside a function |
| Multi-file project | Split code across `main.py`, `game_data.py`, `art.py` |
| Seen-entries tracking | List to prevent repeat comparisons in the same game session |
| `try` / `except ValueError` | Handle invalid user input gracefully |

---

## 🎮 Project — Higher Lower Game

Guess which celebrity or brand has more Instagram followers — score increases on every correct answer.
- 📄 [higher_lower.py](./higher_lower.py)

### Rules
- Two people/brands shown — A and B
- Player guesses who has more followers — type `A` or `B`
- Correct guess → score +1, B becomes new A, new B picked
- Wrong guess → game over, final score shown
- Already seen entries tracked — no repeats in one session
- Invalid input → `ValueError` caught, player prompted again

### Functions Breakdown

| Function | Responsibility |
|---|---|
| `random_pick()` | Return a random entry from `data` |
| `call_out(person_a, person_b)` | Display both options with name, description, country |
| `compare_followers(data1, data2)` | Compare follower counts — return `True`/`False` |
| `play_game(seen_entries)` | Orchestrate full game loop with seen-entry tracking |

---

---