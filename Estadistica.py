import ast

# def validar(lista):
#     largo=len()-1
#     for x in range(largo):

def sacar_media(lista):
    largo=len(lista)-1
    if largo%2!=0:
        indice=int(largo/2)
        indice2=int((largo/2)+1)
        media=(lista[indice]+lista[indice2])/2
        print(media)
    else:
        print(lista[int(largo/2)+1])
        # print("Hubo un pequeño error, la lista no puede contener letras")


def main():
    milist=input("Pasame una lista de números que quieres sacarle las medidas \
de tendencia central: \n")
    milista=list(ast.literal_eval(milist))
    milista.sort()
    desicion=bool(input(f"¿Esta es la lista que quieres que calcular?\n({milista})\n"))
    while desicion==False:
        try:
            if desicion == False:
                milist=input("Pasame la lista otra vez ")
                milista=list(ast.literal_eval(milist))
                desicion=bool(input(f"¿Esta es la lista que quieres calcular?\n( {milista} )\n"))
        except:
            break
    sacar_media(milista)
if __name__=='__main__':
    main()