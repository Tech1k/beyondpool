from p2pool.bitcoin import networks

PARENT = networks.nets['beyondcoin_testnet']
SHARE_PERIOD = 4 # seconds
CHAIN_LENGTH =  20*60//3 # shares
REAL_CHAIN_LENGTH = 20*60//3 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'cca5e24ec6408b1e'.decode('hex')
PREFIX = 'ad9614f6466a39cf'.decode('hex')
P2P_PORT = 14333
MIN_TARGET = 0
MAX_TARGET = 2**256//2**12 - 1
PERSIST = True
WORKER_PORT = 14332
BOOTSTRAP_ADDRS = '54.157.251.114 52.13.212.231'.split(' ')
ANNOUNCE_CHANNEL = '#beyondpool'
VERSION_CHECK = lambda v: None if 140300 <= v else 'Beyondcoin version too old. Upgrade to 0.15.1 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 1700
NEW_MINIMUM_PROTOCOL_VERSION = 1700
SEGWIT_ACTIVATION_VERSION = 17
