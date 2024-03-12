Count letter 
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

# Get the filename from the user
filename = input("Enter the name of the text file: ")

# Count the letters and print the result
letter_count = count_letters_in_file(filename)

if letter_count > 0:
   print(f"The text file '{filename}' contains {letter_count} letters.")