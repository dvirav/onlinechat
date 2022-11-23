from chats.group_chat import GroupChat
from chats.private_chat import PrivateChat
from users.user import User
from users.user_service import UserService

user_service = UserService()

user1 = User("Dvir", 1)
user_service.add_user(user1)
user2 = User("Matan", 2)
user_service.add_user(user2)
user3 = User("Ayellet", 3)
user_service.add_user(user3)
user4 = User("Maayan", 4)
user_service.add_user(user4)
user5 = User("Yair", 5)
user_service.add_user(user5)

user_service.add_friend_request(1, 2)
user2.handle_request()
print(user1.user_friends, user2.user_friends)
print(user1.user_requests, user2.user_requests)
