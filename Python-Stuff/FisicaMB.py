# importar funções do Sistema
import os

#Verificar comando do OS para limpar o terminal Repl.it = "clear" | Windows = "cls"
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

from math import sin,cos,sqrt,radians

#Definir Constantes#
gravidade = 9.8
####################

def Programa():
  h_solo = float(input("Insira a altura de lançamento a partir do solo (metros): "))
  vel_init = float(input("Insira a velocidade de lançamento inicial (m/s): "))
  angulo = float(input("Insira o ângulo de lançamento - (Ângulo deve ser entre 0 e 90°): "))


  if not (angulo > 0 and angulo <= 90): 
    clear()
    print("Por favor, coloque apenas entre 0 e 90 graus o angulo\n")
    Programa()
  angulo = radians(angulo)

  TD = float(input("Insira um instante de tempo após o lançamento (segundos): "))


  #Velocidade incial [X, Y]
  VelocidadeInicial = [
    sin(angulo)*vel_init,
    cos(angulo)*vel_init
  ]

  # Altura maxima
  AlturaMaxima = h_solo+VelocidadeInicial[0]*VelocidadeInicial[0]/(2*gravidade)

  # Tempo subida e h_decend
  h_init = VelocidadeInicial[0]/gravidade
  h_decend = sqrt(2*AlturaMaxima/gravidade)

  # Alcance Máximo (Alcance horizontal)
  AlcanceHorizontal = VelocidadeInicial[1]*(h_init + h_decend)

  # Tempo total da bola no ar
  tempo_total = h_init + h_decend

  # Pos do objeto [X, Y]
  PosicaoObjeto = [
    VelocidadeInicial[1]*TD, 
    h_solo+(VelocidadeInicial[0]*TD)-(0.5*gravidade* pow(TD, 2))
  ]

  # Velocidade do objeto [Vx, Vy]
  VelocidadeN = sqrt(pow(gravidade*h_decend, 2) + pow(VelocidadeInicial[1], 2))
  VelocidadeObjeto = [
    cos(angulo)*VelocidadeN,
    VelocidadeInicial[0]-(gravidade*TD),
  ]

  # Velocidade na altura maxima
  VelocidadeAlturaMax = VelocidadeN*cos(angulo)

  #Velocidade final [Vxf, Vyf]
  VelocidadeFinal = [
    VelocidadeN*cos(angulo),
    VelocidadeInicial[0]-gravidade*tempo_total,
  ]

  # PRINTAR INFORMAÇÃO #
  print("""
-------------------------------
Os componentes nos eixos x e y da velocidade inicial da bola:
V0x = {xvel_i:.3f} m/s 
V0y = {yvel_i:.3f} m/s
-------------------------------
Tempo em que a bola permanece no ar: {max_t:.3f}
-------------------------------
A posição da bola no instante Td = {i_td}:
TX: {inst_x:.3f}
TY: {inst_y:.3f}
-------------------------------
Velocidade e suas componentes nos eixos X e Y no instante Td = {i_td}
T-Vx = {instvel_x:.3f}
T-Vy = {instvel_y:.3f}
T-Velocidade = {vel_inst:.3f}
-------------------------------
Altura máxima alcançada pela bola: {max_h:.3f}
-------------------------------
Alcance horizontal:  {alc_h:.3f}
-------------------------------
Velocidade Final nos eixos x e y no instante Td = {i_td}: 
Vxf = {finalvel_x:.3f}
Vyf = {finalvel_y:.3f}
Velocidade = {vel_final:.3f}
-------------------------------
Velocidade no instante em que a bola atinge a altura máxima e suas componentes noseixos x e y.
Vx = {velx_max:.3f}
Vy = 0
Velocidade = {vel_hmax:.3f}
-------------------------------""".format(
  i_td       = TD,                   #TEMPO INSTANTE
  max_h      = AlturaMaxima,           #ALTURA MAXIMA
  max_t      = tempo_total,          #TEMPO EM SEGUNDOS
  alc_h      = AlcanceHorizontal,         #H
  xvel_i     = VelocidadeInicial[1], #VYO
  yvel_i     = VelocidadeInicial[0], #VXO
  inst_x     = PosicaoObjeto[0],     #XO
  inst_y     = PosicaoObjeto[1],     #YO
  instvel_x  = VelocidadeObjeto[0],  #VOX
  instvel_y  = VelocidadeObjeto[1],  #VOY
  vel_inst   = VelocidadeObjeto[0],  #VOX
  finalvel_x = VelocidadeFinal[0],
  finalvel_y = VelocidadeFinal[1],
  vel_final  = VelocidadeN,
  velx_max   = VelocidadeAlturaMax,
  vel_hmax   = VelocidadeAlturaMax,
  ))

Programa()