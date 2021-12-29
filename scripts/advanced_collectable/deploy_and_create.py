from scripts.helpful_script import (
    OPENSEA_URL,
    get_account,
    get_contract,
    fund_contract_with_link,
)
from brownie import AdvancedCollectable, network, config


sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"

ACTIVE_NETWORK = network.show_active()
NETWORK_CONFIG = config["networks"][ACTIVE_NETWORK]


def deploy_and_create():
    account = get_account()
    advanced_collectable = AdvancedCollectable.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        NETWORK_CONFIG["keyhash"],
        eval(NETWORK_CONFIG["fee"]),
        {"from": account},
    )
    fund_contract_with_link(advanced_collectable.address)
    tx = advanced_collectable.createCollectable({"from": account})
    tx.wait(1)
    print(
        f"Awesome you can view your NFT at {OPENSEA_URL.format(advanced_collectable.address, advanced_collectable.tokenCounter() - 1)}"
    )
    return advanced_collectable


def main():
    deploy_and_create()
