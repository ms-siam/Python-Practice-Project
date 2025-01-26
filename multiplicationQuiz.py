import pyinputplus as pyip
import random, time

numOfQues = 10
correctAns = 0

for quesNo in range(numOfQues):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    mulNum = num1 * num2
    quesSerial = quesNo + 1
    prompt = f'#{quesSerial}: {num1} x {num2} = '
    try:
        pyip.inputStr(prompt, allowRegexes=[f'^{mulNum}$'], blockRegexes=[('.*', 'Incorrect!')], timeout=8,limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correctAns =+ 1
    time.sleep(1)
print(f'Score: {correctAns}/{numOfQues}')