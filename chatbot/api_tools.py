from langchain.tools import tool
import requests

BASE_URL = "http://127.0.0.1:8000"  # URL base do servidor FastAPI

@tool
def read_root():
    """
    Fetch the root message from the API.

    Returns:
        dict: A dictionary containing the root message.
    """
    response = requests.get(f"{BASE_URL}/message")
    return response.json()

@tool
def create_message(user: str, message: str):
    """
    Creates a message by sending a POST request to the specified endpoint.
    Args:
        user (str): The username of the user creating the message.
        message (str): The content of the message to be created.
    Returns:
        dict: A dictionary containing the response from the server. If the message
        creation is successful, the response will contain the created message data.
        Otherwise, it will contain an error message.
    """
    response = requests.post(f"{BASE_URL}/message", json={"user": user, "message": message})
    
    if response.status_code == 201:
        return response.json()
    else:
        # return the error
        return response.json()

@tool
def read_messages():
    """
    Fetch all messages from the API.

    Returns:
        dict: A dictionary containing a list of messages.
    """
    response = requests.get(f"{BASE_URL}/message/all")
    return response.json()

@tool
def read_message(user_id: int):
    """
    Fetch a specific message by user ID.

    Args:
        user_id (int): The ID of the message to fetch.

    Returns:
        dict: A dictionary containing the message data.
    """
    response = requests.get(f"{BASE_URL}/message/{user_id}")
    return response.json()

# Exemplos de uso:
if __name__ == "__main__":
    # # Teste do endpoint root
    # print(read_root())

    # Criar uma nova mensagem
    #print(create_message(user="John Doe", message = "Hello, FastAPI!AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"))

    # # Buscar todas as mensagens
    # print(read_messages())

    # # Buscar mensagem específica por ID
    # print(read_message(1))
    pass