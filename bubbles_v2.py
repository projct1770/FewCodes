import pygame
import random,sys

# Initialize Pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("By Vijay")

def main_game_loop():

    # Screen dimensions
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    s3=pygame.Rect(325,500,150,65)


    # Colors
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    CYAN=pygame.Color('cyan')
    LI_GRAY=(110, 109, 106)

    

    # Bubble class
    class Bubble(pygame.sprite.Sprite):
        def __init__(self, color, x, y):
            super().__init__()
            self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
            pygame.draw.circle(self.image, color, (25, 25), 25)  # Drawing circle on the surface as a bubble
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.color = color

        def update(self):
            self.rect.y -= 2
            if self.rect.y < -50:
                self.kill()

    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    bubbles = pygame.sprite.Group()

    # Clock for controlling the frame rate
    clock = pygame.time.Clock()

    # Score and time
    score = 0
    nbp = 0
    red_bubbles_popped = 0
    game_time = 45  # Game duration in seconds
    start_ticks = pygame.time.get_ticks()

    #Watermark
    kfont = pygame.font.SysFont('comic sans', 30)
    watermark=kfont.render(f"VIJAY", True, LI_GRAY)

    # Main game loop
    running = True
    game_over = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                pos = pygame.mouse.get_pos()
                clicked_bubbles = [b for b in bubbles if b.rect.collidepoint(pos)]
                for bubble in clicked_bubbles:
                    if bubble.color in [BLUE, GREEN, YELLOW]:
                        score += 10
                        nbp += 1
                    elif bubble.color == RED:
                        score -= 15
                        red_bubbles_popped += 1
                    bubble.kill()

        if not game_over:
            # Adding more bubbles
            if random.randint(1, 10) == 1:
                x = random.randint(0, width - 50)
                y = height
                color = random.choice([BLUE, GREEN, YELLOW, RED])
                bubble = Bubble(color, x, y)
                all_sprites.add(bubble)
                bubbles.add(bubble)

            # Update sprites
            all_sprites.update()

            # Draw everything
            screen.fill(BLACK)
            all_sprites.draw(screen)

            #Watermark
            screen.blit(watermark,(680,540))

            # Display score and time
            font = pygame.font.SysFont('comic sans', 30)
            g_font = pygame.font.SysFont('comic sans', 45)
            score_text = font.render(f"Score: {score}", 1, WHITE)
            screen.blit(score_text, (10, 10))
            
            #time
            elapsed_seconds = (pygame.time.get_ticks() - start_ticks) / 1000
            remaining_time = max(game_time - elapsed_seconds, 0)
            time_text = font.render(f"Time: {int(remaining_time)}", 1, WHITE)
            screen.blit(time_text, (width - 150, 10))

            # End
            if remaining_time <= 0:
                game_over = True
                

        else:
            # Display game over screen with final score and high score
            screen.fill(BLACK)
            game_over_text = g_font.render("Game Over!", True, CYAN)
            screen.blit(game_over_text, (width // 2 - 150+30, height // 2 - 120+30-50))

            final_score_text = g_font.render(f"Final Score: {score}", True, CYAN)
            screen.blit(final_score_text, (width // 2 - 180+30, height // 2 - 30-50))

            normal_bubbles_text = font.render(f"Normal Bubbles Popped: {nbp}", True, CYAN)
            screen.blit(normal_bubbles_text, (width // 2 - 230+70,height // 2 + 80-50))

            red_text=font.render(f"Red Bubbles Popped: {red_bubbles_popped}", True, CYAN)
            screen.blit(red_text, (width // 2 - 230+85,height // 2 + 160-50))

            pygame.draw.rect(screen, pygame.Color('white'), s3)
            retry=font.render(f"Retry", True, pygame.Color('black'))
            screen.blit(retry,(355,510))
            

            mouse = pygame.mouse.get_pos()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if (s3.x<mouse[0]<s3.x+150) and  (s3.y<mouse[1]<s3.y+65):
                    for i in range(1,10000000):
                        pass
                    score = 0
                    start_ticks = pygame.time.get_ticks()
                    game_over = False
                    all_sprites.empty()
                    bubbles.empty()
                

            """keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:    # Reset the game
                score = 0
                start_ticks = pygame.time.get_ticks()
                game_over = False
                all_sprites.empty()
                bubbles.empty()
            elif keys[pygame.K_q]:
                running = False"""

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()



def How():
    
    WIDTH,LENGTH=800,600
    screen=pygame.display.set_mode((WIDTH,LENGTH))
    clock= pygame.time.Clock()
    run =True
    FPS=60
    a,b=310,65
    font=pygame.font.SysFont("comicsans",45 )
    new_font=pygame.font.SysFont("comicsans",23 )
    k2=pygame.Rect(600,530,170,55)

    def window():
        screen.fill(pygame.Color('light green '))
        pygame.draw.rect(screen, pygame.Color('black'), pygame.Rect(400-(a/2),60,a,b))
        
        rules=font.render("Rules", 1 ,pygame.Color('Yellow'))
        point1=new_font.render("1.you will be having 45 seconds , pop as many bubbles as you can", 1 ,pygame.Color('black'))
        point2=new_font.render("2.for every bubble u pop which is not red , u will receive +10 score", 1 ,pygame.Color('black'))
        point3=new_font.render("3.for every bubble u pop that is red , u will receive -15 score", 1 ,pygame.Color('black'))
        point4=new_font.render("Home Screen", 1 ,pygame.Color('white'))

        screen.blit(rules,((350,60)))
        screen.blit(point1,(60,200))
        screen.blit(point2,(60,240))
        screen.blit(point3,(60,280))

        pygame.draw.rect(screen, pygame.Color('black'),k2)
        screen.blit(point4,(610,540))
        #print(pygame.mouse.get_pos())
        pygame.display.update()


    while run:
        clock.tick(FPS)
        window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit ()
            elif event.type == pygame.MOUSEBUTTONDOWN :
                mouse = pygame.mouse.get_pos()
                if (k2.x<mouse[0]<k2.x+170) and  (k2.y<mouse[1]<k2.y+55):
                    for i in range(1,10000000):
                        pass
                    main()


def main():
    WIDTH,LENGTH=800,600
    screen=pygame.display.set_mode((WIDTH,LENGTH))
    clock= pygame.time.Clock()
    run =True
    FPS=60
    a,b=310,65
    font=pygame.font.SysFont("comicsans",45 )
    new_font=pygame.font.SysFont("comicsans",23 )
    title_font=pygame.font.SysFont("comicsans",65 )
    k1=pygame.Rect(400-(a/2),300-(b/2)-75+100,a,b)
    k2=pygame.Rect(400-(a/2),300-(b/2)+100,a,b)

    def window():
        screen.fill(pygame.Color('light blue'))
        pygame.draw.rect(screen, pygame.Color('black'), k1)
        pygame.draw.rect(screen, pygame.Color('black'), k2)
        hp=font.render("How to Play(H)", 1 ,pygame.Color('white'))
        p=font.render("Play(P)", 1 ,pygame.Color('white'))
        text=new_font.render("click the button for the option u want", 1 ,pygame.Color('black'))
        screen.blit(text,(195,550))
        screen.blit(hp,((400-(a/2))-0,300-(b/2)-75+100))
        screen.blit(p,(480-(a/2),300-(b/2)+100))
        #print(pygame.mouse.get_pos())
        #title
        title=title_font.render("Pop the Bubbles !",1,pygame.Color('red'))
        screen.blit(title,(160,120))
        pygame.display.update()


    while run:
        clock.tick(FPS)
        window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit ()
            elif event.type == pygame.MOUSEBUTTONDOWN :
                mouse = pygame.mouse.get_pos()
                if (k1.x<mouse[0]<k1.x+310) and  (k1.y<mouse[1]<k1.y+65):
                    for i in range(1,10000000):
                        pass
                    How()
                if (k2.x<mouse[0]<k2.x+310) and  (k2.y<mouse[1]<k2.y+65):
                    for i in range(1,10000000):
                        pass
                    main_game_loop()

            """keys=pygame.key.get_pressed()
            if(keys[pygame.K_h] ):
                for i in range(1,10000000):
                    pass
                How()
            elif(keys[pygame.K_p] ):
                for i in range(1,10000000):
                    pass
                main_game_loop()"""


main()