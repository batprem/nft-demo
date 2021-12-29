from scripts.helpful_script import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    get_contract,
)
from brownie import network
import pytest
from scripts.advanced_collectable.deploy_and_create import deploy_and_create
import time


def test_can_collectable():
    account = get_account()
    ACTIVE_NETWORK = network.show_active()
    if ACTIVE_NETWORK in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration test")

    # Act
    advanced_collectable, create_transaction = deploy_and_create()
    time.sleep(180)

    # Assert
    assert advanced_collectable.tokenCounter() > 0
