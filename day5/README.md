# Day 5 — For Loops, range(), sum(), join(), random.shuffle()

## 📚 Concepts Learned

| Concept | Description |
|---|---|
| `for` loop | Iterate over a sequence or range |
| `range(start, stop)` | Generate numbers from start to stop-1 |
| `range(start, stop, step)` | Skip numbers — e.g. `range(0,10,2)` = 0,2,4,6,8 |
| `sum()` | Add all items in a list or range |
| `list.append()` | Add item to end of a list |
| `random.shuffle()` | Randomly shuffle a list in place |
| `''.join()` | Convert list of characters → single string |

---

## 🔢 Exercise — FizzBuzz

Classic programming challenge using `for` loop + modulo operator.
- 📄 [fizzbuzz.py](./fizzbuzz.py)

### Rules
- Loop through numbers 1 to 100
- If divisible by both 3 and 5 → print `FizzBuzz`
- If divisible by 3 only → print `Fizz`
- If divisible by 5 only → print `Buzz`
- Otherwise → print the number

## 🔐 Project — Password Generator

Generates a random secure password based on user-defined character counts.
- 📄 [password_generator.py](./password_generator.py)

### Rules
- Ask user how many letters, symbols, and numbers they want
- Randomly pick from each character set using `random.choice()`
- Shuffle the full list using `random.shuffle()` so it's unpredictable
- Join the list into a string using `''.join()` and print

---

## 💡 Key Takeaways

- `for` loop + `range()` is the go-to combo for repeating actions N times
- Always check the **most specific condition first** in if/elif chains (FizzBuzz lesson)
- `random.shuffle()` modifies the list **in place** — no need to assign it back
- `''.join(list)` is the standard Pythonic way to convert character list → string
- Keep character sets as **named lists** for consistency and readability

---