import btcde

class BtcdeOrderBook:
  connection = None
  def __init__(self, api_key, api_secret):
        self.connection = btcde.Connection(
            api_key, api_secret)

  def current(self, trading_pair='btceur', amount=0.1):
    orderbook = self.connection.showOrderbook(
        'buy', trading_pair=trading_pair, order_requirements_fullfilled=1, amount=amount, only_express_orders=1)
    min_buy_price = orderbook['orders'][0]['price']

    orderbook = self.connection.showOrderbook(
        'sell', trading_pair=trading_pair, order_requirements_fullfilled=1, amount=amount, only_express_orders=1)
    max_sell_price = orderbook['orders'][0]['price']

    return {
      'min_buy_price': min_buy_price,
      'max_sell_price': max_sell_price
    }
