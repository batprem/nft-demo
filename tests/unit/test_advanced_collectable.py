from scripts.helpful_script import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    get_contract,
)
from brownie import network
import pytest
from scripts.advanced_collectable.deploy_and_create import deploy_and_create


def test_can_collectable():
    account = get_account()
    ACTIVE_NETWORK = network.show_active()
    if ACTIVE_NETWORK not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    advanced_collectable, create_transaction = deploy_and_create()
    requestId = create_transaction.events["requestedCollectable"]["requestId"]
    random_nubmer = 777
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, random_nubmer, advanced_collectable.address, {"from": account}
    )
    assert advanced_collectable.tokenCounter() == 1
    assert advanced_collectable.tokenIdToBreed(0) == random_nubmer % 3
