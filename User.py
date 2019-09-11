Class User:
    def __init__(self,is_admin):
        self.is_logged_in = False
        self.is_admin = is_admin

    def make_user_admin(self, other):
        if self_admin == true:
            other.admin = True
        else:
            print("admin privelages required")

    def login(self):
        self.is_logged_in = True

    def log_out(self):
        self.is_logged_in = False
    
    def logout_other_user(self, other):
        if self_admin == True:
            if other.is_logged_in == False:
                print("user is already logged out")
            else:
                other.is_logged_in = False
        else:
            print("admin privelages requires")
    
    def login_other_user(self, other):
        if self_admin == True:
            if other.is_logged_in == True:
                print("user is already logged in")
            else:
                other.is_logged_int = True
        else:
            print("admin privelages required")

    def get_role(self):
            print(str(self.is_admin))

if __name__ == "__main__":
    user1 = user(True)
    user2 = user(False)
    user1.make_user_admin(user2)
    user1.get_role()
    user2.get_role()
