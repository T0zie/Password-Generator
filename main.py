import secrets
import string 

class PwdGen:
    def __init__(self):
        self.letters = string.ascii_letters
        self.digits = string.digits
        self.special_chars = string.punctuation

    def generatePassword(self):
        #get user preference for password length
        while True:
            try:
                pwd_length = int(input("Enter your preferred password length (e.g., 12) "))
                break
            except ValueError:
                print("Value provided is not valid. Please enter a valid integer.")

        #get user preference for special characters
        while True:
            use_punctuation_input = input("Would you like to include special characters in the password? (y/n): ")
            if use_punctuation_input.lower() in ['y','n']:
                use_punctuation = use_punctuation_input.lower() == 'y'
                break
            else: 
                print("Invalid Response. Please enter 'y' for yes or 'n' for no.")
        alphabet = self.letters + self.digits
        if use_punctuation:
            alphabet += self.special_chars

        pwd = ''
        for _ in range(pwd_length):
            pwd += secrets.choice(alphabet)

        return pwd 
    
generator = PwdGen()

password = generator.generatePassword()
print("Generated password:", password)