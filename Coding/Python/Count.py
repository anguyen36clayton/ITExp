import os

def count_letters_in_file(filename):
   """Counts the number of letters in a text file, excluding spaces.

   Args:
       filename (str): The name of the text file to analyze.

   Returns:
       int: The total number of letters found in the file.
   """

   try:
       with open(filename, 'r') as file:
           text = file.read()

           # Efficiently count letters using a generator expression
           letter_count = sum(char.isalpha() for char in text)

           return letter_count

   except FileNotFoundError:
       print(f"Error: The file '{filename}' was not found.")
       return 0

# Get the current working directory
current_directory = os.getcwd()

# Prompt the user to enter the name of the text file
filename = input("Enter the name of the text file to analyze: ")

# Construct the full path to the file
full_path = os.path.join(current_directory, filename)

# Count the letters and print the result
letter_count = count_letters_in_file(full_path)

if letter_count > 0:
   print(f"The text file '{filename}' contains {letter_count} letters.")

# Keep the terminal open
input("Press Enter to exit...")
