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

count = 0

SAVE_FLAG = False
ZOOM_FLAG = False
HSBC_FLAG = False

####################################################################################################
while True:

    print('****************************************************************************   Start Again!!!  **********************************************')
    robin_stocks.login('zeboxiong.texas@gmail.com', 'XKSJSG@Kuhgd98173~&%$#')

    print('SAVE_FLAG = ' + str(SAVE_FLAG));
    print('ZOOM_FLAG = ' + str(ZOOM_FLAG));
    print('HSBC_FLAG = ' + str(HSBC_FLAG));

    count = 0

    while True:

        time.sleep(6)

        if(count>1000):
            break

        #####################################################################   SAVE
        if(in_time_range('0800-1730')):

                count = count + 1
                my_stocks = robin_stocks.build_holdings()

                cur = robin_stocks.stocks.get_latest_price('SAVE', True)
                cur = float(cur[0])

                print('Spirit -->  ' + str(datetime.datetime.now()) +  '    Price -->  '  +  str(cur)    + '  ---------------> SAVE' )

                if(cur < 9.0 and SAVE_FLAG == False):
                    robin_stocks.order_buy_market('SAVE', 110)  # buy!
                    SAVE_FLAG = True
                    print('Bought ' + str(110) + ' SAVE !!!')

        #####################################################################   Zoom
                count = count + 1
                my_stocks = robin_stocks.build_holdings()

                cur = robin_stocks.stocks.get_latest_price('ZM', True)
                cur = float(cur[0])

                print('Zoom   -->  ' + str(datetime.datetime.now()) +  '    Price -->  '  +  str(cur)   )

                if(cur < 133 and ZOOM_FLAG == False):
                    robin_stocks.order_buy_market('ZM', 7)  # buy!
                    ZOOM_FLAG = True
                    print('Bought ' + str(7) + ' ZOOM !!!')

        #####################################################################   HSBC
                count = count + 1
                my_stocks = robin_stocks.build_holdings()

                cur = robin_stocks.stocks.get_latest_price('HSBC', True)
                cur = float(cur[0])

                print('HSBC   -->  ' + str(datetime.datetime.now()) +  '    Price -->  '  +  str(cur) )

                if(cur < 15 and HSBC_FLAG == False):
                    robin_stocks.order_buy_market('HSBC', 41)  # buy!
                    HSBC_FLAG = True
                    print('Bought ' + str(V) + ' HSBC !!!')
