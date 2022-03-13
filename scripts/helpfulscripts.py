from brownie import accounts,network,config

LOCAL_BLOCKCHAIN_ENVIRONMENT = [
    "development",
    "hardhat",
    "mainnet-fork",
    "polygon-test",
    
] 

def get_account(index=None, id=None):
   # if index:
        #return accounts[index]
   # if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT:
     #  return accounts[0]
    #if id:
      # return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"]) 
    
    