# Day 3 — Control Flow & Logical Operators

## 📚 Concepts Learned

| Concept | Description |
|---|---|
| **if / else** | Execute code based on a condition |
| **elif** | Check multiple conditions in sequence |
| **Nested if** | if/else inside another if/else block |
| **Multiple if** | Independent conditions checked separately |
| **Comparison Operators** | `==`, `!=`, `>`, `<`, `>=`, `<=` |
| **Logical Operators** | `and`, `or`, `not` — combine multiple conditions |
| **Chained Comparison** | Python unique — `12 <= age <= 18` instead of `age >= 12 and age <= 18` |

---

## 📝 Tasks

### 1. Even or Odd Exercise
- Take a number from user and determine if it is even or odd
- Uses modulo operator `%` from Day 2
- 📄 [even_or_odd.py](./even_or_odd.py)

**Test Case:**
```
Input : 34
Output: The number 34 is an even number
```

---

### 2. Rollercoaster Ticket Pricing
- Check height eligibility for ride
- Calculate ticket price based on age category
- Optional photo package adds $3
- Handles free ride for age >= 45
- 📄 [rollercoaster_ticket.py](./rollercoaster_ticket.py)

**Ticket Pricing:**
```
Height < 120cm  → Not eligible
Age < 12        → $5  (Child)
Age 12–18       → $7  (Youth)
Age 19–44       → $12 (Adult)
Age >= 45       → Free ride
Photo package   → +$3 (optional)
```

**Test Case:**
```
Input : Height = 150, Age = 25, Photo = 1
Output: The final ticket price is $15
```

---

## 💡 Key Takeaways
- Python supports chained comparisons: `12 <= age <= 18` — cleaner than using `and`
- Always initialize variables like `ticket_price = 0` before conditional assignments
- Nested if/else helps handle multi-level decision logic cleanly