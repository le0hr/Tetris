import random, time, os
from pynput.keyboard import Key, Listener
import pygame
import math

class Brick:
    def __init__(self):
        self.Rotation = 0
        self.color = 0
        self.fig = [[0,0],[0,0],[0,0],[0,0]]
        self.clone = 0
        self.figID = 0
        self.v = 0
        self.delta = 0
        self.wait = 0.15
        self.FPS = 5

        self.fill()
    def fill(self):
        #Перший eлемент -- лівий іерхній край фігури!!
        self.figID = random.randint(0,6)
        print(self.figID)
        if self.figID == 0:
            self.color = (255,128,0)
            self.fig = [[[-3,4],[-2,4],[-1,4],[-1,5]],
                        [[-2,3],[-2,4],[-2,5],[-1,3]],
                        [[-3,3],[-3,4],[-2,4],[-1,4]],
                        [[-1,3],[-1,4],[-1,5],[-2,5]]]
        elif self.figID == 1:
            self.color = (0,0,255)
            self.fig = [[[-3,4],[-2,4],[-1,4],[-1,3]],
                        [[-1,3],[-1,4],[-1,5],[-2,3]],
                        [[-3,4],[-3,3],[-2,3],[-1,3]],
                        [[-2,3],[-2,4],[-2,5],[-1,5]]]
        elif self.figID == 2:
            self.color = (255,0,0)
            self.fig = [[[-2,4],[-2,5],[-1,5],[-1,6]],
                        [[-2,4],[-2,5],[-3,5],[-1,4]],
                        [[-2,4],[-2,5],[-1,5],[-1,6]],
                        [[-2,4],[-2,5],[-3,5],[-1,4]]]
        elif self.figID == 3:
            self.color = (0,255,0)
            self.fig = [[[-2,5],[-2,6],[-1,4],[-1,5]],
                        [[-3,4],[-2,4],[-2,5],[-1,5]],
                        [[-2,5],[-2,6],[-1,4],[-1,5]],
                        [[-3,4],[-2,4],[-2,5],[-1,5]]]
        elif self.figID == 4:
            self.color = (255,255,0)
            self.fig = [[[-2,4],[-2,5],[-1,4],[-1,5]],
                        [[-2,4],[-2,5],[-1,4],[-1,5]],
                        [[-2,4],[-2,5],[-1,4],[-1,5]],
                        [[-2,4],[-2,5],[-1,4],[-1,5]]]
            
        elif self.figID == 5:
            self.color = (128,0,255)
            self.fig = [[[-2,4],[-2,5],[-2,6],[-1,5]],
                        [[-2,4],[-2,5],[-3,5],[-1,5]],
                        [[-1,4],[-1,5],[-1,6],[-2,5]],
                        [[-3,4],[-2,4],[-1,4],[-2,5]]]
        elif self.figID == 6:
            self.color = (0,255,255)
            self.fig = [[[-4,4],[-3,4],[-2,4],[-1,4]],
                        [[-1,3],[-1,4],[-1,5],[-1,6]],
                        [[-4,4],[-3,4],[-2,4],[-1,4]],
                        [[-1,3],[-1,4],[-1,5],[-1,6]]]
            

    def Copy(self, arr, x, y, z, a):    #Функція копіювання списків
        qq = [[["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]]]

        qqq = [[[-2,4],[-2,5],[-2,6],[-1,5]],
                            [[-2,4],[-2,5],[-3,5],[-1,5]],
                            [[-1,4],[-1,5],[-1,6],[-2,5]],
                            [[-3,4],[-2,4],[-1,4],[-2,5]]]
        if a == 1:
            for i in range(x):
                for j in range(y):
                    for q in range(z):
                        qqq[i][j][q] = arr[i][j][q]
            return qqq
        else:
            for i in range(x):
                for j in range(y):
                    for q in range(z):
                        qq[i][j][q] = arr[i][j][q]
            return qq
    



def Fall ( Tetramino, field, static):
        
        field= Tetramino.Copy(static, 17, 10,2, 0)
        for i in range(4):
            for j in range(4):
                Tetramino.fig[j][i][0] += 1
        for i in range(3, -1, -1):
            if Tetramino.fig[Tetramino.Rotation][i][0] >= 0:
                field[Tetramino.fig[Tetramino.Rotation][i][0]][Tetramino.fig[Tetramino.Rotation][i][1]][0] = "[]"
                field[Tetramino.fig[Tetramino.Rotation][i][0]][Tetramino.fig[Tetramino.Rotation][i][1]][1] = Tetramino.figID

        
            else:   
                pass

        return field

def render(field, screen):
    screen.fill((0,0,0))
    for i in range(9):
        pygame.draw.line(screen, (11,11,11), (40 + i*(8+40), 0),(40+i*(8+40), 808), 8 )
    for i in range(16):
        pygame.draw.line(screen, (11,11,11), (0, 40 + i*(8+40)),(480,40+i*(8+40)), 8 )
    for i in range(10):
        for j in range(17):
            if field[j][i][0] == "[]":
                if field[j][i][1]== 0:
                    rgb = (255,128,0)
                elif field[j][i][1] == 1:
                    rgb = (0,0,255)
                elif field[j][i][1] == 2:
                    rgb = (255,0,0)
                elif field[j][i][1] == 3:
                    rgb = (0,255,0)
                elif field[j][i][1] == 4:
                    rgb = (255,255,0)
                elif field[j][i][1] == 5:
                    rgb = (128,0,255)
                elif field[j][i][1] == 6:
                    rgb = (0,255,255)
                
                rect = pygame.Rect(i*48, j*48, 40, 40)
                pygame.draw.rect(screen, rgb, rect, 40)
    os.system("color 2")
    os.system("cls")
    for i in range(17):
        for j in range(9):
            print(field[i][j][0], end=" ")
        print("\n")

    

    pygame.display.flip()

def move(Tetramino, static, field):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os.abort()
            if event.type == pygame.KEYDOWN:
                yOfBlocks = []
                xOfBlocks = []
                colission = False
                for i in range(4):
                    yOfBlocks.append(Tetramino.fig[Tetramino.Rotation][i][0])
                    xOfBlocks.append(Tetramino.fig[Tetramino.Rotation][i][1])
                if max(yOfBlocks) !=16:
                    if event.key == pygame.K_LEFT:
                        field= Tetramino.Copy(static, 17, 10,2, 0)
                        for i in range(4):
                            if Tetramino.fig[Tetramino.Rotation][i][1]-1 <0 or field[Tetramino.fig[Tetramino.Rotation][i][0]+1][Tetramino.fig[Tetramino.Rotation][i][1]-1][0] == "[]" or Tetramino.fig[Tetramino.Rotation][i][1]-1 <0:
                                break
                        else:
                            for j in range(4):
                                for i in range(4):
                                    Tetramino.fig[j][i][1]-=1
                                    field[Tetramino.fig[Tetramino.Rotation][i][0]][Tetramino.fig[Tetramino.Rotation][i][1]][0] = "[]"
                    elif event.key == pygame.K_RIGHT:
                        field= Tetramino.Copy(static, 17, 10,2, 0)
                        for i in range(4):
                            if Tetramino.fig[Tetramino.Rotation][i][1]+1 >9 or field[Tetramino.fig[Tetramino.Rotation][i][0]+1][Tetramino.fig[Tetramino.Rotation][i][1]+1][0] == "[]" or Tetramino.fig[Tetramino.Rotation][i][1]+1 >9:
                                break
                        else:
                            for j in range(4):
                                for i in range(4):
                                    Tetramino.fig[j][i][1]+=1
                                    field[Tetramino.fig[Tetramino.Rotation][i][0]][Tetramino.fig[Tetramino.Rotation][i][1]][0] = "[]"
                    elif event.key == pygame.K_UP:
                        for i in range(4):
                             if Tetramino.fig[(Tetramino.Rotation+1)%4][i][1]>=0 and Tetramino.fig[(Tetramino.Rotation+1)%4][i][1]<=0 and static[Tetramino.fig[(Tetramino.Rotation+1)%4][i][0]+1][Tetramino.fig[(Tetramino.Rotation+1)%4][i][1]] == "[]":
                                 colission = True
                        if colission== False:
                            field= Tetramino.Copy(static, 17, 10,2, 0)
                            for i in range(4):
                                if Tetramino.fig[(Tetramino.Rotation+1)%4][i][1]+1 >9 or field[Tetramino.fig[(Tetramino.Rotation+1)%4][i][0]+1][Tetramino.fig[(Tetramino.Rotation+1)%4][i][1]][0] == "[]":
                                    break
                            else:
                                Tetramino.Rotation = (Tetramino.Rotation + 1)%4
                                for j in range(4):
                                    field[Tetramino.fig[Tetramino.Rotation][i][0]][Tetramino.fig[Tetramino.Rotation][i][1]][0] = "[]"

    return field

def Check(Tetramino,static):
    try:
        for i in range (4):
            n = 1
            if Tetramino.fig[Tetramino.Rotation][i][0]+1 >16:
                return False
            
            if Tetramino.fig[Tetramino.Rotation][i][0]+1 < 0:
                while Tetramino.fig[Tetramino.Rotation][i][0]+n != 0:
                    n+=1                                        

            if static[Tetramino.fig[Tetramino.Rotation][i][0]+n][Tetramino.fig[Tetramino.Rotation][i][1]][0] =="[]":
                raise IndexError
        return True
                     
    except IndexError:
        
        return False

def clear(field):
    for i in range(17):
        n = 0
        for j in range(10):
            if field[i][j][0] == "..":
                break
            else:
                n+=1
                if n==10:
                    for q in range (10):
                            field[i][q][0] = ".."
                    for q in range(i, 0, -1):
                        for u in range(10):
                            for o in range(2):
                                field[q][u][o] = field[q-1][u][o]
                                field[q-1][u][0] = ".."
        

    return field

def start(screen):    
    Gameover = 0
    field = [[["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]]]

    static= [[["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
        [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]],
         [["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0],["..", 0]]]
    while True:
        Tetramino = Brick()
        while True:
            
            InAir = Check(Tetramino,static)
            if InAir == False:
                if Tetramino.fig[Tetramino.Rotation][0][0]<0:
                    Gameover = True
                static = field
                break
            field = move(Tetramino, static, field)
            a = time.time()
            field = Fall( Tetramino, field, static) 
            
            time.sleep(math.fabs(1/Tetramino.FPS))   

            render(field,screen)
        if Gameover:
            GOSurface = pygame.Surface((480, 808))
            GOSurface.fill((0,0,0))
            GOSurface.set_alpha(200)
            sourceGO_image = pygame.image.load('pic\—Pngtree—game over pixel transparent background_5995763.png').convert_alpha()
            GameOver_image = pygame.transform.scale(sourceGO_image, (320, 320))
            GOSurfaceIMG = pygame.Surface((320, 320))
            GOSurfaceIMG.blit(GameOver_image, (0,0))
            GOSurface.blit(GOSurfaceIMG, (80, 244))
            screen.blit(GOSurface, (0,0))
            break
    