import time

# 成绩评判
score = int(input('Please enter your score:'))
if score >= 0 and score < 60:
    print('Unqualified')
elif score >= 60 and score < 70:
    print('Qualified')
elif score >= 70 and score < 80:
    print('Normal')
elif score >= 80 and score < 90:
    print('Good')
elif score >= 90 and score <= 100:
    print('Excellent')
elif not (score >= 0 and score <= 100):
    print('Invalid Input')

time.sleep(3)
# 火车站安检
ticket = input('Enter anything or press Enter:')
if ticket :
    print('检票通过，请接受安检')
    knife_length = int(input('knife length:'))
    if knife_length > 20 :
        print('knife length is too long, %dcm' % knife_length)
    else :
        print('Safety check passed,Welcome!')
else :
    print('Please buy ticket first')