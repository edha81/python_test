from question import question
test = [
   'a?\n1\n2\n3\n',
   'b?\n1\n2\n3\n',    
   'c?\n1\n2\n3\n',
]

questions = [
  question(test[0],'a'),
  question(test[1],'b'),
  question(test[2],'c')
]

def run_test(questions):
  s = 0
  for question in questions:
    ans = input(question.description)
    if ans == question.ans:
      s += 1
    print('score='+str(s)+'/'+str(len(questions)))

run_test(questions)