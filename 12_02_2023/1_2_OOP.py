class Datum:
    def __init__(self, Tag, Monat, Jahr):
        self.__Tag = Tag
        self.__Monat = Monat
        self.__Jahr = Jahr

    def __str__(self):
        return f'Heute ist {self.__Tag} im Jahr {self.__Jahr}'

    def andern_Datum(self, Tag, Monat, Jahr):
        if isinstance([Tag, Monat, Jahr], int):
            if Tag <= 31 and Monat <= 12:
                self.__Tag = Tag
                self.__Monat = Monat
                self.__Jahr = Jahr
        else:
            print('falsche Dateien')

mein_Datum = Datum(12, 2, 2023)
print(mein_Datum)

mein_Datum.andern_Datum(111, 3223, -44)