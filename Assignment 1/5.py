import cryptocode
import hashlib
import base64

text = input("Enter text: ")

print("\n--- Encryption / Decryption ---")
key = input("Enter secret key: ")
encrypted = cryptocode.encrypt(text, key)
print("Encrypted:", encrypted)
print("Decrypted:", cryptocode.decrypt(encrypted, key))

print("\n--- Message Digest ---")
print("MD5    :", hashlib.md5(text.encode()).hexdigest())
print("SHA-1  :", hashlib.sha1(text.encode()).hexdigest())
print("SHA-256:", hashlib.sha256(text.encode()).hexdigest())

print("\n--- Base64 ---")
encoded = base64.b64encode(text.encode()).decode()
print("Encoded:", encoded)
print("Decoded:", base64.b64decode(encoded).decode())