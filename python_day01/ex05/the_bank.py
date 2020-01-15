import random

class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if not hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1
        if hasattr(self, 'the_bank'):
            self.the_bank.add([self, self.id, self.name])
    def transfer(self, amount):
        self.value += amount

# in the_bank.py
class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []
    def add(self, account):
        self.account.append(account)
    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return         True if success, False if an error occured
"""

    #Collect index + Check even number
        index_origin = -1
        index_dest = -1
        for index, elem in enumerate(self.account):
            if origin == elem[1] or origin == elem[2]:
                index_origin = index
            elif dest == elem[1] or dest == elem[2]:
                index_dest = index
        if (index_origin != -1 and index_dest != -1):
            if len(dir(self.account[index_origin][0])) % 2 == 0 or len(dir(self.account[index_dest][0])) % 2 == 0:
                print("EVEN NUMBER OF ATTRIBUTE\n")
                return False
        else:
            print("NOT AN ACCOUNT\n")
            return False


    #Attribute with b
        for elem in dir(self.account[index_origin][0]):
            if elem[0] == "b":
                print("ORIGIN ACCOUNT HAS AN ATTRIBUTE STARTING WITH B\n")
                return False
        for elem in dir(self.account[index_dest][0]):
            if elem[0] == "b":
                print("DEST ACCOUNT HAS AN ATTRIBUTE STARTING WITH B\n")
                return False


    #Attribute with zip or addr
        verif_attr_origin = False
        verif_attr_dest = False
        dir_origin = dir(self.account[index_origin][0])
        list_tmp = []
        for elem in dir_origin:
            list_tmp.append(elem.replace("_", "", 2))
        dir_origin = list_tmp
        dir_dest = dir(self.account[index_dest][0])
        list_tmp = []
        for elem in dir_dest:
            list_tmp.append(elem.replace("_", "", 2))
        dir_dest = list_tmp
        for elem in dir_origin:
            if elem[0:3] == "zip" or elem[0:4] == "addr":
                verif_attr_origin = True

        for elem in dir_dest:
            if elem[0:3] == "zip" or elem[0:4] == "addr":
                verif_attr_dest = True

        if verif_attr_origin != True or verif_attr_dest != True:
            print("NO ATTRIBUTE ZIP OR ADDR")
            return False


    #Attributes name id value
        if not "name" in dir(self.account[index_origin][0]) or not "id" in dir(self.account[index_origin][0]) or not "value" in dir(self.account[index_origin][0]):
            print("NO ATTRIBUTE NAME / ID / VALUE in ORIGIN ACCOUNT")
            return False
        if not "name" in dir(self.account[index_dest][0]) or not "id" in dir(self.account[index_dest][0]) or not "value" in dir(self.account[index_dest][0]):
            print("NO ATTRIBUTE NAME / ID / VALUE in DEST ACCOUNT")
            return False

    #Amount
        if amount > self.account[index_origin][0].value:
            print("NOT ENOUGH MONEY")
            return False

    #transfer
        self.account[index_origin][0].value -= amount
        self.account[index_dest][0].transfer(amount)
        print("TRANSFER DONE")
        return True

    #def fix_account(self, account):
    #    fix the corrupted account
        #    @account: int(id) or str(name) of the account
    #        @return         True if success, False if an error occured

def main():
    my_bank = Bank()
    alex_account = Account("Alex", value=1000, the_bank=my_bank, zip="test")
    john_account = Account("John doe", value=900, the_bank=my_bank, zip="test")


    print("\n--- PRINT OBJ ---\n")
    print(my_bank)
    print(alex_account)
    print(john_account)

    print("\n--- PRINT DIR ---\n")
    print(dir(my_bank))
    print("\n")
    print(dir(alex_account))
    print("\n")
    print(dir(john_account))

    print("\n--- PRINT ACCOUNT INFORMATIONS ---\n")
    print("NAME = {0}    ID = {1}    AMOUNT = {2}".format(alex_account.name, alex_account.id, alex_account.value))
    print("NAME = {0}    ID = {1}    AMOUNT = {2}".format(john_account.name, john_account.id, john_account.value))

    print("\n--- PRINT BANK INFORMATIONS ---\n")
    print(my_bank.account)

    print("\n--- PRINT TRANSFER ---")
    print("\nWITH NAMES")
    print("Alex account amount before transfer = {0}".format(alex_account.value))
    print("John account amount before transfer = {0}".format(john_account.value))
    my_bank.transfer("Alex", "John doe", 10)
    print("Alex account amount after transfer = {0}".format(alex_account.value))
    print("John account amount after transfer = {0}".format(john_account.value))

    print("\nWITH ID")
    print("Alex account amount before transfer = {0}".format(alex_account.value))
    print("John account amount before transfer = {0}".format(john_account.value))
    my_bank.transfer(1, 2, 10)
    print("Alex account amount after transfer = {0}".format(alex_account.value))
    print("John account amount after transfer = {0}".format(john_account.value))

    print("\nWITH ERROR AMOUNT")
    print("Alex account amount before transfer = {0}".format(alex_account.value))
    print("John account amount before transfer = {0}".format(john_account.value))
    my_bank.transfer("Alex", "John doe", 10000)
    print("Alex account amount after transfer = {0}".format(alex_account.value))
    print("John account amount after transfer = {0}".format(john_account.value))

main()
