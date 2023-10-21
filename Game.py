# import pygame
# import time
# from pygame.rect import *
# x = pygame.init()
# #Screen
# l = 30
# screen_width = 900
# screen_height = 600
# gamewindow = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Snake Game With Prince")

# # fonts
# image = pygame.image.load(r"C:\Users\princ\Documents\instruct.jpg")
# image = pygame.transform.scale(image, (screen_width,screen_height)).convert_alpha()
# imagef = pygame.image.load(r"C:\Users\princ\Documents\instruct.jpg")
# imagef = pygame.transform.scale(imagef, (screen_width-l-l,screen_height-l-l)).convert_alpha()
# imagel = pygame.image.load(r"C:\Users\princ\Downloads\Music\lines.png")
# imagel = pygame.transform.scale(imagel, (30,30)).convert_alpha()

# # Game specific variables
# exit_game = False
# game_over = False
# size = 50

# def text_object(text ,font,color):
#     text = font.render(text, True,color)
#     textrect = text.get_rect()
#     textrect.center = (200,200)
#     gamewindow.blit(text,textrect)

# def button(msg,x,y,w,h,i_color,f_color,act=None):
#     mouse_pos = pygame.mouse.get_pos()
#     click = pygame.mouse.get_pressed()
#     if x+w > mouse_pos[0] > x and y+h > mouse_pos[1] > y:
#         # pygame.draw.rect(gamewindow, (68,71,59),(x+1,y+1,w+5,h+5))
#         pygame.draw.rect(gamewindow, f_color,(x,y,w,h))
#         if click[0] == 1:
#             pygame.draw.rect(gamewindow, blue,(x,y,w,h))
#     else:
#         pygame.draw.rect(gamewindow, (68,71,59),(x+1,y+1,w+5,h+5))
#         pygame.draw.rect(gamewindow, i_color,(x,y,w,h))
    

#     textSurf, textRect = text_object(msg, button_f)
#     textRect.center = ( (x+(w/2)), (y+(h/2)) )
#     gamewindow.blit(textSurf, textRect)



# black = (0,0,0)
# white = (255,255,255)
# first = (255,126,0)
# second = (240,120,0)
# dark = (150,75,0)

# rect = Rect(200,200,208,77)
# rect_2 = Rect(200,200,200,70)
# rect_3 = Rect(200,200,200,70)
# rect_2.center = (400,192)
# rect_3.center = (400,200)
# rect.center = (400,200)

# rect_4 = Rect(200,200,208,78)
# rect_5 = Rect(200,200,200,68)
# rect_6 = Rect(200,200,200,70)
# rect_5.center = (400,198)
# rect_6.center = (400,202)
# rect_4.center = (400,200)


# while not exit_game:
#     gamewindow.fill(white)
#     gamewindow.blit(image,(0,0))
#     # gamewindow.blit(imagef,(l,l))
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             exit_game = True
#             pygame.quit()
#             quit()
#     pos = pygame.mouse.get_pos()

#     # if rect_4[0] + 208 < pos[0] and rect_4[1]+78 < pos[1]: 
#     #     pygame.draw.rect(gamewindow,black,rect_4)
#     #     pygame.draw.rect(gamewindow,dark,rect_6)
#     #     pygame.draw.rect(gamewindow,second,rect_5)
#     # else: 
#     #     pygame.draw.rect(gamewindow,black,rect)
#     #     pygame.draw.rect(gamewindow,dark,rect_3)
#     #     pygame.draw.rect(gamewindow,first,rect_2)

#     # gamewindow.blit(imagel,(842,-1))
#     print(pos)
#     pygame.display.update()
    
                
# pygame.quit()
# quit()
