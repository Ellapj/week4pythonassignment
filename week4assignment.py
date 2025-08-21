# File Read & Write Challenge + Error Handling Lab

def modify_file_content(content: str) -> str:
    """
    Takes the original file content and returns a modified version.
    Here we simply convert text to uppercase as an example.
    """
    return content.upper()


def process_file():
    # Ask the user for the filename
    filename = input("Enter the filename to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r") as infile:
            content = infile.read()
            print("\n✅ File read successfully!")

        # Modify the content (example: convert to uppercase)
        modified_content = modify_file_content(content)

        # Create a new output file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# Run the program
process_file()
