import random

def Show(a):
    for l in a:
        print(l)
    print("\n")

def GenerateMap(n_rooms, matrix_size):
    if matrix_size**2 > n_rooms:
        arr = [[0 for x in range(matrix_size)] for y in range(matrix_size)]
        
        #set spawn
        spawn_coords = [random.randint(1,matrix_size-2),random.randint(1,matrix_size-2)]
        print(spawn_coords)

        arr[spawn_coords[0]][spawn_coords[1]] = 2
        generatedRooms = 1;
        rooms = [(spawn_coords[0],spawn_coords[1])]
        Show(arr)
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
            
        Show(arr)