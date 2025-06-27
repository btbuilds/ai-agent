import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    working_dir = os.path.abspath(working_directory)
    file = os.path.abspath(os.path.join(working_directory, file_path))

    if not file.startswith(working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(file, "r") as f:
            content = f.read(MAX_CHARS)
            if os.path.getsize(file) > MAX_CHARS:
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
        return content
    except Exception as e:
        return f"Error: {e}"
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the content of a specified file, truncated to a maximum of 10,000 characters for safety and performance.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory.",
            ),
        },
    ),
)