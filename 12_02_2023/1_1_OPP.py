class Baltic_States:
    def __init__(self, city, language, neighbour):
        self.capital = city
        self.inhabitants = 1300000
        self.official_language = language
        self.__border = neighbour

    def update_inhabitants(self, how_much):
        self.inhabitants += how_much

    def show_border(self):
        print(self.__border)

    def change_border(self, new_border):
        self.__border = new_border

Estonia = Baltic_States('tallinn', 'Estonian', 'Latvia')

print(Estonia.capital)
Estonia.update_inhabitants(20000)
print(Estonia.inhabitants)
# print(Estonia.__border)
# Estonia.show_border()
Estonia.change_border('Finland')
Estonia.show_border()