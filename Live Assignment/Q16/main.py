from file_operations import read_file, write_file, append_file

file_path = 'Q16/employees.txt'
info = """
1)Name: Jane Doe
  Age: 23
  ID: 1000
2)Name: John Doe
  Age: 25
  ID: 1200
"""
write_message = info
write_result = write_file(file_path, write_message)
print(write_result)