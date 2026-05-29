# Day 9 — Dictionaries & Nested Collections
---

## 📚 Concepts Learned

| Concept | Description |
|---|---|
| Dictionary `{}` | Key-value pairs — `{"name": "Sai", "age": 25}` |
| Add/update key | `dict[key] = value` |
| Access by key | `dict["name"]` → value |
| `.keys()` | Returns all keys |
| `.values()` | Returns all values |
| Key error | `dict["missing"]` → KeyError |
| Safe access | `dict.get("missing", default)` → no error |
| `for` loop on dict | `for key in dict:` iterates keys |
| `max()` on dict | `max(dict, key=dict.get)` → key with max value |
| Nested dict/list | Dict inside list, list inside dict |

---


## 🏆 Project — Secret Auction

Blind auction system — multiple bidders enter bids, highest bid wins.
- 📄 [secret_auction_program.py](./secret_auction_program.py)

### Rules
- Each bidder enters name and bid amount
- Screen cleared between bidders so others can't see bids
- All bids stored in a dictionary `{name: price}`
- After all bids, find the winner with highest bid
- Winner announced with name and bid amount


## 💡 Key Takeaways

- **Dictionary** — best data structure when you need key → value mapping
- Always use `.get()` instead of `[]` when key might not exist — avoids KeyError
- `for key in dict` iterates over **keys** — use `dict[key]` to get value
- `max(dict, key=dict.get)` — one line to find key with highest value
- `print("\n" * 20)` — simple trick to simulate screen clear in terminal
- Duplicate key in dict → **silently overwrites** — always check with `if name in dict` when needed


