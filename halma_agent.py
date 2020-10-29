#import numpy as np
din = open('input.txt', 'r+')
game_type = din.readline().split()
#print("game_type : ", game_type[0])
playing_color = din.readline().split()
#print("color to play : ",playing_color[0])
ttime = din.readline().split()
total_time = float(ttime[0])
#print("total game time  : ", total_time)
board_matrix = []
for i in range(16):
    a = din.readline().split()
    x = a[0]
    bm = [x[b] for b in range(0,len(x))]
    #print("each : ",bm)
    board_matrix.append(bm)
#print(board_matrix)

din.close()
if playing_color[0] == "WHITE":
    player_turn = "W"
elif playing_color == "BLACK":
    player_turn = "B"
pawn_location = dict()
parent_child = dict()

class halma_agent:
    def __init__(self):
#        self.initiate_halma_agent()
        pass
    def initiate_halma_agent(self):
        self.initial_configuration = board_matrix
#        print(self.initial_configuration)
        self.halma_agent_turn = player_turn
#        print("halma agent palyer colour : ", self.halma_agent_turn)
        pawn_location.clear()
        for i in range(16):
            #print(i)
            for j in range(16):
                if self.initial_configuration[j][i] == player_turn:
                    #print("configuration : ",i,j)#location of pawns
                    pawn_location.update({(j,i) : 1})
        #print("location of pawns : ", pawn_location.keys())
        for i in pawn_location:
            self.current = i
#            print(self.current)
            self.currenty,self.currentx = i[0],i[1]
            #print(self.currenty,self.currentx)
            self.matrix_mover(self.currenty,self.currentx)

    def matrix_mover(self,currenty,currentx):
        self.initial_configuration = board_matrix
        self.currenty,self.currentx = currenty,currentx
        print("mover : ",self.currenty,currentx)
        for j in range(self.currenty-1,self.currenty+2):
            for k in range(self.currentx-1,self.currentx+2):
                if j >= 0 and k >=0 and j <= 15 and k <= 15 and (self.currenty,self.currentx) != (j,k):
                    if self.initial_configuration[j][k] == ".":
                        parent_child.setdefault((self.currenty,self.currentx), []).append((j,k))
                        #parent_child.update({(self.currenty,self.currentx) : (j,k)})
                        #print("E : ", parent_child)       
                    elif self.initial_configuration[j][k] == "W" or "B":                         
                        self.jump_move_interator(self.currenty,self.currentx,j,k)

    def jump_move_interator(self,yold,xold,cuy,cux):
        self.initial_configuration = board_matrix
        self.yold = yold
        self.xold = xold
        self.cuy = cuy
        self.cux = cux
        newy,newx = self.yold - (self.yold-self.cuy) * 2 ,self.xold - (self.xold-self.cux)*2
        if newy >= 0 and newx >=0 and newy <= 15 and newx <= 15:
            if self.initial_configuration[newy][newx] == ".":
                parent_child.setdefault((self.yold,self.xold), []).append((newy,newx))
                self.matrix_mover(newy,newx)
                #print("J : ", parent_child)
            elif self.initial_configuration[newy][newx] == "B" or self.initial_configuration[newy][newx] == "W":
                return
    #print("parent child relationship dict : ",parent_child)
    print("E : ", parent_child)
"""        
        for j in range(self.cuy-1,self.cuy+2):
                for k in range(self.cux-1,self.cux+2):
                    if j,k >= 0 and j,k <= 15 and (self.cuy,self.cux) != (j,k):
                        if self.initial_configuration[j][k] == ".":
                            self.jump_move_iterator
                        elif self.initial_configuration[j][k] == "W" or "B":
                            self.jump_move_iterator(k,j)
    def 
"""

h = halma_agent()
h.initiate_halma_agent()

"""
dout = open('output.txt', 'w+')
dout.write("hello")
dout.write("hi")
dout.close()
"""
