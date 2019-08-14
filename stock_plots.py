
import matplotlib.pyplot as plt
import numpy
import time
from matplotlib.widgets import Button

from stock_trade import Jesus
from stock_connect import Connection
from stock_reg import Errors

err = Errors()

graphswitcheroo = 0


con = Connection()
jes = Jesus()
con.socket()

plt.ion()
fig, axs = plt.subplots(4, 1,figsize=(8,10), constrained_layout=True)
x1, y1 = [],[]
x2, y2 = [], []
x3, y3 = [], []
x4, y4 = [], []
buyx, buyy = [], []
sellx, selly = [], []

s=2

livedata = axs[0].scatter(x1,y1,s=s, c = 'blue')
selldata = axs[0].scatter(sellx, selly, s = 15, c = 'r')
buydata = axs[0].scatter(buyx, buyy, s = 15, c = 'g')
lnn, = axs[0].plot([],[], 'green', linewidth = 1.0)
ln, = axs[0].plot([],[],'red', linewidth = 1.0)

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


axs[2].set_title('Regression Trader: Control Panel')
axs[3].set_title('Historical Data')
axs[2].set_ylabel('Price')
axs[2].set_xlabel('Server Time')
ticker_text = fig.text(0.5, 0.43, '' , multialignment="left")
time_text = fig.text(0.5, 0.40, '' , multialignment="left")
yield_text = fig.text(0.5, 0.37, '', multialignment="left")
lossyield_text = fig.text(0.5, 0.34, '', multialignment="left")
totalsell_text = fig.text(0.5, 0.31, '', multialignment="left")


def _closeshop(event,tickerlist):
    jes.closeshop(tickerlist)

def on_click(event):
       print('doubleclick')

#definition to cycle through graphs
def _yes(event):
    global graphswitcheroo
    graphswitcheroo += 1
    if(graphswitcheroo>=14):
        graphswitcheroo = 0



#Renders the graph for all of the trading data
def _rendergraph(event):
    print('Generating Graph')
    axs[3].clear()
    axs[2].set_title('Regression Trader: Controll Panel')
    axs[3].set_title('Historical Data')
    axs[3].set_ylabel('Price')
    axs[3].set_xlabel('Server Time')
    axs[3].grid()
    x5 = [float(i) for i in con.trackertime_list[graphswitcheroo]]
    y5 = [float(i) for i in con.tracker_list[graphswitcheroo]]
    axs[3].plot(x5,y5)
    axs[3].scatter(sellx, selly,c='red', linewidths=2.0,edgecolors='black',s=60)
    axs[3].scatter(buyx,buyy,c='green',linewidths=2.0,edgecolors='black',s=60)

#Everything to get the buttons together
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

    #print(con.tracker_list)
    x1 = [float(i) for i in con.trackertime_list[graphswitcheroo][-1000:]]
    y1 = [float(i) for i in con.tracker_list[graphswitcheroo][-1000:]]
    x2 =[float(i) for i in con.temptime_list[graphswitcheroo]]
    y2 =[float(i) for i in con.temp_list[graphswitcheroo]]
    buyx = [float(i) for i in jes.buytime_list[graphswitcheroo]]
    buyy = [float(i) for i in jes.buy_list[graphswitcheroo]]
    sellx =[float(i) for i in jes.selltime_list[graphswitcheroo]]
    selly =[float(i) for i in jes.sell_list[graphswitcheroo]]


    ##Make sure the graphs are all tidy like
    if((len(y1)>0)):
        axs[0].set_ylim(0.98*float(min(y1)) ,1.02*float(max(y1)))
        time_text.set_text('Current Price:  ' + con.temp_list[graphswitcheroo][0].rstrip('0'))
        ticker_text.set_text(con.tickerlist[graphswitcheroo])
        yield_text.set_text('Permanent Yield:   ' + str(jes.tdyyield))
        lossyield_text.set_text('Unsold Yield:   ' + str(sum(jes.lssyield)))
        totalsell_text.set_text('Amount of Trades Holding Assets:   ' + str(sum(jes.totalsell)))
        axs[0].set_xlim(float(x1[0]), float(x1[-1]))
        axs[1].set_xlim(float(x1[0]), float(x1[-1]))

    if(len(buyx) == len(buyy)):
        buydata.set_offsets(numpy.c_[buyx, buyy])
    if(len(sellx)==len(selly)):
        selldata.set_offsets(numpy.c_[sellx, selly])
    if(numpy.shape(numpy.array(x1))==numpy.shape(numpy.array(y1))):
        livedata.set_offsets(numpy.c_[x1, y1])

    toparray =  [float(i) for i in con.toperror_list[graphswitcheroo]]
    print(toparray)
    bottomarray =  [float(i) for i in con.bottomerror_list[graphswitcheroo]]
    toparray2 = [float(i) for i in con.toperror2_list[graphswitcheroo]]
    bottomarray2 = [float(i) for i in con.bottomerror2_list[graphswitcheroo]]


    if(len(con.tracker_list[graphswitcheroo])>=35):


        x3 =[float(i) for i in con.slopetime_list[graphswitcheroo]]
        y3 =[float(i) for i in con.slope_list[graphswitcheroo]]
        ln1.set_data(x3, toparray)
        ln2.set_data(x3, bottomarray)

        print("The dimensin of x2 is: {}".format(len(x2)))
        print("The dimensin of of line1 is: {}".format(len(con.line1_list[graphswitcheroo])))
        print(con.line1_list[graphswitcheroo])
        ln.set_data(x2,con.line1_list[graphswitcheroo])
        slopedata.set_offsets(numpy.c_[x3,y3])

        axs[1].set_xlim(x3[0], x3[-1])
        axs[1].set_ylim(min(bottomarray),max(toparray))

    if(len(con.tracker_list[graphswitcheroo])>=95):
        x4 =[float(i) for i in con.slopetime2_list[graphswitcheroo]]
        y4 =[float(i) for i in con.slope2_list[graphswitcheroo]]
        y60 = [float(i) for i in con.line2_list[graphswitcheroo]]
        x60 = [float(i) for i in con.temptime2_list[graphswitcheroo][0:64]]
        ln11.set_data(x4, toparray2)
        ln22.set_data(x4, bottomarray2)
        lnn.set_data(x60 ,y60)
        slopedata2.set_offsets(numpy.c_[x4,y4])

        for i in range(len(con.tickerlist)):
            if len(con.tracker_list[i])>100:
                jes.defender[i] = True;

        Jesus().decide(con.startbalnace, con.toperror_list, con.bottomerror_list, con.toperror2_list, con.bottomerror2_list, con.temp_list, con.temptime_list, con.tickerlist, con.tracker_list)

    plt.pause(0.01)


