
from User import User

class FreeUser(User):

    def __init__(self, name, email_address, driver_liscense):
        User.__init__(self, name, email_address, driver_liscense)

    def add_post(self, post):
        if len(self.user_posts) < 2:
            self.user_posts.append(post)
            User.posts[self.name] = self.user_posts
        else:
            return "Please upgrade to premium to post more."

# theo = FreeUser('theo', 'nhud@gmail.com', 35443)
# print(theo)

    
