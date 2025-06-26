import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'
    if not target_file[-3:] == ".py":
        f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(["python3", target_file],
                                timeout=30,
                                capture_output=True,
                                cwd=working_dir,
                                text=True)
        
        if not result.stdout and not result.stderr:
            return "No output produced."
        
        output = []
        output.append(f"STDOUT:\n{result.stdout.strip()}")
        output.append(f"STDERR:\n{result.stderr.strip()}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output)
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file and returns its standard output and error messages, if any.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to run, relative to the working directory.",
            ),
        },
    ),
)