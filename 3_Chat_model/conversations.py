from langchain_google_genai import ChatGoogleGenerativeAI as genAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import HumanMessage, SystemMessage,AIMessage
model=genAI(model="gemini-1.5-pro")

chat_history = []

SystemMessage=SystemMessage(content="You are an helpful AI assistant")
chat_history.append(SystemMessage)

#chat loop

while True:
    query=input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)
    response=result.content
    chat_history.append(AIMessage(content=response))
    print("AI: ", response)


    # print("Chat History:")
    # print(chat_history)