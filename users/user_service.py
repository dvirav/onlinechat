from users.user import User


def find_user_by_id(user_service, custom_id: int):
    for u in user_service.user_list:
        if u.user_id == custom_id:
            return u


class UserService(object):
    """

    Class UserService - manage all the users

    """
    user_list = []

    def add_user(self, user=User):
        self.user_list.append(user)

    def remove_user(self, user=User):
        try:
            self.user_list.remove(user)
        except:
            print('no such user')

    def add_friend_request(self, user_id_followee: int, user_id_follower: int):
        followee = find_user_by_id(self, user_id_followee)
        follower = find_user_by_id(self, user_id_follower)
        follower.user_requests.append(followee)

    def remove_from_friends(self, user_id_unfollowee: int, user_id_unfollower: int):
        unfollowee = find_user_by_id(self, user_id_unfollowee)
        unfollower = find_user_by_id(self, user_id_unfollower)
        unfollower.user_friends.remove(unfollowee)
        unfollowee.user_friends.remove(unfollower)
