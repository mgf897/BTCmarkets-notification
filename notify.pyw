from plyer import notification as n
import requests
import json
import locale


# Matthew Flynn, 4 Nov 17
# Checks BTCmarkets and shows prices in a system notification
#
# if you have issues with plyer, install the latest from Github
# "pip install -I https://github.com/kivy/plyer/zipball/master"



my_message = ""

coins = ['https://www.btcmarkets.net/data/market/BTCMarkets/ETH/AUD/tick',
	'https://www.btcmarkets.net/data/market/BTCMarkets/XRP/AUD/tick',
	'https://www.btcmarkets.net/data/market/BTCMarkets/LTC/AUD/tick',
	'https://www.btcmarkets.net/data/market/BTCMarkets/BTC/AUD/tick']

	
precision = {'BTC':100000000,'LTC':100000000,'XRP':100000000,'ETH':100000000}
	
locale.setlocale( locale.LC_ALL, '' )	
	
for coin in coins:
	req = requests.get(coin)
	parsed_json = json.loads(req.text)
	
	str_instrument = parsed_json['instrument']
	price = locale.currency(parsed_json['lastPrice']/precision[str_instrument], grouping=True )
	
	my_message += str_instrument + "/" + parsed_json['currency'] + " " + str(price) + "\r\n"


n.notify(title='BTCmarkets', message=my_message)

