mamifero:- possui(pelo),possui(leite).
carnivoro:- possui(presas),possui(garras).

macaco:- mamifero, possui(cauda).
baleia:- mamifero, possui(aquatico).
jacare:- carnivoro, possui(cauda).

confere(macaco):- macaco.
confere(baleia):- baleia.
confere(jacare):- jacare.
