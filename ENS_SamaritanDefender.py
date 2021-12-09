# ENS Domains Samaritan Defender: A simple python script to send/post a bunch of random stuff to ENS phishing sites
# Goal: To flood the database of phishing sites with thousands of fake credentials making it difficult for them to identify real credentials they've collected

### Identified phishing sites:
###     - https://ensdomain.online
###     - https://claimens.domains/

import requests
import threading
import random

##### Endpoint of the phishing sites, where the results are posted to once credentials have been collected
#url = "https://ensdomain.online/metamask/action_page.php" # Ensdomain.online is no longer online and has been taken down
url = "https://claimens.domains/Ens/wallet-RD266-loadingAdd-frontchange/next.php"

##################
### Variables/Parameters: The headers/data collected could vary so posting entries for different possible combinations

# 1 - List of wallets being phished from the site
wallets = [
    "Portis", 
    "Coinbase+Wallet", 
    "Torus", 
    "MEW+wallet", 
    "WalletConnect",
    "Bitski"]

# 2 - List of userAgents (i.e: Browser/Platform)
# Todo: Add multiple varied userAgents, so entries posted to phishing database simulate being collected from a variety of platforms (not just Macs)
# Good source is: https://developers.whatismybrowser.com/useragents/explore/ althgough not very scalable. Maybe chuck a bunch of them into a file like the word bank below?
userAgents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
    "Mozilla/5.0 (X11; CrOS x86_64 13597.94.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.186 Safari/537.36"
    ]

# 3 - Seed phase prep from which to post to the database (i.e: Fake passwords)
with open("RandomWordBank.txt", "r") as file:
    text = file.read()
    words = list(map(str, text.split())) #This is the bank from which the words will be selected at random to make the seed phrase
seed_phrase_length = 18 #Could be either 12, 18 or 24

# Method/Function for sending/posting the requests
def send_requests():
    while True: # Run forever until interrupted
        for wallet in wallets:
            for userAgent in userAgents:
                # Looping though the list of userAgents and wallets and creating a different combination of data to be sent
                array_of_random_seeds = random.sample(words, seed_phrase_length)
                seed_phrase = ' '.join(array_of_random_seeds)
                data = {
                    #"seed": seed_phrase,
                    #"wallet": wallet
                    "pk": seed_phrase,
                    "walletselected": wallet,
                    "btn1":"",
                    }
                headers = {
                    "Host": "claimens.domains",
                    "User-Agent": userAgent,
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                    "Accept-Language": "en-GB,en;q=0.5",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Referer": "https://claimens.domains/Ens/wallet-RD266-loadingAdd-frontchange/",
                    "Content-Type": "application/json",
                    "Origin": "https://claimens.domains",
                    "Content-Length": "44",
                    "DNT": "1",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "1",
                    "Sec-Fetch-Dest": "document",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-User": "?1"
                    }
                response = requests.post(url = url, data = data, headers = headers)
                print(wallet, response) # Upon completion of a request, print to terminal giving visual feedback

## Multi-threading the script
threads = []
num_of_threads = 50 #The number of threads you wanna run. i.e: how many parallels do you want running the application at the same time

for i in range(num_of_threads):
    t = threading.Thread(target = send_requests)
    t.daemon = True
    threads.append(t)

for i in range(num_of_threads):
    threads[i].start()

for i in range(num_of_threads):
    threads[i].join()

### Final note: This script is over-commented on purpose so others can easily pick it up and run wilder with it