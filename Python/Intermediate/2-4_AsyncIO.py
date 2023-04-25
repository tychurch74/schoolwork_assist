"""
AsyncIO is a library to write concurrent code using the async/await syntax.
In other words, it allows us to write code that runs at the same time in Python.
"""

import asyncio

async def function1(large_list_of_text):
    print("Summarizing large list of text...")
    await asyncio.sleep(2)  # Simulate time-consuming task
    summary = "summary"
    print("Summary ready.")
    return summary

async def function2(summary, question):
    print(f"Using summary '{summary}' to answer question '{question}'...")
    await asyncio.sleep(2)  # Simulate time-consuming task
    answer = f"Answer for '{question}'"
    print(f"Answer ready: {answer}")
    return answer

async def function3(prompt):
    print(prompt)
    await asyncio.sleep(0.5)
    question = input()
    return question

async def main():
    large_list_of_text = []  # Your large list of text
    summary = await function1(large_list_of_text)

    while True:
        question = await function3("Enter a question (or type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        # Run function2
        chatbot_answer = await function2(summary, question)
        
        # Update the large list of text
        await update_large_list_of_text(large_list_of_text, chatbot_answer)
        
        # Update the summary
        summary = await function1(large_list_of_text)
        
        await function3(f"Chatbot's answer: {chatbot_answer}\n")

async def update_large_list_of_text(large_list_of_text, chatbot_answer):
    await asyncio.sleep(0.5)
    large_list_of_text.append(chatbot_answer)
    print(f"Updated large list of text: {large_list_of_text}")

if __name__ == "__main__":
    asyncio.run(main())


