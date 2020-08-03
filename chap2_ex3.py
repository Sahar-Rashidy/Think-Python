def hour_turn_seconds(x):
    if type(x) is int:
        x = str(x) + ':0'
    hour = int(x.split(":")[0])
    min = int(x.split(":")[1])
    if 0 <= hour<= 24 and 0 <= min <= 60:
        time_in_scond = (hour * 3600) + (min * 60)
        return (time_in_scond)
    else:
        print('wrong input! you should put time in format of hour:minute, 0<=hour<24 and 0<=sec<60')
        exit()


def min_turn_seconds(y):
    if type(y) is int:
        y = str(y) + ':0'
    if 0<= int(y.split(':')[1]) and 0<= int(y.split(':')[1]) < 60:
        time_in_seconds = int(y.split(':')[0]) * 60 + int(y.split(':')[1])
        return (time_in_seconds)
    else:
        print('you should put speed in format of  minute: second(0 <= min < 60 & 0 <= sec < 60)')
        exit()

import sqlite3
import pyinputplus as pyip
conn=sqlite3.connect('running_archivedb.sqlite')
cur=conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS Archive (date DATE , duration INTEGER)')
date= pyip.inputDate('Please enter the date: \n')
start = pyip.inputInt('when did you leave your house and started running?\n', allowRegexes=[':'])
time1=hour_turn_seconds(start)
while True:
    mile = pyip.inputNum('how many miles did you run? \n')
    speed = pyip.inputInt('what was your speed (minute/miles)? \n', allowRegexes=[':'])
    speed = min_turn_seconds(speed)
    time2 = speed * mile
    arrive = time1 + time2
    z = pyip.inputYesNo('did you run more? please answer with yes or no. \n')
    if z.lower() == 'no':
        cur.execute('INSERT INTO Archive (date, duration) VALUES (?, ?)',(date, time2) )
        conn.commit()
        if arrive > 24 * 3600:
            arrive = arrive - (24 * 3600)
        arrive_hour = arrive // 3600
        arrive_min = (arrive % 3600) // 60
        arrive_sec = (arrive % 3600) % 60
        arrival = ('%d:%d:%d') % (arrive_hour, arrive_min, arrive_sec)
        print('You arrived home at:', arrival)
        i=0
        summ=0
        cur.execute('SELECT duration FROM Archive')
        for row in cur:
            summ=summ+row[0]
            i=i+1
        if i==1:
            print('This seems to be your first day of running. Well done!')
        else:
            average=summ/i
            if time2 > average:
                print('You ran better than most days. Keep it up')
            elif time2 == average:
                print('you are keeping in track')
            else:
                print('You did better the other days. try harder')
        conn.close()
        break
    if z.lower() == 'yes':
        time1 = arrive
        continue






