from brownie import SimpleCollectible, accounts, network, config
from scripts.helpfulscripts import get_account
from web3 import Web3

sample_token_uri = "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
OPENSEA_URL = "https://testnets.opensea.io//assets/{}/{}"
def deploy_create():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from":account}) 
    tx = simple_collectible.createCollectible(sample_token_uri, {"from":account})
    tx.wait(1)
    print(f"Awesome you can see your NFT at {OPENSEA_URL.format(simple_collectible.address,simple_collectible.tokenCounter() - 1)}")  
    print(account)
    web3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/754f2d41981e41e99ea338b6ea063bc7"))
    print(web3.isConnected())
    return simple_collectible

def main():
    deploy_create() 
     

