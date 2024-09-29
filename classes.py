class Product:
    types =  {0:"Cухой", 1 : "Влажный"}

    def __init__(self, type: int , name: str, cost:float):
        self.type = type
        self.name = name
        self.cost = cost
    def __str__(self):
        return Product.types[self.type] + " корм " + self.name + ' со вкусом: ' + ', cтоит: ' + str(self.cost) + ' p.'

class CommandInput:
    def __init__(self, command_str: str):
        command_split = command_str.split(" ")

        self.command = command_split[0]
        self.params = command_split[1:]

    def __str__(self):
        return "Название команды: " + self.command + "\nКоличество параметров: " + str(len(self.params))


class Prorab:
    def __init__(self, spisok: {}):
        self.spisok = spisok


class ProductStorage:
    def __init__(self, name: str, storage: [Product]):
        self.name = name
        self.storage = storage