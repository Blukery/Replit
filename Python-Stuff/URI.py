QNode, TCores = [int(i) for i in input("").split()]

Nodes     = [] #Imput de dados
NodeCache = [] #Armazenar temp da array pra trocar de lugar
Impossible = False #Se for impossivel -> True (e mata o programa)

for i in range(QNode):
    TableCNum = [int(i) for i in input("").split()] #Append ja em INT
    Nodes.append(TableCNum)

print("-------------------------------------")

for i in range(len(Nodes)):
    if not (Impossible):

        Num = (Nodes[i][0]) - 1 #compensate index array
        ColorImg = Nodes[Num][1]
        if (Nodes[i][1] == ColorImg):
            if (Nodes[i] != Nodes[Num]):
                print(f"[!] Troca possivel encontrada: {Nodes[i]} com {Nodes[Num]}")
            #Switch pos#
            NodeCache  = Nodes[i]
            Nodes[i]   = Nodes[Num]
            Nodes[Num] = NodeCache
            ###########
        else:
            Impossible = True
            print(f"[E] Não é possivel trocar {Nodes[i]} com {Nodes[Num]}")
    else:
        break
print("")
print("Y" if (not Impossible) else "N")

