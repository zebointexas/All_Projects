import datetime
import csv
import robin_stocks
from robin_stocks import *
import sched, time

s = sched.scheduler(time.time, time.sleep)

def in_time_range(ranges):
    now = time.strptime(time.strftime("%H%M%S"),"%H%M%S")
    ranges = ranges.split(",")
    for range in ranges:
        r = range.split("-")
        if time.strptime(r[0],"%H%M%S") <= now <= time.strptime(r[1],"%H%M%S") or time.strptime(r[0],"%H%M%S") >= now >=time.strptime(r[1],"%H%M%S"):
            return True
    return False

while True:
    time.sleep(30)
    print('Now -->  ' + str(datetime.datetime.now()))
    if(in_time_range('0830-1600')):
        robin_stocks.login('zeboxiong.texas@gmail.com', 'XKSJSG@Kuhgd98173~&%$#')
        cur_Price = robin_stocks.stocks.get_latest_price('SAVE', True)
        csvdata = [datetime.datetime.now()]
        csvFile = open("2020_0521_SAVE.csv", "a")
        Fileout = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_ALL)
        ##Fileout.writerow(csvdata)
        Fileout.writerow(cur_Price)
        csvFile.close()




