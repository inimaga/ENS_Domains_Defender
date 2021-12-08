# ENS Domains Samaritan Defender: A simple python script to send/post a bunch of random stuff to ENS phishing sites
# Goal: To flood the database of phishing sites with thousands of fake credentials making it difficult for them to identify real credentials they've collected

### Identified phishing sites:
###     - https://ensdomain.online

import requests
import threading

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
userAgents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"
    ]

# 3 - List of seed phrases to post to the database (i.e: Fake passwords)
# Todo: Write a function that generates random words to use as seed phrases so results posted are more varied
seeds = [
    'Oii dickheads stop scamming people. why meat orange are mango expecting to with this mango Twat wankers bellend',
    'immense wanker helpful severe popular you superb skinny general twat cute important',
    'conscious weak lumpy craven hard terrible you scammers sedate beneficial truthful accidental',
    'puffy wanker wry dependent bawdy oi healthy painful scarce stop angry damp abhorrent scam quizzical craven bored lean',
    'bellend sending bunch of seemingly legit request you will never know which is right quizzical craven yasoy lean',
    'Gonna Run wry this bawdy every healthy day to screw yoy damp abhorrent quickest quizzical craven wenin tlir',
    'random generated online words smoggy online hesitant internal bad financial sweet rich woebegone well-made nippy harsh minor amuck utter draconian slimy lewd sexual witty',
    'long steady futuristic popular spiteful clean fascinated earthy decisive sassy savory grumpy adjoining flimsy mixed frail burly naughty imminent puffy keen like reasonable tiresome'
    ]

# Method/Function for sending/posting the requests
def send_requests():
    while True: # Run forever until interrupted
        for seed in seeds: 
            for wallet in wallets:
                for userAgent in userAgents:
                    # Looping though the list of seeds, userAgents and Wallets and creating a different combination of data to be sent
                    data = {
                        #"seed": seed,
                        #"wallet": wallet
                        "pk": seed,
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