import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    working_dir = os.path.abspath(working_directory)
    target_dir = working_dir

    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))

    if not target_dir.startswith(working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    try:
        contents = []
        for item in os.listdir(target_dir):
            filepath = os.path.join(target_dir, item)
            contents.append(f"- {item}: file_size={int(os.path.getsize(filepath))} bytes, is_dir={os.path.isdir(filepath)}")
        return "\n".join(contents)
    except Exception as e:
        return f"Error: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
