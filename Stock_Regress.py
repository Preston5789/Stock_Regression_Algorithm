

'''WELCOME TO OPERATION BLUEBOOK'''
'''Put Your Personal Stuff In Here:'''

api_key = ''
api_secret = ''




tickerlist = ['oaxeth@ticker', 'wtceth@ticker','bateth@ticker', 'ltceth@ticker','trxeth@ticker',
              'zrxeth@ticker', 'adaeth@ticker','engeth@ticker', 'naveth@ticker','eoseth@ticker',
              'ltceth@ticker', 'rlceth@ticker','rcneth@ticker', 'evxeth@ticker','icxeth@ticker']

import time
import datetime
import math
import numpy
from scipy.stats import linregress
import matplotlib.pyplot as plt
from binance.client import Client
from binance.websockets import BinanceSocketManager
from matplotlib.widgets import Button


'''...........This Bool Will Start Moving Money.......'''
Jesus=0
'''..................DO NOT TOUCH....................'''

stop=datetime.datetime.now()
position =0
tdyyield=0.0
lssyield= [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
buy_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
sell_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
buytime_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
selltime_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
temp_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
temp2_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
temptime_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
temptime2_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
trackertime_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
tracker_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
slope_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
slope2_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
slopetime_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
slopetime2_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
toperror_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
bottomerror_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
toperror2_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
bottomerror2_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
line1_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
line2_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
decider = [True, True, True, True, True,True, True, True, True, True,True, True, True, True, True]
totalsell = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
graphswitcheroo = 0
wrap = False

client = Client(api_key, api_secret)
startbalnace=client.get_asset_balance('ETH')
startbalnace = startbalnace['free']

print(startbalnace)

def buy():

    global decider
    if(sum(totalsell) < 10.0):
        print('We are looking to buy!!')
        lssyield[position]=0

        if((float(bottomerror_list[position][-1]) > float(toperror2_list[position][-1])) & (float(bottomerror2_list[position][-1])>0.0)):
            print('Buying That SHIT!')
            buy_list[position].append(temp_list[position][len(temp_list[position])-1])
            buytime_list[position].append((temptime_list[position][len(temptime_list[position])-1]))
            totalsell[position] = 1
            if(wrap == True):
                decider[position] = True
            else:
                decider[position] = False
            buyvolume=float(startbalnace)/(10.0*float(temp_list[position][len(temp_list[position])-1]))
            buyvolume=math.trunc(buyvolume)
            print("We are buying {} Shares of {}".format(buyvolume, tickerlist[position]))
            tempname=tickerlist[position].split("@")
            tempname = str(tempname[0]).upper()

            print(tempname)
            if(Jesus==1):
                order = client.create_order(
                    symbol=tempname,
                    side=Client.SIDE_BUY,
                    type=Client.ORDER_TYPE_MARKET,
                    quantity=buyvolume)
                print(order)
    else:
        print('holding')


def sell():
    global decider
    global tdyyield
    lssyield[position]=100*((float(tracker_list[position][-1])-float(buy_list[position][-1]))/(float(buy_list[position][-1]))-0.002)/10
    if( (1.00519*float(buy_list[position][-1]) < float(temp_list[position][-1])) ):

        print('We are looking to Sell!!!')

        if((float(toperror_list[position][-1]) >=  1.0*float(bottomerror2_list[position][-1]))& (float(toperror_list[position][-1]) < 0.0)):
            print('Selling That SHIT!')
            sell_list[position].append(temp_list[position][-1])
            selltime_list[position].append((temptime_list[position][-1]))
            tdyyield += -100*((float(buy_list[position][-1])-float(sell_list[position][-1]))/float((buy_list[position][-1]))-0.002)/10
            lssyield[position]=0
            totalsell[position] = 0
            decider[position] = True

            tempname=tickerlist[position].split("@")
            tempname = str(tempname[0]).upper()
            tempvolname = tempname[0:3]
            print(tempvolname)
            print("We are selling ")
            if(Jesus==1):
                sellvolume=client.get_asset_balance(tempvolname)
                sellvolume=math.trunc(float(sellvolume['free']))
                print("We are selling {} Shares of {}".format(sellvolume, tickerlist[position]))
                order = client.create_order(
                    symbol=tempname,
                    side=Client.SIDE_SELL,
                    type=Client.ORDER_TYPE_MARKET,
                    quantity=sellvolume)
                print(order)

def decide():
    if(decider[position] == True):
        buy()

    if(decider[position] == False):
        sell()

def process_m_message(msg):

    if((msg['data']['e'] != 'error')):

        global position

        tickername = str(msg['stream'])
        position = tickerlist.index(tickername)
        '''print("stream: {} data: {}".format(msg['stream'], msg['data']))'''


        tester = str(msg['data']['c'])
        timer = str(msg['data']['E'])

        tracker_list[position].append(tester)
        trackertime_list[position].append(timer)
        temp_list[position].append(tester)
        temptime_list[position].append(timer)
        temp2_list[position].append(tester)
        temptime2_list[position].append(timer)



        if(len(tracker_list[position]) >= 35):
            print("The stock: {} is currently has a time of: {}".format(tickerlist[position], trackertime_list[position][-1]))
            temptimearray = numpy.asarray(temptime_list[position]).astype(numpy.float)
            temparray = numpy.asarray(temp_list[position]).astype(numpy.float)
            temparray /= numpy.float(tracker_list[position][0])


            model = linregress(temptimearray,temparray)
            slope = model.slope
            slope_list[position].append(slope)
            slopetime_list[position].append(timer)

            intercept = model.intercept
            line = slope*temptimearray + intercept

            avgx = sum(temptimearray)/len(temptimearray)
            devx = (temptimearray - avgx)**2
            devx = sum(devx)
            devx = (devx)**0.5

            error = (temparray - line)**2
            error = sum(error)/33
            error = (error)**(.5)
            error = 4.957*error/devx


            toperror_list[position].append(error+slope)
            bottomerror_list[position].append(slope-error)

            temp_list[position].remove(temp_list[position][0])
            temptime_list[position].remove(temptime_list[position][0])
            line1_list[position] = numpy.delete(line, [0])

        if(len(tracker_list[position]) >= 95):
            longtimearray2 = numpy.asarray(temptime2_list[position]).astype(numpy.float)
            longarray2 = numpy.asarray(temp2_list[position]).astype(numpy.float)
            longarray2 /= numpy.float(tracker_list[position][0])
            temptimearray2 = numpy.asarray(temptime2_list[position][29:94]).astype(numpy.float)
            temparray2 = numpy.asarray(temp2_list[position][29:94]).astype(numpy.float)
            temparray2 /= numpy.float(tracker_list[position][0])

            modell = linregress(temptimearray2, temparray2)
            slope2 = modell.slope
            slope2_list[position].append(slope2)
            slopetime2_list[position].append(timer)

            intercept2 = modell.intercept
            line2 = slope2*longtimearray2 + intercept2
            line2_list[position] = numpy.delete(line2, [0])
            avgx2 = sum(temptimearray2)/len(temptimearray2)
            devx2 = (temptimearray2 - avgx2)**2
            devx2 = sum(devx2)
            devx2 = (devx2)**0.5

            error2 = (longarray2 - line2)**2
            error2 = sum(error2)/93
            error2 = (error2)**(.5)
            error2 = 4.957*error2/devx2



            toperror2_list[position].append(error2+slope2)
            bottomerror2_list[position].append(slope2-error2)

            temp2_list[position].remove(temp2_list[position][0])
            temptime2_list[position].remove(temptime2_list[position][0])
            decide()

    if (len(slope_list[position])> 120):

            slope_list[position].remove(slope_list[position][0])
            slopetime_list[position].remove(slopetime_list[position][0])
            toperror_list[position].remove(toperror_list[position][0])
            bottomerror_list[position].remove(bottomerror_list[position][0])
    if (len(slope2_list[position])> 120):
            slope2_list[position].remove(slope2_list[position][0])
            slopetime2_list[position].remove(slopetime2_list[position][0])
            toperror2_list[position].remove(toperror2_list[position][0])
            bottomerror2_list[position].remove(bottomerror2_list[position][0])

def clock_reset():
    global stop
    stop = (datetime.datetime.now() + datetime.timedelta(seconds=30))


plt.ion()
fig, axs = plt.subplots(4, 1,figsize=(8,10), constrained_layout=True)
x1, y1 = [],[]
x2, y2 = [], []
x3, y3 = [], []
x4, y4 = [], []
buyx, buyy = [], []
sellx, selly = [], []

s=2
lnn, = axs[0].plot([],[], 'purple', linewidth = 0.75)
ln, = axs[0].plot([],[],'black', linewidth = 0.75)
livedata = axs[0].scatter(x1,y1,s=s, c = 'blue')
selldata = axs[0].scatter(sellx, selly, s = 15, c = 'r')
buydata = axs[0].scatter(buyx, buyy, s = 15, c = 'g')

livedata = axs[0].scatter(x1,y1,s=s)
selldata = axs[0].scatter(sellx, selly, s = 15, c = 'r')
buydata = axs[0].scatter(buyx, buyy, s = 15, c = 'g')

axs[0].set_title('Live Data')
axs[1].set_title('Linear Regression Analysis')
axs[1].set_ylabel('Slope Value')

axs[0].set_ylabel('Price Over Time')
axs[0].set_xlabel('time (s)')
axs[1].set_xlabel('time (s)')


ln1, = axs[1].plot([],[], 'r', linewidth = 0.2,)
ln2, = axs[1].plot([],[], 'r', linewidth=0.2)
ln11, = axs[1].plot([],[], 'g', linewidth=0.4)
ln22, = axs[1].plot([],[], 'g', linewidth=0.4)
slopedata = axs[1].scatter(x3,y3, s=s, c = 'black')
slopedata2 = axs[1].scatter(x4,y4, s=s, c = 'blue')
maxtime = time.time()*1000.0 + 20000
begintime = time.time()*1000.0
axs[0].set_xlim(begintime,maxtime)
axs[1].set_xlim(begintime,maxtime)
axs[0].grid()
axs[1].grid()
plt.draw()


axs[2].set_title('Operation Pinkbook: Control Panel')
axs[3].set_title('Historical Data')
axs[2].set_ylabel('Price')
axs[2].set_xlabel('Server Time')
ticker_text = fig.text(0.5, 0.43, '' , multialignment="left")
time_text = fig.text(0.5, 0.40, '' , multialignment="left")
yield_text = fig.text(0.5, 0.37, '', multialignment="left")
lossyield_text = fig.text(0.5, 0.34, '', multialignment="left")
totalsell_text = fig.text(0.5, 0.31, '', multialignment="left")

print('Starting Websocket')
bm = BinanceSocketManager(client, user_timeout=20)
conn_key = bm.start_multiplex_socket(tickerlist, process_m_message)
bm.start()
'''Buttons'''
def on_click(event):
       print('doubleclick')


def _yes(event):
    global graphswitcheroo
    graphswitcheroo += 1
    if(graphswitcheroo>=len(tickerlist)):
        graphswitcheroo = 0

def _closeshop(event):
    global wrap
    print('Wrapping It All Up!!!')
    wrap = True
    for(i,item) in enumerate(totalsell):
        if(item==1):
            print(i)

            tempname=tickerlist[i].split("@")
            tempname = str(tempname[0]).upper()
            tempvolname = tempname[0:3]
            print(tempvolname)
            sellvolumefinal=client.get_asset_balance(tempvolname)
            sellvolumefinal=math.trunc(float(sellvolumefinal['free']))
            print("The sellvolume is {}".format(sellvolumefinal))

            print("We are selling {} Shares of {}".format(sellvolumefinal, tickerlist[i]))
            if(Jesus==1):
                order = client.create_order(
                    symbol=tempname,
                    side=Client.SIDE_SELL,
                    type=Client.ORDER_TYPE_MARKET,
                    quantity=sellvolumefinal)
                print(order)
                totalsell[i] = 0;

def _rendergraph(event):
    print('Generating Graph')
    axs[3].clear()
    axs[2].set_title('Operation Pinkbook: Controll Panel')
    axs[3].set_title('Historical Data')
    axs[3].set_ylabel('Price')
    axs[3].set_xlabel('Server Time')
    axs[3].grid()
    x5 = [float(i) for i in trackertime_list[graphswitcheroo]]
    y5 = [float(i) for i in tracker_list[graphswitcheroo]]
    axs[3].plot(x5,y5)
    axs[3].scatter(sellx, selly,c='red', linewidths=2.0,edgecolors='black',s=60)
    axs[3].scatter(buyx,buyy,c='green',linewidths=2.0,edgecolors='black',s=60)


plt.connect('button_press_event', on_click)
nexcut = plt.axes([0.15, 0.40, .17, .05], facecolor='k')
graphcut = plt.axes([0.15, 0.32, .3,.06], facecolor = 'k')
wrapcut = plt.axes([0.78, 0.38, .17,.05], facecolor = 'k')
bnexcut = Button(nexcut, 'Next Stock', color='red', hovercolor='white')
bgraphcut = Button(graphcut, 'Generate Graph', color='blue', hovercolor='white')
bwrapcut = Button(wrapcut, 'Wrap It Up', color='yellow',hovercolor='white')
bgraphcut.on_clicked(_rendergraph)
bnexcut.on_clicked(_yes)
bwrapcut.on_clicked(_closeshop)


while(True):

    if datetime.datetime.now() > stop:
        print('closing socket')
        bm.close()
        bm.start_multiplex_socket(tickerlist, process_m_message)
        clock_reset()

    x1 = [float(i) for i in trackertime_list[graphswitcheroo][-1000:]]
    y1 = [float(i) for i in tracker_list[graphswitcheroo][-1000:]]
    x2 =[float(i) for i in temptime_list[graphswitcheroo]]
    y2 =[float(i) for i in temp_list[graphswitcheroo]]
    buyx = [float(i) for i in buytime_list[graphswitcheroo]]
    buyy = [float(i) for i in buy_list[graphswitcheroo]]
    sellx =[float(i) for i in selltime_list[graphswitcheroo]]
    selly =[float(i) for i in sell_list[graphswitcheroo]]

    if((len(y1)>0)):
        axs[0].set_ylim(0.98*float(min(y1)) ,1.02*float(max(y1)))
        time_text.set_text('Current Price:  ' + temp_list[graphswitcheroo][0].rstrip('0'))
        ticker_text.set_text(tickerlist[graphswitcheroo])
        yield_text.set_text('Permanent Yield:   ' + str(tdyyield))
        lossyield_text.set_text('Unsold Yield:   ' + str(sum(lssyield)))
        totalsell_text.set_text('Amount of Trades Holding Assets:   ' + str(sum(totalsell)))
        axs[0].set_xlim(float(x1[0]), float(x1[-1]))

    if(len(buyx) == len(buyy)):
        buydata.set_offsets(numpy.c_[buyx, buyy])
    if(len(sellx)==len(selly)):
        selldata.set_offsets(numpy.c_[sellx, selly])
    if(numpy.shape(numpy.array(x1))==numpy.shape(numpy.array(y1))):
        livedata.set_offsets(numpy.c_[x1, y1])

    toparray =  [float(i) for i in toperror_list[graphswitcheroo]]
    bottomarray =  [float(i) for i in bottomerror_list[graphswitcheroo]]
    toparray2 = [float(i) for i in toperror2_list[graphswitcheroo]]
    bottomarray2 = [float(i) for i in bottomerror2_list[graphswitcheroo]]


    if(len(tracker_list[graphswitcheroo])>=35):


        x3 =[float(i) for i in slopetime_list[graphswitcheroo]]
        y3 =[float(i) for i in slope_list[graphswitcheroo]]
        ln1.set_data(x3, toparray)
        ln2.set_data(x3, bottomarray)
        ln.set_data(x2,line1_list[graphswitcheroo])
        slopedata.set_offsets(numpy.c_[x3,y3])

        axs[1].set_xlim(x3[0], x3[-1])
        axs[1].set_ylim(min(bottomarray),max(toparray))

    if(len(tracker_list[graphswitcheroo])>=95):
        x4 =[float(i) for i in slopetime2_list[graphswitcheroo]]
        y4 =[float(i) for i in slope2_list[graphswitcheroo]]
        x60 = [float(i) for i in temptime2_list[graphswitcheroo]]
        ln11.set_data(x4, toparray2)
        ln22.set_data(x4, bottomarray2)
        lnn.set_data(x60,line2_list[graphswitcheroo])
        slopedata2.set_offsets(numpy.c_[x4,y4])

    plt.pause(0.01)



