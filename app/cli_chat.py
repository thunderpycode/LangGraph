# from langgraph_config import build_graph

# def main():
#     graph = build_graph()
#     print("Chatbot is ready! Type 'exit' to quit.")

#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ("exit", "quit"):
#             break

#         try:
#             response = graph.invoke({"input": user_input})
#             print("Bot:", response.get("output") or response)
#         except Exception as e:
#             print("Error:", str(e))

# if __name__ == "__main__":
#     main()

from langgraph_config import build_graph

def main():
    graph = build_graph()
    print("Chatbot is ready! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ("exit", "quit"):
            break

        try:
            result = graph.invoke({"input": user_input})
            print("Bot:", result.get("output") or result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
