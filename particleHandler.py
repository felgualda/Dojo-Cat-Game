from PPlay.sprite import *

bloodsplats = []

def FX_blood(pos_x,pos_y):
    x = Sprite('assets/blood_splat.png',8)
    x.set_position(pos_x-x.width/2,pos_y-x.height/2)

    x.set_sequence_time(0,7,50)
    bloodsplats.append(x)

def UpdateParticles():
    for b in bloodsplats:
        if(b.get_curr_frame() == b.get_final_frame()-1):
            bloodsplats.remove(b)
        else:
            b.update()
            b.draw()
