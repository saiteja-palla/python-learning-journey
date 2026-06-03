# Day 15 — Local Development, pip & Coffee Machine

---

## 📚 Concepts Learned

| Concept | Description |
|---|---|
| Local dev environment | Running Python outside Replit — VS Code + terminal |
| `pip` | Python package manager — `pip install <package>` |
| `if __name__ == "__main__"` | Entry point guard — code runs only when file executed directly, not on import |
| Constants `UPPER_SNAKE_CASE` | Coin values defined as module-level constants — not magic numbers |
| Multi-file project | Logic in `main.py`, data in `data.py` — separation of concerns |
| `dict.get(key)` | Safe dictionary access — returns `None` if key missing instead of `KeyError` |
| `sum()` with list | `sum([a, b, c])` — cleaner than chaining `+` operators |
| `.items()` | Iterate over key-value pairs in a dictionary |

---

## ☕ Project — Coffee Machine

Terminal-based coffee machine simulator with resource tracking, coin processing and change calculation.
- 📄 [coffee_machine.py](./coffee_machine.py)
- 📄 [data.py](./data.py)

### Rules
- User selects `espresso`, `latte`, or `cappuccino`
- Type `report` → print current resource levels and money collected
- Type `off` → shut down machine
- Coins inserted — penny, dime, nickel, quarter
- Not enough coins → refund, no drink dispensed
- Not enough ingredients → inform user, no coins taken
- Exact amount or overpay → drink dispensed, change returned if applicable
- Resources deducted after every successful transaction

### Functions Breakdown

| Function | Responsibility |
|---|---|
| `get_user_choice()` | Prompt user, handle `report`/`off`/invalid input |
| `ask_for_coins()` | Collect coin counts from user — return as tuple |
| `monetory_value(p, d, n, q)` | Calculate total monetary value from coin counts |
| `is_coins_enough(amount, choice)` | Check if inserted amount covers drink cost |
| `process_change(amount, choice)` | Calculate and return change if overpaid |
| `is_resources_sufficient(choice, resources)` | Verify all ingredients available for chosen drink |
| `deduct_resources(drink, resources)` | Subtract used ingredients from resource dict |
| `resources_report(resources)` | Print current water, milk, coffee and money levels |

---

## 💡 Key Takeaways

- **`if __name__ == "__main__"`** — standard Python entry point pattern — prevents code running on import — always use in project files
- **Constants over magic numbers** — `QUARTER = 0.25` is readable, `0.25` scattered in code is not

---