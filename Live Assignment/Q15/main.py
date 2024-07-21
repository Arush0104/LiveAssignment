from file_operations import read_file, write_file, append_file

file_path = 'example.txt'

# Writing to the file
write_message = "Hello, world!"
write_result = write_file(file_path, write_message)
print(write_result)

# Appending to the file
append_message = "\nAppending a new line."
append_result = append_file(file_path, append_message)
print(append_result)

# Reading from the file
content = read_file(file_path)
print("File content:")
print(content)
