# Hangman Game

## Overview

This is a two-player Python-based Hangman game where one player provides a secret word and a hint, and the other player attempts to guess the word within a limited number of attempts. The program demonstrates the use of various Python functionalities, including `getpass` for hiding input, loops, and string manipulation.

## Features

- **Interactive Gameplay**: One player sets the secret word and provides a hint, while the other player guesses the word letter by letter.
- **Hidden Input**: The secret word and hint are hidden from view using the `getpass` module.
- **Custom Attempts**: The number of attempts allowed is calculated as 2 plus the length of the secret word.
- **Dynamic Feedback**: Players receive real-time updates on their progress with the word.

## How It Works

1. **Secret Word Input**: The first player enters a secret word (alphabets only) and a hint category.
2. **Attempts Calculation**: The number of attempts is calculated as `len(word) + 2`.
3. **Gameplay**:
   - The second player guesses the word by entering one letter at a time.
   - If a guessed letter is in the word, the game updates the displayed progress.
   - If the guessed letter is incorrect, the player loses one attempt.
4. **Win or Lose**:
   - The player wins if they guess the word within the given attempts.
   - The player loses if they run out of attempts.


## Code Highlights

- **`getpass.getpass()`**: Ensures the secret word and hint are hidden from view.
- **Dynamic String Manipulation**: Updates and displays the progress of guessed letters in real-time.
- **Error Handling**: Validates user inputs to ensure they are alphabetic.

## Learning Journey

Creating this game helped me:
- Understand and utilize the `getpass` module.
- Enhance my logic-building skills for game mechanics.
- Debug and solve technical challenges, such as updating partially guessed words dynamically.
- Build confidence in Python programming.

## Challenges Faced

- Implementing the logic for dynamically updating the guessed word.
- Ensuring input validation and smooth user interaction.

## Future Enhancements

- Add a single-player mode with a predefined word list.
- Implement a graphical user interface (GUI) for improved user experience.
- Include difficulty levels to modify the number of attempts.

## Author

**Oalmiposi Marvelous Ogunbiyi**

I am a Python enthusiast and beginner programmer, continuously improving my skills through hands-on projects. This Hangman game is my second Python project, and I am excited to continue learning and growing as a developer.



---

Enjoy the game and happy coding!
