import os

def get_file_content(working_directory, file_path):
    working_dir = os.path.abspath(working_directory)
    file = os.path.abspath(os.path.join(working_directory, file_path))

    if not file.startswith(working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    MAX_CHARS = 10000
    
    try:
        with open(file, "r") as f:
            file_content_string = f.read()
            if len(file_content_string) > MAX_CHARS:
                return file_content_string[:MAX_CHARS] + f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string
    except Exception as e:
        return f"Error: {e}"