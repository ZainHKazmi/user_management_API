class register:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.password_min_len = 7
    def password_verification(self):
        ##TODO: implement password_verification
        lowercase_alphabets = 'abcdefghijklmnopqrstuvwxyz'
        uppercase_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '1234567891'
        special_charachters = '@#$%^&*()+_-!.'
        has_lowercase = False
        has_uppercase = False
        has_numbers = False
        has_special_charachters = False
        for i in lowercase_alphabers:
            if i in self.password:
                has_lowercase = True
                break
        for i in uppercase_alphabets:
            if i in self.password:
                has_uppercase = True
                break
        for i in numbers:
            if i in self.password:
                has_numbers = True
                break
        for i in special_charachters:
            if i in self.password:
                has_special_charachters = True
                break
        return has_numbers and has_special_charachters and has_uppercase and\
                has_lowercase and (len(self.password) > self.password_min_len)


    def check_username(self):
        ##TODO: Implement username check
        pass

    def register_user(self):
        ##TODO: Implement username check
        pass

    if __name__ == "__main__":
        pass
