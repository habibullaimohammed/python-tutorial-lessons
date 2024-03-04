questions = [['What is the capital of France?', 'Paris'], # The first question
             ['Which planet is known as the "Red Planet', 'Mars'],
             ['What is the largest mammal on Earth', 'Elephant']]
score = 0
failed_ans = []

firstQ = input(f'{questions[0][0]}: ').lower()
if firstQ == questions[0][1].lower():
    score = score + 10
else:
    failed_ans.append(questions[0])

secondQ = input(f'{questions[1][0]}: ').lower()
if secondQ == questions[1][1].lower():
    score += 10
else:
    failed_ans.append(questions[1])

thirdQ = input(f'{questions[2][0]}: ').lower()
if secondQ == questions[2][1].lower():
    score += 10
else:
    failed_ans.append(questions[2])

print(f'Score: {score}')
print('Failed question answer\n', failed_ans)
