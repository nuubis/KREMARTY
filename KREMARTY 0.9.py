import pygame

black=(0,0,0)
white=(255,255,255)
gray=(105,105,105)
red=(255,0,0)
darkred=(155,0,0)

pygame.init()

font=pygame.font.SysFont("Harrington",110,bold=0.5)
font2=pygame.font.SysFont("Harrington",50,bold=0.3)
font3=pygame.font.SysFont("Harrington",30)
fontbutton=pygame.font.SysFont("Harrington",30)

laius=800
kõrgus=600

Screen=pygame.display.set_mode((laius,kõrgus)) #teeb akna
pygame.display.set_caption("KREMARTY") #aknale pealkiri

introtaust=pygame.image.load("mainmenu.jpg")
human=pygame.image.load("human.png")
elf=pygame.image.load("elf.png")
mainmenutaust=pygame.image.load("actionmenu.jpg")
adventureicon=pygame.image.load("adventureicon.png")
crafticon=pygame.image.load("crafticon.png")
townicon=pygame.image.load("townicon.png")

def button(message,x,y,width,height,inactive_color,active_color,action=None):
    cursor=pygame.mouse.get_pos() #võtab hiire asukoha (x ja y koordinaadid)
    click=pygame.mouse.get_pressed() #registreerib hiire vajutuse (kas ja kus)
    if x+width>cursor[0]>x and y+height>cursor[1]>y: #kontrollib, kas hiir asub nupu peal
        pygame.draw.rect(Screen,active_color,(x,y,width,height))
        if click[0]==1 and action!=None:
            if action=="Play":
                game_begin=True
                return game_begin
    else:
        pygame.draw.rect(Screen,inactive_color,(x,y,width,height))
    #text_to_button(message,black,x,y,width,height)

    tekst_nupule=fontbutton.render(message,False,white)
    #Screen.blit(tekst_nupule,(375,250))
    Screen.blit(tekst_nupule,(x+10,y))
    pygame.display.update()

tase="mainmenu"

game_begin=True

while game_begin:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_begin=False

    #BUTTONS

    if tase=="mainmenu":
        vastus1=button("PLAY",170,250,100,40,black,darkred,action="Play")
        vastus2=button("LOAD",170,300,100,40,black,darkred,action="Play")
        vastus3=button("HELP",170,350,100,40,black,darkred,action="Play")
        vastus4=button("QUIT",170,400,100,40,black,darkred,action="Play")
        if vastus1==True:
            tase="choose_race"
        if vastus2==True:
            pass
        if vastus3==True:
            tase="help"
        if vastus4==True:
            game_begin=False

    elif tase=="help":
        vastus1=button("BACK",170,400,100,40,black,darkred,action="Play")
        if vastus1==True:
            tase="mainmenu"

    elif tase=="choose_race":
        vastus1=button("human",70,350,110,40,black,darkred,action="Play")
        vastus2=button("    elf",190,350,110,40,black,darkred,action="Play")
        if vastus1==True:
            tase="choose_name"
        if vastus2==True:
            tase="choose_name"

    elif tase=="choose_name":
        vastus1=button("[name goes here]",80,230,240,40,black,darkred,action="Play")
        vastus2=button("START GAME",100,300,200,40,black,darkred,action="Play")
        if vastus1==True:
            pass
        if vastus2==True:
            tase="actionmenu"

    elif tase=="actionmenu":
        vastus1=button("adventure",90,390,160,40,black,darkred,action="Play")
        vastus2=button("  craft",350,390,110,40,black,darkred,action="Play")
        vastus3=button("  town",600,390,110,40,black,darkred,action="Play")
        vastus4=button("SAVE",280,490,90,40,black,darkred,action="Play")
        vastus5=button("QUIT",420,490,90,40,black,darkred,action="Play")
        if vastus1==True:
            tase="adventure"
        if vastus2==True:
            tase="adventure"
        if vastus3==True:
            tase="adventure"
        if vastus4==True:
            pass
        if vastus5==True:
            game_begin=False

    elif tase=="adventure":
        vastus1=button("back to main menu",280,300,240,40,black,darkred,action="Play")
        if vastus1==True:
            tase="mainmenu"

    #DISPLAY

    if tase=="mainmenu":
        Screen.blit(introtaust,(0,0))
        teksti_pilt=font.render("KREMARTY",False,black)
        Screen.blit(teksti_pilt,(65,30))

    elif tase=="help":
        Screen.blit(introtaust,(0,0))
        teksti_pilt=font2.render("Instructions",False,black)
        Screen.blit(teksti_pilt,(60,60))
        teksti_pilt=font3.render("Here will be some instructions.",False,black)
        Screen.blit(teksti_pilt,(60,120))

    elif tase=="choose_race":
        Screen.blit(introtaust,(0,0))

        teksti_pilt=font2.render("Choose your race:",False,black)
        Screen.blit(teksti_pilt,(60,60))

        human=pygame.transform.scale(human,(97,200))
        Screen.blit(human,(70,140))

        elf=pygame.transform.scale(elf,(121,200))
        Screen.blit(elf,(190,140))

    elif tase=="choose_name":
        Screen.blit(introtaust,(0,0))
        teksti_pilt=font2.render("Type your name:",False,black)
        Screen.blit(teksti_pilt,(60,60))

    elif tase=="actionmenu":
        Screen.blit(mainmenutaust,(0,0))

        adventureicon=pygame.transform.scale(adventureicon,(115,100))
        Screen.blit(adventureicon,(100,270))

        crafticon=pygame.transform.scale(crafticon,(100,104))
        Screen.blit(crafticon,(350,270))

        townicon=pygame.transform.scale(townicon,(100,105))
        Screen.blit(townicon,(600,270))

    elif tase=="adventure":
        Screen.fill(white)
        teksti_pilt=font2.render("[under construction]",False,black)
        Screen.blit(teksti_pilt,(150,150))

    pygame.display.update() #update'ib eelnevat

pygame.quit()
quit()