# *******Getting inputs for encryption or decryption*******
def code_input(cipher, message, num, res, s):
    cipher = input("Type 'encode' to encrypt or 'decode' to decrypt -----> ")
    print("\n")
    res = []
    if cipher == "encode" or cipher == "decode":
        message = list(input("Enter the message in small alphabets -----> "))
        num = (int(input("Enter the shift number -----> "))) % 26
        print("\n")
        if cipher == "encode":
            s += 1
        else:
            s -= 1
        encode_decode(cipher, res, message, num, s)
    else:
        print("Wrong Input, please try again\n\n")
        code_input(cipher, message, num, res, s)

# ***** encoding and decoding process ***** 
def encode_decode(cipher, res, message, num, s):
    for i in message:
        if ord(i) > 96 and ord(i) < 123:
            if ord(i) + (s * num) < 97 or ord(i) + (s * num) > 122:
                res.append(chr(ord(i) + (s * (num - 26))))
            else:
                res.append(chr(ord(i) + (s * num)))
        else:
            res.append(i)
    print(f"Here is the {cipher}d result -----> {''.join(res)}\n\n")
    rep_process(rep)

# ***** To repeat the program *****
def rep_process(rep):
    rep = input("Type 'yes' if you want to go again, else type 'no' -----> ")
    print("\n")
    
    if rep == "yes":
        code_input(cipher, message, num, res, s)
    elif rep == "no":
        print("***** Thank You *****\n\n")
    else:
        print("Wrong Input, please try again\n\n")
        rep_process(rep)
        
# ***** Inputs *****
cipher = message = rep = ""
num = s = 0
res = []

code_input(cipher, message, num, res, s)