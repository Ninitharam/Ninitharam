# HANGMAN GAME

### TABLE OF CONTENTS 
- About
- Prerequisite
- Game Features
- Git
- UML
- Requirements Engneering
- DDD
- Metrics
- Clean Code Development
- Build Management
- Unit tests
- IDE
- Functional Programming
  
### ABOUT
In an electronic version of the word guessing game Hangman, participants use letter suggestions to try and solve a hidden word. Usually, a randomly chosen word that is represented by a string of dashes for each letter appears at the start of the game. As players guess, the word's proper letters are exposed, while their wrong guesses help to gradually draw a hangman figure. When the word is correctly guessed or the hangman is entirely drawn, which indicates a loss, the game is over. The gallows and letter displays, among other visual components, give users an interactive and interesting interface experience.

### PREREQUISITE
- Software and Tools
   - Visual Studio: Ensure you have Visual Studio installed. You can download it from the https://visualstudio.microsoft.com/ website.
     The Community Edition is free and should suffice for this project.
   - Python Development Workload in Visual Studio: During the installation (or modification, if already installed) of Visual Studio,
     select the Python development workload. This includes the Python runtime and necessary tools to develop Python applications.
   - Python Interpreter: While the Python development workload in Visual Studio typically installs a Python interpreter,
      you can also use an existing installation of Python on your system.
   - Pygame Library: Pygame is a set of Python modules designed for writing video games. Install it using pip (Python's package installer)
     by running pip install pygame in the command line or terminal.
     
- Learning Resources
  - Pygame Documentation: Essential for understanding the functions and modules in Pygame.
  - Visual Studio Python Documentation: Helpful for leveraging Visual Studio's features for Python development.
    
### GAME FEATURES
- Core Game Features
  - Word Bank: A collection of words from which the game randomly selects a secret word for each round.
  - Display of Blanks: Representing the secret word with underscores or dashes for each missing letter.
  - Letter Guessing Mechanism: Allowing the player to input guesses, typically one letter at a time.
  - Limited Attempts: A maximum number of incorrect guesses before the game is lost.

- Visual Representation
   - Text-Based Hangman: Displaying the hangman and gallows as ASCII art, updating with each incorrect guess.
   - Graphical Hangman (using Pygame ): A more visually appealing hangman and gallows that get drawn or revealed progressively.
     
- User Interface
   - Input Validation: Ensuring that user inputs are valid (e.g., single characters, alphabetic input).
   - Real-Time Feedback: Immediate feedback on guesses, showing correctly guessed letters and previously attempted letters.
   - Game Status: Displaying the number of remaining guesses and, optionally, a list of incorrect guesses.
     
- Game Logic and Flow
   - Win/Lose Conditions: Clear conditions for winning (guessing the word) and losing (exceeding the incorrect guess limit).
   - Game Restart Option: Allowing the player to start a new game once the current game ends.

### GIT
Usage of GitHub for the whole project time

Commit History 


https://github.com/Ninitharam/Ninitharam/commits/91513ffed749415ea4d3a1662572b54d90d0fdd1

### UML
UML Diagrams created with Plantext UML

+ Dynamic-Activity diagram
+ Static- Class and Deployment Diagram

PNGs and Planttext Files


https://github.com/Ninitharam/Ninitharam/tree/origin/UML%20Diagrams%20Link

### REQUIREMENTS ENGINEERING
Two variants used and by mapping functional and non-functional requirements in 2 tools .

- Self-made version
  - Trello
    
   https://trello.com/b/7pobofqu/hangman-game
  
- Professional version 
  - Jira
    
   https://softwaredevelopmentproject.atlassian.net/jira/software/projects/HG/boards/3

 A permissions restriction may prevent access; an overview of the images is given

 https://github.com/Ninitharam/Ninitharam/tree/origin/JIRA

 
### DDD (DOMAIN DRIVEN DEVELOPMENT )
Link to DDD Miro Board 

https://miro.com/app/board/uXjVN9lL9H8=/?share_link_id=452751581660
### METRICS
### CLEAN CODE DEVLOPMENT
### BUILD MANAGEMENT
### UNIT TESTS
### IDE 
+ Visual Studio Code
  
### Favourite Shortcut Keys

+ F5 (Start Debugging) - Handy for quickly refactoring code, which is useful when iterating on game logic.

+ Ctrl + Shift + B (Build Solution) - Essential for running  Hangman game to test changes as I develop.

+ Ctrl + Space (IntelliSense) - Quickly builds the game to check for compile-time errors.

+ F9 (Toggle Breakpoint) - Offers code completion suggestions which are useful when coding game logic.

+ F12 (Go To Definition) - Extremely helpful for debugging game logic, like checking conditions for winning or losing.

+ Ctrl + - (Navigate Backwards) / Ctrl + Shift + - (Navigate Forwards) - Find where a specific method or variable is used throughout the game code.

+ Ctrl + Shift + F (Find in Files) - Quickly find and jump to any file or symbol in the project.

+ Ctrl + K, Ctrl + D (Format Document) - Quickly delete lines of code.

+ Alt + Enter (Full Screen) - Format game code to make it more readable and maintain a consistent coding style.

+ Ctrl + Z (Undo) / Ctrl + Y (Redo) - Focus on coding without distractions.

### FUNCTIONAL PROGRAMMING
  
