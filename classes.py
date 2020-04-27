from modules import *

class menu:
    def __init__(self):
        self.status = True

    def start(self):
        self.print_menu()
        self.option = self.select_option("\nEingabe: ")
        if  self.option == 2:
            self.decrypt()
        elif self.option == 0:
            sys.exit()
        else:
            self.start()

    def print_menu(self):
        print("\n\n\n2: Entschlüsseln\n0: Beenden")

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
        print("\n\n\n\n\nEntschlüsseln:\n")
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
        self.nm = (self.factor1 - 1) * (self.factor2 - 1)
        self.ee = 0
        self.rest = 0
        while self.rest != 1:
            self.ee += 1
            self.rest = (self.ee * self.encrypt_exponent) % self.nm
        self.rest_main_module = self.encryptet_code % self.main_module
        self.gross = pow(self.rest_main_module, self.ee)
        self.pos = self.gross % self.main_module
        print("\n\n\n\n\n")
        print("Aus Code {} wird die Position {}".format(self.encryptet_code, self.pos))
        print("Der geheime Schlüssel ist {}\n\n\n".format(self.ee))
        time.sleep(5)