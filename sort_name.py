def sort_names_in_file(file_path):
    """
    Sorts the names in a .dat file in alphabetical order and writes the sorted names back to the file.

    Args:
        file_path (str): The path to the .dat file.
    """
    try:
        # Open the file in read mode and read all the lines into a list
        with open(file_path, 'r') as file:
            names = file.read().splitlines()

        # Sort the names in alphabetical order
        names.sort()
        print('Alphabetically sorted names from file: ', names)

        # Open the file in write mode and write the sorted names back to the file
        with open(file_path, 'w') as file:
            file.write('\n'.join(names).strip())

        # Print a success message
        print(f"Names in {file_path} have been sorted and written back to the file.")

    # Handle the case where the file is not found
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        exit(1)

    # Handle any other exceptions that may occur
    except Exception as e:
        # Print an error message with the exception details
        print(f"An error occurred: {e}")
        exit(1)


if __name__ == '__main__':
    # Prompt the user to enter the file path and call the sort_names_in_file function
    sort_names_in_file(file_path=input('Enter file path that takes ".dat" file: '))
