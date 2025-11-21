import random
from typing import List, Tuple, Optional
import config

class Board:
    def __init__(self, size: int = config.boardSize):
        self.size = size
        self.grid: List[List[int]] = [[0 for _ in range(size)] for _ in range(size)]
        self.score = 0
        self.moved = False

    def addRandomTile(self) -> None:
        # Cari kotak yang masih kosong (nilainya 0)
        emptyCells = [
            (r, c) for r in range(self.size) for c in range(self.size)
            if self.grid[r][c] == 0
        ]
        if emptyCells:
            r, c = random.choice(emptyCells)
            # 90% muncul angka 2, 10% muncul angka 4
            self.grid[r][c] = 4 if random.random() > 0.9 else 2

    def reset(self) -> None:
        self.grid = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.score = 0
        self.addRandomTile()
        self.addRandomTile()

    def _compress(self, row: List[int]) -> List[int]:
        # Buang angka 0 dari baris
        return [x for x in row if x != 0]

    def _merge(self, row: List[int]) -> List[int]:
        # Gabungin angka yang sama bersebelahan
        for i in range(len(row) - 1):
            if row[i] != 0 and row[i] == row[i + 1]:
                row[i] *= 2
                self.score += row[i]
                row[i + 1] = 0
        return row

    def _fill(self, row: List[int]) -> List[int]:
        # Tambahin 0 di belakang biar panjangnya sama
        return row + [0] * (self.size - len(row))

    def _processRow(self, row: List[int]) -> List[int]:
        # Ini yang ngatur gerakan: padatin -> gabung -> padatin lagi -> isi 0
        compressed = self._compress(row)
        merged = self._merge(compressed)
        final = self._compress(merged)
        return self._fill(final)

    def moveLeft(self) -> bool:
        oldGrid = [row[:] for row in self.grid]
        newGrid = []
        for row in self.grid:
            newGrid.append(self._processRow(row))
        self.grid = newGrid
        return self.grid != oldGrid

    def moveRight(self) -> bool:
        oldGrid = [row[:] for row in self.grid]
        newGrid = []
        for row in self.grid:
            # Balik dulu, proses, terus balik lagi
            reversedRow = row[::-1]
            processed = self._processRow(reversedRow)
            newGrid.append(processed[::-1])
        self.grid = newGrid
        return self.grid != oldGrid

    def moveUp(self) -> bool:
        oldGrid = [row[:] for row in self.grid]
        # Transpose (kolom jadi baris)
        transposed = [list(row) for row in zip(*self.grid)]
        newTransposed = []
        for row in transposed:
            newTransposed.append(self._processRow(row))
        # Transpose balik
        self.grid = [list(row) for row in zip(*newTransposed)]
        return self.grid != oldGrid

    def moveDown(self) -> bool:
        oldGrid = [row[:] for row in self.grid]
        transposed = [list(row) for row in zip(*self.grid)]
        newTransposed = []
        for row in transposed:
            reversedRow = row[::-1]
            processed = self._processRow(reversedRow)
            newTransposed.append(processed[::-1])
        self.grid = [list(row) for row in zip(*newTransposed)]
        return self.grid != oldGrid

    def isGameOver(self) -> bool:
        # Kalau masih ada kotak kosong, berarti belum kalah
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == 0:
                    return False
        
        # Cek apakah masih bisa gabung horizontal
        for r in range(self.size):
            for c in range(self.size - 1):
                if self.grid[r][c] == self.grid[r][c + 1]:
                    return False
                    
        # Cek apakah masih bisa gabung vertikal
        for r in range(self.size - 1):
            for c in range(self.size):
                if self.grid[r][c] == self.grid[r + 1][c]:
                    return False
        
        # Kalau sampai sini berarti udah gak bisa gerak lagi
        return True

    def isWin(self) -> bool:
        for row in self.grid:
            if config.winningTile in row:
                return True
        return False

class GameModel:
    def __init__(self):
        self.board = Board()
        self.bestScore = 0
        self.moves = 0
        self.board.reset()

    def move(self, direction: str) -> bool:
        moved = False
        if direction == 'UP':
            moved = self.board.moveUp()
        elif direction == 'DOWN':
            moved = self.board.moveDown()
        elif direction == 'LEFT':
            moved = self.board.moveLeft()
        elif direction == 'RIGHT':
            moved = self.board.moveRight()
            
        if moved:
            self.moves += 1
            self.board.addRandomTile()
            # Update best score kalau skor sekarang lebih gede
            if self.board.score > self.bestScore:
                self.bestScore = self.board.score
                
        return moved
