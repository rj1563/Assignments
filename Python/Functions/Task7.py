# 7. Combining Lambda and Functions
        # Write a function analyze_numbers that:
        # Takes a list of integers as input.
        # Uses map() with a lambda function to square each number.
        # Uses filter() with a lambda function to keep only numbers greater than 50 after squaring.
        # Returns the filtered list

# Function to filter an input list
def analyze_numbers(input_list):
    squared_list = list(map(lambda x: x**2, input_list))  # Squaring each number in the list
    filtered_list = list(filter(lambda x: x > 50, squared_list)) # Filtering the list such that it contains the numbers > 50
    return filtered_list

# Function call
print("Filtered List: ", analyze_numbers([9, 10, 11, 12]))