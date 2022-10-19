import random

S = 10  # Alfabeto de 10 numeros


def createRandomVector(n):
    temp =  range(n)
    random.shuffle(temp)
    return temp


def myindex(k,l, element):
    length = len(l)
    count = 0
    for i in range(length):
        if element == l[(k+i)%length]:
            return count
        count = count + 1



class rotor:

    def __init__(self,r,desloc):
        self.r = r[:]
        self.desloc = desloc
        self.starting_position = 0
        self.count = 0
        self.flag = False

    def cifra(self,x):
        assert x >= 0
        assert x < len(self.r)
        assert x < S
        #print self.r
        return self.r[(self.starting_position+x)%len(self.r)]

    def decifra(self,x):
        assert x >= 0
        assert x < len(self.r)
        assert x < S
        #print self.r
        return myindex(self.starting_position,self.r,x)

    # Anda uma casa. o "primeiro" elemento vai para o fim
    def rot(self):
        self.starting_position = (self.starting_position + 1)%len(self.r)
        self.count = self.count + 1
        print "count" ,self.count, "len (self.r) ", len(self.r)
        #print self.r
        if(self.count >= len(self.r)):
            self.flag = True
            self.count = self.count%len(self.r) 


    # Responde se eu acabei de completar um ciclo. Se SIM, a rotacao deve ser propagada
    # para o proximo rotor
    def stepNext(self):
        aux = self.flag
        if self.flag == True:
            self.flag = False
        return aux


    def minuslist(self):

        for i in range(len(self.r)):
            if self.r[i] > 0:
                self.r[i] = self.r[i] - 1
            else:
                self.r[i]= len(self.r) - 1


class enigma:

    def __init__(self, rotors):
        self.rotors = []
        for i in rotors:
            self.rotors.append(rotor(i[0],i[1]))


    # Chama o cifra de cada um dos rotores.
    # Executa a rotacao do primeiro (sempre)
    # e dos demais (quando necessario)
    def ecifra(self,x):
        aux = self.rotors[0].cifra(x)
        self.rotors[0].rot()
        self.rotors[0].minuslist()
        flag = self.rotors[0].stepNext()

       #print "rotor 0:",aux

        if len(self.rotors) > 1:
            for i in range(1,len(self.rotors)):
                if flag == True:
                    self.rotors[i].rot()
                    self.rotors[i].minuslist()
                    flag = self.rotors[i].stepNext()

                aux = self.rotors[i].cifra(aux)
                #print "rotor ",i,":",aux

        return aux


    def edecifra(self,x):

        aux = x

        for i in range(len(self.rotors)-1,-1,-1):
            aux = self.rotors[i].decifra(aux)

            #print "rotor",i,":",aux

        self.rotors[0].rot()
        self.rotors[0].minuslist()
        flag = self.rotors[0].stepNext()

        if len(self.rotors) > 1:
            for i in range(1,len(self.rotors)):
                if flag == True:
                    self.rotors[i].rot()
                    self.rotors[i].minuslist()
                    flag = self.rotors[i].stepNext()

        return aux

    def prepara(self):

        for i in range(len(self.rotors)):
            #print self.rotors[i].r
            for j in range(self.rotors[i].desloc):
                self.rotors[i].rot()
                self.rotors[i].minuslist()
                flag = self.rotors[i].stepNext()

                if i < len(self.rotors)-1:
                    for k in range(i+1,len(self.rotors)):
                        if flag == True:
                            self.rotors[i].rot()
                            self.rotors[i].minuslist()
                            flag = self.rotors[i].stepNext()
        '''       
        print "Rotores"
        for i in self.rotors:
            print i.r
        '''

"""
segredo1 = createRandomVector(S)
segredo2 = createRandomVector(S)
segredo3 = createRandomVector(S)
"""

"""
segredo1 = [5, 8, 0, 3, 7, 2, 6, 1, 4, 9]
segredo2 = [6, 5, 3, 7, 4, 8, 1, 2, 9, 0]
segredo3 = [7, 4, 1, 0, 2, 5, 3, 6, 9, 8]
"""

"""
segredo21 = [5, 8, 0, 3, 7, 2, 6, 1, 4, 9]
segredo22 = [6, 5, 3, 7, 4, 8, 1, 2, 9, 0]
segredo23 = [7, 4, 1, 0, 2, 5, 3, 6, 9, 8]
"""


"""
print 'segredo1:',segredo1
print 'segredo2:',segredo2
print 'segredo3:',segredo3
# 5,3 e 4 Sao os deslocamentos iniciais.. fazem parte da chave
"""


"""
e = enigma ( [ (segredo1,5),(segredo2,3),(segredo3,4)])
d = enigma ( [ (segredo1,5),(segredo2,3),(segredo3,4)])
e.prepara()
d.prepara()
"""

"""
e = enigma ( [ (segredo3,5),(segredo2,3),(segredo1,4)])
d = enigma ( [ (segredo23,5),(segredo22,3),(segredo21,4)])
"""


"""
segredo: [4, 2, 8, 0, 6, 5, 3, 1, 7, 9]
texto claro = [0,0,0,0,0....]
Texto cifrado:
[4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0]
"""
"""
segredo = [4, 2, 8, 0, 6, 5, 3, 1, 7, 9]
segredo1 = [4, 2, 8, 0, 6, 5, 3, 1, 7, 9]
e = enigma( [(segredo,0)] )
d = enigma( [(segredo1,0)] )
"""



"""
e = enigma ( [ (segredo3,4),(segredo2,3),(segredo1,5)])
d = enigma ( [ (segredo3,4),(segredo2,3),(segredo1,5)])
"""

'''
for k in range(5):
    for i in range(2):
        print ""
        print "texto claro: ",i
        x = e.ecifra(i)
        print "Criptografado: ",x
        y = d.edecifra(x)
        print "Decriptografado: ",y
        assert i==y
'''
'''
for i in range(S):
    for i in d.rotors:
        print i.flag
        print i.starting_position
'''
"""
Enigma minimo: disco unico
segredo: [9, 0, 6, 5, 4, 7, 2, 3, 8, 1]
Texto Claro: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[9, 9, 4, 2, 0, 2, 6, 6, 0, 2, 9, 9, 4, 2, 0, 2, 6, 6, 0, 2, 9, 9, 4, 2, 0, 2, 6, 6, 0, 2, 9, 9, 4, 2, 0, 2, 6, 6, 0, 2, 9, 9, 4, 2, 0, 2, 6, 6, 0, 2, 9, 9, 4, 2, 0, 2, 6, 6, 0, 2, 9, 9, 4, 2, 0, 2, 6, 6, 0, 2, 9, 9, 4, 2, 0, 2, 6, 6, 0, 2, 9, 9, 4, 2, 0, 2, 6, 6, 0, 2, 9, 9, 4, 2, 0, 2, 6, 6, 0, 2]
"""
"""
segredo = [9, 0, 6, 5, 4, 7, 2, 3, 8, 1]
segredo1 = [9, 0, 6, 5, 4, 7, 2, 3, 8, 1]
e = enigma( [(segredo,0)] )
d = enigma( [(segredo1,0)] )
"""

"""
Enigma minimo: disco unico, rotacao inicial de 3
segredo: [3, 2, 5, 0, 4, 6, 9, 7, 8, 1]
Texto Claro: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[7, 0, 1, 3, 0, 0, 2, 3, 1, 3, 7, 0, 1, 3, 0, 0, 2, 3, 1, 3, 7, 0, 1, 3, 0, 0, 2, 3, 1, 3, 7, 0, 1, 3, 0, 0, 2, 3, 1, 3, 7, 0, 1, 3, 0, 0, 2, 3, 1, 3, 7, 0, 1, 3, 0, 0, 2, 3, 1, 3, 7, 0, 1, 3, 0, 0, 2, 3, 1, 3, 7, 0, 1, 3, 0, 0, 2, 3, 1, 3, 7, 0, 1, 3, 0, 0, 2, 3, 1, 3, 7, 0, 1, 3, 0, 0, 2, 3, 1, 3]
"""
"""
segredo = [3, 2, 5, 0, 4, 6, 9, 7, 8, 1]
segredo1 = [3, 2, 5, 0, 4, 6, 9, 7, 8, 1]
e = enigma( [(segredo,3)] )
d = enigma( [(segredo,3)] )
e.prepara()
d.prepara()
"""

"""
for k in range(5):
    for i in range(S):
        x = e.ecifra(i)
        y = d.edecifra(x)
        print "passou"
        assert i==y
"""


"""
segredo = [4, 6, 0, 1, 7, 5, 2, 8, 9, 3]
segredo1 = [4, 6, 0, 1, 7, 5, 2, 8, 9, 3]
e = enigma( [(segredo,3)] )
d = enigma( [(segredo1,3)] )
p = [ i for i in range(4,0,-1)]
c = [e.ecifra(_p) for _p in p]
print c
print [d.edecifra(_c) for _c in c]
"""
'''
#testadoOK
segredo1 = [5, 6, 1, 8, 2, 0, 7, 3, 4, 9]
segredo2 = [9, 3, 8, 5, 0, 6, 1, 2, 4, 7]
segredo3 = [7, 9, 5, 8, 0, 1, 2, 4, 3, 6]
e = enigma ( [ (segredo1,5),(segredo2,3),(segredo3,4)])
d = enigma ( [ (segredo1,5),(segredo2,3),(segredo3,4)])
e.prepara()
d.prepara()
p = [i for i in range(5)]
'''

"""
segredo1 = [2, 8, 7, 5, 9, 3, 1, 0, 4, 6]
segredo2 = [0, 4, 7, 3, 8, 9, 2, 1, 5, 6]
segredo3 = [7, 9, 4, 3, 8, 2, 1, 0, 5, 6]
e = enigma ( [ (segredo1,4),(segredo2,3),(segredo3,5)])
d = enigma ( [ (segredo1,4),(segredo2,3),(segredo3,5)])
e.prepara()
d.prepara()
"""
'''
p=[0]*100
#p = [i for i in range(100)]
c=[e.ecifra(_p) for _p in p]
print c
print [d.edecifra(_c) for _c in c]
'''
'''
segredo1 =  createRandomVector(S)
segredo2 =  createRandomVector(S)
segredo3 =  createRandomVector(S)
'''

segredo1 = [5, 8, 0, 3, 7, 2, 6, 1, 4, 9]
segredo2 = [6, 5, 3, 7, 4, 8, 1, 2, 9, 0]
segredo3 = [7, 4, 1, 0, 2, 5, 3, 6, 9, 8]

print 'segredo1:',segredo1
print 'segredo2:',segredo2
print 'segredo3:',segredo3
# 5,3 e 4 Sao os deslocamentos iniciais.. fazem parte da chave
e = enigma ( [ (segredo1,5),(segredo2,3),(segredo3,4)])
d = enigma ( [ (segredo1,5),(segredo2,3),(segredo3,4)])


e.prepara()
d.prepara()


for k in range(5):
    for i in range(S):
        x = e.ecifra(i)
        y = d.edecifra(x)
        #assert i==y


p=[0]*100

c=[e.ecifra(_p) for _p in p]

print c

print [d.edecifra(_c) for _c in c]




'''
Saida do programa:
segredo1: [5, 8, 0, 3, 7, 2, 6, 1, 4, 9]
segredo2: [6, 5, 3, 7, 4, 8, 1, 2, 9, 0]
segredo3: [7, 4, 1, 0, 2, 5, 3, 6, 9, 8]
[8, 1, 4, 3, 1, 4, 9, 2, 1, 5, 9, 1, 7, 6, 1, 5, 3, 6, 4, 4, 1, 5, 1, 9, 3, 8, 7, 6, 5, 2, 7, 5, 0, 1, 5, 8, 7, 5, 1, 3, 7, 1, 6, 0, 1, 3, 2, 9, 5, 7, 2, 5, 6, 0, 5, 3, 1, 6, 8, 7, 1, 8, 4, 9, 8, 1, 7, 9, 2, 5, 7, 2, 4, 8, 2, 6, 1, 7, 4, 5, 1, 4, 8, 0, 4, 3, 0, 1, 4, 6, 0, 4, 7, 8, 4, 6, 8, 2, 1, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''
