A playable 2D chess game and custom move-generation engine built from scratch in Python and Pygame with zero external chess libraries. Everything runs on custom board state management, turn tracking, and piece move logic—checkmate doesn't work yet, along with a few other advanced chess rules still in progress.
Prerequisites

    Python 3.x installed on your computer

    Pygame installed via command prompt

Open cmd and install Pygame:
Bash

pip install pygame

Install Instructions

    Download chess.zip containing the project files and piece images:

HTML

<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/2dfe5fe1-1d2a-4d35-8295-4a1d8f652b33" />

    Extract chess.zip so all scripts and the images folder stay together in the same directory:

HTML

<img width="1917" height="1078" alt="Screenshot 2026-11-23 160056" src="https://github.com/user-attachments/assets/52be92a0-f17d-4a9d-afdb-9edac62c44eb" />

    Open the chess folder and verify ChessMain.py, ChessEngine.py, and images/ are present:

HTML

<img width="996" height="967" alt="Screenshot 2026-11-23 160529" src="https://github.com/user-attachments/assets/b1a757c5-e5d7-4457-8b8f-b43e47a55ceb" />

    Double-click ChessMain.py (or run python ChessMain.py from the folder in cmd) to launch the board:

HTML

<img width="1917" height="1078" alt="Screenshot 2026-11-23 160401" src="https://github.com/user-attachments/assets/e89654d3-6199-48f9-952a-a19bbcb4eb8a" />

Controls

    Click to move a piece: Select a friendly piece on your turn, then click a destination square to move it (click another friendly piece to switch selection or the same square to deselect):

HTML

<img width="652" height="681" alt="image" src="https://github.com/user-attachments/assets/c8da41f8-d87a-4fd1-8567-6a84757851f5" />

    Press Z to undo a move: Step back through previous moves in the game history.
