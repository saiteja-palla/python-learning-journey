# Day 7 — String Manipulation & Hangman Game

## 📚 Concepts Learned

| Concept | Description |
|---|---|
| `str.lower()` / `str.upper()` | Convert string case |
| `str.replace()` | Replace characters in a string |
| String slicing | `str[start:end]` — extract or rebuild parts |
| `in` operator | Check if character/substring exists |
| Convert string ↔ list | `list(str)` and `''.join(list)` |
| `while` loop with `break` | Loop until condition met, exit cleanly |
| Immutability | Strings can't be changed in place — must rebuild |

---

## 🪓 Project — Hangman Game

Classic word guessing game — guess letters before the hangman is complete!
- 📄 [hangman_game.py](./hangman_game.py)

### Rules
- Random word is chosen from a word list
- Player guesses one letter at a time
- Correct guess → letter revealed in placeholder
- Wrong guess → lives reduce by 1
- 6 lives total — one body part per wrong guess
- Win → guess all letters before lives run out
- Lose → lives reach 0

---

## 💡 Key Takeaways

- Strings are **immutable** — convert to list when you need to modify by index
- Always check win condition **outside** the for loop to avoid false triggers
- `break` is cleaner than `game_over` flag for simple game loops
- `in` operator works on both strings and lists — very versatile
- Print **once** per loop iteration — avoid duplicate prints by structuring if/else carefully

---
