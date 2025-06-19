import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if len(args) < 1:
        print("No arguments provided.")
        print('\nUsage: python3 main.py "What is the meaning of life?"')
        print('\nFlags available: "--verbose"')
        sys.exit(1)

    load_dotenv()

    

    user_prompt = " ".join(args)
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
    verbose_flag(response)


def verbose_flag(response):
    if "--verbose" in sys.argv:
        print("User prompt: ", sys.argv[1])
        print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
        print("Response tokens: ", response.usage_metadata.candidates_token_count)


if __name__ == "__main__":
    main()