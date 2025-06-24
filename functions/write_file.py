import os

def write_file(working_directory, file_path, content):
    working_dir = os.path.abspath(working_directory)
    file = os.path.abspath(os.path.join(working_directory, file_path))

    if not file.startswith(working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        dir_name = os.path.dirname(file)
        if dir_name:  # only make dirs if there actually is a dir part
            os.makedirs(dir_name, exist_ok=True)

        with open(file, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
