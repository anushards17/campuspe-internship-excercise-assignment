#  API Configuration
from groq import Groq

# Set API Key
client = Groq(api_key="")


# Query Function
def ask_ai(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Error: {e}"


#  Main Execution
if __name__ == "__main__":
    user_input = input("Enter your question: ")
    result = ask_ai(user_input)
    print("\nAI Response:\n", result)
