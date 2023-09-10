import pygame
import math
pygame.init()
WIDTH, HEIGHT = 700, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brat robotic")
FONT = pygame.font.SysFont("comicsans", 16)
from decimal import Decimal

class invers:
    
    def __init__(self,x,y,lenght):
        self.lenght=lenght
        self.bx=x
        self.by=y
        
    def setA(self, x,y):
        #self.b=pos
        self.follow(x,y,0)
        
        
    def follow(self,tx,ty,z):
        #self.tx,self.ty = pygame.mouse.get_pos()
        
        if z==1:
            self.tx=tx
            self.ty=ty
            self.bx=self.tx+self.cal_lungimex(self.tx,self.ty)
            self.by=self.ty-self.cal_lungimey(self.tx,self.ty)
            self.b = [self.bx,self.by]
        else:
            self.bx=tx
            self.by=ty
            self.tx=self.bx+self.cal_lungimex1(self.bx,self.by)
            self.ty=self.by-self.cal_lungimey1(self.bx,self.by)
            self.b = [self.bx,self.by]
        

    def draw(self, win,i):
        if i==1:
            pygame.draw.line(win, "blue",(self.tx,self.ty),self.b,2)
        else:
            pygame.draw.line(win, "white",(self.tx,self.ty),(self.bx,self.by),2)
        #print(self.b)
           
        pygame.draw.rect(win, "white",(560,10,150,300),2)
        #Desenare coordonate
    
    
    def cal(self,  x,y):

        u=math.atan2(x,y)
        u=u-math.radians(90)
        #print(math.degrees(u))
        return u
    def cal_lungimex(self,x,y):
        #print(math.degrees(self.cal(self.bx-x,self.by-y)))
        return (self.lenght*math.cos(self.cal(self.bx-x,self.by-y)))
    def cal_lungimey(self,x,y):
        return (self.lenght*math.sin(self.cal(self.bx-x,self.by-y)))
    def cal_lungimex1(self,x,y):
        #print(math.degrees(self.cal(self.tx-x,self.ty-y)))
        return (self.lenght*math.cos(self.cal(self.tx-x,self.ty-y)))
    def cal_lungimey1(self,x,y):
        return (self.lenght*math.sin(self.cal(self.tx-x,self.ty-y)))

def main():
    run = True
    Segment=[]
    clock= pygame.time.Clock()
    nr=5
    #for i in range(nr):
        #Segment.append(invers(350, 700, 2))
    
    Segment.append(invers(100, 0, 100))#700
    Segment.append(invers(70, 0, 200))#700-220+310
    Segment.append(invers(70, 0, 200))#700-220
    Segment.append(invers(70, 0, 100))#700-220
    Segment.append(invers(70, 0, 100))#700-220
    while run:    
        WIN.fill((0,1,0))
        pygame.draw.line(WIN, "white",(0,700),(0,580),100)
        pygame.draw.line(WIN, "white",(0,580),(70,480),10)
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        tx,ty= pygame.mouse.get_pos()
        Segment[0].follow(tx,ty,1)
        for i in list(range(1,nr)):
            Segment[i].follow(Segment[i-1].bx,Segment[i-1].by,1)
        
        #Segment[nr-1].setA(350,350)
        Segment[nr-1].setA(70,700-220)
        for i in range(nr-2,-1,-1):
            Segment[i].setA(Segment[i+1].tx,Segment[i+1].ty)
        #Desenare linii
        for i in range(0,nr):
            Segment[i].draw(WIN,i)
        #print ("---------------------")
        #Desenare ultima coordonata 
        #'''
        distance_text = FONT.render(f"{round(Segment[0].tx, 1),round(Segment[0].ty, 1)}", 1, "white")
        WIN.blit( distance_text, (570, 40))
        #'''
        #Desenare unghiuri
        distance_text = FONT.render(f"Unghiuri", 1, "white")
        WIN.blit( distance_text, (570, 180))
        for i in range(0,nr-1):
            #print(Segment[0].tx)
            x2,y2=Segment[i].tx-Segment[i].bx,Segment[i].by-Segment[i].ty
            x1,y1=Segment[i+1].bx-Segment[i+1].tx,Segment[i+1].ty-Segment[i+1].by
            angle=math.atan2( x1*y2-y1*x2, x1*x2+y1*y2 )
            angle=math.degrees(angle)
            if angle<0:
                angle=360+angle
            distance_text = FONT.render(f"Joint{nr-i}:{round(angle, 2)}", 1, "white")
            WIN.blit( distance_text, (570, 180+(i+1)*20))
        x1,y1=10,0
        x2,y2=Segment[nr-1].tx-Segment[nr-1].bx,-Segment[nr-1].ty+Segment[nr-1].by
        angle=math.atan2( x1*y2-y1*x2, x1*x2+y1*y2 )
        angle=math.degrees(angle)
        if angle<0:
            angle=360+angle
        distance_text = FONT.render(f"Joint{nr-nr}:{round(angle, 2)}", 1, "white")
        WIN.blit( distance_text, (570, 260))
        
        
        pygame.display.update()
    pygame.quit()

main()
