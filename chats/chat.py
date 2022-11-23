from abc import ABC, abstractmethod


class Chat(ABC):
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.users_chatting = []
        self.users_messeges = []

    @abstractmethod
    def post_message(self, messege: str):
        pass

    def display_messages(self):
        for i in self.users_messages:
            print(i)
