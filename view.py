import os
import config
from model import GameModel

class TerminalRenderer:
    def clearScreen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw(self, game: GameModel):
        self.clearScreen()
        self._drawHeader()
        self._drawStats(game)
        self._drawBoard(game.board)
        self._drawControls()

    def _drawHeader(self):
        # Nah ini yang bikin ASCII art gede "2048" di atas
        import pyfiglet
        asciiArt = pyfiglet.figlet_format("2048", font="slant")
        print(config.Colors.BRIGHT_GREEN)
        print(asciiArt)
        print(config.Colors.RESET)
        print()

    def _drawStats(self, game: GameModel):
        width = 30
        print(f"+{'-' * width}+")
        print(f"| SCORE:       {game.board.score:<13} |")
        print(f"| BEST SCORE:  {game.bestScore:<13} |")
        print(f"| MOVES:       {game.moves:<13} |")
        print(f"+{'-' * width}+")
        print()

    def _drawBoard(self, board):
        cellWidth = 6
        horizontalLine = ("+" + "-" * cellWidth) * board.size + "+"
        
        # Gambar grid per baris
        for row in board.grid:
            print(horizontalLine)
            rowStr = "|"
            for tile in row:
                # Ambil warna sesuai angkanya
                color = config.tileColors.get(tile, config.Colors.RESET)
                tileStr = str(tile) if tile != 0 else ""
                
                # Biar angkanya di tengah kotaknya
                paddingLeft = (cellWidth - len(tileStr)) // 2
                paddingRight = cellWidth - len(tileStr) - paddingLeft
                
                rowStr += f"{' ' * paddingLeft}{color}{tileStr}{config.Colors.RESET}{' ' * paddingRight}|"
            print(rowStr)
        print(horizontalLine)
        print()

    def _drawControls(self):
        for line in config.controlsText:
            print(line)
            
    def drawGameOver(self, win: bool):
        if win:
            print(f"\n{config.Colors.BRIGHT_GREEN}YOU WIN! CONGRATULATIONS!{config.Colors.RESET}")
        else:
            print(f"\n{config.Colors.BRIGHT_RED}GAME OVER! TRY AGAIN!{config.Colors.RESET}")
