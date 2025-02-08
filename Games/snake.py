import pygame
import random
import sys
from pygame.math import Vector2

# Initialize Pygame
pygame.init()

# Constants
CELL_SIZE = 40
CELL_NUMBER = 20
SCREEN_SIZE = CELL_SIZE * CELL_NUMBER

# Colors
BACKGROUND_COLOR = (40, 40, 40)
SNAKE_COLOR = (0, 200, 0)
FOOD_COLOR = (200, 50, 50)
SCORE_COLOR = (255, 255, 255)

class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False
        
        # Load snake graphics
        self.head_up = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.head_up.fill(SNAKE_COLOR)
        pygame.draw.rect(self.head_up, (0, 150, 0), (10, 0, 20, 20))
        
    def draw(self, screen):
        for index, block in enumerate(self.body):
            block_rect = pygame.Rect(block.x * CELL_SIZE, block.y * CELL_SIZE, CELL_SIZE - 2, CELL_SIZE - 2)
            if index == 0:  # Head
                screen.blit(self.head_up, block_rect)
            else:  # Body
                pygame.draw.rect(screen, SNAKE_COLOR, block_rect, border_radius=8)
    
    def move(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
    
    def add_block(self):
        self.new_block = True

class Food:
    def __init__(self):
        self.randomize()
        
    def draw(self, screen):
        food_rect = pygame.Rect(self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE - 2, CELL_SIZE - 2)
        pygame.draw.rect(screen, FOOD_COLOR, food_rect, border_radius=10)
        
    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.font = pygame.font.Font(None, 60)
        
    def update(self):
        self.snake.move()
        self.check_collision()
        self.check_fail()
        
    def draw(self, screen):
        self.draw_grass(screen)
        self.snake.draw(screen)
        self.food.draw(screen)
        self.draw_score(screen)
        
    def check_collision(self):
        if self.food.pos == self.snake.body[0]:
            self.food.randomize()
            self.snake.add_block()
            self.score += 1
            
    def check_fail(self):
        # Check if snake hits walls
        if not 0 <= self.snake.body[0].x < CELL_NUMBER or not 0 <= self.snake.body[0].y < CELL_NUMBER:
            self.game_over()
            
        # Check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
                
    def game_over(self):
        pygame.quit()
        sys.exit()
        
    def draw_grass(self, screen):
        for row in range(CELL_NUMBER):
            for col in range(CELL_NUMBER):
                if (row + col) % 2 == 0:
                    grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(screen, (50, 50, 50), grass_rect)
                    
    def draw_score(self, screen):
        score_text = str(self.score)
        score_surface = self.font.render(score_text, True, SCORE_COLOR)
        score_rect = score_surface.get_rect(center=(SCREEN_SIZE//2, 40))
        screen.blit(score_surface, score_rect)

# Main game loop
def main():
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    clock = pygame.time.Clock()
    game = Game()
    
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)  # Snake speed (lower = faster)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and game.snake.direction.y != 1:
                    game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN and game.snake.direction.y != -1:
                    game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT and game.snake.direction.x != 1:
                    game.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT and game.snake.direction.x != -1:
                    game.snake.direction = Vector2(1, 0)
        
        screen.fill(BACKGROUND_COLOR)
        game.draw(screen)
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()