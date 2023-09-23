import random
import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
width=1920/4
height=1080/1.5
pygame.display.set_caption("SuperDuperEpicTitle")
screen= pygame.display.set_mode((width,height))

# Get all the words
f = open("Better_Words.txt",'r')
a = open("Words.txt",'r')
words = []
gwords=[]

for l in f:
    l=l[0:5]
    words.append(l)

for l in a:
    l=l[0:5]
    gwords.append(l)

f.close()
a.close()

colours = [[130,131,133],[58,58,59],[181,158,61],[82,141,77]]


# Top part variables
cubeh = height-(height/3)

# Rect for the cubes
cube_rect = pygame.Rect(0,0,width-(width/4),cubeh-(cubeh/6))
cube_rect.center = (width/2,cubeh/2)

small_cubes = []
scw = (cube_rect.width-40)/5
# sc_rect = pygame.Rect(0,0,scw,scw)

for i in range(6):
    sc_rect = pygame.Rect(0,0,scw,scw)
    if i == 0:
        sc_rect.topleft = cube_rect.topleft
        small_cubes.append(sc_rect)
    else:
        sc_rect.topleft = small_cubes[((i-1)*5)].bottomleft
        sc_rect.centery = sc_rect.centery + 10
        small_cubes.append(sc_rect)
    for i in range(4):
        sc_rect = pygame.Rect(0,0,scw,scw)
        sc_rect.topleft = small_cubes[-1].topright
        sc_rect.centerx = sc_rect.centerx+11
        small_cubes.append(sc_rect)

keyboard = []
kw = (cube_rect.width-(5*9))/10
kh = scw-20

for i in range(10):
    k_rect = pygame.Rect(0,0,kw,kh)
    if i == 0:
        k_rect.topleft = small_cubes[25].bottomleft
        k_rect.centery = k_rect.centery+50
        keyboard.append(k_rect)
    else:
        k_rect.topleft = keyboard[i-1].topright
        k_rect.centerx=k_rect.centerx+6
        keyboard.append(k_rect)

for i in range(9):
    k_rect = pygame.Rect(0,0,kw,kh)
    if i == 0:
        k_rect.topleft = keyboard[0].bottomleft
        k_rect.centery = k_rect.centery+6
        k_rect.centerx = k_rect.centerx+(kw/2)+3
        keyboard.append(k_rect)
    else:
        k_rect.topleft = keyboard[i+9].topright
        k_rect.centerx=k_rect.centerx+6
        keyboard.append(k_rect)

for i in range(9):
    k_rect = pygame.Rect(0,0,kw,kh)
    if i == 0:
        k_rect.topleft = keyboard[0].bottomleft
        k_rect.centery = k_rect.centery+12+kh
        keyboard.append(k_rect)
        keyboard[-1].width = kw+(kw/2)+2
    else:
        k_rect.topleft = keyboard[i+18].topright
        k_rect.centerx=k_rect.centerx+6
        keyboard.append(k_rect)

keyboard[-1].width = kw+(kw/2)+2




# Font
kFonts = pygame.font.SysFont("Arial", 17, True)
gFonts = pygame.font.SysFont("Arial", 30, True)
keyfonts = []
keys = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Enter","Z","X","C","V","B","N","M","Back"]
keys_pressed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

colour_keys = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
colour_guesses = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(len(keyboard)):
    text = kFonts.render(keys[i],True,(255,255,255))
    text_rect = text.get_rect()
    text_rect.center = keyboard[i].center
    keyfonts.append([text,text_rect])

word = [[],[],[],[],[],[]]
stage = 0
guesses = []
guess_update = False
new_game = True
lword = []
f=True

main = True
while main:
    work = True
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            main=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                main=False
            # All keyboard inputs
            if event.key == pygame.K_q:
                keys_pressed[0] = True
            if event.key == pygame.K_w:
                keys_pressed[1] = True
            if event.key == pygame.K_e:
                keys_pressed[2] = True
            if event.key == pygame.K_r:
                keys_pressed[3] = True    
            if event.key == pygame.K_t:
                keys_pressed[4] = True
            if event.key == pygame.K_y:
                keys_pressed[5] = True
            if event.key == pygame.K_u:
                keys_pressed[6] = True
            if event.key == pygame.K_i:
                keys_pressed[7] = True
            if event.key == pygame.K_o:
                keys_pressed[8] = True    
            if event.key == pygame.K_p:
                keys_pressed[9] = True
            if event.key == pygame.K_a:
                keys_pressed[10] = True
            if event.key == pygame.K_s:
                keys_pressed[11] = True
            if event.key == pygame.K_d:
                keys_pressed[12] = True
            if event.key == pygame.K_f:
                keys_pressed[13] = True     
            if event.key == pygame.K_g:
                keys_pressed[14] = True
            if event.key == pygame.K_h:
                keys_pressed[15] = True
            if event.key == pygame.K_j:
                keys_pressed[16] = True
            if event.key == pygame.K_k:
                keys_pressed[17] = True
            if event.key == pygame.K_l:
                keys_pressed[18] = True
            if event.key == pygame.K_RETURN:
                keys_pressed[19] = True
            if event.key == pygame.K_z:
                keys_pressed[20] = True
            if event.key == pygame.K_x:
                keys_pressed[21] = True
            if event.key == pygame.K_c:
                keys_pressed[22] = True
            if event.key == pygame.K_v:
                keys_pressed[23] = True
            if event.key == pygame.K_b:
                keys_pressed[24] = True     
            if event.key == pygame.K_n:
                keys_pressed[25] = True
            if event.key == pygame.K_m:
                keys_pressed[26] = True
            if event.key == pygame.K_BACKSPACE:
                keys_pressed[27] = True


    clock.tick(60)
    
    screen.fill((18,18,20))

    for i in range(len(small_cubes)):
        pygame.draw.rect(screen,(57,57,59),small_cubes[i],2)

    # prints the coloured guesses
    for i in range(len(small_cubes)):
        if colour_guesses[i] != 0:
            pygame.draw.rect(screen,(colours[colour_guesses[i]][0],colours[colour_guesses[i]][1],colours[colour_guesses[i]][2]),small_cubes[i])

    for i in range(len(keyboard)):
        pygame.draw.rect(screen,(colours[colour_keys[i]][0],colours[colour_keys[i]][1],colours[colour_keys[i]][2]),keyboard[i],0,4)    
        screen.blit(keyfonts[i][0],keyfonts[i][1])

    # Gets a new word if a new game starts
    if new_game:
        final=words[random.randint(0,len(words)-1)]
        for i in range(5):
            lword.append(final[i])
        new_game = False

    # The game part
    for i in range(len(keys_pressed)):
        if keys_pressed[i] == True and i != 27 and i != 19 and len(word[stage])<5:
            word[stage].append(keys[i])
    
    # Checks for the back and return key
    if keys_pressed[27] == True:
        if len(word[stage])>0:
            word[stage].pop(-1)

    if keys_pressed[19] == True:
        if len(word[stage]) == 5:
            user_word = ""
            for i in range(5):
                user_word+=word[stage][i]
            if user_word.lower() in gwords or user_word.lower() in words:
                guess_update = True
            else:
                print("Not real word")
        else:
            print("Not big enough")

    if guess_update:
        for i in range(5):
            if word[stage][i].lower() == lword[i]:
                colour_guesses[(stage*5)+i] = 3
                colour_keys[keys.index(word[stage][i])] = 3
            elif word[stage][i].lower() in lword:
                colour_guesses[(stage*5)+i] = 2
                colour_keys[keys.index(word[stage][i])] = 2
            else:
                colour_guesses[(stage*5)+i] = 1
                colour_keys[keys.index(word[stage][i])] = 1

        if stage != 5:
            stage+=1
        guess_update = False
        
    if stage == 5:
        if f:
            print(lword)
        f=False

    # Puts the active letters on screen
    for i in range(stage+1):
        for j in range(len(word[i])):
            text = gFonts.render(word[i][j],True,(255,255,255))
            text_rect = text.get_rect()
            text_rect.center = small_cubes[(i*5)+j].center
            screen.blit(text,text_rect)

    keys_pressed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    pygame.display.flip()
pygame.quit()
sys.exit()




f = open("Words.txt",'r')

words = []

for l in f:
    l=l[0:5]
    words.append(l)


word=words[random.randint(0,len(words)-1)]
print(word)


f.close()
