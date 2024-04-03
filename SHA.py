import hashlib

h = hashlib.new("sha256")
correct_password = "MyPSWS32I3"
h.update(correct_password.encode())

password_hash = h.hexdigest()
print("Password Hash:", password_hash)

user_input = "MYPASSKAS2332"
h = hashlib.new("sha256")
h.update(user_input.encode())
input_hash = h.hexdigest()

print("Input Hash:", input_hash)
print("Passwords Match:", input_hash == password_hash)
