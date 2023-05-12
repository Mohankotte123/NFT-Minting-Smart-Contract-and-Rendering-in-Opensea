from brownie import SimpleCollectible, accounts, network, config
from scripts.helpfulscripts import get_account

sample_token_uri = "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
OPENSEA_URL = "https://testnets.opensea.io//assets/{}/{}"
def deploy_create():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from":account}) 
    tx = simple_collectible.createCollectible(sample_token_uri, {"from":account})
    tx.wait(1)
    print(account)
    print(f"Awesome you can see your NFT at {OPENSEA_URL.format(simple_collectible.address,simple_collectible.tokenCounter() - 1)}")  
   
def main():
    deploy_create() 
     

