import random
from sala import *

todasSalas = []
lista_coords = []
spawn = []

def Show(a):
    for l in a:
        print(l)
    print("\n")

def GenerateMap(n_rooms, matrix_size):
    if matrix_size**2 > n_rooms:
        arr = [[0 for x in range(matrix_size)] for y in range(matrix_size)]
        
        #set spawn
        spawn_coords = [random.randint(1,matrix_size-2),random.randint(1,matrix_size-2)]
        spawn.append(spawn_coords[0])
        spawn.append(spawn_coords[1])
        print(spawn_coords)

        arr[spawn_coords[0]][spawn_coords[1]] = 2
        generatedRooms = 1;
        rooms = [(spawn_coords[0],spawn_coords[1])]
        
        cr_i = spawn_coords[0] #stands for current room line
        cr_j = spawn_coords[1] #stands for current room row

        while(generatedRooms < n_rooms):
            for i_adj, j_adj in [(cr_i-1, cr_j), (cr_i, cr_j-1), (cr_i, cr_j+1), (cr_i+1, cr_j)]:
                    if i_adj < 0 or i_adj >= matrix_size or j_adj < 0 or j_adj >= matrix_size:
                        continue
                    
                    g_chance = 20 #(50%)
                    if(random.randint(0,100) <= g_chance) and ((i_adj,j_adj) not in rooms) and (generatedRooms < n_rooms):
                        arr[i_adj][j_adj] = 1
                        generatedRooms+=1
                        rooms.append((i_adj,j_adj))
            
            roomPick = random.randint(0,len(rooms)-1)
            cr_i = rooms[roomPick][0]
            cr_j = rooms[roomPick][1]
            
        # Achar extremidade para posicionar boss
        hasBoss = 0
        while(hasBoss == 0):
            r_i = random.randint(0,matrix_size-1)
            r_j = random.randint(0,matrix_size-1)
            condition = True
            adj_rooms = 0
            for i_adj, j_adj in [(r_i-1, r_j), (r_i, r_j-1), (r_i, r_j+1), (r_i+1, r_j)]:
                if i_adj < 0 or i_adj >= matrix_size or j_adj < 0 or j_adj >= matrix_size:
                    continue
                if(adj_rooms > 1):
                    break
                if(arr[i_adj][j_adj] != 0):
                    adj_rooms += 1
                else:
                    continue
            for i_adj,j_adj in [(r_i-2, r_j), (r_i, r_j-2), (r_i, r_j+2), (r_i+2, r_j),(r_i-1, r_j-1), (r_i-1, r_j+1), (r_i+1, r_j-1), (r_i+1, r_j+1)]:
                if i_adj < 0 or i_adj >= matrix_size or j_adj < 0 or j_adj >= matrix_size:
                    continue
                if(arr[i_adj][j_adj] != 0):
                    break
            if(condition and adj_rooms==1):
                arr[r_i][r_j]=3
                hasBoss = 1

             
                     
        Show(arr)
        return arr
        
    
            
def SetSalas(a):
     #definir spawn
     salaSpawn = Sala((0,0), 0)
     todasSalas.append(salaSpawn)

     for i in range(len(a)):
          for j in range(len(a)):
                if a[i][j] == 1:
                    variation = random.randint(2,21)
                    x = Sala((j-spawn[1],i-spawn[0]),variation)
                    #[(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                    if(i-1 < 0 or i-1 >= len(a) or j < 0 or j >= len(a)):
                        pass
                    else:
                        if(a[i-1][j]==3):
                            x.chefao='top'
                    if(i+1 < 0 or i+1 >= len(a) or j < 0 or j >= len(a)):
                        pass
                    else:
                        if(a[i+1][j]==3):
                            x.chefao='bottom'

                    if(i < 0 or i >= len(a) or j-1 < 0 or j-1 >= len(a)):
                        pass
                    else:
                        if(a[i][j-1]==3):
                            x.chefao='left'

                    if(i < 0 or i >= len(a) or j+1 < 0 or j+1 >= len(a)):
                        pass
                    else:
                        if(a[i][j+1]==3):
                            x.chefao='right'

                    todasSalas.append(x)
                        

                if a[i][j] == 3:
                    todasSalas.append(Sala((j-spawn[1],i-spawn[0]),30))
    
     for i in todasSalas:
          lista_coords.append(i.adress)
     for i in todasSalas:
          i.SetPortas(lista_coords)