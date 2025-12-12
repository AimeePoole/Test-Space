def shift(letter, shift_letter):
    s = ord(shift_letter) - ord('A')
    
    l = ord(letter) - ord('A')
    
    l = (l + s) % 26
    
    return chr(l + ord('A'))


plaintext = input("plaintext ")
key = input("key ")

key = key.upper()
plaintext = [x.upper() for x in plaintext if x.isalpha()]

print(plaintext)
print(key)

ciphertext = ""
i = 0

for p in plaintext:
    ciphertext += shift(p, key[i])

    if i == len(key) - 1:
        i = 0
    else:
        i += 1

print(ciphertext)
