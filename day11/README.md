# Day 11 — Blackjack Capstone Project

---

## 📚 Concepts Learned

| Concept | Description |
|---|---|
| Refactoring | Restructure existing code without changing behaviour |
| DRY Principle | Don't Repeat Yourself — eliminate duplicate logic |
| Modular functions | Break game into small, single-responsibility functions |
| `None` return | Functions that mutate in-place vs return a value |
| Type hints `list` | `hand: list` — clarify expected argument type |
| `while True` + `break` | Game loop control — cleaner than flag variables |
| Edge case handling | Blackjack on deal, Ace as 1 or 11, dealer bust |
| `list.remove(value)` | Remove first occurrence of a value — nothing returned |
| `list.pop(index)` | Remove by index — returns the removed value |

---

## 🎴 Project — Blackjack Game

Terminal-based Blackjack card game following standard casino rules.
- 📄 [blackjack.py](./blackjack.py)

### Rules
- Player and dealer each get **2 cards** on deal
- Player hits (`y`) or stands (`n`)
- Dealer draws automatically until score **≥ 17**
- **Ace** dynamically valued as `11` or `1` to avoid bust
- **Blackjack** (21 on initial deal) — game ends immediately, no extra draws
- If both player and dealer have 21 on deal → Draw

### Functions Breakdown

| Function | Responsibility |
|---|---|
| `deal_card(hand)` | Draw one card, handle ace, append to hand |
| `validate_ace(hand)` | Return `11` or `1` based on current hand total |
| `calculate_score(hand)` | Return `sum(hand)` |
| `display_state(...)` | Print current or final hand state |
| `check_winner(...)` | Compare scores and print result |
| `play_round()` | Orchestrate one full round of the game |

---