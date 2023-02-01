#Nicolle Ruiz Quintero / Ing Biomedica

#PUNTO 1
mat = [[11, 23, 76, 34, 11],
[14, 30, 92, 30, 101],
[12, 45, 58, 92, 22],
[74, 56, 49, 56, 100],
[99, 5, 28, 47, 99]]


diag_principal = [mat[i][i] for i in range(len(mat))]
diag_secundaria = [mat[i][len(mat)-i-1] for i in range(len(mat))]

if diag_principal == diag_secundaria:
    print(True)
else:
    print(False)


def comprobar(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i!=j:
                return False
        return True

a = [[11, 23, 76, 34, 11],
[14, 30, 92, 30, 101],
[12, 45, 58, 92, 22],
[74, 56, 49, 56, 100],
[99, 5, 28, 47, 99]]

print(comprobar(a))

#PUNTO 2
print(" ")

def esCapicua(lista):
    for i in range(len(lista) // 2):
        if lista[i] != lista[len(lista) - i - 1]:
            return False
    return True
    
lista=[42, 12, 90, 90, 12, 42]

print(esCapicua(lista))

# PUNTO 3 A

print(" ")

def diferenciaDeListas(listaA,listaB):
    
    diferenciaA_B=[]

    for i in listaA:
        if  i not in listaB:
                diferenciaA_B.append(i)
    return diferenciaA_B

lista1=[40, 10, 22, 12, 33, 33, 33]
    
lista2=[41, 22, 31, 15, 13, 12, 33, 19]

print(diferenciaDeListas(lista1,lista2))
print(diferenciaDeListas(lista2,lista1))

#PUNTO 3 B

#PUNTO 4 

print(" ")


def mostrarPrimos(n):
    lista2=[]
    for num in range(2,n+1):
        contador=0
        for i in range(2,num):
            if num%i==0:
                contador+=1
        if contador==0:
            lista2.append(num)
    print("Numeros primos entre 1 y",n)
    for j in lista2:
        print("-->",j,",")

z = int(input())

print(mostrarPrimos(z))



#PUNTO 5