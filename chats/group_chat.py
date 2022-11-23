from users.user import User
from chats.chat import Chat


class GroupChat(Chat):
    """

    Class GroupChat

    """
    def __init__(self, chat_id: int, *args):
        super().__init__(chat_id)
        for arg in args:
            self.users_chatting.append(arg)

    def post_message(self, messsege:str):
        self.users_messeges.append(messsege)

    def add_user(self, member: User):
        self.users_chatting.append(member)
