from scripts.helpfulscripts import get_account,LOCAL_BLOCKCHAIN_ENVIRONMENT
from brownie import network
import pytest
from scripts.deploy_and_create import deploy_create 

def test_can_create_simple_collection():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        pytest.skip() 
    simple_collectible = deploy_create()
    assert simple_collectible.ownerOf(0) == get_account()