import msvcrt
import sys
from model import GameModel
from view import TerminalRenderer
import save

class InputHandler:
    def getInput(self) -> str:
        # Tunggu sampe user neken tombol, terus balikin command-nya
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                try:
                    char = key.decode('utf-8').lower()
                    if char in ['w', 'k']: return 'UP'
                    if char in ['s', 'j']: return 'DOWN'
                    if char in ['a', 'h']: return 'LEFT'
                    if char in ['d', 'l']: return 'RIGHT'
                    if char in ['z', 'p']: return 'SAVE'
                    if char == 'q': return 'QUIT'
                    
                    # Handle tombol panah (kirim 2 byte)
                    if key == b'\xe0':
                        arrow = msvcrt.getch()
                        if arrow == b'H': return 'UP'
                        if arrow == b'P': return 'DOWN'
                        if arrow == b'K': return 'LEFT'
                        if arrow == b'M': return 'RIGHT'
                except:
                    pass
    
    def getMenuInput(self) -> str:
        """Buat input di menu start"""
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                try:
                    char = key.decode('utf-8')
                    return char
                except:
                    pass

class GameController:
    def __init__(self):
        self.model = None
        self.view = TerminalRenderer()
        self.input = InputHandler()
        self.running = True
    
    def showStartMenu(self):
        """Tampilkan menu awal buat pilih new game atau continue"""
        self.view.clearScreen()
        print("=== 2048 GAME ===\n")
        
        if save.hasSavedGame():
            print("1. New Game")
            print("2. Continue Game")
            print("\nPilih (1/2): ", end="", flush=True)
            
            choice = self.input.getMenuInput()
            
            if choice == '2':
                loadedGame = save.loadGame()
                if loadedGame:
                    self.model = loadedGame
                    print("Game loaded!")
                    import time
                    time.sleep(1)
                    return
        
        # Kalau gak ada saved game atau pilih new game
        self.model = GameModel()

    def run(self):
        # Tampilkan menu dulu sebelum mulai
        self.showStartMenu()
        
        self.view.draw(self.model)
        
        # Loop utama game jalan di sini
        while self.running:
            command = self.input.getInput()
            
            if command == 'QUIT':
                self.running = False
                break
            
            # Handle save game
            if command == 'SAVE':
                if save.saveGame(self.model):
                    print("\n✓ Game saved!")
                    import time
                    time.sleep(1)
                    self.view.draw(self.model)
                continue
            
            moved = False
            if command in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
                moved = self.model.move(command)
            
            # Kalau ada gerakan, gambar ulang layarnya
            if moved:
                self.view.draw(self.model)
                
                # Cek menang atau kalah
                if self.model.board.isWin():
                    self.view.drawGameOver(win=True)
                    self.waitForExit()
                    break
                
                if self.model.board.isGameOver():
                    self.view.drawGameOver(win=False)
                    self.waitForExit()
                    break

    def waitForExit(self):
        print("\nPress any key to exit...")
        msvcrt.getch()

