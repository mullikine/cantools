import cantools

db = cantools.database.load_file('tests/files/dbc/motohawk.dbc')

import shanepy
import shanepy as spy
from shanepy import *
myembed(globals(), locals())