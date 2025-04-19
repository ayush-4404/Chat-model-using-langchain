from langchain_google_genai import ChatGoogleGenerativeAI as genAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage,AIMessage
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
model=genAI(model="gemini-1.5-pro")


load_dotenv()
chat_history = []

SystemMessage=SystemMessage(content="You are an helpful AI assistant")
chat_history.append(SystemMessage)


# setup firebaqse firestore
PROJECT_ID = "langchain-e296e"
SESSION_ID = "user_session_new" #this could be a username or a unique id
COLLECTION_NAME = "chat_history"

#initialising firestore client
print("initialising firestore client")
client=firestore.Client(project=PROJECT_ID)

#initialising firestore chat message history
print("initialising firestore chat message history")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)
print("chat history initialised")
print("current chat history: ", chat_history.messages)

#initialising the model

#chat loop
while True:
    query=input("You: ")
    if query.lower() == "exit":
        break
    chat_history.add_user_message(query)

    result = model.invoke(chat_history.messages)
    response=result.content
    chat_history.add_ai_message(response)
    print("AI: ", response)


    # print("Chat History:")
    # print(chat_history)