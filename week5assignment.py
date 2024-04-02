# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("2nd line: 12345\n")
        file.write("Another line here.\n")
    print("File 'my_file.txt' created successfully and content written.")
except Exception as e:
    print("Error occurred:", e)
finally:
    print("File creation process completed.\n")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        file_content = file.read()
        print("Content of 'my_file.txt':\n", file_content)
except FileNotFoundError:
    print("File 'my_file.txt' not found.")
except PermissionError:
    print("Permission denied to read the file.")
except Exception as e:
    print("Error occurred:", e)
finally:
    print("File reading process completed.\n")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Additional line 1\n")
        file.write("Line 5: New content\n")
        file.write("Appending another line.\n")
    print("Content appended to 'my_file.txt' successfully.")
except Exception as e:
    print("Error occurred:", e)
finally:
    print("File appending process completed.\n")
