Exercise 5b:

Create a Python program that simulates a basic quiz. The quiz should consist of three multiple-choice questions, each with four options (A, B, C, D). The user should be prompted to answer each question, and at the end of the quiz, the program should display the user's score.

Here are the questions:

1. What is the capital of France? 
   - A Berlin
   - B. Madrid
   - C. Paris
   - D. Rome

2. Which planet is known as the "Red Planet"?
   - A. Jupiter
   - B. Mars
   - C. Venus
   - D. Saturn

3. What is the largest mammal on Earth?
   - A. Elephant
   - B. Blue Whale
   - C. Giraffe
   - D. Gorilla

Create a program `quiz` that handles the quiz logic. The program return the user's score. Make sure to provide feedback on the correctness of each answer.

Here's a starter code to help you get started:

```python
questions = [['What is the capital of France?', 'Paris']]
score = 0
failed_ans = []

firstQ = input('What is the capital of France? ')
if firstQ == questions[0][0]:
   score += 1
else:
   failed_ans.append(questions[0][0])
   
secondQ = input('Which planet is known as the "Red Planet"? ')

```

This code provides a framework for the quiz, with questions, options, correct answers, and user input handling. You can modify or expand it as needed.