
# 1. API CONFIGURATION


import cohere
from groq import Groq

print("🔥 PROGRAM STARTED")

#API keys
COHERE_API_KEY = ""
GROQ_API_KEY = ""

# Initialize clients
co = cohere.Client(COHERE_API_KEY)
groq_client = Groq(api_key=GROQ_API_KEY)

# 2. QUERY FUNCTIONS

def query_cohere(prompt):
    try:
        response = co.chat(message=prompt)
        return response.text
    except Exception as e:
        return f"❌ Cohere Error: {e}"


def query_groq(prompt):
    try:
        response = groq_client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Groq Error: {e}"


# 3. MAIN EXECUTIONs

def main():
    print("=== Multi-API AI Assistant 🤖 ===")

    while True:
        print("\n1. Cohere")
        print("2. Groq")
        print("3. Exit")

        choice = input("Choose (1/2/3): ")

        if choice == "3":
            print("Bye 👋")
            break

        prompt = input("Enter your question: ")

        if choice == "1":
            print("\nAI (Cohere):")
            print(query_cohere(prompt))

        elif choice == "2":
            print("\nAI (Groq):")
            print(query_groq(prompt))

        else:
            print("❌ Invalid choice")

# RUN PROGRAM
if __name__ == "__main__":
    main()