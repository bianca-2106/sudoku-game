from math import floor
import pygame
import random


def valid(board, row, col, num):
    if num in board[row]:
        return False

    for i in range(9):
        if board[i][col]==num:
            return False

    box_x=(row//3)*3
    box_y=(col//3)*3
    for i in range(box_x, box_x+3):
        for j in range(box_y, box_y+3):
            if board[i][j]==num:
                return False
    return True


def generate_board(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                random.shuffle(numbers)

                for num in numbers:
                    if valid(board, row, col, num):
                        board[row][col] = num

                        if generate_board(board):
                            return True

                        board[row][col] = 0

                return False

    return True

def easy():
    global correct_matrix, sudoku_matrix, original_matrix, left_to_complete
    correct_matrix = [[0 for _ in range(9)] for _ in range(9)]

    generate_board(correct_matrix)

    uncompleted_cells = []

    left_to_complete = 30

    for i in range(30):
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        if (x,y) not in uncompleted_cells:
            uncompleted_cells.append((x,y))
        else:
            left_to_complete -= 1


    sudoku_matrix = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(9):
        for j in range(9):
            sudoku_matrix[i][j] = correct_matrix[i][j]

    for i, j in uncompleted_cells:
        sudoku_matrix[i][j] = 0

    original_matrix = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if sudoku_matrix[i][j] != 0:
                original_matrix[i][j] = 1

def medium():
    global correct_matrix, sudoku_matrix, original_matrix, left_to_complete
    correct_matrix = [[0 for _ in range(9)] for _ in range(9)]

    generate_board(correct_matrix)

    uncompleted_cells = []

    left_to_complete = 45

    for i in range(45):
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        if (x, y) not in uncompleted_cells:
            uncompleted_cells.append((x, y))
        else:
            left_to_complete -= 1

    sudoku_matrix = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(9):
        for j in range(9):
            sudoku_matrix[i][j] = correct_matrix[i][j]

    for i, j in uncompleted_cells:
        sudoku_matrix[i][j] = 0

    original_matrix = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if sudoku_matrix[i][j] != 0:
                original_matrix[i][j] = 1

def hard():
    global correct_matrix, sudoku_matrix, original_matrix, left_to_complete
    correct_matrix = [[0 for _ in range(9)] for _ in range(9)]

    generate_board(correct_matrix)

    uncompleted_cells = []

    left_to_complete = 65

    for i in range(65):
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        if (x, y) not in uncompleted_cells:
            uncompleted_cells.append((x, y))
        else:
            left_to_complete -= 1

    sudoku_matrix = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(9):
        for j in range(9):
            sudoku_matrix[i][j] = correct_matrix[i][j]

    for i, j in uncompleted_cells:
        sudoku_matrix[i][j] = 0

    original_matrix = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if sudoku_matrix[i][j] != 0:
                original_matrix[i][j] = 1

pygame.init()
screen = pygame.display.set_mode((1440, 1440))
pygame.display.set_caption("Sudoku Game")
running = True
state=0
offset = 180
grid_size = 1440-2*offset
cell_size = grid_size / 9
pygame.font.init()
number_font = pygame.font.SysFont("Arial", 60)

correct_matrix = [[0 for _ in range(9)] for _ in range(9)]
sudoku_matrix = [[0 for _ in range(9)] for _ in range(9)]
original_matrix = [[0 for _ in range(9)] for _ in range(9)]

selected_cell = None
selected_number = 0

added_number = 0
deleted_cell = None
mistakes = 0
left_to_complete = 0
assist=0

heart1=pygame.transform.scale(pygame.image.load("assets/heart.png"), (80, 74))
heart2=pygame.transform.scale(pygame.image.load("assets/heart.png"), (80, 74))
heart3=pygame.transform.scale(pygame.image.load("assets/heart.png"), (80, 74))
toggle_off=pygame.transform.scale(pygame.image.load("assets/toggle-off.png"), (150, 150))
toggle_on=pygame.transform.scale(pygame.image.load("assets/toggle-on.png"), (150, 150))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if state==1:
                mouse_x, mouse_y=pygame.mouse.get_pos()

                if offset<=mouse_x <=offset+grid_size and offset<=mouse_y <=offset+grid_size:
                    clicked_col=(mouse_x-offset)//cell_size
                    clicked_row=(mouse_y-offset)//cell_size

                    selected_cell=(clicked_col,clicked_row)
                elif 150<= mouse_x <=300 and 1180<=mouse_y<=1380:
                        if assist==0:
                            assist=1
                        else:
                            assist=0
                else:
                    selected_cell=None
            elif state==0:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 580<=mouse_x <= 580+280:
                    if 670<=mouse_y<=670+120:
                        easy()
                    elif 920<=mouse_y<=920+120:
                        medium()
                    elif 1170<=mouse_y<=1170+120:
                        hard()
                    state=1
        elif state==1 and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                added_number=1
            elif event.key == pygame.K_2:
                added_number=2
            elif event.key == pygame.K_3:
                added_number=3
            elif event.key == pygame.K_4:
                added_number=4
            elif event.key == pygame.K_5:
                added_number=5
            elif event.key == pygame.K_6:
                added_number=6
            elif event.key == pygame.K_7:
                added_number=7
            elif event.key == pygame.K_8:
                added_number=8
            elif event.key == pygame.K_9:
                added_number=9
            elif event.key == pygame.K_BACKSPACE:
                deleted_cell=selected_cell
            elif event.key == pygame.K_r:
                state=0



    screen.fill((148, 115, 189))
    if state==1:
        pygame.draw.rect(screen, (192, 252, 246), pygame.Rect((offset, offset), (grid_size, grid_size)))

        if selected_cell is not None:
            sel_row, sel_col=selected_cell
            highlight_x=sel_col*cell_size+offset
            highlight_y=sel_row*cell_size+offset

            selected_number=sudoku_matrix[floor(sel_col)][floor(sel_row)]

            pygame.draw.rect(screen, (191, 160, 250), pygame.Rect((highlight_y, highlight_x), (cell_size, cell_size)))

            for i in range(9):
                ok=0
                highlight_cell=None
                for j in range(9):
                    cell_value=sudoku_matrix[i][j]
                    if cell_value != 0 and cell_value == selected_number:
                        highlight_cell=(j*cell_size+offset,i*cell_size+offset)
                        if assist==1:
                            pygame.draw.rect(screen, (171, 245, 255), pygame.Rect(
                                (offset + (j//3) *3* cell_size,
                                 offset + (i//3) *3* cell_size), (3 * cell_size, 3 * cell_size)))
                        ok=1
                if ok==1:
                    if assist==1:
                        pygame.draw.rect(screen, (171, 245, 255), pygame.Rect((offset, highlight_cell[1]), (grid_size, cell_size)))
                        pygame.draw.rect(screen, (171, 245, 255), pygame.Rect((highlight_cell[0], offset), (cell_size, grid_size)))
                    pygame.draw.rect(screen, (219, 203, 247), pygame.Rect((highlight_cell[0], highlight_cell[1]), (cell_size, cell_size)))

            if selected_number!=0 and sudoku_matrix[floor(sel_col)][floor(sel_row)] != correct_matrix[floor(sel_col)][floor(sel_row)]:
                pygame.draw.rect(screen, (255, 0, 0),
                pygame.Rect((highlight_y, highlight_x), (cell_size, cell_size)))
            else:
                pygame.draw.rect(screen, (191, 160, 250), pygame.Rect((highlight_y, highlight_x), (cell_size, cell_size)))

            if added_number!=0 and selected_number==0:
                sudoku_matrix[floor(sel_col)][floor(sel_row)]=added_number
                if sudoku_matrix[floor(sel_col)][floor(sel_row)]!=correct_matrix[floor(sel_col)][floor(sel_row)]:
                    mistakes+=1
                else:
                    left_to_complete-=1
            added_number=0

            if deleted_cell is not None:
                if original_matrix[floor(sel_col)][floor(sel_row)]==0:
                    sudoku_matrix[floor(sel_col)][floor(sel_row)]=0
                deleted_cell=None





        for i in range(10):
            thickness = 5 if i%3==0 else 1

            #vertical lines
            pygame.draw.line(
                screen, (0,0,0),
                (offset + i * cell_size, offset),
                (offset + i * cell_size, offset + grid_size),
                thickness)

            #horizontal lines
            pygame.draw.line(
                screen, (0,0,0),
                (offset, offset + i * cell_size),
                (offset + grid_size, offset + i * cell_size),
                thickness
            )

            for row in range(9):
                for col in range(9):
                    cell_value=sudoku_matrix[row][col]
                    if cell_value != 0:
                        text_surface=number_font.render(str(cell_value), True, (0,0,0))

                        center_x=offset+(col*cell_size)+(cell_size//2)
                        center_y=offset+(row*cell_size)+(cell_size//2)

                        text_rect=text_surface.get_rect(center=(center_x,center_y))

                        screen.blit(text_surface, text_rect)

        if mistakes==0:
            screen.blit(heart1, (680, 50))
            screen.blit(heart2, (520, 50))
            screen.blit(heart3, (820, 50))
        elif mistakes==1:
            screen.blit(heart1, (680, 50))
            screen.blit(heart2, (520, 50))
        elif mistakes==2:
            screen.blit(heart1, (520, 50))

        if mistakes==3:
            screen.fill((255, 13, 37))
            font=pygame.font.SysFont('Arial', 150)
            you_lost=font.render('You lost!', True, (255, 255, 255))
            textRect=you_lost.get_rect()
            textRect.center=(720, 720)
            screen.blit(you_lost, textRect)

            pygame.display.flip()

            pygame.time.wait(3000)

            state=0
            mistakes=0

        if left_to_complete==0:
            pygame.display.flip()
            pygame.time.wait(1000)

            screen.fill((143, 250, 135))
            font = pygame.font.SysFont('Arial', 150)
            you_won = font.render('You won!', True, (0, 0, 0))
            textRect = you_won.get_rect()
            textRect.center = (720, 720)
            screen.blit(you_won, textRect)

            pygame.display.flip()

            pygame.time.wait(3000)

            state = 0
            mistakes = 0

        if assist==0:
            screen.blit(toggle_off, (150, 1260))
        else:
            screen.blit(toggle_on, (150, 1260))

        font=pygame.font.SysFont('Arial', 56)
        assist_font=font.render('Assist', True, (0, 0, 0))
        assistRect=assist_font.get_rect()
        assistRect.center=(380, 1340);
        screen.blit(assist_font, assistRect)

        font2=pygame.font.SysFont('Arial', 45)
        reset=font2.render('Press R to restart', True, (0, 0, 0))
        resetRect=reset.get_rect()
        resetRect.center=(1100, 1340);
        screen.blit(reset, resetRect)



    elif state==0:
        pygame.draw.rect(screen, (115, 185, 250), pygame.Rect((360, 240), (720, 240)))
        font1=pygame.font.SysFont('Arial', 150)
        new_game=font1.render('New game', True, (0, 79, 153))
        textRect=new_game.get_rect()
        textRect.center=(360+(720//2), 240+(240//2))
        screen.blit(new_game, textRect)

        font = pygame.font.SysFont('Arial', 78)

        pygame.draw.rect(screen, (0, 79, 153), pygame.Rect((580, 670), (280, 120)))
        easymode=font.render('Easy', True, (115, 185, 250))
        easyRect=easymode.get_rect()
        easyRect.center=(580+(280//2), 670+(120//2))
        screen.blit(easymode, easyRect)

        pygame.draw.rect(screen, (0, 79, 153), pygame.Rect((580, 920), (280, 120)))
        mediummode = font.render('Medium', True, (115, 185, 250))
        mediumRect = mediummode.get_rect()
        mediumRect.center = (580 + (280 // 2), 920 + (120 // 2))
        screen.blit(mediummode, mediumRect)

        pygame.draw.rect(screen, (0, 79, 153), pygame.Rect((580, 1170), (280, 120)))
        hardmode = font.render('Hard', True, (115, 185, 250))
        hardRect = hardmode.get_rect()
        hardRect.center = (580 + (280 // 2), 1170 + (120 // 2))
        screen.blit(hardmode, hardRect)


    pygame.display.flip()

pygame.quit()