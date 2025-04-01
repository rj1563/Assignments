# 3. Recursive Function
        # Write a recursive function fibonacci that generates the nth Fibonacci number.
        # Test the function for inputs 10, 15, and 20.
        # Bonus: Optimize the function using memoization (e.g., with functools.lru_cache)

from functools import lru_cache

@lru_cache(maxsize=None) # Optimizing the function using memoization 

# Recursive function that generates the nth Fibonacci number.
def fibonacci(n): 
    # base case
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# Function call
print(f"Fibonacci Number at position 10: ",fibonacci(10))
print(f"Fibonacci Number at position 15: ",fibonacci(15))
print(f"Fibonacci Number at position 20: ",fibonacci(20))