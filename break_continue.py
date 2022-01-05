#def run():
    
    #for contador in range(1001):
    #    if contador %2 != 0:
    #        continue
    #    print(contador)

    #for i in range(10000):
    #    print(i)
    #    if i == 5678:
    #        break
#
#    texto = input("Escribe un texto: ")
#    for letra in texto:
#        if letra == "o":
#            break
#        print(letra)
#
#
#if __name__ == '__main__':
#    run()

#CONTINUE usado con WHILE
#def run():
#    LIMITE = 101
#    contador = 0
#
#    while contador < LIMITE:
#        contador += 1
#        if contador %2 != 0:
#            continue
#        print(str(contador))
#
#
#if __name__ == '__main__':
#    run()


#BREAK usado con WHILE
def run():
    LIMITE = 100
    contador = 0

    while contador < LIMITE:
        print(str(contador))
        contador += 1

        if contador == 34:
            break
        

if __name__ == '__main__':
    run()