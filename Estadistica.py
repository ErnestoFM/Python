# valor=False
# def validar(valor):
#     for x 

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
    milist=[]
    milista=list(input("Pasame una lista de números que quieres sacarle las medidas \
de tendencia central: \n"))
    desicion=bool(input(f"¿Esta es la lista que quieres que calcular?\n({milista})\n"))
    while desicion==False:
        try:
            if desicion == False:
                milista=list(input("Pasame la lista otra vez "))
                desicion=bool(input(f"¿Esta es la lista que quieres que calcular?\n({milista})\n"))
        except:
            break
    milista.sort()
    sacar_media(milista)
if __name__=='__main__':
    main()