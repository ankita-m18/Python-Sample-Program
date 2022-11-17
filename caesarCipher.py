import string

def caesar(plain_text, shift_num=1):
    letters = string.ascii_lowercase
    mask = letters[shift_num:] + letters[:shift_num]
    trantab = str.maketrans(letters, mask)
    return plain_text.translate(trantab)

sentence=input("Enter a sentence = ")
code=""
code=caesar(plain_text=sentence,shift_num=1)

print("Caesar Cipher of entered sentence : ", code)