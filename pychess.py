import pygame


def main():
    pygame.init()

    pygame.display.set_caption("PyChess")

    screen = pygame.display.set_mode((512,512))
    screen.fill((0,0,0))

    chess_board = [[1,0,1,0,1,0,1,0],
                   [0,1,0,1,0,1,0,1],
                   [1,0,1,0,1,0,1,0],
                   [0,1,0,1,0,1,0,1],
                   [1,0,1,0,1,0,1,0],
                   [0,1,0,1,0,1,0,1],
                   [1,0,1,0,1,0,1,0],
                   [0,1,0,1,0,1,0,1]]

    pawn_piece = pygame.image.load('test_image.png')

    piece_positions = [['e','e','e','e','e','e','e','e'],
                       ['p','p','p','p','p','p','p','p'],
                       ['e','e','e','e','e','e','e','e'],
                       ['e','e','e','e','e','e','e','e'],
                       ['e','e','e','e','e','e','e','e'],
                       ['e','e','e','e','e','e','e','e'],
                       ['p','p','p','p','p','p','p','p'],
                       ['e','e','e','e','e','e','e','e']]

    for i in range(8):
        for j in range(8):

            if chess_board[i][j] == 1:
                colour = (10,10,10)
            else:
                colour = (255,255,255)
            square = pygame.Rect(j*64,i*64,64,64)
            pygame.draw.rect(screen,colour,square)

            


    running = True
    while running:
        for i in range(8):
            for j in range(8):
                if piece_positions[i][j] == 'p':
                    screen.blit(pawn_piece,(64*j,64*i))
                else :
                    #clear the moved piece

        pygame.display.update()
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            piece_positions[1][1] = 'e'
            piece_positions[0][0] = 'p'


if __name__=="__main__":
    main()