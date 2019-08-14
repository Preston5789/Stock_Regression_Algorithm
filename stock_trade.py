import math
from binance.client import Client

wrap = False

'''...........This Bool Will Start Moving Money.......'''
Jesus=0
'''..................DO NOT TOUCH....................'''

class Jesus:
    def __init__(self):
        self.tdyyield=0.0
        self.lssyield= [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        self.buy_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
        self.sell_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
        self.buytime_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
        self.selltime_list = [[], [], [], [], [],[], [], [], [], [],[], [], [], [], []]
        self.decider = [False, False, False, False, False, False, False, False, False, False,False, False, False, False, False]
        self.defender = [False, False, False, False, False, False, False, False, False, False,False, False, False, False, False]
        self.totalsell = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


    def buy(self, position, startbalnace, Jesus, toperror2_list, bottomerror_list,bottomerror2_list, temp_list, temptime_list, tickerlist):

        #We can only buy 10 different stocks at a time
        if(sum(self.totalsell) < 10.0):
            print('We are looking to buy!!')

            #We compare the errors in the two regression models to determine when to buy or sell
            if((float(bottomerror_list[position][-1]) > float(toperror2_list[position][-1])) & (float(bottomerror2_list[position][-1])>0.0)):
                print('Buying That SHIT!')
                ##Append the appropriate lists for plotting
                self.buy_list[position].append(temp_list[position][len(temp_list[position])-1])
                self.buytime_list[position].append((temptime_list[position][len(temptime_list[position])-1]))
                #Stores that we are currently trading a stock
                self.totalsell[position] = 1
                #We dont want to buy if we hit the sell-all button
                if(wrap == True):
                    self.decider[position] = True
                else:
                    #Dont buy again
                    self.decider[position] = False
                    #Buy 1/10 of starting amount of ETH
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


    def sell(self, position, tracker_list, temp_list, toperror_list, bottomerror2_list, temptime_list, tickerlist):

        #Calculate current trading yeild for this stock
        self.lssyield[position]=100*((float(tracker_list[position][-1])-float(self.buy_list[position][-1]))/(float(self.buy_list[position][-1]))-0.002)/10
        #We make sure to account for 0.02% trading fees and to account for slippage
        if( (1.00519*float(self.buy_list[position][-1]) < float(temp_list[position][-1])) ):

            print('We are looking to Sell!!!')
            #We compare the errors in the two regression models to determine when to buy or sell
            if((float(toperror_list[position][-1]) >=  1.0*float(bottomerror2_list[position][-1]))& (float(toperror_list[position][-1]) < 0.0)):
                print('Selling That SHIT!')
                #Append appropriate lists for plotting
                self.sell_list[position].append(temp_list[position][-1])
                self.selltime_list[position].append((temptime_list[position][-1]))
                #Since we have sold back to ETH, we calculate our total profit
                self.tdyyield += -100*((float(self.buy_list[position][-1])-float(self.sell_list[position][-1]))/float((buy_list[position][-1]))-0.002)/10
                self.lssyield[position]=0
                self.totalsell[position] = 0
                self.decider[position] = True
                #Sell all of the stock we own
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
    def decide(self, startbalnace, toperror_list, bottomerror_list, toperror2_list, bottomerror2_list, temp_list, temptime_list, tickerlist, tracker_list):
        print(tickerlist)
        for position in range(len(tickerlist)):

            if(self.decider[position] == True and self.defender == True):
                self.buy( position ,startbalnace, Jesus, toperror2_list, bottomerror_list,bottomerror2_list, temp_list, temptime_list, tickerlist)

            if(self.decider[position] == False and self.defender == True):
                self.sell( position, tracker_list, temp_list, toperror_list, bottomerror2_list, temptime_list, tickerlist)


