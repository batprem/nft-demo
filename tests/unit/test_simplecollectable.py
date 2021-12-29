from scripts.helpful_script import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
from brownie import network
import pytest
from scripts.simple_collectable.deploy_and_create import deploy_and_create


def test_can_collectable():
    ACTIVE_NETWORK = network.show_active()
    if ACTIVE_NETWORK not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    simple_collectable = deploy_and_create()
    assert simple_collectable.ownerOf(0) == get_account()
