
import string

ciphertext = "y4$sufo_ra_nb_GLK_GRVI_wd4iu_yfwwb_CW"

def rot_n(text, n):
    result = ""
    for char in text:
        if char.islower():
            result += chr((ord(char) - ord('a') + n) % 26 + ord('a'))
        elif char.isupper():
            result += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
        else:
            result += char
    return result

print(f"Original: {ciphertext}")
print(f"Length: {len(ciphertext)}")

print("\n--- Caesar Cipher / ROT ---")
for i in range(1, 26):
    print(f"ROT{i:02}: {rot_n(ciphertext, i)}")

def atbash(text):
    result = ""
    for char in text:
        if char.islower():
            result += chr(ord('z') - (ord(char) - ord('a')))
        elif char.isupper():
            result += chr(ord('Z') - (ord(char) - ord('A')))
        else:
            result += char
    return result

print("\n--- Atbash ---")
print(atbash(ciphertext))

print("\n--- Reversed ---")
print(ciphertext[::-1])
