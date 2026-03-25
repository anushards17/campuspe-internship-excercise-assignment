# ==============================
# 1. API CONFIGURATION
# ==============================

import cohere

API_KEY = "wI4BNYOTRv1BKoDq67wdQDI6VOJeMtxNmk6Hp9MN"   
co = cohere.Client(API_KEY)


# ==============================
# 2. QUERY FUNCTION
# ==============================

def query_cohere(prompt):
    try:
        response = co.chat(
            message=prompt   
        )
        return response.text

    except Exception as e:
        return f"❌ Error: {e}"


# ==============================
# 3. MAIN EXECUTION
# ==============================

def main():
    print("=== AI Assistant 🤖 ===")
    print("Type 'exit' to quit")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("Bye 👋")
            break

        answer = query_cohere(user_input)

        print("\nAI:")
        print(answer)


# Run program
if __name__ == "__main__":
    main()