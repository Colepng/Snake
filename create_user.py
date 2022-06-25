import  pygame 
from pygame.locals import *
from pygame.rect import *

from fun import calc_mid_of_rect_for_text, draw_surfaces
from serve_fun import main
def create_user(screen):
    #create user
    clock = pygame.time.Clock()
    
    
    rect_width = 140
    rect_height  = 32

    BLACK = (0, 0, 0)

    pygame.font.init()

    base_font = pygame.font.Font(None, 32)

    username_good_bad = "none"

    p_username_good_bad = "none"

    #rects


    username_input_rect = pygame.Rect(screen.get_width()/2 - rect_width/2, screen.get_height()/2 - rect_height/2 - 100, rect_width, rect_height,)
    public_username_input_rect = pygame.Rect(username_input_rect.left, username_input_rect.bottom + 50, rect_width, rect_height,)
    password_input_rect = pygame.Rect(public_username_input_rect.left, public_username_input_rect.bottom + 50, rect_width, rect_height,)
    confirm_password_input_rect = pygame.Rect(password_input_rect.left, password_input_rect.bottom + 50, rect_width, rect_height,)

    input_rects = [username_input_rect, public_username_input_rect, password_input_rect, confirm_password_input_rect]

    #texts
    username_input_text = ""
    public_username_input_text = ""
    password_input_text = ""
    confirm_password_input_text = ""

    input_texts = [username_input_text, public_username_input_text, password_input_text, confirm_password_input_text] 

    create_user_rect = pygame.Rect(confirm_password_input_rect.left, confirm_password_input_rect.bottom + 100, rect_width, rect_height,)
    back_rect = pygame.Rect (0, 0, rect_width, rect_height,)

    color_active = pygame.Color('lightskyblue3')

    color_passive = pygame.Color('chartreuse4')
    color = color_passive
    active = False

    while True:

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:

                for i in input_rects:

                    if i.collidepoint(event.pos):
                        print(i.collidepoint(event.pos))
                        active = True
                        hit_rect = input_rects.index(i)
                        print(hit_rect)
                        break

                    if not i.collidepoint(event.pos):
                        active = False
                        print("not colliding")

                if create_user_rect.collidepoint(event.pos):
                    if input_texts[2] == input_texts[3]:
                        username_good_bad, p_username_good_bad = main("create_user", input_texts[0], input_texts[2], input_texts[1])
                        if username_good_bad == "good" and p_username_good_bad == "good":
                            print("good")
                        main("login", input_texts[0], input_texts[2])
                        return
                elif back_rect.collidepoint(event.pos):
                    return
                    
        

            elif event.type == KEYDOWN and active == True:
                text = event.unicode

                if event.key == K_BACKSPACE: 

                    input_texts[hit_rect] = input_texts[hit_rect][:-1]


                else:
                    input_texts[hit_rect] += text

            elif event.type == QUIT:
                pygame.quit()
                exit()

        screen.fill((255, 255, 255, 100))
    
        if active:
            color = color_active
        else:
            color = color_passive

        for i in input_rects:
            pygame.draw.rect(screen, color, i, 5)

        pygame.draw.rect(screen, color, create_user_rect, 5)

        username_surface = base_font.render('username', True, BLACK)
        public_username_surface = base_font.render('public username', True, BLACK)
        password_surface = base_font.render('password', True, BLACK)
        confirm_password_surface = base_font.render('confirm password', True, BLACK)

        username_bad_surface = base_font.render('username taken', True, BLACK)
        public_username_bad_surface = base_font.render('public username taken', True, BLACK)
        
        passowrd_same_surface = base_font.render('passwords do not match', True, BLACK)

        back_surface = base_font.render('Back', True, BLACK)

        surfaces = [username_surface, public_username_surface, password_surface, confirm_password_surface]

        username_input_surface = base_font.render(input_texts[0], True, BLACK)
        public_username_input_surface = base_font.render(input_texts[1], True, BLACK)
        password_input_surface = base_font.render(input_texts[2], True, BLACK)
        confirm_password_input_surface = base_font.render(input_texts[3], True, BLACK)

        screen.blit(back_surface, calc_mid_of_rect_for_text(back_rect, back_surface))
        pygame.draw.rect(screen, BLACK, back_rect, 5)


        input_surfaces = [username_input_surface, public_username_input_surface, password_input_surface, confirm_password_input_surface]

        for i in range(len(input_rects)):
            draw_surfaces(screen, input_surfaces[i], surfaces[i], input_rects[i])

        if username_good_bad == "bad":
            screen.blit(username_bad_surface, (username_input_rect.left, username_input_rect.top - 20))

        if p_username_good_bad == "bad":
            screen.blit(public_username_bad_surface, (public_username_input_rect.left, public_username_input_rect.top - 20))

        if input_texts[2] != input_texts[3]:
            screen.blit(passowrd_same_surface, (password_input_rect.left, password_input_rect.top - 20))
        pygame.display.flip()

        clock.tick(60)
        
if __name__ == "__main__":
    create_user()