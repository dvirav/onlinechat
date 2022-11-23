class User(object):
    """
    Class user

    """

    def __init__(self, name=str, user_id=int):
        self.name = name
        self.user_id = user_id
        self.user_friends = []
        self.user_requests = []

    def update_user_name(self, name):
        self.name = name

    def handle_request(self):
        for request in self.user_requests:
            handle = input(f"type APPROVE / DENY for {request}")
            if handle == "APPROVE":
                self.user_friends.append(request)
                request.user_friends.append(self)
                self.user_requests.remove(request)
                print('approved')
            elif handle == "DENY":
                self.user_requests.remove(request)
                print('denied')

            else:
                raise ValueError('Valid values are APPROVE / DENY')

    def __str__(self):
        return f"User {self.name}, {self.user_id}."
