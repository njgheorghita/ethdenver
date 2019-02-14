from eth_account import Account
from web3.auto.infura.endpoints import build_infura_url
from web3.providers.auto import load_provider_from_uri
from web3.middleware import construct_sign_and_send_raw_middleware
from web3 import Web3


DR_PK = '0x<insert private key here>'
DR_ADDRESS = Account.privateKeyToAccount(DR_PK).address

COOP_PK = '0x<insert private key here>'
COOP_ADDRESS = Account.privateKeyToAccount(COOP_PK).address

GMA_PK = '0x<insert private key here>'
GMA_ADDRESS = Account.privateKeyToAccount(GMA_PK).address


coop_w3 = Web3(load_provider_from_uri(build_infura_url('mainnet.infura.io')))
coop_middleware = construct_sign_and_send_raw_middleware(COOP_PK)
coop_w3.middleware_onion.add(coop_middleware)
coop_w3.eth.defaultAccount = COOP_ADDRESS
coop_w3.enable_unstable_package_management_api()


def print_balances(w3, multisig):
    print("Dr: ", w3.eth.getBalance(DR_ADDRESS))
    print("Grandma: ", w3.eth.getBalance(GMA_ADDRESS))
    print("Multisig: ", w3.eth.getBalance(multisig))
    print("Coop: ", w3.eth.getBalance(COOP_ADDRESS))
