# Stevie Hardy
# 2025-10-29
# P4HW1 Assignment
# This program collects scores, validates them, drops the lowest, calculates average, and assigns a grade.

# Pseudocode:
# 1. Ask user how many scores they want to enter.
# 2. Initialize an empty list to store valid scores.
# 3. Use a loop to collect scores:
#    a. For each score, validate that it's between 0 and 100.
#    b. If invalid, prompt again until a valid score is entered.
#    c. Add valid score to the list.
# 4. After collecting all scores:
#    a. Find and display the lowest score.
#    b. Remove the lowest score from the list.
#    c. Display the modified list.
#    d. Calculate and display the average of the modified list.
#    e. Determine and display the letter grade based on average.
# Ask user how many scores they want to enter

num_scores = int(input("How many scores would you like to enter? "))

# Initialize score list
score_list = []

# Loop to collect valid scores
for i in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score #{i+1}: "))
            if 0 <= score <= 100:
                score_list.append(score)
                break
            else:
                print("Invalid score. Please enter a value between 0 and 100.")
        except ValueError:
                print("Invalid input. Please enter a numeric value.")

# Process scores
lowest_score = min(score_list)
score_list.remove(lowest_score)
average_score = sum(score_list) / len(score_list)

# Determine letter grade
if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'
    
# Display results
print("\nResults:")
print(f"Lowest score dropped: {lowest_score}")
print(f"Modified score list: {score_list}")
print(f"Average of remaining scores: {average_score:.2f}")
print(f"Letter grade: {grade}") 
 