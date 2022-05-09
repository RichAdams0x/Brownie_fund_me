from brownie import network, accounts, config, MockV3Aggregator

LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development","ganache-local"]
FORKED_LOCAL_ENVIRONMENT = ["mainnet-fork"]

def get_account ():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mock():
    if len(MockV3Aggregator) <=0 :
            mock_aggregator = MockV3Aggregator.deploy(18,21000000000000000000000,{"from":get_account()}) #because in developpement we cant use normal pricefeed_adress so we must mock the V3Aggregator