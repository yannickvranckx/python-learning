import pygame
import random

# Initialize Pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BIRD_WIDTH = 34
BIRD_HEIGHT = 24
PIPE_WIDTH = 52
PIPE_HEIGHT = 320
PIPE_GAP = 100
GRAVITY = 1
FLAP_STRENGHT = -10
BIRD_X = 50

# Load images
bird_image = pygame.image.load("bird.png")
pipe_image = pygame.image.load("pipe.png")
background_image = pygame.image.load("background.png")

# Game Variables
bird_y = SCREEN_HEIGHT // 2
bird_velocity = 0
pipes = []
score = 0
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Setup display
screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Function to create a new pipe
def create_pipe():
    y = random.randint(PIPE_GAP, SCREEN_HEIGHT - PIPE_GAP)
    pipe_top = pipe_image.get_rect(midbottom=(SCREEN_WIDTH + PIPE_WIDTH, y - PIPE_GAP // 2))
    pipe_bottom = pipe_image.get_rect(midtop=(SCREEN_WIDTH + PIPE_WIDTH, y + PIPE_GAP // 2))
    return pipe_top, pipe_bottom

# Function to check for collisions
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe[0]) or bird_rect.colliderect(pipe[1]):
            return True
        if bird_rect.top <= 0 or bird_rect.bottom >= SCREEN_HEIGHT:
            return True
        return False
    
# Main game loop
running = True
while running:
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = FLAP_STRENGHT

    # Bird mechanics
    bird_velocity += GRAVITY
    bird_y += bird_velocity
    bird_rect = bird_image.get_rect(center=(BIRD_X, bird_y))

    # Pipe mechanics
    if len(pipes) == 0 or pipes[-1][0].right < SCREEN_WIDTH - 200:
        pipes.append(create_pipe())

    for pipe in pipes:
        pipe[0].centerx -= 5
        pipe[1].centerx -= 5
        screen.blit(pipe_image, pipe[0])
        screen.blit(pipe_image, pipe[1])

    pipes = [pipe for pipe in pipes if pipe[0].right > 0]

    # Draw bird
    screen.blit(bird_image, bird_rect)

    # Check for collisions
    if check_collision(pipes):
        running = False

    # Update score
    for pipe in pipes:
        if pipe[0].centerx == BIRD_X:
            score += 1

    # Display score
    score_text = font.render(str(score), True, (255, 255, 255))
    screen.blit(score_text, (SCREEN_WIDTH // 2, 50))

    # Update the display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()