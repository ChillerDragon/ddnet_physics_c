import ctypes
from ddnet_maploader import load_map

from ddnet_physics.collision import SCollision
from ddnet_physics.gamecore import SCharacterCore, SConfig, STeeGrid, SWorldCore
from . __version__ import __version__

from . import cbindings

class DDNetPhysics:
    def __init__(self, map_path: str):
        self.map_data = load_map(map_path)
        self.collision = SCollision()
        self.config = SConfig()
        self.tee_grid = cbindings.tg_empty()
        self.world = SWorldCore()
        cbindings.init_collision(
            ctypes.byref(self.collision),
            ctypes.byref(self.map_data._internal_data)
        )
        cbindings.init_config(
            ctypes.byref(self.config))
        cbindings.tg_init(
            ctypes.byref(self.tee_grid),
            self.collision.m_MapData.width,
            self.collision.m_MapData.height
        )
        cbindings.wc_init(
            ctypes.byref(self.world),
            ctypes.byref(self.collision),
            ctypes.byref(self.tee_grid),
            ctypes.byref(self.config)
        )

    def add_character(self):
        cbindings.wc_add_character(ctypes.byref(self.world), 1)

    def tick(self):
        cbindings.wc_tick(ctypes.byref(self.world))

    def characters(self):
        array_type = SCharacterCore * self.world.m_NumCharacters
        return ctypes.cast(self.world.m_pCharacters, ctypes.POINTER(array_type)).contents
