import os
import subprocess

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
        output.append(f"STDOUT: {result.stdout.strip()}")
        output.append(f"STDERR: {result.stderr.strip()}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output)
    
    except Exception as e:
        return f"Error: executing Python file: {e}"