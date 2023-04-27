#|------------------------------- Undirected Graph-----------------------


"""                       
-La baza grafurilor stau cateva notiuni de baza:
   a)noduri(nodes/vertices)
   b)muchii(edges)
-Nodurile pot fi sau nu coectate intre ele"""

#|----------------------------------------------------------------------

"""
-In Python, vom implementa grafurile neorientate cu ajutorul dictionarelor
-Vom avea ca si exemplu graph-ul din "graph_img.png"
"""
#|----------------------------------------------------------------------


#1.Citirea grafului

import numpy as np
graph={'1':[2,3],
       '2':[1,3,5],
       '3':[1,2],
       '4':[],
       '5':[2]
       }

"""
OBS:
   -Key-le dictionrului sunt nodurile din graf
   -valorile Key-lor reprezinta nodurile adiacente corespunzatoare
   -memorarea valorilor se face folosind liste
  """

#2.Implementarea functiei ce adauga un nod si o muchie in graph

def add():
    nod=input("Adaugati un nod: ")
    n=eval(input("Introduceti numarul de muchii ce pleaca de la nodul introdus: "))
    graph[nod]=[]
    for i in range(n):
        muchie=input("Introduceti nodul de legatura: ")
        graph[muchie].append(nod)#la nodul existent deja in graph adaugam legatura cu noul nod
        graph[nod].append(muchie)#la nodul adaugat in graph se adauga legutile
   
#3.Implementarea functiei ce afiseaza nodurile grafului
def nod():
    global lista_noduri
    lista_noduri=[]
    for node in graph:
        lista_noduri.append(node)
    return lista_noduri

#4.Implementarea functiei ce afiseaza muchile din graf
def muchii():
    lista_muchii=[]
    d={}
    for node in graph:
        d[node]=0
        for muchie in graph[node]:
            lista_muchii.append((node,muchie))
            d[node]+=1
    return list(set(lista_muchii)) 

#5.Implementarea functiei ce afiseaza nodurile izolate din graf
def nod_izolat():
    noduri_izolate=set()
    for nod in graph:
        if not graph[nod]:
            noduri_izolate.add(nod)
    return list(noduri_izolate)

#6.Implementarea functiei ce calculeaza gradul fiecarui nod

def grad():
    global d
    d={}
    for node in graph:
        d[node]=0
        for muchie in graph[node]:
            d[node]+=1
        print("Nodul ",node," are gradul ",d[node])   


#7.Implementarea functiei ce afiseaza nodurile in ordine crescatoare a gradelor

def grad_max():
    print("Un dictionar cu nodurile si gradele lor este: ",d)
    l=list(d.items())
    l1=[(i[1],i[0]) for i in l]
    print("Lista inversa: ",l1)
    l1.sort()
    print("Lista inversa sortata",l1)
    print("Nodurile asezate crescator in functie de grade:")
    for i in l1:
        print("Nodul ",i[1]," are gradul ",i[0])  

#8.Testarea functiilor de prelucrare a grafurilor neorientate
print("-------------------------------  Test  ----------------------------------------------")    
add()
print("--------------------------------------------------------------------------------------")
print()
print("Noul graph: ",graph)
print()
print("Lista nodurilor este: ",nod())
print()
print("Lista muchiilor este: ",muchii())
print()
print("Lista nodurilor izolate este: ",nod_izolat())
print()
grad()
print()
grad_max()









    
    

    
















    

   
