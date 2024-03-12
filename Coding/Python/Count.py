import os

def count_letters_and_numbers_in_file(filename):
   """Counts the number of letters and numbers in a text file.

   Args:
       filename (str): The name of the text file to analyze.

   Returns:
       tuple: A tuple containing the count of letters and numbers found in the file.
   """

   try:
       with open(filename, 'r') as file:
           text = file.read()

           # Count letters and numbers using generator expressions
           letter_count = sum(char.isalpha() for char in text)
           number_count = sum(char.isdigit() for char in text)

           return letter_count, number_count

   except FileNotFoundError:
       print(f"Error: The file '{filename}' was not found.")
       return 0, 0

# Get the current working directory
current_directory = os.getcwd()

# Prompt the user to enter the name of the text file
filename = input("Enter the name of the text file to analyze: ")

# Construct the full path to the file
full_path = os.path.join(current_directory, filename)

# Count the letters and numbers
letter_count, number_count = count_letters_and_numbers_in_file(full_path)

# Print the result
print(f"The text file '{filename}' contains {letter_count} letters and {number_count} numbers.")
total_count = letter_count + number_count
print(f"The total number of letters and numbers is {total_count}.")

# Keep the terminal open
input("Press Enter to exit...")
