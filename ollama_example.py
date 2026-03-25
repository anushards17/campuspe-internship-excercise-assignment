import ollama

client = ollama

def query_api(prompt):
    try:
        response = client.chat(
            model="gemma:2b",   # 👈 WRITE HERE
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response['message']['content']

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying API...")

    result = query_api(user_prompt)

    print("Response:")
    print(result)
