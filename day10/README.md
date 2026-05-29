# Day 10 — Functions with Output, Return & Docstrings
---

## 📚 Concepts Learned

| Concept | Description |
|---|---|
| `return` | Function output — return value to caller |
| `return` vs `print` | `return` reusable, `print` only displays |
| Docstrings `"""..."""` | Document what a function does |
| Nested functions | Function inside a function |
| Functions as variables | Store function reference in variable/dict |
| `str.title()` | Capitalize first letter of each word |
| Multiple return values | `return val1, val2` |

## 🧮 Exercise — Leap Year Finder

Determines whether a given year is a leap year.
- 📄 [leap_year_finder.py](./leap_year_finder.py)

### Rules
- year % 4 == 0   → potential leap year
- year % 100 == 0 → not a leap year (century year)
- year % 400 == 0 → is a leap year (exception to century rule)

## 🧮 Project — Calculator

Full calculator with functions stored in a dictionary — continues with previous result.
- 📄 [calculator.py](./calculator.py)

### Rules
- User enters first number
- Choose operation: `+`, `-`, `*`, `/`
- Enter second number
- Result shown — option to continue with result or exit
- Functions stored in dictionary — called dynamically

## 💡 Key Takeaways

- Always use `return` instead of `print` inside functions — makes value reusable
- **Docstrings** go right after `def` line — `help(func)` తో చూడొచ్చు
- Functions stored in dict → dynamic calling possible — very powerful pattern!
- Nested functions — inner function only accessible inside outer function
- `title()` — each word first letter capitalize — name formatting కి useful

---