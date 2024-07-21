
def read_file(file_path):
    """Read and return the content of the file."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return str(e)

def write_file(file_path, data):
    """Write data to a file. Overwrite if the file already exists."""
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        return "Write operation successful."
    except Exception as e:
        return str(e)

def append_file(file_path, data):
    """Append data to a file. Create the file if it does not exist."""
    try:
        with open(file_path, 'a') as file:
            file.write(data)
        return "Append operation successful."
    except Exception as e:
        return str(e)
