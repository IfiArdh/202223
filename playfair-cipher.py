def print_key_matrix(mat):
    print("\n")
    for i in mat:
        print(i)
    print("\n")
    
def index_2d(keyMatrix, v):
    for i, x in enumerate(keyMatrix):
        if v in x:
            return [i, x.index(v)]

ikey=list(input("Enter the key : ").upper())
key=[]
for i in ikey:
    if i not in key:
        key.append(i)


#Creating 5x5 Matrix

alp = list("ABCDEFGHIKLMNOPQRSTUVWXYZ");

for i in alp:
    if i not in key:
        key.extend(i)

keymat = []
for i in range(0,25,5):
    keymat.append(key[i:i+5])
   

#Getting and spliting the keys into pair


plain=list(input("Enter the plain text : ").upper())
if(len(plain)%2!=0):
    plain.append('Z')
plain_text = []
for i in range(0,len(plain),2):
    plain_text.append(plain[i:i+2])


#For encrypting with keymatrix
ciphertext = ""
for i in range(0,len(plain_text)):
    first = []
    second = []
    first.extend(index_2d(keymat, plain_text[i][0]))
    second.extend(index_2d(keymat, plain_text[i][1]))
    
    if first[0] == second[0]:
        if first[1]+1 < len(keymat[first[0]]):
            ciphertext += keymat[first[0]][first[1]+1]
        else:
            ciphertext += keymat[first[0]][0]
            
        if second[1]+1 < len(keymat[second[0]]):
            ciphertext += keymat[second[0]][second[1]+1]
        else:
            ciphertext += keymat[second[0]][0]
            
    elif first[1] == second[1]:
        
        if first[0]+1 < len(keymat[first[0]]):
            ciphertext += keymat[first[0]+1][first[1]]
        else:
            ciphertext += keymat[[0][first[0]]]
            
        if second[0]+1 < len(keymat[second[0]]):
            ciphertext += keymat[second[0]+1][second[1]]
        else:
            ciphertext += keymat[[0][second[0]]]
    else:
        ciphertext += keymat[first[0]][second[1]] + keymat[second[0]][first[1]]
print("\nThe Encrypted text is ",ciphertext)
        
#Decryption

encr = list(input("Enter the Encrypted text : ").upper())
encr_text = []
for i in range(0,len(encr),2):
    encr_text.append(encr[i:i+2])

decrtext = ""
    
for i in range(0, len(encr_text)):

    first = []
    second = []
    first.extend(index_2d(keymat, encr_text[i][0]))
    second.extend(index_2d(keymat, encr_text[i][1]))

    if first[0] == second[0]:
        if first[0] - 1 >= 0:
            decrtext += keymat[first[0]][first[1]-1]
        else:
            decrtext += keymat[first[0]][4]

        if second[1] - 1 >= 0:
            decrtext += keymat[second[0]][second[1]-1]
        else:
            decrtext += keymat[second[0]][4]

    elif first[1] == second[1]:

        if first[0] - 1 >= 0:
            decrtext += keymat[first[0] - 1][first[1]]
        else:
            decrtext += keymat[4][first[1]]

        if second[0] - 1 >= 0:
            decrtext += keymat[second[0]-1][second[1]]
        else:
            decrtext += keymat[4][second[1]]
    else:
        decrtext += keymat[first[0]][second[1]] + keymat[second[0]][first[1]]

print("\nThe Decrypted text is : ",decrtext)
