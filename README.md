# Quizzler App in Python

**Try the Quiz App on Replit: [Quizzler app]([https://replit.com/@YashMasane/Project-quiz-game](https://replit.com/@YashMasane/Quizzler-App))**

Welcome to the Quizzler App in Python! This project is a simple interactive quiz application that tests your general knowledge by asking a series of questions. You'll be presented with a question and need to answer with either "yes" or "no". At the end of the quiz, you'll receive a score based on the number of correct answers.

## Table of Contents

- [Project Structure](#project-structure)
- [Usage](#usage)
- [Contributions](#contributions)
- [Acknowledgments](#acknowledgments)

## Project Structure

The project is organized into different modules, each containing specific classes and functionalities:

- **data**: This module contains a list of questions for the quiz. Each question is represented as a dictionary with the "question" and "correct_answer" keys.

- **question_model**: This module defines the `Question` class. Each question object has attributes for the question itself and its correct answer.

- **quiz_brain**: This module contains the `QuizBrain` class, which handles the main logic of the quiz. It has methods to move to the next question, display the current question, and check the user's answer. 
- **ui**: This module is responsible for GUI of app.
## Usage

## Usage

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/your-username/quiz-app.git
    ```

2. Navigate to the project directory:

    ```
    cd quiz-app
    ```

3. Run the `main.py` file to start the quiz:

    ```
    python main.py
    ```

4. Follow the prompts to answer the quiz questions. Type "yes" or "no" to answer each question.

5. Once you've answered all the questions, your final score will be displayed.

## Contributions

Contributions to this project are welcome! If you'd like to improve the quiz app, add more questions, enhance the user interface, or fix any issues, feel free to open a pull request.

## Acknowledgments

Special thanks to the contributors and developers who have contributed to this project.

---

Have fun testing your general knowledge with the Console-Based Quiz App in Python! If you have any questions, suggestions, or issues, feel free to open an issue on the GitHub repository. Enjoy the quiz!
