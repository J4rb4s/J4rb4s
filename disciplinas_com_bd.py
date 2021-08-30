import sqlite3
from itertools import permutations
from tabulate import tabulate


import numpy as np

###########
#  DADOS  #
###########


import numpy as np


dis=["D1","D2","D3","D4"]



professores=[]



#################
#  PARTIÇÕES    #
#################


def partition(collection):
    if len(collection) == 1:
        yield [ collection ]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
        # put `first` in its own subset 
        yield [ [ first ] ] + smaller



def listap(dis):
    lista_p=[]
    for n, p in enumerate(partition(dis), 1):
        lista_p.append(sorted(p))
    return lista_p


#print(lista_p)
limite1=len(listap(dis))
#print(limite)

################################    
#SUPOMOS QUE SÃO 4 PROFESSORES#
###############################


matriz= listap(dis)

def numero_prof(matriz,limite1):
    lista=[]
    i=-1
    while i<=limite1-2:
        i=i+1
        if len(matriz[i])==len(professores):
            lista.append(matriz[i])
    return lista


#print(numero_prof())
#print(str(len(numero_prof()))+ "   Possibilidades....")
numero_profi=numero_prof(matriz,limite1)


#########################
# CHOQUES DE HORÁRIO    #
########################

listaco=[]

def addchoque():
    disc1=input("      Digite a disciplina 1: ")
    disc2=input("      Digite a disciplina 2: ")
    listaco.append([disc1,disc2])
    return


def choque(numero_profi):
    listak=[]
    for a in numero_profi:
        for b in a:
            i=-1
            while i<=len(listaco)-2:
                i=i+1
                if listaco[i][0] in a[a.index(b)] and listaco[i][1] in a[a.index(b)]:
                    listak.append(a)
              
    return [x for x in numero_profi if x not in listak]                
            
    
choquei=choque(numero_profi)


def pco(choquei):
    listapco=[]
    for k in range(0,len(choquei)):
        for i in list(permutations(choquei[k])):
            listapco.append(list(i))
    return listapco	
    
permco=pco(choquei)    


#################################################
#     PROFESSOR ESCOLHE AS DISCIPLINAS          #
#################################################


#disciplinas professor


listaj=[]

def localizar():
    i=-1
    while i<=len(professores)-2:
        i=i+1
        listaj.append(adc(i))
    return listaj

        
def tabelap():
    if len(listaj)==0:
        print("Lista vazia!!")    
    else:
        tabela=[]
        i=-1
        while i<=len(professores)-2:
            i=i+1
            tabela.append(["Professor "+str(professores[i])]+listaj[i])
        return tabela
    

def printlocal():
    print(tabulate(tabelap(), tablefmt='grid'))
    return

    
def adc(i):
    ded=input("      Fixar disciplina para o(a) Professor(a) "+str(professores[i])+"?")
    listat=[]
    while ded:
        if ded=="sim":
            fixando=input("      Digite a disciplina: ")
            listat.append(fixando)
            print(listat)
            ded=input("      Fixar disciplina para o(a) Professor(a) "+str(professores[i])+"?")
        else:
            return listat


def identf(permco):
    listaf=[]
    if len(listaj)==0:
        return permco
            
    if len(listaj)==len(professores):
        for a in range(0,len(permco)):
            j=-1
            listavf=[]
            while j<=len(professores)-2:
                j=j+1
                listavf.append(set(listaj[j]).issubset(set(permco[a][j])))
            if all(listavf):
                listaf.append(permco[a])
    if len(listaj)>len(professores):
        print("      Número de professores incompatível!!")

                       
    return listaf                
                


fixai=identf(permco)



#################################################
#   NUMERO DE DISCIPLINAS PARA CADA PROFESSOR  #
#################################################




listann=[]

def lnn():
    k=-1
    while k<=len(professores)-2:
        k=k+1
        listann.append(True)
    return    
          
    


def prof(i):
    dado1=input("      Adicionar número de disciplinas para o(a) Professor(a) "+str(professores[i])+"?")
    return dado1






def adn(i):
    dado2=int(input("      Quantas disciplinas para o(a) Professor(a) "+str(professores[i])+"?"))
    return dado2
    




def addnumero():
    listann.clear()
    lnn()
    i=-1
    while i<=len(professores)-2:
        i=i+1
        if prof(i)=="sim":
            listann[i]=adn(i)
      

def maxima(fixai):
    lnn()
    lista_m=[]
    for a in fixai:
        k=-1
        valorv=[]
        while k<=len(professores)-2:
            k=k+1
            if listann[k]==True:
                b=True
                valorv.append(b)
            else:
                b=(len(a[k])==listann[k])
                valorv.append(b)
        if all(valorv):
            lista_m.append(a)
            
    return lista_m        
                
        
        


    
            
maximai=maxima(fixai)




########################################
# BLOCO DE CARACTERÍSTICAS             #
########################################




def addbloco(titulo):
    adce=input("Adicionar elemento em "+str(titulo)+"?")
    blc=[]
    while adce:
        if adce=="sim":
            elem=input("Digite o elemento:")
            blc.append(elem)
            print(blc)
            adce=input("Adicionar elemento em "+str(titulo)+"?")
        else:
            return blc
    
        
listablc=[]
def blocos():
    titulo=input("Digite um Título para esse Bloco: ")
    listablc.append([str(titulo)]+ addbloco(titulo))
    
    

def imprimirblocos():
    print("+--------------------+")
    print("| Blocos Adicionados |")
    print("+====================+")
    print(tabulate(listablc,tablefmt='grid'))
    
    

listabbl=[]

def listvv(dis):
    i=-1
    while i<=len(professores)-2:
        i=i+1
        gat=input("Adicionar bloco para o(a) professor(a) "+str(professores[i])+" ?")
        if gat=="sim":
            escolha=input("Atribua um bloco para o professor(a) "+str(professores[i])+" :")
            for k in listablc:
                if k[0]==escolha:
                    listabbl.append(k)
        else:
            listabbl.append(dis)
    

def todosvdd(elem):
    vdd=[]
    for j in range(0,len(professores)):
                vdd.append(set(elem[j]).issubset(set(listabbl[j])))
    return vdd            
   
def problc(maximai):    
    novalista=[]
    if len(listabbl)==0:
        return maximai
    
    else:
        for a in maximai:
            if all(todosvdd(a)):
                novalista.append(a)
    return novalista        


def tabat(dis):
    tabat=[]
    for k in range(0,len(professores)):
        if listabbl[k]==dis:
            tabat.append([professores[k],"Tanto Faz!"])
        else:
            tabat.append([professores[k],listabbl[k][0]])
            
    return tabat



def impat(dis):
    print("+-------------------------+")
    print("| Atribuições Adicionadas |")
    print("+=========================+")
    if len(listabbl)==0:
        return
    print(tabulate(tabat(dis),tablefmt='grid'))
    

        
        

            
            
    
    
    



########################
# PRINTANDO DISCIPLINAS#
########################


def proplista(i,dis):
    tabelaprop=[]
    for j in range(0,len(professores)):
        tabelaprop.append([professores[j]]+problc(maxima(identf(pco(choque(numero_prof(listap(dis),len(listap(dis))))))))[i][j])
    return tabelaprop    
    


def imprimir(maximai,dis):
    print("***************************")
    print("* Proposta de Disciplinas *")
    print("***************************")
    i=-1
    while i<=len(maximai)-2:
        i=i+1
        print(" ")
        print(" ")
        print("PROPOSTA "+str(i+1))
        print("+----------------------+")
        print("|Professor(a) / Horário|")
        print("+======================+")
        print(tabulate(proplista(i,dis),tablefmt='grid'))    

    


###############################################################################
#                         LAYOUT                                              #
###############################################################################


teste=[]
def menu():
    carregar_dados()
    print(" ")
    print ("[[  POSSIBLIDADES DE HORÁRIOS  ]]")
    opcao = le_opcao()
    while opcao:
        
        if opcao==1:
            submenu22(teste)
        elif opcao==2:
            submenu2(teste)
        elif opcao == 3:
            if len(teste)==0:
                print(" ")
                print("DISCIPLINAS NÃO ADICIONADAS!!")
            else:
                print(" ")
                print("EXISTEM "+ str(len(problc(maxima(identf(pco(choque(numero_prof(listap(teste),len(listap(teste)))))))))) + " POSSIBILIDADES!!")
        elif opcao == 4:
            if len(teste)==0:
                print(" ")
                print("DISCIPLINAS NÃO ADICIONADAS!!")
            else:
                imprimir(problc(maxima(identf(pco(choque(numero_prof(listap(teste),len(listap(teste)))))))),teste)
        elif opcao not in range(1,4):
            print(" ")
            print("Opção Inválida!!")
        opcao = le_opcao()
        


def le_opcao():
    print (" ")
    print ("+---------------------------+")
    print ("|        MENU INICIAL       |")
    print ("+===========================+")
    print ("|1 - >> Adicionar Dados >>  |")
    print ("+---------------------------+")       
    print ("|2 - >> Adicionar Filtros >>|")
    print ("+---------------------------+")       
    print ("|3 - nº de possibilidades   |")
    print ("+---------------------------+")       
    print ("|4 - Possibilidades         |")
    print ("+---------------------------+")
    opcao = int(input("==>"))
    return opcao
        
def submenu22(teste):
    opcao22=opmenu22()
    while opcao22:
        if opcao22 == 1:
            submenu1(teste)
        elif opcao22==2:
            submenu1p(teste)
        elif opcao22==3:
            submenu4(teste)
        elif opcao22==4:
            return
        elif opcao22 not in range(1,4):
            print("Opção Inválida!!")
            
        opcao22=opmenu22()
    return teste


def opmenu22():
    print(" ")
    print ("    +-----------------------------+")
    print ("    |         INCLUIR DADOS       |")
    print ("    +=============================+")
    print ("    |1 - >> Disciplinas >>        |")
    print ("    +-----------------------------+")
    print ("    |2 - >> Professores(as) >>    |")
    print ("    +-----------------------------+")
    print ("    |3 - >> Choques de Horários >>|")
    print ("    +-----------------------------+")
    print ("    |4 - <<<<<<                   |")
    print ("    +-----------------------------+")
    opcao22 = int(input("    ==>"))
    return opcao22

def submenu1(teste):
    opcao1=opmenu1()
    while opcao1:
        if opcao1==1:
            adicionar_disciplina()
            
        elif opcao1==2:
            deletar_disciplinas()
            
        elif opcao1==3:
            listar_na_lista(teste)
        
        elif opcao1==4:
            return
        elif opcao1 not in range(1,4):
            print("Opção Inválida!!")
            
        opcao1=opmenu1()
    return teste


def opmenu1():
    print(" ")
    print ("        +----------------------------------+")
    print ("        |           DISCIPLINAS            |")
    print ("        +==================================+")
    print ("        |1 - Adicionar uma nova disciplina |")
    print ("        +----------------------------------+")
    print ("        |2 - Excluir todas as disciplinas  |")
    print ("        +----------------------------------+")
    print ("        |3 - Listar disciplinas            |")
    print ("        +----------------------------------+")
    print ("        |4 - <<<<<<                        |")
    print ("        +----------------------------------+")
    opcao1 = int(input("        ==>"))
    return opcao1
    
def submenu1p(teste):
    opcao1p=opmenu1p()
    while opcao1p:
        if opcao1p==1:
            adicionar_professor()
            
        elif opcao1p==2:
            deletar_professores()
            
        elif opcao1p==3:
            i=-1
            print(" ")
            print("Os Professores Adionados Foram...")
            while i<=len(professores)-2:
                i=i+1
                print("* "+str(professores[i]))
                
        elif opcao1p==4:
            return
        elif opcao1p not in range(1,4):
            print("Opção Inválida!!")
            
        opcao1p=opmenu1p()
    return 


def opmenu1p():
    print(" ")
    print ("        +----------------------------------+")
    print ("        |  PROFESSORES                     |")
    print ("        +==================================+")
    print ("        |1 - Adicionar professores         |")
    print ("        +----------------------------------+")
    print ("        |2 - Excluir lista de professores  |")
    print ("        +----------------------------------+")
    print ("        |3 - Listar professores            |")
    print ("        +----------------------------------+")
    print ("        |4 - <<<<<<                        |")
    print ("        +----------------------------------+")
    opcao1p = int(input("        ==>"))
    return opcao1p


def submenu2(teste):
    opcao2=opmenu2()
    while opcao2:
        if opcao2==1:
            submenu3(teste)
                        
        elif opcao2==2:
            submenu5(teste)
            
        elif opcao2==3:    
            submenu6(teste)
        elif opcao2==4:
            return
        elif opcao2 not in range(1,4):
            print("Opção Inválida!!")
            
        opcao2=opmenu2()
    return teste    
    

def opmenu2():
    print(" ")
    print ("    +-----------------------------------+")
    print ("    |              FILTROS              |")
    print ("    +===================================+")
    print ("    |1 - >> Disciplinas fixas >>        |")
    print ("    +-----------------------------------+")
    print ("    |2 - >> Número de disciplinas >>    |")
    print ("    +-----------------------------------+")
    print ("    |3 - >> Blocos de Características >>|")
    print ("    +-----------------------------------+")
    print ("    |4 - <<<<<<                         |")
    print ("    +-----------------------------------+")
    opcao2 = int(input("    ==>"))
    return opcao2

def submenu3(teste):
    opcao3=opmenu3()
    while opcao3:
        if opcao3==1:
            localizar()    
        if opcao3==2:
            listaj.clear()
        if opcao3==3:
            printlocal()

        if opcao3==4:
            return
        if opcao3 not in range(1,4):
            print("Opção Inválida!!")
        opcao3=opmenu3()
        
    return teste    

def opmenu3():
    print(" ")
    print ("        +--------------------------------------+")
    print ("        |          FIXAR DISCIPLINAS           |")
    print ("        +======================================+")
    print ("        |1 - Fixar disciplinas para professores|")
    print ("        +--------------------------------------+")
    print ("        |2 - Limpar lista                      |")
    print ("        +--------------------------------------+")
    print ("        |3 - Imprimir lista                    |")
    print ("        +--------------------------------------+")
    print ("        |4 - <<<<<<                            |")
    print ("        +--------------------------------------+")
    opcao3 = int(input("        ==>"))
    return opcao3

def submenu4(teste):
    opcao4=opmenu4()
    while opcao4:
        if opcao4==1:
            adicionar_choque_de_horarios()    
        if opcao4==2:
            deletar_choque()
        if opcao4==3:
            print("+-------------+")
            print("|   Choques   |")
            print("+=============+")
            print(tabulate(listaco, tablefmt='grid'))
            


        if opcao4==4:
            return
        elif opcao4 not in range(1,4):
            print("Opção Inválida!!")
        opcao4=opmenu4()
        
    return teste    

def opmenu4():
    print(" ")
    print ("        +-------------------------------+")
    print ("        |       CHOQUES DE HORÁRIOS     |")
    print ("        +===============================+")
    print ("        |1 - Adicionar choque de horário|")
    print ("        +-------------------------------+")
    print ("        |2 - Limpar lista               |")
    print ("        +-------------------------------+")
    print ("        |3 - Imprimir lista             |")
    print ("        +-------------------------------+")
    print ("        |4 - <<<<<<                     |")
    print ("        +-------------------------------+")
    opcao4 = int(input("        ==>"))
    return opcao4




def listapr(teste):
    listapr=[]
    for k in range(0,len(professores)):
        if int(listann[k])==int(True):
            listapr.append([professores[k],"Tanto Faz!"])
        else:
            listapr.append([professores[k],str(listann[k])+" disciplinas!"])
            
    return listapr



def listan(teste):
    if len(listann)==0:
        print("Lista Vazia!")
        return
    print("+--------------------+")
    print("| Números Atribuidos |")
    print("+====================+")
    print(tabulate(listapr(teste),tablefmt='grid'))
    
    
           
def submenu5(teste):
    opcao5=opmenu5()
    while opcao5:
        if opcao5==1:
            addnumero()    
        elif opcao5==2:
            listann.clear()
        elif opcao5==3:
            listan(teste)

        elif opcao5==4:
            return
        elif opcao5 not in range(1,4):
            print("Opção Inválida!!")
        opcao5=opmenu5()
        
    return teste    

def opmenu5():
    print(" ")
    print ("        +------------------------------+")
    print ("        |     NÚMERO DE DISCIPLINAS    |")
    print ("        +================================================+")
    print ("        |1 - Adicionar nº de disciplinas para professores|")
    print ("        +------------------------------------------------+")
    print ("        |2 - Limpar números   |")
    print ("        +---------------------+")
    print ("        |3 - Imprimir números |")
    print ("        +---------------------+")
    print ("        |4 - <<<<<<           |")
    print ("        +---------------------+")
    opcao5 = int(input("        ==>"))
    return opcao5
            


def submenu6(teste):
    opcao6=opmenu6()
    while opcao6:
        if opcao6==1:
            submenu6b(teste)
            #blocos()    
        elif opcao6==2:
            submenu6p(teste)
            #listablc.clear()
        elif opcao6==3:
            return
            #imprimirblocos()
        #elif opcao6==4:
         #   listvv(teste)
        #elif opcao6==5:
         #   impat(teste)
        #elif opcao6==6:
         #   return
        elif opcao6 not in range(1,3):
            print("Opção Inválida!!")
        opcao6=opmenu6()
        
        
    return teste    

def opmenu6():
    print(" ")
    print ("        +---------------------------+")
    print ("        | BLOCOS DE CARACTERÍSITCAS |")
    print ("        +===========================+")
    print ("        |1 - >> Blocos >>           |")
    print ("        +---------------------------+")
    print ("        |2 - >> Blocados >>         |")
    print ("        +---------------------------+")
    print ("        |3 - <<<<<<                 |")
    print ("        +---------------------------+")
    opcao6 = int(input("      ==>"))
    return opcao6
            
def submenu6b(teste):
    opcao6b=opmenu6b()
    while opcao6b:
        if opcao6b==1:
            blocos()    
        elif opcao6b==2:
            listablc.clear()
        elif opcao6b==3:
            imprimirblocos()
        elif opcao6b==4:
            return
         #   listvv(teste)
        #elif opcao6==5:
         #   impat(teste)
        #elif opcao6==6:
         #   return
        elif opcao6b not in range(1,4):
            print(" ")
            print("Opção Inválida!!")
        opcao6b=opmenu6b()
        
        
    return teste    

def opmenu6b():
    print(" ")
    print ("            +---------------------------+")
    print ("            |          BLOCOS           |")
    print ("            +===========================+")
    print ("            |1 - Adicionar Blocos       |")
    print ("            +---------------------------+")
    print ("            |2 - Limpar Lista de Blocos |")
    print ("            +---------------------------+")
    print ("            |3 - Imprimir Blocos        |")
    print ("            +---------------------------+")
    print ("            |4 - <<<<<<                 |")
    print ("            +---------------------------+")
    opcao6b = int(input("            ==>"))
    return opcao6b

def submenu6p(teste):
    opcao6p=opmenu6p()
    while opcao6p:
        if opcao6p==1:
            listvv(teste)    
        elif opcao6p==2:
            listabbl.clear()
            #tabat(teste).clear()
        elif opcao6p==3:
            impat(teste)
        elif opcao6p==4:
            return
        elif opcao6p not in range(1,4):
            print(" ")
            print("Opção Inválida!!")
        opcao6p=opmenu6p()
        
        
    return teste    

def opmenu6p():
    print(" ")
    print ("            +------------------------+")
    print ("            |        BLOCADOS        |")
    print ("            +========================+")
    print ("            |1 - Atribuir Blocos     |")
    print ("            +------------------------+")
    print ("            |2 - Limpar Blocados     |")
    print ("            +------------------------+")
    print ("            |3 - Imprimir Blocados   |")
    print ("            +------------------------+")
    print ("            |4 - <<<<<<              |")
    print ("            +------------------------+")
    opcao6p = int(input("==>"))
    return opcao6p
    

def insere_na_lista(teste):
    disc = input("Digite o nome da disciplina:")
    if disc in teste:
        print("Esta disciplina já foi incluída!")
        return
    teste.append(str(disc))
    return teste

   
    
def listar_na_lista(teste):
    print("As disciplinas incluídas foram...")
    for b in teste:    
        print("* "+b)


###################
# BANCO DE DADOS  #      
###################

def adicionar_professor():
    banco_p=sqlite3.connect("professores_d.db")

    cursor_p=banco_p.cursor()
    #desmarcar abaixo para criar a tabela (primeira vez)
    #cursor.execute("CREATE TABLE professores_d (nome text)")
    nome_p=input("Digite o nome de um professor: ")

    cursor_p.execute("INSERT INTO professores_d VALUES ('"+nome_p+"') ")

    banco_p.commit()
    carregar_dados()

def deletar_professores():
    banco_p=sqlite3.connect("professores_d.db")

    cursor_p=banco_p.cursor()
    cursor_p.execute("DELETE FROM professores_d;",);
    banco_p.commit()
    
    professores.clear()    

    

#Disciplinas    

def adicionar_disciplina():
    banco_d=sqlite3.connect("disciplinas_d.db")

    cursor_d=banco_d.cursor()
    #desmarcar abaixo para criar a tabela (primeira vez)
    #cursor_d.execute("CREATE TABLE disciplinas_d (nome text)")
    nome_p=input("Digite o nome de uma disciplina: ")

    cursor_d.execute("INSERT INTO disciplinas_d VALUES ('"+nome_p+"') ")

    banco_d.commit()
    carregar_dados()

       
def deletar_disciplinas():
    banco_d=sqlite3.connect("disciplinas_d.db")

    cursor_d=banco_d.cursor()
    cursor_d.execute("DELETE FROM disciplinas_d;",);
    banco_d.commit()
    
    teste.clear()    

def adicionar_choque_de_horarios():
    banco_c=sqlite3.connect("choque_d.db")
    cursor_c=banco_c.cursor()
    #cursor_c.execute("CREATE TABLE choque_d (disc1 text,disc2 text)")
    disc1=input("      Digite a disciplina 1: ")
    disc2=input("      Digite a disciplina 2: ")
    cursor_c.execute("INSERT INTO choque_d VALUES ('"+disc1+"','"+disc2+"')")
    banco_c.commit()
    carregar_dados()
    
def deletar_choque():
    banco_c=sqlite3.connect("choque_d.db")

    cursor_c=banco_c.cursor()
    cursor_c.execute("DELETE FROM choque_d;",);
    banco_c.commit()
    
    listaco.clear()  
    
    

def carregar_dados():
    banco=sqlite3.connect("professores_d.db")

    cursor=banco.cursor()
    banco.commit()

    cursor.execute("SELECT * FROM professores_d")
    professores.clear()
    
    linha=list(cursor.fetchall())
    for x in linha:
        professores.append(list(x)[0])    

    banco_d=sqlite3.connect("disciplinas_d.db")

    cursor_d=banco_d.cursor()
    banco_d.commit()

    cursor_d.execute("SELECT * FROM disciplinas_d")
    teste.clear()
    
    lista_d=list(cursor_d.fetchall())
    for x in lista_d:
        teste.append(list(x)[0])

    banco_c=sqlite3.connect("choque_d.db")

    cursor_c=banco_c.cursor()
    banco_c.commit()

    cursor_c.execute("SELECT * FROM choque_d")
    listaco.clear()
    
    lista_c=list(cursor_c.fetchall())
    for x in lista_c:
        listaco.append(list(x))    
    












