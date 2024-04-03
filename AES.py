# by @Marlon-Souza16
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

class Encryptor:
    def __init__(self):
        self.key = get_random_bytes(32)

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message):
        message = self.pad(message.encode())
        iv = os.urandom(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        return iv + cipher.encrypt(message)

    def decrypt(self, ciphertext):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])

        return plaintext.rstrip(b"\0").decode()

enc = Encryptor()

texto_a_ser_criptografado = input("Digite o texto a ser criptografado: ")
print("Texto inserido:", texto_a_ser_criptografado)

ciphertext = enc.encrypt(texto_a_ser_criptografado)
print("Texto criptografado:", ciphertext)

plaintext = enc.decrypt(ciphertext)
print("Texto descriptografado:", plaintext)
