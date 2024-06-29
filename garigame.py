import pygame
from pygame.locals import *
import random

# Function to reset the game
def reset_game():
    global speed, car_loc, car2_loc
    speed = 1
    car_loc.center = rightlane, height * 0.8
    car2_loc.center = leftlane, height * 0.2

size = width, height = (800, 800)
road_w = int(width / 1.6)
road_mark = int(width / 80)
rightlane = width / 2 + road_w / 4
leftlane = width / 2 - road_w / 4
speed = 1
game_over = False

pygame.init()
running = True
screen = pygame.display.set_mode((size))

pygame.display.set_caption("MinahilHUB")

screen.fill((60, 220, 0))
pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_w / 2, 0, road_w, height))
pygame.draw.rect(screen, (255, 240, 60), (width / 2 - road_mark / 2, 0, road_mark, height))
pygame.draw.rect(screen, (255, 255, 255), (width / 2 - road_w / 2 + road_mark * 2, 0, road_mark, height))
pygame.draw.rect(screen, (255, 255, 255), (width / 2 + road_w / 2 - road_mark * 3, 0, road_mark, height))

pygame.display.update()

car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = rightlane, height * 0.8

car2 = pygame.image.load("otherCar.png")
car2_loc = car2.get_rect()
car2_loc.center = leftlane, height * 0.2

counter = 0
game_over_font = pygame.font.Font(None, 100)

# Main game loop
while running:
    if not game_over:
        counter += 1
        if counter == 5000:
            speed += 0.25
            counter = 0
            print("Next Level", speed)
        car2_loc[1] += speed
        if car2_loc[1] > height:
            car2_loc[1] = -200
            if random.randint(0, 1) == 0:
                car2_loc.center = rightlane, -200
            else:
                car2_loc.center = leftlane, -200

        # Check for collision between cars
        if car_loc.colliderect(car2_loc):
            game_over = True

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w / 2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([+int(road_w / 2), 0])
        if event.type == MOUSEBUTTONDOWN:  # Check for mouse click events
            if event.button == 1:  # Check if left mouse button is clicked
                if game_over:
                    if width - 100 <= event.pos[0] <= width - 20 and 10 <= event.pos[1] <= 40:
                        reset_game()  # Reset the game if restart button is clicked
                        game_over = False

    pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_w / 2, 0, road_w, height))
    pygame.draw.rect(screen, (255, 240, 60), (width / 2 - road_mark / 2, 0, road_mark, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 - road_w / 2 + road_mark * 2, 0, road_mark, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 + road_w / 2 - road_mark * 3, 0, road_mark, height))

    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)

    if game_over:
        game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (width // 2 - 200, height // 2 - 50))
        # Draw restart button
        pygame.draw.rect(screen, (255, 0, 0), (width - 100, 10, 80, 30))
        font = pygame.font.Font(None, 36)
        text = font.render("Restart", True, (255, 255, 255))
        screen.blit(text, (width - 90, 15))  # Adjusted text position to fit within the button area

    pygame.display.update()

pygame.quit()


