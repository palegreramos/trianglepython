from triangulo import Triangulo 

datos=[]  #datos=list()

while True:
    base=input("base: ")
    if (base==""):
        break
    altura=input("altura: ")
    try:
        base=float(base)
        altura=float(altura)
    except:
        print("Deben ser números")
    else:
        nuevo=Triangulo(base, altura)
        datos.append(nuevo.area())
        print(datos)
    finally:
        print("Prueba de nuevo, pulsa Enter para salir")
print("adiós")