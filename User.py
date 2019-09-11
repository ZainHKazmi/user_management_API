Class User:
    def __init__(self):
        self.is_logged_in = False
        self.is_admin = False

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

