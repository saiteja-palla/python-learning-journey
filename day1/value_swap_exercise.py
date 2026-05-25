"""
Value Swapping Exercise
-----------------------
Swap the contents of two variables without typing the actual values directly.
 
Test Case:
    Before : glass1 = milk, glass2 = juice
    After : glass1 = juice, glass2 = milk
"""
 
glass1 = "milk"
glass2 = "juice"

print("Before swap: glass1 = " + glass1 + ", glass2 = " +glass2)

# Method 1: Using a temporary variable
temp = glass1
glass1 = glass2
glass2 = temp
 
print("After swap (temp variable): glass1 = " + glass1 + ", glass2 = " +glass2)
 
# Reset
glass1 = "milk"
glass2 = "juice"
 
# Method 2: Python one-liner swap
glass1, glass2 = glass2, glass1
 
print("After swap (one-liner): glass1 = " + glass1 + ", glass2 = " + glass2)