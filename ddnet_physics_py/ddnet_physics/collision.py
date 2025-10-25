import ctypes
import ddnet_maploader
from .simd import m128

NUM_TUNE_ZONES = 256
DISTANCE_FIELD_RESOLUTION = 32

class SPickup(ctypes.Structure):
    _fields_ = [
        ("m_Type", ctypes.c_int8),
        ("m_Number", ctypes.c_uint8),
        ("m_Subtype", ctypes.c_uint8),
    ]

class STuningParams(ctypes.Structure):
    _fields_ = [
        ("m_GroundControlSpeed", ctypes.c_float),
        ("m_GroundControlAccel", ctypes.c_float),
        ("m_GroundFriction", ctypes.c_float),
        ("m_GroundJumpImpulse", ctypes.c_float),
        ("m_AirJumpImpulse", ctypes.c_float),
        ("m_AirControlSpeed", ctypes.c_float),
        ("m_AirControlAccel", ctypes.c_float),
        ("m_AirFriction", ctypes.c_float),
        ("m_HookLength", ctypes.c_float),
        ("m_HookFireSpeed", ctypes.c_float),
        ("m_HookDragAccel", ctypes.c_float),
        ("m_HookDragSpeed", ctypes.c_float),
        ("m_Gravity", ctypes.c_float),
        ("m_VelrampStart", ctypes.c_float),
        ("m_VelrampRange", ctypes.c_float),
        ("m_VelrampCurvature", ctypes.c_float),
        ("m_VelrampValue", ctypes.c_float),
        ("m_GunCurvature", ctypes.c_float),
        ("m_GunSpeed", ctypes.c_float),
        ("m_GunLifetime", ctypes.c_float),
        ("m_ShotgunCurvature", ctypes.c_float),
        ("m_ShotgunSpeed", ctypes.c_float),
        ("m_ShotgunSpeeddiff", ctypes.c_float),
        ("m_ShotgunLifetime", ctypes.c_float),
        ("m_GrenadeCurvature", ctypes.c_float),
        ("m_GrenadeSpeed", ctypes.c_float),
        ("m_GrenadeLifetime", ctypes.c_float),
        ("m_LaserReach", ctypes.c_float),
        ("m_LaserBounceDelay", ctypes.c_float),
        ("m_LaserBounceNum", ctypes.c_float),
        ("m_LaserBounceCost", ctypes.c_float),
        ("m_LaserDamage", ctypes.c_float),
        ("m_PlayerCollision", ctypes.c_float),
        ("m_PlayerHooking", ctypes.c_float),
        ("m_JetpackStrength", ctypes.c_float),
        ("m_ShotgunStrength", ctypes.c_float),
        ("m_ExplosionStrength", ctypes.c_float),
        ("m_HammerStrength", ctypes.c_float),
        ("m_HookDuration", ctypes.c_float),
        ("m_HammerFireDelay", ctypes.c_float),
        ("m_GunFireDelay", ctypes.c_float),
        ("m_ShotgunFireDelay", ctypes.c_float),
        ("m_GrenadeFireDelay", ctypes.c_float),
        ("m_LaserFireDelay", ctypes.c_float),
        ("m_NinjaFireDelay", ctypes.c_float),
        ("m_HammerHitFireDelay", ctypes.c_float),
        ("m_GroundElasticityX", ctypes.c_float),
        ("m_GroundElasticityY", ctypes.c_float),
    ]

class SCollision(ctypes.Structure):
    _fields_ = [
        ("m_MapData", ddnet_maploader.ddnet_maploader._MapDataInternal),
        ("m_pWidthLookup", ctypes.POINTER(ctypes.c_uint32)),
        ("m_pBroadSolidBitField", ctypes.POINTER(ctypes.c_uint64)),
        ("m_pBroadIndicesBitField", ctypes.POINTER(ctypes.c_uint64)),
        ("m_pTileInfos", ctypes.POINTER(ctypes.c_uint8)),
        ("m_pPickups", ctypes.POINTER(SPickup)),
        ("m_pFrontPickups", ctypes.POINTER(SPickup)),
        ("m_pMoveRestrictions", ctypes.POINTER((ctypes.c_uint8 * 5))),
        ("m_pTileBroadCheck", ctypes.POINTER(ctypes.c_uint8)),
        ("m_pSolidTeleDistanceField", ctypes.POINTER(ctypes.c_uint8)),
        ("m_pBroadTeleInBitField", ctypes.POINTER(ctypes.c_uint64)),
        ("m_apTeleOuts", (ctypes.POINTER(m128) * 256)),
        ("m_apTeleCheckOuts", (ctypes.POINTER(m128) * 256)),
        ("m_pSpawnPoints", ctypes.POINTER(m128)),
        ("m_NumSpawnPoints", ctypes.c_int),
        ("m_aNumTeleOuts", ctypes.c_int * 256),
        ("m_aNumTeleCheckOuts", ctypes.c_int * 256),
        ("m_aTuningList", STuningParams * NUM_TUNE_ZONES),
        ("m_HighestSwitchNumber", ctypes.c_int),
        ("m_MoveRestrictionsFound", ctypes.c_bool),
    ]
