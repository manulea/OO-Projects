from threading import Thread
import random

import time
import datetime

tokens = []

class BITCoin():
    CHARS = "0123456789abcdefghijklmnopqrstuvwxyz"
    COIN_LEN = 6
	
    def __init__(self):

        for _ in range(0, 100000):
            token = ""
            for _ in range(0, self.COIN_LEN):
                token += random.choice(self.CHARS)
            tokens.append(token)
        self._tokens = set(tokens)

    _instance = None
    @staticmethod
    def getInstance():
        if not BITCoin._instance:
            BITCoin._instance = BITCoin()
        return BITCoin._instance

    def isCoin(self, token):
        return token in self._tokens

class Counter(object):
    def __init__(self):
        self.value = 0
    def increment(self):
        self.value += 1

c = Counter()

g = Counter()

wallet = []

def go():
	CHARS = "0123456789abcdefghijklmnopqrstuvwxyz"
	COIN_LEN = 6
	
	for i in range(100000):
		# to check if value is a valid coin:
		token = ""
		
		for _ in range(0, COIN_LEN):
			token += random.choice(CHARS)
		
		if (BITCoin.getInstance().isCoin(token)):
			c.increment()
			wallet.append(token)
			print(token)

def sequentialScan():
	CHARS = "0123456789abcdefghijklmnopqrstuvwxyz"
	COIN_LEN = 6

	token = ""

	notFound = True
	
	while notFound == True:
	
		for _ in range(0, COIN_LEN):
			token += random.choice(CHARS)
			
		if (tokens[g.value] == token):
			c.increment()
			wallet.append(token)
			notFound = False
			g.increment()
			print(token)
			
		end = time.time()	
			
		if (end - start) > 30:
			break;
			
print("Commencing the mining program!")
fruit = False
start = time.time()

while fruit == False:
	end = time.time()

	
	t1 = Thread(target=go)
	t1.start()

	t2 = Thread(target=go)
	t2.start()
	
	t3 = Thread(target=sequentialScan)
	t3.start()
	t4 = Thread(target=sequentialScan)
	t4.start()
	
	print("Now starting Randomly Generated Hash Scan")
	
	t1.join()
	t2.join()
	
	print("Now starting sequential scan")
	
	t3.join()
	t4.join()
		
	if (end - start) > 30:
		fruit = True
		
print(c.value, " BIT's mined")


