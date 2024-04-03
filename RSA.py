import rsa

class Encrytor:
    def __init__(self):
        (self.__public_key, self.__private_key) = rsa.newkeys(2048)
        self.__crypto = None
        self.__initial_message = ""
        self.__message = ""

    def start(self, message):
        self.__initial_message = message

        self.__encrypt()
        self.__decrypt()

    def __encrypt(self):
        self.__crypto = rsa.encrypt(
            self.__initial_message.encode('utf-8'), self.__public_key
        )

    def __decrypt(self):
        self.__message = (rsa
                          .decrypt(self.__crypto, self.__private_key)
                          .decode('utf-8'))

    def get_public_key(self):
        return self.__public_key

    def get_private_key(self):
        return self.__private_key

    def get_hash(self):
        return self.__crypto

    def get_initial_message(self):
        return self.__initial_message

    def get_message(self):
        return self.__message

encryptor = Encrytor()
encryptor.start(input("Insira um texto para criptografar: "))

print("Texto inserido: "+encryptor.get_initial_message())
print("\n")
print("Chave pública usada para criptografar:")
print(encryptor.get_public_key())
print("\n")
print("Texto criptografado: ")
print(encryptor.get_hash())
print("\n")
print("Chave privada usada para descriptografar:")
print(encryptor.get_private_key())
print("\n")
print("Texto descriptografado: "+encryptor.get_message())
