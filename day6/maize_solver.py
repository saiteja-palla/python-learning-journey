"""
Reeborg's World — Hurdle 4 Maze Solver
-------------------------------------
Solves a maze using the right-hand wall follower algorithm.

Rules:
- Reeborg must reach the goal without hitting walls
- No built-in turn_right() exists — must create it manually
- Always try to turn right first (hug the right wall)
- If wall on right → go straight
- If wall in front → turn left
- Repeat until at_goal()

Key concepts:
- def to create custom turn_right() function
- while loop to keep moving until goal
- Nested if/else for wall checking logic
- Boolean conditions: not, at_goal(), wall_on_right(), wall_in_front()
"""

# --- Mock Reeborg functions ---
def turn_left():
    print("Turned left")

def move():
    print("Moved forward")

def at_goal():
    return False  # change to True to stop the loop

def wall_on_right():
    return False  # simulate wall conditions

def wall_in_front():
    return False

# --- My Function to turn right ---
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    else:
        if wall_in_front():
            turn_left()
        else:
            move()