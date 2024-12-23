import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors (Green and Black Theme)
black = (0, 0, 0)
dark_green = (0, 100, 0)
green = (0, 255, 0)
light_green = (144, 238, 144)

# Set up display
width = 600
height = 400
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Quiz Game')

# Game clock
clock = pygame.time.Clock()

snake_block = 10  # Snake size
snake_speed = 10  # Increased speed for better gameplay experience

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
question_font = pygame.font.SysFont("comicsansms", 20)
score_font = pygame.font.SysFont("comicsansms", 35)

# General Knowledge Questions (as provided)
questions = [
    {
        "question": "What is the primary purpose of a class in OOP?",
        "options": ["Wraps", "Inherit", "Abstract"],
        "answer": "Wraps"
    },

    {
        "question": "Which keyword is used to create a class in Python?",
        "options": ["def", "class", "method"],
        "answer": "class"
    },
    {
        "question": "What is the term for a function defined inside a class?",
        "options": ["Method", "Subfunc", "Action"],
        "answer": "Method"
    },

    {
        "question": "What is an instance of a class called?",
        "options": ["Object", "Model", "Sample"],
        "answer": "Object"
    },
    {
        "question": "Which OOP concept allows new classes to inherit properties?",
        "options": ["Extend", "Child", "Derive"],
        "answer": "Extend"
    },

    {
        "question": "What keyword is used to inherit a class?",
        "options": ["class", "inherits", "extends"],
        "answer": "extends"
    },
    {
        "question": "What is the access level that restricts visibility?",
        "options": ["Private", "Protected", "Public"],
        "answer": "Private"
    },
]

# Shuffle questions to randomize
random.shuffle(questions)

# Function to display score
def display_score(score):
    value = score_font.render("Score: " + str(score), True, green)
    display.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(display, green, [block[0], block[1], snake_block, snake_block])

# Function to display messages on the screen
def message(msg, color, position):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, position)

# Function to display question and options
def display_question(question_data):
    question = question_data["question"]
    options = question_data["options"]
    
    # Display the question at the top
    question_text = question_font.render(question, True, green)
    display.blit(question_text, [width / 9, height / 6])
    
    # Return options to be placed as food on the screen
    return options

# Function to check if snake collides with an option
def check_collision(x, y, option_pos):
    option_width = 100  # Width of the option block
    option_height = 30  # Height of the option block
    return (x >= option_pos[0] and x < option_pos[0] + option_width and 
            y >= option_pos[1] and y < option_pos[1] + option_height)

# Function to get centered positions for options
# Function to get centered positions for options
def get_option_positions(options):
    option_positions = []
    
    # Define option block size and spacing
    option_width = 150  # Increased width
    option_height = 50  # Increased height
    space_between = 30   # Increased space between options
    
    # Calculate the total width of all options combined, plus spaces between them
    total_width = len(options) * option_width + (len(options) - 1) * space_between

    # Start x position to center the combined options
    start_x = (width - total_width) // 2
    y_position = height // 2.5  # Vertically centered

    for i in range(len(options)):
        option_x = start_x + i * (option_width + space_between)
        option_positions.append((option_x, y_position))

    return option_positions

    # Inside the main game loop, modify the rectangle drawing for options
    # Display the options on the screen
    for i, option in enumerate(options):
        option_text = question_font.render(option, True, green)
        # Draw a rectangle around options for better visibility
        pygame.draw.rect(display, green, [option_positions[i][0], option_positions[i][1], 150, 50], 2)  # Updated size
        # Center the text within the option rectangle
        text_rect = option_text.get_rect(center=(option_positions[i][0] + 75, option_positions[i][1] + 25))  # Updated centering
        display.blit(option_text, text_rect.topleft)


# Main game loop
def game_loop():
    game_over = False
    game_close = False
    score = 0
    question_index = 0
    total_questions = len(questions)

    # Snake initial position
    x = width / 2
    y = height / 2
    x_change = 0
    y_change = 0

    # Snake properties
    snake_list = []
    snake_length = 1

    # Get the first question
    current_question = questions[question_index]

    # Get option positions
    option_positions = get_option_positions(current_question["options"])

    while not game_over:

        # Game over screen
        while game_close:
            display.fill(black)
            message(f"Game Over! Final Score: {score}", green, [width / 6, height / 3])
            message("Press Q-Quit or C-Play Again", green, [width / 6, height / 2])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # Check if snake hits boundaries
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += x_change
        y += y_change
        display.fill(black)

        # Display question and options
        options = display_question(current_question)
        
        # Display the options on the screen
        for i, option in enumerate(options):
            option_text = question_font.render(option, True, green)
            # Draw a rectangle around options for better visibility
            pygame.draw.rect(display, green, [option_positions[i][0], option_positions[i][1], 100, 30], 2)
            # Center the text within the option rectangle
            text_rect = option_text.get_rect(center=(option_positions[i][0] + 50, option_positions[i][1] + 15))
            display.blit(option_text, text_rect.topleft)

        # Snake movement
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Snake collides with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        display_score(score)

        # Check if the snake eats one of the options
        for i, option_pos in enumerate(option_positions):
            if check_collision(x, y, option_pos):
                chosen_option = options[i]
                if chosen_option == current_question["answer"]:
                    score += 1
                else:
                    score -= 1
                question_index += 1
                if question_index >= total_questions:
                    game_close = True
                else:
                    current_question = questions[question_index]
                    option_positions = get_option_positions(current_question["options"])

        # Update display and control game speed
        pygame.display.update()
        clock.tick(snake_speed)

    # Quit game
    pygame.quit()
    quit()

# Run the game
game_loop()

