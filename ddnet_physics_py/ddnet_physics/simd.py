import ctypes

class m128(ctypes.Structure):
    _fields_ = [("values", ctypes.c_float * 4)]
    _align_ = 16

class uivec2(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_uint),
        ("y", ctypes.c_uint),
    ]
