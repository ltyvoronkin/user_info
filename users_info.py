class User_profile():
    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name=first_name
        self.login_attempts=0

    def describe_user(self):
        print(self.first_name.title()+" "+self.last_name.title())

    def great_user(self):
        print("Hi "+self.first_name.title())

    def increment_login_attempts(self):
    	self.login_attempts += 1

    def reset_login_attempts(self):
    	self.login_attempts =0

    def read_login_attempts(self):
    	print(self.login_attempts)



user1 = User_profile('denis', 'voronkin')
user1.describe_user()
user1.great_user()

user1.read_login_attempts()

user1.increment_login_attempts()
user1.read_login_attempts()

user1.reset_login_attempts()
user1.read_login_attempts()



