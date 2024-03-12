import os

def count_letters_and_numbers_in_file(filename):
   """Counts the number of letters and numbers in a text file.

   Args:
       filename (str): The name of the text file to analyze.

   Returns:
       int: The total number of letters and numbers found in the file.
   """

   try:
       with open(filename, 'r') as file:
           text = file.read()

           # Count letters and numbers using a generator expression
           letter_and_number_count = sum(char.isalnum() for char in text)

           return letter_and_number_count

   except FileNotFoundError:
       print(f"Error: The file '{filename}' was not found.")
       return 0

# Get the current working directory
current_directory = os.getcwd()

# Prompt the user to enter the name of the text file
filename = input("Enter the name of the text file to analyze: ")

# Construct the full path to the file
full_path = os.path.join(current_directory, filename)

# Count the letters and numbers
count = count_letters_and_numbers_in_file(full_path)

# Print the result
if count > 0:
   print(f"The text file '{filename}' contains {count} letters and numbers.")
else:
   print("No letters or numbers found in the file.")

# Keep the terminal open
input("Press Enter to exit...")
