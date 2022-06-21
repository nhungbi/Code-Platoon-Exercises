import FreeUser, PremiumUser, User


anna = PremiumUser.PremiumUser('Anna', 'annahhello@gmail.com', 78743987957)
anna.add_post('helloworld')
anna.add_post('goodbye')
anna.delete_post('goodbye')
print(anna)

john = FreeUser.FreeUser('John', 'johhnyy@gmail.com', 7908098098)
john.add_post('evening')
john.add_post('hello')
john.add_post('awe')
print(john)

