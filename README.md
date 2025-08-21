File Read & Write Challenge + Error Handling Lab
📌 Objective
This project demonstrates how to work with file handling and error handling in Python.
It reads a file provided by the user, modifies the content, and writes the result to a new file while handling common errors gracefully.

🛠 Features
✅ Reads an existing file

✅ Modifies the file content (example: converts all text to uppercase)

✅ Writes the modified content into a new file (modified_<filename>)

✅ Handles common file errors:

File not found

Permission denied

Unexpected runtime errors

📂 Files
main.py → Contains the Python program

README.md → Documentation for the assignment

💻 How to Run
Save the code in a file named main.py.

Open a terminal/command prompt.

Run the script:

bash
Copy
Edit
python main.py
Enter the filename you want to read (e.g., notes.txt).

🔎 Example Usage
Input
Suppose you have a file notes.txt with the content:

bash
Copy
Edit
Hello world!
This is a test file.
Program Run
pgsql
Copy
Edit
Enter the filename to read: notes.txt
✅ File read successfully!
✅ Modified content written to 'modified_notes.txt'
Output File (modified_notes.txt)
css
Copy
Edit
HELLO WORLD!
THIS IS A TEST FILE.
📖 Concepts Practiced
File Handling → open(), read(), write(), with statements

Error Handling → try-except blocks with specific error types

String Manipulation → Transforming file content

Code Organization → Using functions for reusability

✨ This assignment shows how Python can safely handle file input/output while ensuring the program doesn’t crash when errors occur.
