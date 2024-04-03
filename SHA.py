import hashlib

class Encrytor:
    def __init__(self, password):
        self.__hash = None
        self.__password = password

    def __correct_password(self):
        return "gelo"

    @staticmethod
    def tip():
        return "É feito de água, mas se for colocado dentro da água morrerá."

    def __new(self):
        self.__hash = hashlib.new("sha256")

    def __encode(self, value):
        self.__hash.update(value.encode())

    def __get(self):
        return self.__hash.hexdigest()

    def start(self):
        data = {}

        data["initial_correct_password"] = self.__correct_password()
        self.__new()
        self.__encode(self.__correct_password())
        data["correct_password"] = self.__get()

        data["initial_inserted_password"] = self.__password
        self.__new()
        self.__encode(self.__password)
        data["inserted_password"] = self.__get()

        data["matches"] = data["correct_password"] == data["inserted_password"]

        return data

print("A resposta da charada a seguir é a senha!")
print("\n")
print(Encrytor.tip())
print("\n")
password = input("Senha: ")

encryption = Encrytor(password)
encryptionResult = encryption.start()

print("Senha Inserida Inicial: "+encryptionResult["initial_inserted_password"])
print("Senha Correta Inicial: "+encryptionResult["initial_correct_password"])
print("Senha Inserida com SHA: "+encryptionResult["inserted_password"])
print("Senha Correta com SHA: "+encryptionResult["correct_password"])
print("\n")
print("Senhas Batem: "+("Sim" if encryptionResult["matches"] else "Não")+"!")
