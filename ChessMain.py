import pygame
import ChessEngine

pygame.init()

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.smoothscale(
            pygame.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE)
        )


def is_friendly_piece(gs, row, col):
    piece = gs.board[row][col]
    if piece == "--":
        return False
    return (piece[0] == "w" and gs.whiteToMove) or (piece[0] == "b" and not gs.whiteToMove)


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess")
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    validMoves = gs.getValidMoves()
    moveMode = False
    running = True
    sqSelected = ()       # tuple: (row, col)
    playerClicks = []     # list of tuples: [(row1, col1), (row2, col2)]

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            elif e.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                clicked_sq = (row, col)

                # 1. Clicking the already-selected square deselects it
                if sqSelected == clicked_sq:
                    sqSelected = ()
                    playerClicks = []

                # 2. If a piece is already selected...
                elif sqSelected != ():
                    # Clicking another friendly piece switches selection immediately
                    # (unless it's a valid capture/castling move—check validMoves first)
                    candidate_move = ChessEngine.Move(sqSelected, clicked_sq, gs.board)
                    if candidate_move in validMoves:
                        playerClicks.append(clicked_sq)
                    elif is_friendly_piece(gs, row, col):
                        sqSelected = clicked_sq
                        playerClicks = [clicked_sq]
                    else:
                        # Clicked an invalid square -> reset selection
                        sqSelected = ()
                        playerClicks = []

                # 3. No piece selected yet -> select only if it's a friendly piece
                else:
                    if is_friendly_piece(gs, row, col):
                        sqSelected = clicked_sq
                        playerClicks = [clicked_sq]

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_z:
                    gs.undoMove()
                    sqSelected = ()
                    playerClicks = []
                    moveMode = True

            if len(playerClicks) == 2:
                move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                print(move.getChessNotation())
                if move in validMoves:
                    moveMode = True
                    gs.makeMove(move)
                sqSelected = ()
                playerClicks = []

            if moveMode:
                validMoves = gs.getValidMoves()
                moveMode = False

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        pygame.display.flip()


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


def drawBoard(screen):
    colors = [pygame.Color("#F0D9B5"), pygame.Color("#B58863")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()