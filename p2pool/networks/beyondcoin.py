from p2pool.bitcoin import networks

PARENT = networks.nets['beyondcoin']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'e037d5b8c6923410'.decode('hex')
PREFIX = '7208c1a53ef629b0'.decode('hex')
PREFIX = ''.decode('hex')
P2P_PORT = 10333
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 10332
BOOTSTRAP_ADDRS = '52.0.220.131 52.11.0.47 18.190.88.101 185.244.150.234 3.132.131.183 3.133.28.194'.split(' ')
ANNOUNCE_CHANNEL = '#beyondpool-bynd'
VERSION_CHECK = lambda v: None if 100400 <= v else 'Beyondcoin version too old. Upgrade to 0.15.1 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 1600
NEW_MINIMUM_PROTOCOL_VERSION = 1700
SEGWIT_ACTIVATION_VERSION = 17
