Day 2 — Data Types, Type Casting & String Formatting
📚 Concepts Learned
1. Primitive Data Types - int, float, str, bool — basic building blocks of Python
2. Type Checking - Using type() to check the data type of a variable
3. Type Casting - Converting between types using int(), float(), str()
4. Mathematical Operations - +, -, *, /, // (floor div), % (modulo), ** (power)
5. String Formatting - (%)Old style formatting — avoided in modern Python
   String Formatting - (.format()) Better style using placeholders
   f-Strings - Modern and preferred — f"Hello {name}"
6. round() - Rounds a float to given decimal places — uses Banker's Rounding

📝 Task
Tip Calculator
- Ask user for total bill amount, tip percentage and number of people
- Calculate and print each person's share including tip, rounded to 2 decimal places

Test Case:
Input : Bill = $150, Tip = 12%, People = 3
Output: Each person should pay: $56.0

💡 Key Takeaways
- Always use float() for money/bill inputs — handles decimals like $150.50
- Python's round() uses Banker's Rounding — rounds to nearest even number when exactly at 0.5
- f-strings are the modern, cleanest way to format strings in Python