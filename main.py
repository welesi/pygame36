import pygame

WIDTH, HEIGHT = 1280, 720
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Рисование прямоугольников")
clock = pygame.time.Clock()


start_pos = None
current_rect = None
rectangles = []
filled = False

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                start_pos = event.pos
                current_rect = pygame.Rect(start_pos[0], start_pos[1], 0, 0)

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and current_rect:
                rectangles.append((current_rect.copy(), filled))
                current_rect = None

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                filled = not filled

    if pygame.mouse.get_pressed()[0] and start_pos:
        end_pos = pygame.mouse.get_pos()
        width = end_pos[0] - start_pos[0]
        height = end_pos[1] - start_pos[1]
        current_rect.width = width
        current_rect.height = height

    for rect, is_filled in rectangles:
        if is_filled:
            pygame.draw.rect(screen, RED, rect)
        else:
            pygame.draw.rect(screen, RED, rect, 2)

    if current_rect:
        if filled:
            pygame.draw.rect(screen, RED, current_rect)
        else:
            pygame.draw.rect(screen, RED, current_rect, 2)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()