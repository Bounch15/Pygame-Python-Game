import pygame, sys, time, random, pickle, os
from pygame.locals import *
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

gameDisplay = pygame.display.set_mode((500,500))
pygame.display.set_caption('Python Game')
fps = pygame.time.Clock()
gameIcon = pygame.image.load("pythongameicon1.png")
pygame.display.set_icon(gameIcon)
title = pygame.image.load("title.png")
config_image = pygame.image.load("config.png")
difficulty_image = pygame.image.load("difficulty_image.png")
deathsound = pygame.mixer.Sound("deathsound.wav")
menuback = pygame.mixer.Sound("menuback.wav")
menuin = pygame.mixer.Sound("menuin.wav")
menuin2 = pygame.mixer.Sound("menuin2.wav")
scoresound = pygame.mixer.Sound("scoresound.wav")
font = pygame.font.SysFont('segoeuisemibold', 20)
font2 = pygame.font.SysFont(None, 30)
game_difficulty=15
random_c=False
high_score=0

#Colors
white = (255, 255, 255) 
green = (14, 116, 41)
bright_green = (0,255,0)
blue = (0, 0, 128)
sky_blue=(36, 205, 193)
black = (0,0,0)
red = (255,0,0)
bright_red = (200,0,0)
grey = (184, 184, 184)
python_color = (237, 124, 25)
dark_grey = (99, 98, 97)
skin_color=python_color
rainbow=((148, 0, 211),(75, 0, 130),(0, 0, 255),(0, 255, 0),(255, 255, 0),(255, 127, 0),(255, 0 , 0))

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac):

    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont('segoeuisemibold',20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
def button2(msg,x,y,w,h,ic,ac):

    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont('segoeuisemibold',15)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def menu():
    menuExit = False    
    while not menuExit:

        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menuback.play()
                    pygame.quit()
                    quit()
                if event.key==K_RETURN and 200+120 > mouse[0] > 200 and 210+50 > mouse[1] > 210:
                    menuin2.play()
                    game_loop()                   
                if event.key==K_RETURN and 200+120 > mouse[0] > 200 and 285+50 > mouse[1] > 285:
                    menuin.play()                    
                    config()
                if event.key==K_RETURN and 200+120 > mouse[0] > 200 and 360+50 > mouse[1] > 360:
                    quit()          
                if event.key==K_RETURN and 410+85 > mouse[0] > 410 and 460+35 > mouse[1] > 460:
                    menuin.play()
                    stats()                          

            if event.type==MOUSEBUTTONDOWN and 200+120 > mouse[0] > 200 and 210+50 > mouse[1] > 210:
                menuin2.play()
                game_loop()
            if event.type==MOUSEBUTTONDOWN and 200+120 > mouse[0] > 200 and 285+50 > mouse[1] > 285:
                menuin.play()
                config()
            if event.type==MOUSEBUTTONDOWN and 200+120 > mouse[0] > 200 and 360+50 > mouse[1] > 360:
                menuback.play()
                quit()
            if event.type==MOUSEBUTTONDOWN and 410+85 > mouse[0] > 410 and 460+35 > mouse[1] > 460:
                menuin.play()
                stats()                

        gameDisplay.fill(dark_grey)
        gameDisplay.blit(title, (-2,0))
        button("PLAY",200,210,120,50,black,grey)
        button("CONFIG",200,285,120,50,black,grey)
        button("EXIT",200,360,120,50,black,bright_red)
        button("Stats",410,460,85,35,dark_grey,grey)

        fps.tick(30)
        pygame.display.update()

def config():

    configExit = False
    while not configExit:

        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menuback.play()
                    menu()
                if event.key==K_RETURN and 200+120 > mouse[0] > 200 and 210+50 > mouse[1] > 210:
                    menuin.play()                    
                    difficulty()                
                if event.key==K_RETURN and 200+120 > mouse[0] > 200 and 285+50 > mouse[1] > 285:
                    menuin.play()
                    color()   
                if event.key==K_RETURN and 200+120 > mouse[0] > 200 and 360+50 > mouse[1] > 360:
                    menuback.play()    
                    menu()

            if event.type==MOUSEBUTTONDOWN and 200+120 > mouse[0] > 200 and 210+50 > mouse[1] > 210:
                menuin.play()                
                difficulty()
            if event.type==MOUSEBUTTONDOWN and 200+120 > mouse[0] > 200 and 285+50 > mouse[1] > 285:
                menuin.play()   
                color()
            if event.type==MOUSEBUTTONDOWN and 200+120 > mouse[0] > 200 and 360+50 > mouse[1] > 360:
                menuback.play()
                menu()

        gameDisplay.fill(dark_grey)
        gameDisplay.blit(config_image, (3,0))
        button("DIFFICULTY",200,210,120,50,black,grey)
        button("COLOR",200,285,120,50,black,grey)
        button("BACK",200,360,120,50,black,bright_red)

        fps.tick(30)
        pygame.display.update()

def difficulty():
    global game_difficulty

    difficultyExit = False
    while not difficultyExit:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menuback.play()
                    config()
                if event.key==K_RETURN and 200+120 > mouse[0] > 200 and 170+50 > mouse[1] > 170:
                    menuin.play()
                    game_difficulty=10   
                if event.key==K_RETURN and 200+120 > mouse[0] > 200 and 245+50 > mouse[1] > 245:
                    menuin.play() 
                    game_difficulty=15
                if event.key==K_RETURN and 200+120 > mouse[0] > 200 and 320+50 > mouse[1] > 320:
                    menuin.play()
                    game_difficulty=20           
                if event.key==K_RETURN and 200+120 > mouse[0] > 200 and 395+50 > mouse[1] > 395:
                    menuback.play()
                    config()

            if event.type==MOUSEBUTTONDOWN and 200+120 > mouse[0] > 200 and 170+50 > mouse[1] > 170:
                menuin.play()
                game_difficulty=10  
            if event.type==MOUSEBUTTONDOWN and 200+120 > mouse[0] > 200 and 245+50 > mouse[1] > 245:
                menuin.play()
                game_difficulty=15   
            if event.type==MOUSEBUTTONDOWN and 200+120 > mouse[0] > 200 and 320+50 > mouse[1] > 320:
                menuin.play()
                game_difficulty=20 
            if event.type==MOUSEBUTTONDOWN and 200+120 > mouse[0] > 200 and 395+50 > mouse[1] > 395:
                menuback.play()
                config()

        gameDisplay.fill(dark_grey)
        gameDisplay.blit(difficulty_image, (3,-20))
        button("Easy",200,170,120,50,black,grey)
        button("Normal",200,245,120,50,black,grey)
        button("HARD",200,320,120,50,black,grey)
        button("BACK",200,395,120,50,black,bright_red)
        if game_difficulty==10:
            pygame.draw.rect(gameDisplay,white,(210,190,10,10))
        if game_difficulty==15:
            pygame.draw.rect(gameDisplay,white,(210,265,10,10))
        if game_difficulty==20:
            pygame.draw.rect(gameDisplay,white,(210,340,10,10))

        fps.tick(30)
        pygame.display.update()

def color():
    f=open("record_score_file.txt","r")
    r=open("total_apple_file.txt","r")
    v=open("total_deaths_file.txt","r")
    record_score= int(f.read())
    total_apple= int(r.read())
    total_deaths= int(v.read())
    global skin_color, random_c

    colorExit=False
    while not colorExit:

        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menuback.play()
                    config()
                if event.key==K_RETURN and 200+120 > mouse[0] > 200 and 115+50 > mouse[1] > 115:
                    menuin.play()
                    random_c=False   
                    skin_color=python_color
                if event.key==K_RETURN and 200+120 > mouse[0] > 200 and 190+50 > mouse[1] > 190 and record_score>=25:
                    menuin.play()
                    random_c=False   
                    skin_color=white
                if event.key==K_RETURN and 200+120 > mouse[0] > 200 and 265+50 > mouse[1] > 265 and total_apple>=100:
                    menuin.play()
                    random_c=False  
                    skin_color=bright_green
                if event.key==K_RETURN and 200+120 > mouse[0] > 200 and 340+50 > mouse[1] > 340 and record_score>=50:
                    menuin.play()  
                    random_c=False       
                    skin_color=sky_blue
                if event.key==K_RETURN and 200+120 > mouse[0] > 200 and 415+50 > mouse[1] > 415:
                    menuback.play()
                    config()

            if event.type==MOUSEBUTTONDOWN and 200+120 > mouse[0] > 200 and 115+50 > mouse[1] > 115:
                menuin.play()
                random_c=False
                skin_color=python_color
            if event.type==MOUSEBUTTONDOWN and 200+120 > mouse[0] > 200 and 190+50 > mouse[1] > 190 and record_score>=25:
                menuin.play()
                skin_color=white
            if event.type==MOUSEBUTTONDOWN and 200+120 > mouse[0] > 200 and 265+50 > mouse[1] > 265 and total_apple>=100:
                menuin.play()   
                skin_color=bright_green                
            if event.type==MOUSEBUTTONDOWN and 200+120 > mouse[0] > 200 and 340+50 > mouse[1] > 340 and record_score>=50:
                menuin.play()
                skin_color=sky_blue
            if event.type==MOUSEBUTTONDOWN and 200+120 > mouse[0] > 200 and 415+50 > mouse[1] > 415:
                menuback.play()
                config()
            if event.type==MOUSEBUTTONDOWN and 0+120 > mouse[0] > 0 and 0+50 > mouse[1] > 0:
                menuback.play()
                print("RANDOM")
                random_c=True 

            gameDisplay.fill(dark_grey)
            button("Default",200,115,120,50,black,grey)
            pygame.draw.rect(gameDisplay,python_color,(320,115,10,50))
            if record_score>=25:            
                button("White",200,190,120,50,black,grey)
                pygame.draw.rect(gameDisplay,white,(320,190,10,50))
            else:
                button("Record = 25",200,190,120,50,black,grey)
                pygame.draw.rect(gameDisplay,white,(320,190,10,50))                

            if total_apple>=100:
                button("Green",200,265,120,50,black,grey)
                pygame.draw.rect(gameDisplay,bright_green,(320,265,10,50))
            else:
                button2("100 apples eaten",200,265,120,50,black,grey)
                pygame.draw.rect(gameDisplay,bright_green,(320,265,10,50))

            if record_score>=50:
                button("Blue",200,340,120,50,black,grey)
                pygame.draw.rect(gameDisplay,sky_blue,(320,340,10,50))
            else:
                button("Record = 50",200,340,120,50,black,grey)
                pygame.draw.rect(gameDisplay,sky_blue,(320,340,10,50))
            button("BACK",200,415,120,50,black,bright_red)
            if skin_color==python_color:
                pygame.draw.rect(gameDisplay,white,(207,135,10,10))
            if skin_color==white:
                pygame.draw.rect(gameDisplay,white,(207,210,10,10))
            if skin_color==bright_green:
                pygame.draw.rect(gameDisplay,white,(207,285,10,10))
            if skin_color==sky_blue and record_score>=50:
                pygame.draw.rect(gameDisplay,white,(207,360,10,10))
            
            fps.tick(30)
            pygame.display.update()

def stats():
    f=open("record_score_file.txt","r")
    r=open("total_apple_file.txt","r")
    v=open("total_deaths_file.txt","r")
    record_score= int(f.read())
    total_apple= int(r.read())
    total_deaths= int(v.read())
    reset=False
    global skin_color

    statsExit=False
    while not statsExit:

        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE and reset==True:
                    menuback.play()
                    total_deaths=0
                    record_score=0
                    total_apple=0
                    v=open("total_deaths_file.txt","w") 
                    v.write(str(total_deaths))
                    v.close()
                    f=open("record_score_file.txt","w")
                    f.write(str(record_score))
                    f.close()
                    r=open("total_apple_file.txt","w")
                    r.write(str(total_apple))
                    r.close()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menuback.play()
                    menu()

                if event.key==K_RETURN and 410+85 > mouse[0] > 410 and 460+35 > mouse[1] > 460 and reset==True:
                    menuback.play()
                    total_deaths=0
                    record_score=0
                    total_apple=0
                    v=open("total_deaths_file.txt","w") 
                    v.write(str(total_deaths))
                    v.close()
                    f=open("record_score_file.txt","w")
                    f.write(str(record_score))
                    f.close()
                    r=open("total_apple_file.txt","w")
                    r.write(str(total_apple))
                    r.close()
                    menu()
                if event.key==K_RETURN and 410+85 > mouse[0] > 410 and 460+35 > mouse[1] > 460:
                    menuback.play()
                    menu()
            if event.type==MOUSEBUTTONDOWN and 410+85 > mouse[0] > 410 and 460+35 > mouse[1] > 460 and reset==True:
                menuback.play()
                total_deaths=0
                record_score=0
                total_apple=0
                v=open("total_deaths_file.txt","w") 
                v.write(str(total_deaths))
                v.close()
                f=open("record_score_file.txt","w")
                f.write(str(record_score))
                f.close()
                r=open("total_apple_file.txt","w")
                r.write(str(total_apple))
                r.close()
                menu()   
            if event.type==MOUSEBUTTONDOWN and 410+85 > mouse[0] > 410 and 460+35 > mouse[1] > 460:
                menuback.play()
                menu()

            if event.type==MOUSEBUTTONDOWN and 15+110 > mouse[0] > 15 and 460+35 > mouse[1] > 460:
                menuback.play()
                record_score=0
                total_apple=0
                total_deaths=0
                reset=True

            gameDisplay.fill(dark_grey)
            button("Back",410,460,85,35,dark_grey,red)
            button("Reset Stats",15,460,110,35,dark_grey,red)
            f.read(int(record_score))
            record = font2.render("Record Score: " + str(record_score), 1, white)
            gameDisplay.blit(record, (180,210))
            r.read(int(total_apple))
            total_apple_stat = font2.render("Total apple eaten: " + str(total_apple), 1, white)
            gameDisplay.blit(total_apple_stat, (160,260))
            v.read(int(total_deaths))
            total_death_stat = font2.render("Total deaths: "+str(total_deaths),1, white)
            gameDisplay.blit(total_death_stat, (180,310))
 
            fps.tick(30)
            pygame.display.update()

def food_spawn():
    food_pos = [random.randrange(4,46)*10, random.randrange(4,46)*10]
    return food_pos

def game_loop():
    global game_difficulty
    snake_pos = [100,100]
    snake_body = [[100,100], [90,100], [80,100]]
    direction = "RIGHT"
    change = direction
    food_pos = food_spawn()
    f=open("record_score_file.txt","r")
    record_score= int(f.read())
    r=open("total_apple_file.txt","r")
    total_apple= int(r.read())
    v=open("total_deaths_file.txt","r")
    total_deaths= int(v.read())
    score = 0
    global high_score

    gameExit = False
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #Pause
            if event.type == pygame.KEYDOWN:
                if event.key == K_p or event.key==K_ESCAPE:
                    menuin.play()
                    while 1: 
                        event = pygame.event.wait()
                        text = font.render("GAME PAUSED", 1, white)
                        gameDisplay.blit(text, (180,230))
                        text = font.render("Press [P] to continue or [ESC] to go back", 1, white)
                        gameDisplay.blit(text, (60,270))
                        pygame.display.flip()
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                menuback.play()
                                menu()
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                            menuin2.play()
                            break        

        #Snake Direction
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    change = "RIGHT"
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    change = "LEFT"
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    change = "UP"
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    change = "DOWN"

        if change == "RIGHT" and direction !="LEFT":
            direction = "RIGHT"
        if change == "LEFT" and direction !="RIGHT":
            direction = "LEFT"
        if change == "UP" and direction !="DOWN":
            direction = "UP"
        if change == "DOWN" and direction !="UP":
            direction = "DOWN"

        if direction == "RIGHT":
            snake_pos[0] += 10
        if direction == "LEFT":
            snake_pos[0] -= 10
        if direction == "UP":
            snake_pos[1] -= 10
        if direction == "DOWN":
            snake_pos[1] += 10

        gameDisplay.fill(black)

        #Food and Body

        snake_body.insert(0, list(snake_pos))
        
        if snake_pos == food_pos:
            scoresound.play()
            food_pos = food_spawn()
            score += 1
            total_apple+=1
            game_difficulty+=0.5
            r=open("total_apple_file.txt","w") 
            r.write(str(total_apple))
            r.close()
        else:
            snake_body.pop()

        #Snake Body

        if random_c:
            for pos in snake_body:
                pygame.draw.rect(gameDisplay, (random.choice(rainbow)), pygame.Rect(pos[0], pos[1], 10,10))
        else:
            for pos in snake_body:
                pygame.draw.rect(gameDisplay, (skin_color), pygame.Rect(pos[0], pos[1], 10,10))

        #Food
        if random_c:
            pygame.draw.rect(gameDisplay, (random.choice(rainbow)), pygame.Rect(food_pos[0], food_pos[1], 10,10))
        else:
            pygame.draw.rect(gameDisplay, (red), pygame.Rect(food_pos[0], food_pos[1], 10,10))

        #Wall Limit Colision

        if snake_pos[0] >= 500 or snake_pos[0] <= -1:
            deathsound.play()
            snake_body.clear()
            direction = "RIGHT"
            snake_pos = [100,100]
            snake_body = [[100,100], [90,100], [80,100]]
            score = 0
            total_deaths+=1
            if game_difficulty>20:
                game_difficulty=20
            else:
                game_difficulty=15
            r=open("total_deaths_file.txt","w") 
            r.write(str(total_deaths))
            r.close()
        if snake_pos[1] >= 500 or snake_pos[1] <= 35:
            deathsound.play()
            snake_body.clear()
            direction = "RIGHT"
            snake_pos = [100,100]
            snake_body = [[100,100], [90,100], [80,100]]
            score = 0
            total_deaths+=1
            if game_difficulty>20:
                game_difficulty=20
            else:
                game_difficulty=15
            r=open("total_deaths_file.txt","w") 
            r.write(str(total_deaths))
            r.close()

        #Body Colision

        if snake_pos in snake_body[1:]:
            deathsound.play()
            direction = "RIGHT"
            snake_body.clear()
            snake_pos = [100,100]
            snake_body = [[100,100], [90,100], [80,100]]
            score = 0
            total_deaths+=1
            if game_difficulty>20:
                game_difficulty=20
            else:
                game_difficulty=15
            r=open("total_deaths_file.txt","w") 
            r.write(str(total_deaths))
            r.close()

        #Score Display

        pygame.draw.rect(gameDisplay, white, (0,0,745,40))
        text = font.render("Score: "+ str(score), 1, black)
        gameDisplay.blit(text, (15,10))

        if score>high_score:
            high_score=score

        if high_score>record_score:
            record_score=high_score
            f=open("record_score_file.txt","w") 
            f.write(str(record_score))
            f.close()
        
        text = font.render("High Score: " + str(high_score), 1, black)
        gameDisplay.blit(text, (365,10))
        f=open("record_score_file.txt","r")
        pygame.display.flip()
        fps.tick(game_difficulty)

menu()
game_loop()
pygame.quit()