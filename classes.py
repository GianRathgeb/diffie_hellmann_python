class menu:
    def __init__(self):
        self.status = True

    def start(self):
        self.print_menu()
        if self.select_option("Eingabe: ") == 1:
            self.decrypt()

    def print_menu(self):
        print("1: Verschlüsseln")

    def select_option(self, user_prompt):
        try:
            self.confirmation = int(input(user_prompt))
            return self.confirmation
        except ValueError:
            print("Keine korrekte eingabe")
            self.select_option(user_prompt)
        except IndexError:
            print("Keine korrekte eingabe")
            self.select_option(user_prompt)

    def decrypt(self):
        self.main_module = int(input("Hauptmodul eingeben: "))
        self.encrypt_exponent = int(input("Verschlüsslungsexponent VE eingeben: "))
        self.encryptet_code = int(input("Code eingeben: "))
        self.factor1 = 1
        self.factor = 1
        # Faktorenzerlegung in 2 Faktoren
        while self.factor != 0:
            self.factor1 += 1
            self.factor = self.main_module % self.factor1

        self.factor2 = self.main_module / self.factor1


