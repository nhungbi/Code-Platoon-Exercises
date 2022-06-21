class User:

    def __init__(self, name, email_address, driver_lisense):
        self.name = name
        self.email_address = email_address
        self.driver_liscense = driver_lisense

    def __str__(self): 
        return f'User: {self.name} with an email address of {self.email_address} has liscense {self.driver_liscense}.'



anna = User('Anna', 'annahhello@gmail.com', 78743987957)
print(anna)

john = User('John', 'johhnyy@gmail.com', 7908098098)
print(john)