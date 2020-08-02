
def hour_turn_seconds(x):
    if type(x) is int:
        x=str(x)+':0'
    hour=int(x.split(":")[0])
    min=int(x.split(":")[1])
    if hour <=24 and min<=60:
        time_in_scond=(hour*3600)+(min*60)
        return (time_in_scond)
    else:
        print('wrong input! you should put time in format of hour:minute, 0<=hour<24 and 0<=sec<60')
        exit()

def min_turn_seconds(y):
    if type(y)is int:
        y=str(y)+':0'
    if int(y.split(':')[1])< 60:
        time_in_seconds=int(y.split(':')[0])* 60 +int(y.split(':')[1])
        return(time_in_seconds)
    else:
        print('you should put speed in format of  minute: second(min <= 60 & sec <= 60)')
        exit()

import pyinputplus as pyip
start = pyip.inputNum('when did you leave your house and started running ?\n',allowRegexes=[':'])
time1 = hour_turn_seconds(start)

while True:
    mile = pyip.inputNum('how many miles did you run? \n')
    speed = pyip.inputNum('what was your speed (minute/miles)? \n',allowRegexes=[':'])
    speed=min_turn_seconds(speed)
    time2= speed * mile
    arrive = time1 + time2
    z=pyip.inputYesNo('did you run more? please answer with yes or no. \n')
    if z.lower() == 'no':
        if arrive > 24 *3600:
            arrive = arrive - (24 * 3600)
        arrive_hour = arrive // 3600
        arrive_min = (arrive % 3600) // 60
        arrive_sec = (arrive % 3600) % 60
        arrival = ('%d:%d:%d')%(arrive_hour, arrive_min, arrive_sec)
        print('You arrived home at:', arrival)
        break
    if z.lower() =='yes':
        time1 = arrive
        continue















