from cryptography.fernet import Fernet

key=Fernet.generate_key()
crypter=Fernet(key)
pw=crypter.encrypt(b'my password')
decrypt_string=crypter.decrypt(pw)
print(str(pw,'utf8'))

