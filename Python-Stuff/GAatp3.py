print("Plano:")
M = [
    [0,0,0], #A x1, y1, z1
    [0,0,0], #B x1, y2, z3
    [0,0,0], #C x1, y2, z3
]

it = -1
for i in range(9):
    
    ABC = "A" if (i >= 0 and i <= 2) else "C" if (i >= 6 and i <= 9) else "B"
    mod = i % 3
    if (mod == 0):
        print(f"Coordenadas do ponto {ABC}:")
        it += 1    
    valor = int(input(f"Digite a {mod+1}a. coordenada: "))
    M[it][mod] = valor

# Contas

AB=[M[1][0] - M[0][0], M[1][1] - M[0][1], M[1][2] - M[0][2]]#(Bx−Ax,By−Ay,Bz−Az)
AC=[M[2][0] - M[0][0], M[2][1] - M[0][1], M[2][2] - M[0][2]]#(Cx−Ax,Cy−Ay,Cz−Az)

a = ((AB[1]*AC[2])-(AC[1]*AB[2])) * -1 #a (By−Ay)(Cz−Az)−(Cy−Ay)(Bz−Az)
b = ((AB[2]*AC[0])-(AC[2]*AB[0])) * -1 #b (Bz−Az)(Cx−Ax)−(Cz−Az)(Bx−Ax)
c = ((AB[0]*AC[1])-(AC[0]*AB[1])) * -1 #c (Bx−Ax)(Cy−Ay)−(Cx−Ax)(By−Ay)

d = ((a*M[0][0])+(b*M[0][1])+(c*M[0][2])) * -1 #−(aAx+bAy+cAz)

if (a > 0):
    print("Equação Geral do plano:")
    print("ax + by + cz + d = 0")
    print("onde:")
    print("a = {0:.2f}, b = {1:.2f}, c = {2:.2f} e d = {3:.2f}".format(a,b,c,d))
else:
    print("Dados Incorretos")