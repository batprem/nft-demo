from brownie import AdvancedCollectable, network, config
from scripts.helpful_script import fund_contract_with_link, get_contract, get_account


def main():
    account = get_account()
    advanced_collectable = AdvancedCollectable[-1]
    fund_contract_with_link(advanced_collectable.address)
    creation_transaction = advanced_collectable.createCollectable({"from": account})
    creation_transaction.wait(1)
    print("Collectable created")
