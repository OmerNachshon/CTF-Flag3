def reverse(string):
   return string[::-1]

def xor(string):
    new = [chr(ord(a) ^ 127) for a in string]
    return ''.join(new)

def caesar(string, pivot):
    new_str=''
    for ch in string:
        new_str += chr(ord(ch)+pivot)
    return new_str

def RXOR1_CAESAR(string,pivot):
    return caesar(xor(reverse(string)),pivot)

def decrypt_RXOR1_CAESAR(string,pivot):
    return reverse(xor(caesar(string, -1*pivot)))

flag='the connels 74 75'
flag=flag.split(' ')
caesar_lst=[1,9,7,4]
cipher=[]

for i in range(len(flag)):
    cipher.append(RXOR1_CAESAR(flag[i],caesar_lst[i]))


print(cipher)
solution=[]
for i,val in enumerate(cipher):
    solution.append(decrypt_RXOR1_CAESAR(val,caesar_lst[i]))
print(' '.join(solution))


