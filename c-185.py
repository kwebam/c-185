import hashlib
from simplecrypt import encrypt, decrypt

value = "Peter : Hello"

def SHA256():
    result = hashlib.sha256( value.encode() )
    print("SHA256 Encypted Data : ", result.hexdigest())
SHA256()

def MD5():
    result = hashlib.md5( value.encode() )
    print("MD5 Encypted Data : ", result.hexdigest())
MD5()

message = "Peter : Hello"
hex_string = ''

def Encryption():
    global hex_string
    ciphercode = encrypt('hfdfjgysdugtsdjkdhe67fche78fheiw67fwe8uidheudhe78dhr67efhdud76gfwe7ft7we87fyhr7e8ufyhe78gyreuvyh7gyerughuhy7th' , message)
    hex_string = ciphercode.hex()
    print("Encyption", hex_string)
    
def Decryption():
    global hex_string
    byte_str = bytes.fromhex(hex_string)
    orignal = decrypt('hfdfjgysdugtsdjkdhe67fche78fheiw67fwe8uidheudhe78dhr67efhdud76gfwe7ft7we87fyhr7e8ufyhe78gyreuvyh7gyerughuhy7th', byte_str)
    final_message = orignal.decode("utf-8")
    print("Decyption", final_message)
    
Encryption()
Decryption()