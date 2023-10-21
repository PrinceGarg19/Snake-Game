# SNAKE GAME ( PYTHON I PROJECT )

import pygame
import pyautogui
import random
import os
pygame.init()

Homes_path = os.find_data_file("Home.wav")
foods_path = os.find_data_file("food.wav")
musics_path = os.find_data_file("music.wav")
Buttonspath = os.find_data_file("Button.wav")
Game_overs_path = os.find_data_file("Game_over.wav")
font1_path = os.find_data_file("font_1.ttf")
font2_path = os.find_data_file("font_2.ttf")
font3_path = os.find_data_file("font_3.ttf")
front_path = os.find_data_file("front.jpg")
cross_path = os.find_data_file("cross.png")
main_path = os.find_data_file("main.jpg")
instruct_path = os.find_data_file("instruct.jpg")
food_path = os.find_data_file("food.jpg")

# Sounds
Home_sound = pygame.mixer.Sound("Homes_path")
Food_sound = pygame.mixer.Sound("foods_path")
main_sound = pygame.mixer.Sound("musics_path")
button_sound = pygame.mixer.Sound("Buttons_path")
end_sound = pygame.mixer.Sound("Game_overs_path")

# Colors
white = (255, 255, 255)
dark_red = (200,0,0)
green = (0,200,0)
voilet = (176,18,255)
blue = (0,80,255)
dark_blue = (0,0,200)
black = (0, 0, 0)
red = (255,0,0)
bright_green = (0,255,0)

# Game variables
screen_width = 900
screen_height = 600
clock = pygame.time.Clock()
pause = False
sound = True
exit_game = False
fps = 30
l = int(screen_height/20)

# fonts
score_f = pygame.font.Font(r"font1_path",40)
score_main_f = pygame.font.SysFont(None,30)
button_f = pygame.font.Font(r"font3_path",30)
Big = pygame.font.Font(r"font2_path",int(80*screen_height*screen_width/540000))

#screen
gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game With Prince")
pygame.display.flip()

#Images
image = pygame.image.load(r"front_path")
image = pygame.transform.scale(image, (screen_width,screen_height)).convert_alpha()
cross = pygame.image.load(r"cross_path")
cross = pygame.transform.scale(cross, (int(screen_width/30),int(screen_height/20))).convert_alpha()
image_instruct = pygame.image.load(r"instruct_path")
image_instruct = pygame.transform.scale(image_instruct, (screen_width,screen_height)).convert_alpha()
image_main = pygame.image.load(r"main_path")
image_main = pygame.transform.scale(image_main, (screen_width-l-l,screen_height-l-l)).convert_alpha()


def text_object(text ,font, color , x,y ,w =0 , h= 0):
    text = font.render(text, True, color)
    textrect = text.get_rect()
    textrect.center = ( int((x+(w/2))), int((y+(h/2))) )
    gamewindow.blit(text, textrect)
def plot_snake(gamewindow, color, snake_list, size):
    for x,y in snake_list:
        pygame.draw.circle(gamewindow, color, (x,y) , size)
def line(l,image,image_main):
    gamewindow.blit(image, (0,0))
    gamewindow.blit(image_main, (l,l))
    pygame.draw.line(gamewindow,black, (l,l), (screen_width-l,l))
    pygame.draw.line(gamewindow,black, (l,l), (l,screen_height-l))
    pygame.draw.line(gamewindow,black, (screen_width-l,l), (screen_width-l,screen_height-l))
    pygame.draw.line(gamewindow,black, (l,screen_height-l), (screen_width-l,screen_height-l))
def quitgame():
    pygame.quit()
    quit()
def unpaused():
    global pause
    pause = False
def paused():
    global pause,sound,fps
    ins = None
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pos = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            music(pos,click,main_sound)
            if int(8*screen_width/9)<pos[0]<int(825*screen_width/900) and 0<pos[1]<l:
                if click[0] == 1:
                    ins = True
        if ins:
            gamewindow.blit(image_instruct,(0,0))
            s = button("Back",5*screen_width/6,7*screen_height/8,100,40,green,bright_green,None)
            if s:
                ins = False
        else:
            gamewindow.blit(image, (0,0))
            gamewindow.blit(image_main, (l,l))
            text_object(" Game Paused ",Big,black,screen_width/2,screen_height/3)
            button("Continue",screen_width/4,screen_height/2+l,150,60,dark_blue,blue,unpaused)
            button("Quit Game",screen_width/2+ 2*l ,screen_height/2+l,170,60,dark_red,red,quitgame)
        if sound == False :
            gamewindow.blit(cross,(screen_width-l-30,-1))
        pygame.display.update()
        clock.tick(fps)
def button(msg,x,y,w,h,i_color,f_color,action=None):
    x,y,w,h = int(x),int(y),int(w),int(h)
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse_pos[0] > x and y+h > mouse_pos[1] > y:
        pygame.draw.rect(gamewindow, i_color,(x+1,y+1,w+2,h+2))
        pygame.draw.rect(gamewindow, f_color,(x,y,w,h))
        if click[0] == 1 and action != None:
            end_sound.stop()
            button_sound.play()
            action()
        elif click[0] == 1 and action == None:
            return True
    else:
        pygame.draw.rect(gamewindow, i_color,(x+2,y+2,w+4,h+4))
        pygame.draw.rect(gamewindow, f_color,(x,y,w,h))

    text_object(msg, button_f,black,x,y,w,h)
def music(pos,click,obj = main_sound):
    global sound,l,pause
    if (screen_width-l-30)<pos[0]<(screen_width-l) and 0<pos[1]<l:
        if click[0] == 1:
            if sound!=False:
                pygame.mixer.stop()
                sound = False
            else:
                obj.play()
                sound = True
    if int(8*screen_width/9)<pos[0]<int(825*screen_width/900) and 0<pos[1]<l:
        if click[0] == 1:
            pause = True
    return
def welcome(): # change (home screen)
    global sound,fps,exit_game,pause
    if sound:
        Home_sound.play()
        main_sound.stop()
    while not exit_game:
        gamewindow.fill(white)
        gamewindow.blit(image,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game = True
                quitgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()
            pos = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if int(210*screen_width/900) <pos[0] < int(412*screen_width/900) and int(390*screen_height/600) <pos[1]< int(480*screen_height/600):
                if click[0] == 1:
                    game_loop()
            music(pos,click,Home_sound)

        if not sound:
            gamewindow.blit(cross,(screen_width-l-30,-1))
        elif pause:
            gamewindow.blit(image_instruct,(0,0))
            button("Back",5*screen_width/6,7*screen_height/8,100,40,green,bright_green,unpaused)
        # Screen_score("Welcome to Snake World", voilet, 260, 150)
        # Screen_score("Press button to play the game.", blue, 220, 200)
        # button("Quit", 510 , 270, 70, 40,bright_red, red, "Quit")
        # button("Play", 270 , 270, 70, 40, green, bright_green, "Play")
        pygame.display.update()
        clock.tick(fps)


# (main screen)
def game_loop():
#game variables....
    global pause, l, sound, fps, exit_game
    game_over = False
    Score = 0
    High_score = 0
    snake_x = 200
    snake_y = 200
    snake_length = 1
    snake_list = []
    snake_size = 10
    food_size = 25
    velocity_x = 0
    velocity_y = 0
    velocity = 5
    indet = screen_height/4
    Home_sound.stop()
    if sound:
        main_sound.play()
        main_sound.set_volume(0.4)
    food_x = random.randint(l, screen_width-l-food_size)
    food_y = random.randint(l+food_size, screen_height-l-food_size)
    image_food = pygame.image.load(r"food_path")
    image_food = pygame.transform.scale(image_food, (food_size,food_size)).convert_alpha()
    image_end = pygame.transform.scale(image_main, (screen_width,screen_height)).convert_alpha()
    try:
        with open("Score.txt", "r") as f:
            High_score = f.read()
    except:
        with open("Score.txt","w+") as f:
            f.write(str(0))
# Game Loop 
    while not exit_game:
        line(l,image,image_main)
        rect_food = pygame.Rect(food_x,food_y,food_size,food_size)

        # Game over code......(End screen)
        if game_over:
            main_sound.stop()
            gamewindow.blit((image_end),(0,0))
            if Score > int(High_score):
                text_object("Well Done", Big , black,screen_width/2, screen_height/4)
                text_object("New HighScore : " + str(Score), score_f , black ,(screen_width/2), (screen_height/4) + indet)
            else:
                text_object("Game Over", Big , black,(screen_width/2), screen_height/4)
                text_object("Score: "+ str(Score) + "   High Score: "+ str(High_score), score_f , black ,(screen_width/2), (screen_height/4) + indet)
            
            button("Home", screen_width/5 , screen_height/4 + 2*indet, 150, 50,dark_red, red, welcome)
            button("Play Again", 3*screen_width/5 , (screen_height/4) + (2*indet), 200, 50,dark_blue,blue,game_loop)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game = True
                    quitgame()
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
                pos = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                music(pos,click)
                
        else:
        # control amd movement code...
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game = True
                    quitgame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and velocity_x != -velocity:
                        velocity_x = velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT and velocity_x != velocity:
                        velocity_x = -velocity
                        velocity_y = 0
                    if event.key == pygame.K_DOWN and velocity_y != -velocity:
                        velocity_y = velocity
                        velocity_x = 0
                    if event.key == pygame.K_UP and velocity_y != velocity:
                        velocity_y = -velocity
                        velocity_x  = 0
                    if event.key == pygame.K_SPACE:
                        pause = True
                        paused()
                pos = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                music(pos,click)
            snake_x += velocity_x
            snake_y += velocity_y

        # food and score code.......
            if abs(rect_food.center[0] - snake_x) < (snake_size + food_size)/2:
                if abs(rect_food.center[1] - snake_y) < (snake_size + food_size)/2:
                    pygame.mixer.Sound.play(Food_sound)  
                    Score += 10
                    snake_length += 8
                    food_x = random.randint(l, screen_width-l-food_size)
                    food_y = random.randint(l+food_size, screen_height-l-food_size)
            gamewindow.blit(image_food, (food_x,food_y))
            if Score > int(High_score):
                text_object("Score : " + str(Score), score_main_f, black ,screen_width/6,l/2)
                with open("Score.txt", "w") as f:
                    f.write(str(Score)) 
            else:
                text_object("Score: "+ str(Score), score_main_f, black ,screen_width/8,l/2)
                text_object("High Score: "+ str(High_score), score_main_f, black ,screen_width/8,(screen_height-l)+15)
            text_object("Use Spacebar to Pause the game." ,score_main_f, black , screen_width/2,l/2)
            
        # snake length increament code......
            snake_list.append([snake_x,snake_y])
            if snake_length > 10:
                snake_size = 8
            if len(snake_list)>snake_length:
                del snake_list[0]
            if [snake_x,snake_y] in snake_list[:-1]:
                game_over = True

    # collision code.....
            if snake_x+snake_size >= screen_width-l:
                pyautogui.keyDown("Down")
                snake_x = int(snake_y * (screen_width/screen_height))
                snake_y = l
            elif snake_y <= l:
                snake_y = int((screen_width - snake_x) * (screen_height/screen_width))
                snake_x = l
                pyautogui.keyDown("Right")
            elif snake_x <= l or snake_y >= screen_height-l:
                velocity_x = 0
                velocity_y = 0 
                game_over = True

            plot_snake(gamewindow, black, snake_list, snake_size)
        if not sound:
            gamewindow.blit(cross,(screen_width-l-30,-1))
        if pause:
            gamewindow.blit(image_instruct,(0,0))
            button("Back",5*screen_width/6,7*screen_height/8,100,40,green,bright_green,unpaused)
            text_object("(Caution : Game is running behind.)",score_main_f,black,screen_width/2,(screen_height-l)+15)
        pygame.display.update()
        clock.tick(fps)
welcome()