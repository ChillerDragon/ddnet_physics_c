import ctypes
from ddnet_maploader import load_map

from ddnet_physics.collision import SCollision
from ddnet_physics.gamecore import SConfig, STeeGrid, SWorldCore
from . __version__ import __version__

from . import cbindings

def sample(map_path):
    cbindings.tg_empty()

    map_data = load_map(map_path)
    collision = SCollision()
    config = SConfig()
    tee_grid = STeeGrid()
    world = SWorldCore()

    cbindings.init_collision(ctypes.byref(collision), ctypes.byref(map_data._internal_data))
    cbindings.init_config(ctypes.byref(collision))
    cbindings.tg_init(ctypes.byref(tee_grid), collision.m_MapData.width, collision.m_MapData.height)
    cbindings.wc_init(ctypes.byref(world), ctypes.byref(collision), ctypes.byref(tee_grid), ctypes.byref(config))


