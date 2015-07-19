__author__ = 'yagel'


class UserCreds:
    def __init__(self, username, password, current_IP, last_IP, current_login_at, last_login_at):
        self.username = username
        self.password = password
        self.current_IP = current_IP
        self.last_IP = last_IP
        self.current_login_at = current_login_at
        self.last_login_at = last_login_at

    def login(self):
        pass
        # TODO: Implement this method.

    def register(self):
        pass
        # TODO: Implement this method.
