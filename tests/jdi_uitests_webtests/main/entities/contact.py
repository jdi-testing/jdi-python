class Contact:
    def __init__(self, name, last_name, description):
        self.first_name = name
        self.last_name = last_name
        self.description = description

    def __str__(self):
        return "Summary: 3\nLast Name: {0}\nDescription: {1}\nVegetables:".format(
            self.last_name, self.description
        )
