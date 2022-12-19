from pyswip import Prolog, Functor, Variable, Query, call, registerForeign

prolog = Prolog()
prolog.consult("database.pl")

#___comandos__
assertz = Functor("assertz", 1)
possivel = Functor("possivel", 2)
confere = Functor("confere", 1)

#___reino___
mamifero = Functor("mamifero", 1)
carnivoro = Functor("carnivoro", 1)
anfibio = Functor("anfibio", 1)

#___animal___
macaco = Functor("macaco",1)
jacare = Functor("jacare",1)
baleia = Functor("baleia",1)

X = Variable()

lista = ["pelo","leite","cauda","come_carne","tem_garra","respiracao_sub-cutanea","molhado_seco","pula"]

def confirma():
    if call(confere("macaco")) == 1:
        print("macaco")
        return 1
    elif call(confere("jacare")) == 1:
        print("jacare")
        return 1
    elif call(confere("baleia")) == 1:
        print("baleia")
        return 1
    return 0

def pergunta(t):
    x = input("seu anima tem " + str(t)+"? ")
    if x == "y":
        call(assertz(possivel("a",str(t))))
    else:
        call(assertz(possivel("f",str(t))))
    
pergunta.arity = 1

registerForeign(pergunta)

q = Query(mamifero(X))
while q.nextSolution():
    print("Hello,", X.value)
q.closeQuery()
k = input()

for i in lista:
    pergunta(i)
    if confirma() == 0:
        continue
    else:
        break



