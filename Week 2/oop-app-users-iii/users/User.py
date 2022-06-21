class User:
    posts = {}

    def __init__(self, name, email_address, driver_lisense):
        self.name = name
        self.email_address = email_address
        self.driver_liscense = driver_lisense
        self.user_posts = []
    
    def add_post(self, post):
        self.user_posts.append(post)
        User.posts[self.name] = self.user_posts
    
    def delete_post(self, post_to_delete):
        self.user_posts.remove(post_to_delete)
        User.posts[self.name] = self.user_posts


    def __str__(self): 
        return f'User: {self.name} with an email address of {self.email_address} has liscense {self.driver_liscense}. Posts includes {self.user_posts}.'


# anna = User('Anna', 'annahhello@gmail.com', 78743987957)
# anna.add_post('helloworld')
# anna.add_post('goodbye')
# anna.delete_post('goodbye')
# print(anna)

# john = User('John', 'johhnyy@gmail.com', 7908098098)
# john.add_post('evening')
# print(john)

# print(User.posts)