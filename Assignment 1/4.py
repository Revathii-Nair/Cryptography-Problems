
import rsa
import base64

username = input("Enter username: ")
password = input("Enter password: ")

public_key, private_key = rsa.newkeys(512)

encrypted = rsa.encrypt(password.encode(), public_key)
decrypted = rsa.decrypt(encrypted, private_key).decode()

print("\nUsername: ", username)
print("Password:", password)
print("Encrypted password:", base64.b64encode(encrypted).decode())
print("Decrypted password:", decrypted)