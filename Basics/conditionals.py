# If statement
a = 20
b = 25
if b > a:
    print("b is greater than a")

# If-else statement 
# Python uses elif for else-if
x = 45
y = 45
if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

# Else statement
# If none of the cases is true then else is executed
m = "a"
n = "c"
if n == m:
    print("m is equal to n")
elif m > n:
    print("m is greater than n")
else:
    print("They are not equal")

# Short hand if-else
p = 10
q = 20
print("q is greater than p") if q > p else print("p is greater than q")
# short hand if-else with 3 conditions
print("p") if p > q else print("=") if p == q else print("q")

# AND operator
if p < q and q>p:
    print("q is greater than p")

# OR operator
if p > q or q > p:
    print("Pass")

# Pass operator
# used to avoid error when if statement is empty for some reason
if p < q: # Empty if throws error
     pass

# Nested if
if q > 5: 
    print("q is greater than 5")
    if q > 10:
        print("q is also greater than 10")
        if q > 15:
            print("q is also greater than 15")