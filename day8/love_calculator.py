"""
Love Calculator
---------------
Calculates a love score between two names.

Rules:
- Count letters of 'TRUE' across both names combined
- Count letters of 'LOVE' across both names combined
- Concatenate both counts as a string → love score

Example:
    name1 = "Kanye West", name2 = "Kim Kardashian"
    TRUE count → 4, LOVE count → 9 → score = "49"

Key concepts:
- Nested for loops
- str.upper().count() for case-insensitive matching
- str concatenation with += 
- Positional arguments
"""

def calculate_love_score(name1, name2):
    love_score = ''
    words = ['TRUE', 'LOVE']
    for word in words:
        match_count = 0
        for i in word:
            match_count += name1.upper().count(i) + name2.upper().count(i)
        love_score += str(match_count)
    print(love_score)

calculate_love_score("Kanye West", "Kim Kardashian")