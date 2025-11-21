# Konfigurasi Game 2048

# Ukuran papan sama target menangnya
boardSize = 4
winningTile = 2048

# Kode warna ANSI buat terminal
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

# Nah ini warna buat tiap angka di kotak
# Makin gede angkanya, makin cantik warnanya
tileColors = {
    0: Colors.BRIGHT_BLACK,
    2: Colors.BRIGHT_MAGENTA,
    4: Colors.BRIGHT_YELLOW,
    8: Colors.BRIGHT_MAGENTA,
    16: Colors.BRIGHT_CYAN,
    32: Colors.BRIGHT_RED,
    64: Colors.BRIGHT_RED,
    128: Colors.BRIGHT_BLUE,
    256: Colors.BRIGHT_BLUE,
    512: Colors.BRIGHT_GREEN,
    1024: Colors.BRIGHT_GREEN,
    2048: Colors.BRIGHT_YELLOW,
}

# Teks kontrol buat petunjuk main
controlsText = [
    "W or K or ↑ => Up",
    "A or H or ← => Left",
    "S or J or ↓ => Down",
    "D or L or → => Right",
    "Z or P => Save",
    "",
    "Press the keys to start and continue."
]
