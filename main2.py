from pyswip import Prolog, Functor, Variable, Query, call, registerForeign

prolog = Prolog()
prolog.consult("dataset.pl")

assertz = Functor("assertz", 1)
confere = Functor("confere", 1)



X = Variable()

def possui(caracteristica):
    resp = input("Animal possui ou tem ",str(caracteristica))
    if resp == 'y' or resp == "yes":
        return 1
    else:
        return 0

possui.arity = 1


Animais = ['macaco', 'baleia', 'jacare']

confere('macaco')