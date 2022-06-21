class ContactList():
    #stored contacts as a list of dictionaries, sorted by contacts' name
    #List should have name that separate  it
    def __init__(self, name, contact_list):
        self.name = name
        self.contact_list = sorted(contact_list, key = lambda x: x['name'] ) #sorted based on 'name'


    def add_contact(self, dict_contact):
        self.contact_list.append(dict_contact)
        self.contact_list.sort(key = lambda x: x['name'])

    def remove_contact(self, remove_name):
        self.contact_list = [contact for contact in self.contact_list if contact['name'] != remove_name]

    def find_shared_contacts(self, contact_list):
        """
        Given another ContactList instance, return a ContactList of shared contacts.
        """
        shared = []
        for contact in self.contact_list:
            if contact in contact_list.contact_list:
                shared.append(contact)
        
        return ContactList(self.name+ ' and ' + contact_list.name, shared)
    
    def __str__(self):
        return f'{self.name}\'s list has {self.contact_list}.'


friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)

friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)
# friends_i_work_with should be: [{'name':'Alice','number':'867-5309'}]

print(my_friends_list, 'friends')
print(work_buddies, 'work')
print('      ')
print(friends_i_work_with, 'shared')