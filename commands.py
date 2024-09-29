from os import remove

import classes


class AddCommand:
    def __init__(self, productStorage: classes.ProductStorage):
        self.productStorage = productStorage

    def execute(self, params: []):
        self.productStorage.storage.append(classes.Product(int(params[0]), params[1],float(params[2])))
class ListCommand:
    def __init__(self, productStorage: classes.ProductStorage):
        self.productStorage = productStorage

    def execute(self, params: []):
        for x in range(len(self.productStorage.storage)):
            print(x, ". " + str(self.productStorage.storage[x]))
class RemovalCommand:
    def __init__(self, productStorage : classes.ProductStorage):
        self.productStorage = productStorage
    def execute(self, params: []):
        self.productStorage.storage.pop(int(params[0]))
class HelpCommand:
    pass