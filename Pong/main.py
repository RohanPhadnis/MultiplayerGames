import pygame.display

from abstractions import *

client = 'mongodb+srv://anyone:xyz@flask.ngjrl.mongodb.net/MultiplayerGames?retryWrites=true&w=majority'
size = 800

pygame.init()
screen = pygame.display.set_mode((size, size))
pygame.display.set_caption('Pong')

start_button = Button('start', size/2, size/2)


while True:
    screen.fill((0, 0, 0))
    start_button.draw()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == MOUSEBUTTONDOWN:
            pass
    pygame.display.update()

# from abstractions import *
#
# SIZE = 800
# pygame.init()
# screen = pygame.display.set_mode((SIZE, SIZE))
# pygame.display.set_caption('Pong')
#
# ball = Ball(SIZE/2, SIZE/2)
# paddle1 = Paddle(10, SIZE/2)
# paddle2 = Paddle(SIZE-20, SIZE/2)
# game_objects = [ball, paddle1, paddle2]
# cycle = 0
# interval = 1 / 50
# last_time = time.time()
#
#
# while True:
#     if time.time() - last_time >= interval:
#         screen.fill((0, 0, 0))
#         for obj in game_objects:
#             obj.draw(screen)
#             obj.move()
#         if ball.pos[1] - ball.rad < 0:
#             ball.vel[1] = random.random() * ball.speed
#         elif ball.pos[1] + ball.rad > SIZE:
#             ball.vel[1] = -random.random() * ball.speed
#         if ball.rect.colliderect(paddle1.rect):
#             ball.vel[0] = random.random() * ball.speed
#         if ball.rect.colliderect(paddle2.rect):
#             ball.vel[0] = -random.random() * ball.speed
#         last_time = time.time()
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             exit()
#         elif event.type == KEYDOWN:
#             if event.key == K_UP:
#                 paddle2.vel = -1
#             elif event.key == K_DOWN:
#                 paddle2.vel = 1
#             elif event.key == K_w:
#                 paddle1.vel = -1
#             elif event.key == K_s:
#                 paddle1.vel = 1
#         elif event.type == KEYUP:
#             if event.key == K_UP or event.key == K_DOWN:
#                 paddle2.vel = 0
#             elif event.key == K_w or event.key == K_s:
#                 paddle1.vel = 0
#             elif event.key == K_SPACE:
#                 ball.pos = [SIZE/2, SIZE/2]
#     pygame.display.update()
