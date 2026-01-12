# 2048.py

Terminal version of the game "2048" written in **Python** with **MVC Pattern**.

> Originally ported from [C++ version](https://github.com/plibither8/2048.cpp), now refactored with modern Python design patterns and amateur-friendly code style!

## 🎮 Features

✨ **Clean MVC Architecture** - Separated concerns for easy maintenance  
🎨 **Colorful Terminal UI** - ANSI colors for beautiful tile display  
💾 **Save/Load System** - Continue your game anytime  
🎯 **Professional ASCII Art** - Generated with `pyfiglet`  
📝 **Beginner-Friendly Code** - camelCase naming with Indonesian narrative comments  

## 🖼️ Preview

```
   ___   ____  __ __  ____ 
  |__ \ / __ \/ // / ( __ )
  __/ // / / / // /_/ __  |
 / __// /_/ /__  __/ /_/ / 
/____/\____/  /_/  \____/  

+------------------------------+
| SCORE:       232           |
| BEST SCORE:  232           |
| MOVES:       39            |
+------------------------------+

+------+------+------+------+
|  2   |  4   |  16  |      |
+------+------+------+------+
|  8   |  16  |  32  |  2   |
+------+------+------+------+
|  2   |  4   |  2   |      |
+------+------+------+------+
|  2   |      |      |      |
+------+------+------+------+
```

## 🚀 Setup

### Requirements
- **Python 3.7+**
- **Windows OS** (for `msvcrt` module)
- **pip** (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/delissesu/Slide-To-2K48.git
   cd 2048
   ```

2. **Install dependencies**
   ```bash
   pip install pyfiglet
   ```

3. **Run the game!** 🎉
   ```bash
   python main.py
   ```

## 🎯 How to Play

### Game Start
When you run the game, you'll see a menu:
- **1**: Start a new game
- **2**: Continue from saved game (if available)

### Controls
| Key | Action |
|-----|--------|
| `W` / `K` / `↑` | Move Up |
| `S` / `J` / `↓` | Move Down |
| `A` / `H` / `←` | Move Left |
| `D` / `L` / `→` | Move Right |
| `P` / `Z` | Save Game |
| `Q` | Quit |

### Goal
Combine tiles with the same number to reach **2048**!

## 🏗️ Architecture

**MVC Pattern** (Model-View-Controller):
- **Model** (`model.py`): Handles game logic, board state, and rules
- **View** (`view.py`): Renders the terminal UI with ASCII art and colors
- **Controller** (`controller.py`): Manages user input and game flow


## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs via [Issues]
- 💡 Suggest new features
- 🔧 Submit pull requests

## 🙏 Credits

- Original C++ version by [Mihir Chaturvedi](https://github.com/plibither8/2048.cpp)
- Python port and refactoring by [Delissesu](https://github.com/delissesu)
- ASCII art powered by [pyfiglet](https://github.com/pwaller/pyfiglet)
