__author__ = 'yagel'
from dvir_methods_suggs import has_inf
from dvir_methods_suggs import c


class UserCreds:
    def __init__(self, username, password, current_IP, last_IP, current_login_at, last_login_at):
        self.username = username
        self.password = password
        self.current_IP = current_IP
        self.last_IP = last_IP
        self.current_login_at = current_login_at
        self.last_login_at = last_login_at

    # def login(self):
    #     pass
    #     # TODO: Implement this method.
    #
    # def register(self):
    #     pass
    #     # TODO: Implement this method.
    #
    # # suggestions by dvir
    #
    # def register_dvir(self, use, pas, email, nick, ver, ans):
    #     if not has_inf("username", "Users", use) and not has_inf("email", "Users", email) and not has_inf("nickname",
    #                                                                                                       "Users",
    #                                                                                                       nick):
    #         c.execute(
    #             "INSERT INTO Users VALUES ('" + nick + "','" + email + "','','','" + use + "','" + pas + "',False,'" + ver + "','" + ans + "')")
    #
    # def register_dvir(self, use, pas, email, fname, lname, nick, ver, ans):
    #     if not has_inf("username", "Users", use) and not has_inf("email", "Users", email) and not has_inf("nickname",
    #                                                                                                       "Users",
    #                                                                                                       nick):
    #         c.execute(
    #             "INSERT INTO Users VALUES ('" + nick + "','" + email + "','" + fname + "','" + lname + "','" + use + "','" + pas + "', False,'" + ver + "','" + ans + "')")
