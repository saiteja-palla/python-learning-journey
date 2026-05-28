# Day 8 — Functions with Inputs & Caesar Cipher


## 📚 Concepts Learned

| Concept | Description |
|---|---|
| Function parameters | `def func(param1, param2)` |
| Positional arguments | Order matters — `func(a, b)` |
| Keyword arguments | `func(name="Sai", age=25)` |
| Default parameters | `def func(name, age=20)` |
| `*args` arbitrary args | Accept any number of arguments |
| `str.count()` | Count occurrences of char in string |
| `list.index()` | Returns position of item in list |
| `enumerate()` | Loop with index + value together |
| `% 26` wrap-around | Modulo for circular index logic |
| Parameter vs Argument | Parameter = definition, Argument = actual value passed |

---

## 💑 Exercise 1 — Love Calculator

Calculates a love score between two names based on letter matches.
- 📄 [love_calculator.py](./love_calculator.py)


## 📅 Exercise 2 — Life in Weeks

Calculates weeks remaining in life based on age.
- 📄 [life_in_weeks.py](./life_in_weeks.py)


## 🔐 Project — Caesar Cipher

Classic encryption algorithm — shifts letters by a fixed number.
- 📄 [caesar_cipher.py](./caesar_cipher.py)

---

## 💡 Key Takeaways

- **Parameter vs Argument** — parameter is the variable in `def`, argument is the value passed when calling
- **Default parameters** — `def func(name, age=20)` — age is optional when calling
- **`% 26` is always cleaner** than manual boundary checks for wrap-around logic
- **`enumerate()`** gives both index and value — avoids manual counter variable
- **`str.count()`** counts ALL occurrences of a substring — not just first match
- **`list.index()`** returns position number — not True/False!

---

## 🔜 Coming Up — Day 9

- Dictionaries
- Nesting — dictionaries inside lists, lists inside dictionaries
- Blind Auction project

---

*Part of the 100 Days of Python → Git → Docker → CI/CD → Azure → ML/AI roadmap*