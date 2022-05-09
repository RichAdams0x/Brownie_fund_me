from brownie import FundMe, MockV3Aggregator,accounts,config,network
from scripts.helpful_scripts import get_account, deploy_mock,LOCAL_BLOCKCHAIN_ENVIRONMENT
from web3 import Web3

def deploy_fund_me ():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mock()
        print("Mock Deployed!!!!")
        price_feed_address = MockV3Aggregator[-1].address
        
    fund_me = FundMe.deploy(price_feed_address,{"from": account})
    print (f"deployed at",fund_me.address)

def main():
    deploy_fund_me()