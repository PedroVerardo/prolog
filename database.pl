mamifero(Animal):- possivel(Animal,pelo), possivel(Animal,leite).
carnivoro(Animal):- possivel(Animal, come_carne), possivel(Animal, tem_garra).
anfibio(Animal):- possivel(Animal, respiracao_sub-cutanea), possivel(Animal,molhado_seco).

macaco(Animal):- mamifero(Animal), possivel(Animal,cauda), not(carnivoro(Animal)), not(anfibio(Animal)).
jacare(Animal):- carnivoro(Animal), possivel(Animal,cauda), not(possivel(Animal,pelo)), not(anfibio(Animal)).
baleia(Animal):- mamifero(Animal), possivel(Animal,aquatico).
sapo(Animal):- anfibio(Animal), possivel(Animal,pula).

confere(macaco):- macaco(a).
confere(jacare):- jacare(a).


