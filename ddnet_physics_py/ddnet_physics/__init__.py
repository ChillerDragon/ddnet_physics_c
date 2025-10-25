from . __version__ import __version__

from typing import Optional
from . import cbindings

def sample():
    cbindings.tg_empty()
