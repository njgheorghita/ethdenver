from eth_account import Account
from web3.auto.infura.endpoints import build_infura_url
from web3.providers.auto import load_provider_from_uri
from web3.middleware import construct_sign_and_send_raw_middleware
from web3 import Web3

DR_PK = <insert_private_key_here>
DR_ADDRESS = Account.privateKeyToAccount(DR_PK).address

COOP_PK = <insert_private_key_here>
COOP_ADDRESS = Account.privateKeyToAccount(COOP_PK).address

GMA_PK = <insert_private_key_here>
GMA_ADDRESS = Account.privateKeyToAccount(GMA_PK).address


coop_w3 = Web3(load_provider_from_uri(build_infura_url('mainnet.infura.io')))
coop_middleware = construct_sign_and_send_raw_middleware(COOP_PK)
coop_w3.middleware_onion.add(coop_middleware)
coop_w3.eth.defaultAccount = COOP_ADDRESS
coop_w3.enable_unstable_package_management_api()


def print_balances(w3, multisig):
    print(f"Grandma:  {w3.fromWei(w3.eth.getBalance(GMA_ADDRESS), 'ether')} ETH")
    print(f"Multisig: {w3.fromWei(w3.eth.getBalance(multisig), 'ether')} ETH")
    print(f"Coop:     {w3.fromWei(w3.eth.getBalance(COOP_ADDRESS), 'ether')} ETH")
