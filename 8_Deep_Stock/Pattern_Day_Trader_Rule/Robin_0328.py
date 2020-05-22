import robin_stocks
from robin_stocks import *

import datetime
import time


def in_time_range(ranges):
    now = time.strptime(time.strftime("%H%M%S"),"%H%M%S")
    ranges = ranges.split(",")
    for range in ranges:
        r = range.split("-")
        if time.strptime(r[0],"%H%M%S") <= now <= time.strptime(r[1],"%H%M%S") or time.strptime(r[0],"%H%M%S") >= now >=time.strptime(r[1],"%H%M%S"):
            return True
    return False

#获取文件倒数第n行
def getTail(file,num):
    readlen=1024 #每次多偏移1024字节
    readoffset=0 #每次从文件末尾向前偏移量
    linenum=0 #当前读取的行号
    preindex=None #上一个换行符所在位置
    while True:
        readoffset=readoffset+readlen #文件每次偏移readoffset个字符
     #   if file.seek(readoffset,2)==None:
      #      file.seek(0,1) #若无num行则移到开始处
        readline=file.read()
        if preindex==None: #当为第一次查找换行符
            index=readline.rfind('\n')
        else:
            index=readline.rfind('\n',0,preindex-1) #否则从前一个换行符开始找
        while index>-1:  #获取读取文本中总共的行数
            linenum=linenum+1
            if linenum==num:
                return readline[index:preindex]
            preindex=index
            index=readline.rfind('\n',0,preindex-1)
    if linenum!=num: #若无这么多行,报错
        print("ERROR:this file only have %d lines"%(linenum))
        return None

hold_price20 = 77777
hold_price5 = 77777
hold_price2 = 77777

V = 1

already_Buy20 = False
already_Buy5 = False
already_Buy2 = False

print('Start while')
while True:
    time.sleep(10)
    print('Now -->  ' + str(datetime.datetime.now()))
    if(in_time_range('0900-1430')):
            robin_stocks.login('zeboxiong.texas@gmail.com', 'XKSJSG@Kuhgd98173~&%$#')
            my_stocks = robin_stocks.build_holdings()

            cur = robin_stocks.stocks.get_latest_price('SAVE', True)
            cur = float(cur[0])

            print('******************************************* Now price *******************************************')
            print('******************************************* Now price *******************************************')
            print('hold_price20: ' + str(hold_price20))
            print('hold_price5:  ' + str(hold_price5))
            print('hold_price2:  ' + str(hold_price2))

            print(' ')
            print('Now price:   ' + str(cur) + '  <----------')
            print(' ')

            file = open('2020_0521_SAVE.csv', 'r')

            print('--20--')
            ## ************************ Get 20 minutes history ************************
            file.close
            file = open('2020_0521_SAVE.csv', 'r')
            his20 = getTail(file, 20)
            his20 = his20[2:]
            his20 = his20[:-1]
            his20 = float(his20)

            rate20_Buy = his20 / cur

            if (rate20_Buy >= 1.02 and already_Buy20 == False):  # buy when DOWN
                hold_price20 = cur  # update hold
                robin_stocks.order_buy_market('SAVE', V)  # buy!
                already_Buy20 = True  # update flag
                print('buy - 20  -->  ' + str(datetime.datetime.now()))
                print('rate20_Buy          ' + str(round(rate20_Buy, 4)))

            rate20_Sell = cur / hold_price20


            if ((rate20_Sell >= 1.01) and already_Buy20 == True):  # sell when up 0.1
                print('hold_price20: ' + str(hold_price20))
                robin_stocks.order_sell_market('SAVE', V)
                already_Buy20 = False
                print('sell - 20 -->  ' + str(datetime.datetime.now()))
                print('Earning!!!  -->  ' + str(cur - hold_price20))
                hold_price20 = 77777
                print('rate20_Sell          ' + str(round(rate20_Sell, 4)) + '      Cur: ' + str(cur) + '     His: ' + str(hold_price2) )

            print('his20 price:      ' + str(his20))

            print('--5--')
            ## ************************ Get 5 minutes history ************************
            file.close
            file = open('2020_0521_SAVE.csv', 'r')
            his5 = getTail(file, 5)
            his5 = his5[2:]
            his5 = his5[:-1]
            his5 = float(his5)

            rate5_Buy = his5 / cur

            if (rate5_Buy >= 1.012 and already_Buy5 == False):  # buy when DOWN
                hold_price5 = cur  # update hold
                robin_stocks.order_buy_market('SAVE', V)  # buy!
                already_Buy5 = True  # update flag
                print('buy - 5  -->  ' + str(datetime.datetime.now()))
                print('rate5_Buy          ' + str(round(rate5_Buy, 4)))

            rate5_Sell = cur / hold_price5

            if ((rate5_Sell >= 1.006) and already_Buy5 == True):  # sell when up 0.1
                print('hold_price5: ' + str(hold_price5))
                robin_stocks.order_sell_market('SAVE', V)
                already_Buy5 = False
                print('sell - 5 -->  ' + str(datetime.datetime.now()))
                print('Earning!!!  -->  ' + str(cur - hold_price5))
                hold_price5 = 77777
                print('rate5_Sell          ' + str(round(rate5_Sell, 4)) + '      Cur: ' + str(cur) + '     His: ' + str(hold_price2) )

            print('his5 price:      ' + str(his5))

            print('--2--')
            ## ************************ Get 2 minutes history ************************
            file.close
            file = open('2020_0521_SAVE.csv', 'r')
            his2 = getTail(file, 2)
            his2 = his2[2:]
            his2 = his2[:-1]
            his2 = float(his2)

            rate2_Buy = cur / his2

            if (rate2_Buy >= 1.001 and already_Buy2 == False):  # buy when UP
                hold_price2 = cur  # update hold
                robin_stocks.order_buy_market('SAVE', V) # buy!
                already_Buy2 = True # update flag
                print('buy - 2  -->  ' + str(datetime.datetime.now()))
                print('rate2_Buy          ' + str(round(rate2_Buy, 4)))

            rate2_Sell = cur / hold_price2


            if ( (rate2_Sell < 1 or rate2_Sell >= 1.001) and already_Buy2 == True):   # sell when up 0.001
                print('hold_price2: ' + str(hold_price2))
                robin_stocks.order_sell_market('SAVE', V)
                already_Buy2 = False
                print('sell - 2 -->  ' + str(datetime.datetime.now()))
                print('Earning!!!  -->  ' + str(  cur - hold_price2 ) + '      Cur: ' + str(cur) + '     His: ' + str(hold_price2) )
                hold_price2 = 77777
                print('rate2_Sell          ' + str(round(rate2_Sell, 4)))

            print('his2 price:      ' + str(his2))

    if (in_time_range('1430-1500')):
            robin_stocks.login('zeboxiong.texas@gmail.com', 'XKSJSG@Kuhgd98173~&%$#')
            my_stocks = robin_stocks.build_holdings()
            robin_stocks.order_sell_market('SAVE', V)
            print('Selling')


