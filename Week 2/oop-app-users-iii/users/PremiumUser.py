# Your PremiumUser class goes here
from User import User

class PremiumUser(User):
    
    def __init__(self, name, email_address, driver_liscense):
        User.__init__(self, name, email_address, driver_liscense)

# theo = PremiumUser('theo', 'nhud@gmail.com', 35443)
# print(theo)