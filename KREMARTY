import pygame

black=(0,0,0)
white=(255,255,255)
gray=(105,105,105)
red=(255,0,0)
darkred=(155,0,0)
brown=(139,69,19)
blue=(0,0,200)
yellow=(200,200,0)
green=(34,177,76)

pygame.init()

laius=800
kõrgus=600
button_width=100
button_height=40

Screen=pygame.display.set_mode((laius,kõrgus)) #teeb akna
pygame.display.set_caption("KREMARTY") #aknale pealkiri

font1=pygame.font.SysFont("Harrington", 110, bold=0.5)
font2=pygame.font.SysFont("Harrington",50,bold=0.3)
font3=pygame.font.SysFont("Harrington",30)


introtaust=pygame.image.load("mainmenu.jpg")
human=pygame.image.load("human.png")
human=pygame.transform.scale(human,(97,200))
elf=pygame.image.load("elf.png")
elf=pygame.transform.scale(elf,(121,200))
mainmenutaust=pygame.image.load("actionmenu.jpg")
adventureicon=pygame.image.load("adventureicon.png")
adventureicon=pygame.transform.scale(adventureicon,(115,100))
crafticon=pygame.image.load("crafticon.png")
crafticon=pygame.transform.scale(crafticon,(100,104))
townicon=pygame.image.load("townicon.png")
townicon=pygame.transform.scale(townicon,(100,105))

# Displays hp_and mana bar
def hp_bar(hp, max_hp, hp_x, hp_y, mp, max_mp, mp_x, mp_y):
    hp_percent = hp/max_hp
    mp_percent = mp/max_mp
    pygame.draw.rect(Screen,red,[hp_x,hp_y,2*100,20])
    pygame.draw.rect(Screen,green,[hp_x,hp_y,2*100*hp_percent,20])
    pygame.draw.rect(Screen,black,[mp_x,mp_y,4*50,20])
    pygame.draw.rect(Screen,blue,[mp_x,mp_y,4*50*mp_percent,20])

def text_objects(text,color,size):
    if size=="small":
        textSurface=font3.render(text, True, color)
    elif size=="medium":
        textSurface=font2.render(text, True, color)
    elif size=="large":
        textSurface=font1.render(text, True, color)
    return textSurface, textSurface.get_rect()

def text_to_button(msg,color,buttonX,buttonY,button_width,button_height,size="small"):
    textSurf, textRect=text_objects(msg,color,size)
    textRect.center=((buttonX+(button_width/2)),buttonY+(button_height/2))
    Screen.blit(textSurf,textRect)

# Text to screen
def message_to_screen(msg, color, y_displace=0,size="small", taust=white,x_displace=0):
    textSurf, textRect=text_objects(msg,color,size)
    textRect.center=(laius/2)+x_displace,(kõrgus/2) + y_displace
    if taust is not None:
        pygame.draw.rect(Screen,white,((laius/2-textRect.width/2+ x_displace),
                                       (kõrgus/2-textRect.height/2+y_displace),textRect.width,textRect.height))
    Screen.blit(textSurf,textRect)

# Button info
class Button():
    def __init__(self, rect, col1,col2, buttontekst, tulemus):
        self.rect=rect
        self.col1=col1
        self.col2=col2
        self.buttontekst=buttontekst
        self.tulemus=tulemus

    def draw(self):
        if collision(self.rect[0], self.rect[1], self.rect[2],self.rect[3],pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
            pygame.draw.rect(Screen,self.col2,self.rect)
        else:
            pygame.draw.rect(Screen,self.col1,self.rect)
        text_to_button(self.buttontekst,white,self.rect[0], self.rect[1], self.rect[2],self.rect[3])
    def mouse_collision(self,mouse_event):
        if collision(self.rect[0], self.rect[1], self.rect[2],self.rect[3],mouse_event.pos[0], mouse_event.pos[1]):
            return self.tulemus
        else:
            return

def handle_buttons(buttons, mouse_event):
    for b in buttons:
        result = b.mouse_collision(mouse_event)
        if result != None:
            return result

def draw_buttons(buttons):
    for b in buttons:
        b.draw()

def collision(box_x,box_y,box_w,box_h,point_x,point_y):
    if point_x < box_x or point_y < box_y or point_x > box_x+box_w or point_y > box_y + box_h:
        return False
    else:
        return True

# BUTTONS

menu_But=[Button((170,250,button_width,button_height),black,darkred,"PLAY", "Play"),
             Button((170,300,button_width,button_height),black,darkred,"LOAD", "Load"),
             Button((170,350,button_width,button_height),black,darkred,"HELP", "Help"),
             Button((170,400,button_width,button_height),black,darkred,"QUIT", "Quit")]

help_But=[Button((170,400,button_width,button_height),black,darkred,"BACK", "Back"),
             Button((570,400,button_width,button_height),black,darkred,"QUIT", "Quit")]

character_But=[Button((70,350,button_width,button_height),black,darkred,"Human", "Human"),
             Button((190,350,button_width,button_height),black,darkred,"Elf", "Elf")]

name_But=[Button((80,230,button_width,button_height),black,darkred,"name", "Play"),
          Button((100,300,button_width+50,button_height),black,darkred,"START GAME", "Play")]

action_But=[Button((90,390,button_width+5,button_height),black,darkred,"Adventure", "Adventure"),
             Button((350,390,button_width+5,button_height),black,darkred,"Craft", "Craft"),
             Button((600,390,button_width+5,button_height),black,darkred,"Village", "Village"),
             Button((280,490,button_width+5,button_height),black,darkred,"SAVE", "Save"),
             Button((420,490,button_width+5,button_height),black,darkred,"QUIT", "Quit")]

adventure_But=[Button((280,300,button_width+100,button_height),black,darkred,"Back to main menu", "Back")]
             #Button(100,300,button_width,button_height,black,darkred,"START GAME", "Play")]


player=""
tase="mainmenu"
game_begin=True

while game_begin:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_begin=False
        if event.type==pygame.MOUSEBUTTONUP:
            if tase=="mainmenu":
                result=handle_buttons(menu_But,event)
                if result=="Play":
                    tase="choose_race"
                elif result=="Load":
                    pass
                elif result=="Help":
                    tase="help"
                elif result=="Quit":
                    game_begin=False

            elif tase=="help":
                result=handle_buttons(help_But,event)
                if result=="Back":
                    tase="mainmenu"
                elif result=="Quit":
                    game_begin=False

            elif tase=="choose_race":
                result=handle_buttons(character_But,event)
                if result=="Human":
                    tase="choose_name"
                    player=human
                elif result=="Elf":
                    tase="choose_name"
                    player=elf

            elif tase=="choose_name":
                result=handle_buttons(name_But,event)
                if result=="Play":
                    tase="actionmenu"

            elif tase=="actionmenu":
                result=handle_buttons(action_But,event)
                if result=="Adventure":
                    tase="adventure"
                elif result=="Craft":
                    tase="adventure"
                elif result=="Village":
                    tase="adventure"
                elif result=="Save":
                    pass
                elif result=="Quit":
                    game_begin=False

            elif tase=="adventure":
                result=handle_buttons(adventure_But,event)
                if result=="Back":
                    tase="mainmenu"

    #DISPLAY

    if tase=="mainmenu":
        Screen.blit(introtaust,(0,0))
        teksti_pilt=font1.render("KREMARTY", False, black)
        Screen.blit(teksti_pilt,(65,30))
        draw_buttons(menu_But)

    elif tase=="help":
        Screen.blit(introtaust,(0,0))
        teksti_pilt=font2.render("Instructions",False,black)
        Screen.blit(teksti_pilt,(60,60))
        teksti_pilt=font3.render("Here will be some instructions.",False,black)
        Screen.blit(teksti_pilt,(60,120))
        draw_buttons(help_But)

    elif tase=="choose_race":
        Screen.blit(introtaust,(0,0))
        teksti_pilt=font2.render("Choose your race:",False,black)
        Screen.blit(teksti_pilt,(60,60))
        Screen.blit(human,(70,140))
        Screen.blit(elf,(190,140))
        draw_buttons(character_But)

    elif tase=="choose_name":
        Screen.blit(introtaust,(0,0))
        teksti_pilt=font2.render("Type your name:",False,black)
        Screen.blit(teksti_pilt,(60,60))
        draw_buttons(name_But)

    elif tase=="actionmenu":
        Screen.blit(mainmenutaust,(0,0))
        Screen.blit(adventureicon,(100,270))
        Screen.blit(crafticon,(350,270))
        Screen.blit(townicon,(600,270))
        draw_buttons(action_But)

    elif tase=="adventure":
        Screen.fill(white)
        teksti_pilt=font2.render("[under construction]",False,black)
        Screen.blit(teksti_pilt,(150,150))
        draw_buttons(adventure_But)

    pygame.display.update() #update'ib eelnevat

pygame.quit()
quit()
