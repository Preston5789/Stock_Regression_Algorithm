from binance.client import Client
from binance.websockets import BinanceSocketManager
from stock_reg import Errors
from stock_trade import Jesus
import datetime
import numpy as np

err = Errors()
import numpy

class Connection():

    print("STARTING CONNECTION")
    stop=datetime.datetime.now()

    def __init__(self):
        self.trackertime_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
        self.tracker_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
        self.temp_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
        self.temp2_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
        self.temptime_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
        self.temptime2_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
        self.startbalnace = 0


        self.slope_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
        self.slope2_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
        self.slopetime_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
        self.slopetime2_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
        self.line1_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
        self.line2_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
        self.toperror_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
        self.bottomerror_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
        self.toperror2_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
        self.bottomerror2_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
        self.tickerlist = ['oaxeth@ticker', 'wtceth@ticker','bateth@ticker', 'ltceth@ticker','trxeth@ticker',
              'zrxeth@ticker', 'adaeth@ticker','engeth@ticker', 'naveth@ticker','eoseth@ticker',
              'ltceth@ticker', 'rlceth@ticker','rcneth@ticker', 'evxeth@ticker','icxeth@ticker']

    def socket(self):
        api_key = 'bDCIpsdAJnuG4nrCgZ3AxKFFPCoQnAh3JLGMwNu8TSMSbMqFFJkOUuKKgGN7AMZm'
        api_secret = '5pQhCY5snDlXiVkTTGfWcux3WgftoAW9RTcfwxbzFvH9WVd0SbZCSIGSy7HUATrj'
        client = Client(api_key, api_secret)

        startbalnace=client.get_asset_balance('ETH')
        self.startbalnace = startbalnace['free']
        print(startbalnace)
        print('Starting Websocket')
        bm = BinanceSocketManager(client, user_timeout=20)
        conn_key = bm.start_multiplex_socket(self.tickerlist, self.process_m_message)
        bm.start()

#Connect the api and get the starting balance of ETH (Our base stock that we trade with)

    def process_m_message(self,msg):

        if((msg['data']['e'] != 'error')):

            tickername = str(msg['stream'])
            position = self.tickerlist.index(tickername)
            tester = str(msg['data']['c'])
            timer = str(msg['data']['E'])
            #Appendthe appropriate lists for plotting
            self.tracker_list[position].append(tester)
            self.trackertime_list[position].append(timer)
            self.temp_list[position].append(tester)
            self.temptime_list[position].append(timer)
            self.temp2_list[position].append(tester)
            self.temptime2_list[position].append(timer)

        if(len(self.tracker_list[position]) >= 35):

            temptimearray = numpy.asarray(self.temptime_list[position]).astype(numpy.float)
            temparray = numpy.asarray(self.temp_list[position]).astype(numpy.float)
            te, be, ln, slp = err.finderrors(temparray, temptimearray, timer, position ,33)

            self.slope_list[position].append(slp)
            self.slopetime_list[position].append(timer)
            self.line1_list[position] = np.delete(ln, [0])
            self.toperror_list[position].append(te)
            self.bottomerror_list[position].append(be)

            self.temp_list[position].remove(self.temp_list[position][0])
            self.temptime_list[position].remove(self.temptime_list[position][0])

        if(len(self.tracker_list[position]) >= 95):
            temptimearray2 = numpy.asarray(self.temptime2_list[position][0:65]).astype(numpy.float)
            temparray2 = numpy.asarray(self.temp2_list[position][0:65]).astype(numpy.float)
            te2, be2, ln2, slp2 = err.finderrors(temparray2, temptimearray2, timer, position ,96)
            self.slope2_list[position].append(slp2)
            self.slopetime2_list[position].append(timer)
            self.line2_list[position] = np.delete(ln2, [0])
            self.toperror2_list[position].append(te2)
            self.bottomerror2_list[position].append(be2)

            self.temp2_list[position].remove(self.temp2_list[position][0])
            self.temptime2_list[position].remove(self.temptime2_list[position][0])


            #Jesus().decide(position, self.startbalnace, self.toperror_list, self.bottomerror_list, self.toperror2_list, self.bottomerror2_list, self.temp_list, self.temptime_list, self.tickerlist, self.tracker_list)



def clock_reset(self):
    global stop
    stop = (datetime.datetime.now() + datetime.timedelta(seconds=30))


