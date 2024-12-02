# This file handles the storage of names in a list and a text file.

# File path to store names
FILE_PATH = "names.txt"

def save_name(name: str):
    """
    Save the provided name to a text file and print the current names list.
    """
    # Append the name to the text file
    with open(FILE_PATH, "a") as file:
        file.write(name + "\n")
    print(f"Name '{name}' has been added to {FILE_PATH}")
