import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    if len(sys.argv) < 2:
        print("No arguments provided.")
        sys.exit(1)

    load_dotenv()

    user_prompt = " ".join(sys.argv[1:])
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]    

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )

    generate_response(client, messages)


def generate_response(client, messages):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()