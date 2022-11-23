from users.user import User
from chats.chat import Chat


class PrivateChat(Chat):
    """

    Class PrivateChat

    """
    def __init__(self, chat_id: int, member1: User, member2: User):
        super().__init__(chat_id)
        self.users_chatting.append(member1, member2)

    def post_message(self, messsege: str):
        self.users_messeges.append(messsege)
