import ctypes
import pathlib
import sys
import os

from .gamecore import SConfig, STeeGrid, SWorldCore

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

tg_empty = _lib_physics.tg_empty
tg_empty.argtypes = []
tg_empty.restype = STeeGrid

wc_init = _lib_physics.wc_init
wc_init.argtypes = [
    ctypes.POINTER(SWorldCore),
    ctypes.POINTER(STeeGrid),
    ctypes.POINTER(SConfig)
]
wc_init.restype = None

