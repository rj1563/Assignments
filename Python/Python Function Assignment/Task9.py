# 9. Data Transformation
        # Given the following data:
        # data = [
        # {"name": "Alice", "age": 30, "score": 85},
        # {"name": "Bob", "age": 25, "score": 90},
        # {"name": "Charlie", "age": 35, "score": 95}]
        # Use a combination of map() and lambda functions to:
        # Extract the names of all individuals.
        # Calculate the average score of all individuals

# given data
data = [
    {"name": "Alice", "age": 30, "score": 85},
    {"name": "Bob", "age": 25, "score": 90},
    {"name": "Charlie", "age": 35, "score": 95}
]

# Extracting the names of all individuals
names = list(map(lambda x: x["name"], data))
print("Names of all individuals: ", names)

# Calculating the average score of all individuals
average_score = sum(list(map(lambda x: x["score"], data))) / len(data) 
print("The average score of all individuals is: ", average_score)