# Grid War - A Turn-Based Chess-Like Game
Grid War is an advanced turn-based strategy game inspired by chess, featuring a unique 5x5 grid-based battlefield. This game is designed for two players, each controlling a team of 5 characters consisting of Pawns, Hero1, and Hero2. The game is built with a server-client architecture using WebSocket communication for real-time interactions, and a web-based user interface that delivers a smooth and engaging experience.

# Key Features:
Real-Time Gameplay: Leverages WebSockets for seamless real-time communication between the server and the clients.
Character Types:
Pawns: Move one block in any direction.
Hero1: Moves two blocks straight and can eliminate any opponent in its path.
Hero2: Moves two blocks diagonally and can eliminate any opponent in its path.
Winning Condition: The game ends when one player eliminates all of their opponent's characters, with the winner announced on the game board.
Intuitive Interface: A clean, responsive UI that presents the game grid, move history, and player status.

# Technology Stack:
Backend: Flask for handling server-side logic and game state management.
Frontend: HTML, CSS, and JavaScript for rendering the game board and managing user interactions.
WebSocket: For real-time communication between the client and server.

# How to Play:
Each player sets up their characters on their respective starting rows.
Players take turns to move their characters according to their move set.
The game board updates in real-time, reflecting the latest moves and character positions.
The game continues until one player wins by eliminating all opponent characters.
This project showcases a blend of real-time gameplay mechanics with a strategic grid-based battle system, making it an exciting and challenging experience for players.
![Screenshot 2024-08-27 115540](https://github.com/user-attachments/assets/d4ac8d66-d75a-49be-9125-1e5156858ea1)
![Screenshot 2024-08-27 115503](https://github.com/user-attachments/assets/0dd0d06c-a416-4107-96d9-c66af7bd231f)
![Screenshot 2024-08-27 115615](https://github.com/user-attachments/assets/ff53fc50-3e50-4da8-937d-7cdc493ac511)


