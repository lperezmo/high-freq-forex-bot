from QuantConnect import *
from Selection.ManualUniverseSelectionModel import ManualUniverseSelectionModel

class LuisCurrencySelectionModel(ManualUniverseSelectionModel):
    def __init__(self):
        super().__init__([Symbol.Create(x, SecurityType.Forex, Market.Oanda) for x in ["AUDCAD","AUDCHF","AUDHKD","AUDJPY","AUDNZD","AUDSGD","AUDUSD",
                                                                                         "CADCHF","CADHKD","CADJPY","CADSGD","CHFHKD","CHFJPY","CHFZAR",
                                                                                         "EURAUD","EURCAD","EURCHF","EURCZK","EURDKK","EURGBP","EURHKD",
                                                                                         "EURHUF","EURJPY","EURNOK","EURNZD","EURPLN","EURSEK","EURSGD",
                                                                                         "EURTRY","EURUSD","EURZAR","GBPAUD","GBPCAD","GBPCHF","GBPHKD",
                                                                                         "GBPJPY","GBPNZD","GBPPLN","GBPSGD","GBPUSD","GBPZAR","HKDJPY",
                                                                                         "NZDCAD","NZDCHF","NZDHKD","NZDJPY","NZDSGD","NZDUSD","SGDCHF",
                                                                                         "SGDHKD","SGDJPY","TRYJPY","USDCAD","USDCHF","USDCNH","USDCZK",
                                                                                         "USDDKK","USDHKD","USDHUF","USDINR","USDJPY","USDMXN","USDNOK",
                                                                                         "USDPLN","USDSAR","USDSEK","USDSGD","USDTHB","USDTRY","USDZAR",
                                                                                         "ZARJPY"]])
        
        
        
        
        
from G10CurrencySelectionModel import G10CurrencySelectionModel
import numpy as np
import copy

class LuisMainCurrencyExchangeProgram(QCAlgorithm):

    """
    Authors
    ----------
    Luis Perez Morales
    
    """

    def Initialize(self):
        self.SetStartDate(2020, 11, 20)  # Set Start Date
        # self.SetEndDate(2020, 10, 29) # Set end date
        self.SetCash(200)  # Set Strategy Cash
        self.SetUniverseSelection(G10CurrencySelectionModel())
        self.start_time = self.Time   # Store starting time
        self.super_counter = 0
        

    def OnData(self, data):
        """
        OnData event is the primary entry point for your algorithm. 
        Each new data point will be pumped in here.
        
        Parameters
        ----------
        currencies = all symbols
        A = matrix with all current prices
        M = A*A - n*A, where n is the size
        luis = A * Inverse(A)
        
        """
        
        if self.super_counter == 0:
            # References
            list_of_currencies = ['USD','GBP','JPY','AUD','NZD','CAD','CHF','NOK','SEK']
    
            list_of_exchanges = ["AUDCAD","AUDCHF","AUDHKD","AUDJPY","AUDNZD","AUDSGD","AUDUSD",
                                 "CADCHF","CADHKD","CADJPY","CADSGD","CHFHKD","CHFJPY","CHFZAR",
                                 "EURAUD","EURCAD","EURCHF","EURCZK","EURDKK","EURGBP","EURHKD",
                                 "EURHUF","EURJPY","EURNOK","EURNZD","EURPLN","EURSEK","EURSGD",
                                 "EURTRY","EURUSD","EURZAR","GBPAUD","GBPCAD","GBPCHF","GBPHKD",
                                 "GBPJPY","GBPNZD","GBPPLN","GBPSGD","GBPUSD","GBPZAR","HKDJPY",
                                 "NZDCAD","NZDCHF","NZDHKD","NZDJPY","NZDSGD","NZDUSD","SGDCHF",
                                 "SGDHKD","SGDJPY","TRYJPY","USDCAD","USDCHF","USDCNH","USDCZK",
                                 "USDDKK","USDHKD","USDHUF","USDINR","USDJPY","USDMXN","USDNOK",
                                 "USDPLN","USDSAR","USDSEK","USDSGD","USDTHB","USDTRY","USDZAR",
                                 "ZARJPY"]
            
    
            # Define the name of all currency exchanges
            array_of_currencies = np.array([['USDUSD', 'USDGBP', 'USDJPY', 'USDAUD', 'USDNZD', 'USDCAD',
                                            'USDCHF', 'USDNOK', 'USDSEK'],
                                          ['GBPUSD', 'GBPGBP', 'GBPJPY', 'GBPAUD', 'GBPNZD', 'GBPCAD',
                                            'GBPCHF', 'GBPNOK', 'GBPSEK'],
                                          ['JPYUSD', 'JPYGBP', 'JPYJPY', 'JPYAUD', 'JPYNZD', 'JPYCAD',
                                            'JPYCHF', 'JPYNOK', 'JPYSEK'],
                                          ['AUDUSD', 'AUDGBP', 'AUDJPY', 'AUDAUD', 'AUDNZD', 'AUDCAD',
                                            'AUDCHF', 'AUDNOK', 'AUDSEK'],
                                          ['NZDUSD', 'NZDGBP', 'NZDJPY', 'NZDAUD', 'NZDNZD', 'NZDCAD',
                                            'NZDCHF', 'NZDNOK', 'NZDSEK'],
                                          ['CADUSD', 'CADGBP', 'CADJPY', 'CADAUD', 'CADNZD', 'CADCAD',
                                            'CADCHF', 'CADNOK', 'CADSEK'],
                                          ['CHFUSD', 'CHFGBP', 'CHFJPY', 'CHFAUD', 'CHFNZD', 'CHFCAD',
                                            'CHFCHF', 'CHFNOK', 'CHFSEK'],
                                          ['NOKUSD', 'NOKGBP', 'NOKJPY', 'NOKAUD', 'NOKNZD', 'NOKCAD',
                                            'NOKCHF', 'NOKNOK', 'NOKSEK'],
                                          ['SEKUSD', 'SEKGBP', 'SEKJPY', 'SEKAUD', 'SEKNZD', 'SEKCAD',
                                            'SEKCHF', 'SEKNOK', 'SEKSEK']])
    
            # Do all calculations only once (?)
    
            # Fill in the matrix with exchange information
            A = np.array(np.zeros(shape = (9,9)), dtype = float)
            for counter, item in np.ndenumerate(array_of_currencies):
                if counter[0] == counter[1]:
                    # Rate for one unit of itself is one
                    A[counter[0], counter[1]] = int(np.divide(2,2))
                else:
                    if item in list_of_exchanges:
                        # Manually doing the stuff
                        try:
                            A[counter[0], counter[1]] = data[str(item)].Close #data[item]
                        except:
                            break
                    else:
                        try:
                            # Flip to existing exchange, get the ask price (sell price)
                            new_item = item[3:7] + item[0:3]
                            A[counter[0], counter[1]] = data[str(new_item)].Value
                        except:
                            # If contract is non-existent, make it a 0.5 (this way it will never be highest number).
                            A[counter[0], counter[1]] = int(np.divide(1,2))
    
                
            # Calculate Luis path
            # The matrix is balanced if A^2 - nA = 0
            M = np.multiply(A,A) - A.shape[0] * A;
            
            # Calculate the "luis" matrix 
            luis = np.multiply(A, np.transpose(A));
    
            
            ###########################################################################
            # Find the most profitable transaction paths in the "Luis" matrix
            # and then saves the pairs of most profitable transaction paths
            # in a list of tuples 
            ###########################################################################
            
            # References
            list_of_currencies = ['USD','GBP','JPY','AUD','NZD','CAD','CHF','NOK','SEK']
            
            # Find location of most profitable paths
            location = np.where(luis == np.max(luis))
            
            # Get the names of those currencies and save as max_currency_name
            # max_currency_name = list_of_currencies[location[0][0]] + list_of_currencies[location[0][1]]
    
            ###########################################################################
            
            # Most profitable transaction path for currency exchange
            one_ = 'USD'
            two_ = list_of_currencies[location[0][0]] 
            try:
                three_ = list_of_currencies[location[0][1]] 
            except IndexError:
                three_ = 'CAD'
            
            # Check for bugs
            if two_ == "USD":
                two_ = "JPY"
            else:
                pass
            if three_ == "USD":
                three_ == "CAD"
            else:
                pass
            
            # Name of exchanges. For each, check if it's in list of exchanges
            # Else, reverse the order
            one_to_two = ''.join(one_+two_)
            if one_to_two in list_of_exchanges:
                pass
            else:
                one_to_two = one_to_two[3:7] + one_to_two[0:3]
            
            two_to_three = ''.join(two_+three_)
            if two_to_three in list_of_exchanges:
                pass
            else:
                two_to_three = two_to_three[3:7] + two_to_three[0:3]
            
            three_to_one = ''.join(three_ + one_)
            if three_to_one in list_of_exchanges:
                pass
            else:
                three_to_one = three_to_one[3:7] + three_to_one[0:3]
        else:
            pass

        
        ###########################################################################################
        ###########################################################################################
        # Main code
        ###########################################################################################
        ###########################################################################################


        # Different way of buying and selling currency
        
        # CurrentPrice = data[str(one_to_two)].Close #self.Securities[one_to_two].Price
        # Only trade for 15 minutes:
        # if (self.Time - self.start_time).Minute < 15:
        
        
        if not self.Portfolio.Invested:
            self.current = self.Time
            
 
            # BUY ONE_TO_TWO BY DEFAULT, once
            if self.super_counter < 1:
                self.SetHoldings(str(two_to_three), 1) # A market buy (buy currency 3 with currency 2)
                self.super_counter += 1
            

            # NOW, SELL ONE_TO_TWO SLOWLY, only if we make money from it
            # REDUCE BY MINI_COUNTER
            mini_counter = 0
            self.current_price_two = data[str(two_to_three)].Close
            for i in range(self.super_counter):
                if mini_counter == 0:
                    if data[str(two_to_three)].Value -  self.current_price_two < 0:
                        self.SetHoldings(str(two_to_three), 0.66) # A market sell (sell currency 3 for currency 2)
                        mini_counter =+ 1
                        return # Will repurchase upon next "OnData"
                elif mini_counter == 1:
                    if data[str(two_to_three)].Value -  self.current_price_two < 0:
                        self.SetHoldings(str(two_to_three), 0.33) # A market sell (sell currency 3 for currency 2)
                        mini_counter =+ 1
                        return # Will repurchase upon next "OnData"
                elif mini_counter == 2:
                    if data[str(two_to_three)].Value -  self.current_price_two < 0:
                        self.SetHoldings(str(two_to_three), 0) # A market sell (sell currency 3 for currency 2)
                        mini_counter =+ 1
                        return # Will repurchase upon next "OnData"
        ###########################################################################################
                
                
        # Buy back dollars only if we make money from it
        # self.current_price_three = data[str(three_to_one)].Close

        # if data[str(three_to_one)].Value -  self.current_price_three > 5:
        #     self.SetHoldings(str(three_to_one), 1) # A market buy (buy currency 1 again)
        #     return # Will repurchase upon next "OnData"
        

        if (self.Time - self.current).days > 8:
          self.Liquidate()
           
           
        ###########################################################################################
        ###########################################################################################
 

        
    def OnOrderEvent(self, OrderEvent):
        """
        Event when the order is filled. Debug log the order fill. :OrderEvent:
        """

        if OrderEvent.FillQuantity == 0:
            return

        fetched = self.Transactions.GetOrderById(OrderEvent.OrderId)

        self.Debug("{} was filled. Symbol: {}. Quantity: {}. Direction: {}"
                   .format(str(fetched.Type),
                           str(OrderEvent.Symbol),
                           str(OrderEvent.FillQuantity),
                           str(OrderEvent.Direction)))
