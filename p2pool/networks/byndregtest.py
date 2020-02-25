from p2pool.bitcoin import networks

PARENT = networks.nets['byndregtest']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 60*60//10 # shares
REAL_CHAIN_LENGTH = 60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'dfbd912938b940af'.decode('hex')
PREFIX = 'e7f240046ff5e960'.decode('hex')
P2P_PORT = 11333
MIN_TARGET = 0
MAX_TARGET = 2**256//2**12 - 1
PERSIST = False
WORKER_PORT = 11332
BOOTSTRAP_ADDRS = []
ANNOUNCE_CHANNEL = '#beyondpool'
VERSION_CHECK = lambda v: None if 140300 <= v else 'Beyondcoin version too old. Upgrade to 0.15.1 or newer!' # not a bug. BIP65 support is ensured by SOFTFORKS_REQUIRED
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 1600
NEW_MINIMUM_PROTOCOL_VERSION = 1700
SEGWIT_ACTIVATION_VERSION = 16
