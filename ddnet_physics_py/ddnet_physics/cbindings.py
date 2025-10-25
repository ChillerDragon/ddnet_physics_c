import ctypes
import pathlib
import sys
import os

from .gamecore import SCharacterCore, SConfig, STeeGrid, SWorldCore
from .collision import SCollision

import ddnet_maploader

so_path = None

path_candidates = [
    "/usr/local/lib/libddnet_physics.so",
    "/usr/lib/libddnet_physics.so",
    "/lib/libddnet_physics.so",
    "libddnet_physics.so"
]

if os.name == 'nt':
    path_candidates.append('libddnet_physics.dll')
    path_candidates.append('ddnet_physics.dll')

for so_path_candidate in path_candidates:
    if pathlib.Path(so_path_candidate).is_file():
        so_path = so_path_candidate
        break

if not so_path:
    print("Missing libddnet_physics library!", file=sys.stderr)
    print("Get it from https://github.com/Teero888/ddnet_physics_c", file=sys.stderr)
    raise ValueError("missing libddnet_physics")

_lib_physics = ctypes.cdll.LoadLibrary(so_path)

# gamecore.h
tg_empty = _lib_physics.tg_empty
tg_empty.argtypes = []
tg_empty.restype = STeeGrid

tg_init = _lib_physics.tg_init
tg_init.argtypes = [
    ctypes.POINTER(STeeGrid),
    ctypes.c_int,
    ctypes.c_int
]
tg_init.restype = None

init_config = _lib_physics.init_config
init_config.argtypes = [ctypes.POINTER(SConfig)]
init_config.restype = None

wc_init = _lib_physics.wc_init
wc_init.argtypes = [
    ctypes.POINTER(SWorldCore),
    ctypes.POINTER(SCollision),
    ctypes.POINTER(STeeGrid),
    ctypes.POINTER(SConfig)
]
wc_init.restype = None

wc_tick = _lib_physics.wc_tick
wc_tick.argtypes = [ctypes.POINTER(SWorldCore)]
wc_tick.restype = None

wc_add_character = _lib_physics.wc_add_character
wc_add_character.argtypes = [ctypes.POINTER(SWorldCore), ctypes.c_int]
wc_add_character.restype = ctypes.POINTER(SCharacterCore)

# collision.h
init_collision = _lib_physics.init_collision
init_collision.argtypes = [
    ctypes.POINTER(SCollision),
    ctypes.POINTER(ddnet_maploader.ddnet_maploader._MapDataInternal)
]

