def master():

  print(
  """ 

  ██████╗░██████╗░░█████╗░░░░░░██╗░░░  ░█████╗░░█████╗░██╗░░░░░░█████╗░
  ██╔══██╗██╔══██╗██╔══██╗░░░░░██║░░░  ██╔══██╗██╔══██╗██║░░░░░██╔══██╗
  ██████╔╝██████╔╝██║░░██║░░░░░██║░░░  ██║░░╚═╝███████║██║░░░░░██║░░╚═╝
  ██╔═══╝░██╔══██╗██║░░██║██╗░░██║░░░  ██║░░██╗██╔══██║██║░░░░░██║░░██╗
  ██║░░░░░██║░░██║╚█████╔╝╚█████╔╝██╗  ╚█████╔╝██║░░██║███████╗╚█████╔╝
  ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░

  ---------------INTEGRANTES---------------
                22121081-8

                22121121-2

                22120050-4
  -----------------------------------------
  """
  )

  def algoritimo():

    W  = complex(input("Digite o W: "))
    EP = float(input("Digite o epsilon (ε): "))
    M  = int(input("Digite o M (sequencia): "))

    #definindo array
    Z = [0]
    pare = False
    
    for k in range(M): 
      form = Z[k] ** 2 + W
      Z.append(form)
      #print(k + 1, ": ", form, "\b")

    Z.pop(0)
    t_Z = len(Z)

    T_count = 0 
    while T_count < t_Z:
      for i in range(T_count - 1, t_Z - 1):
        if T_count - 1 != i:
          raw_C = abs(Z[T_count] - Z[i + 1 if i != t_Z else 0])
          R = raw_C < EP
          #print(f"{raw_C} - ITERATION {i} = {R}")
          if not R:
            break
          elif R and (i == t_Z - 2): 
            pare = True
            break
        #else:
          #print(f"ITSELF {T_count}")
      T_count += 1
      if pare:
        break

      #print("\n")
      
    if pare == True :
      print(f"O menor indice procurado: {T_count}")
    else:
      print(f"Não há índice a partir do qual um elemento e seus subsequentes estejam a uma distância menor a menor que: {EP}")

    
  algoritimo()
master()

