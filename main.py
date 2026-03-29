from math import floor

import pygame

pygame.init()
screen = pygame.display.set_mode((1440, 1440))
pygame.display.set_caption("Sudoku Game")
running = True

offset=120
grid_size=1200
cell_size= grid_size / 9
pygame.font.init()
number_font=pygame.font.SysFont("Arial", 60)

#sudoku_matrix=[[0 for _ in range(9)] for _ in range(9)]

sudoku_matrix = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

selected_cell=None
selected_number=0

added_number=0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y=pygame.mouse.get_pos()

            if offset<=mouse_x <=offset+grid_size and offset<=mouse_y <=offset+grid_size:
                clicked_col=(mouse_x-offset)//cell_size
                clicked_row=(mouse_y-offset)//cell_size

                selected_cell=(clicked_col,clicked_row)
            else:
                selected_cell=None
        elif event.type == pygame.KEYDOWN:
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
                added_number=0



    screen.fill((148, 115, 189))

    pygame.draw.rect(screen, (192, 252, 246), pygame.Rect((120, 120), (1200, 1200)))

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
                    pygame.draw.rect(screen, (171, 245, 255), pygame.Rect(
                        (offset + (j//3) *3* cell_size,
                         offset + (i//3) *3* cell_size), (3 * cell_size, 3 * cell_size)))
                    ok=1
            if ok==1:
                pygame.draw.rect(screen, (171, 245, 255), pygame.Rect((offset, highlight_cell[1]), (grid_size, cell_size)))
                pygame.draw.rect(screen, (171, 245, 255), pygame.Rect((highlight_cell[0], offset), (cell_size, grid_size)))
                pygame.draw.rect(screen, (219, 203, 247), pygame.Rect((highlight_cell[0], highlight_cell[1]), (cell_size, cell_size)))


        pygame.draw.rect(screen, (191, 160, 250), pygame.Rect((highlight_y, highlight_x), (cell_size, cell_size)))

        if added_number!=0 and selected_number==0:
            sudoku_matrix[floor(sel_col)][floor(sel_row)]=added_number
            added_number=0





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



    pygame.display.flip()

pygame.quit()