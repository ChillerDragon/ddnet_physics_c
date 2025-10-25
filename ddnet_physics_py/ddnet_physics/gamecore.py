import ctypes

from ddnet_physics.simd import m128, uivec2
from .collision import STuningParams, SCollision

WEAPON_HAMMER = 0
WEAPON_GUN = 1
WEAPON_SHOTGUN = 2
WEAPON_GRENADE = 3
WEAPON_LASER = 4
WEAPON_NINJA = 5
NUM_WEAPONS = 6

WORLD_ENTTYPE_PROJECTILE = 0
WORLD_ENTTYPE_LASER = 1
NUM_WORLD_ENTTYPES = 2

class SConfig(ctypes.Structure):
    _fields_ = [
        ("m_SvTeleportHoldHook", ctypes.c_int),
        ("m_SvTeleportLoseWeapons", ctypes.c_int),
        ("m_SvDeepfly", ctypes.c_int),
        ("m_SvDestroyBulletsOnDeath", ctypes.c_int),
        ("m_SvDestroyLasersOnDeath", ctypes.c_int),
        ("m_SvFreezeDelay", ctypes.c_int),
        ("m_SvHit", ctypes.c_int),
        ("m_SvEndlessDrag", ctypes.c_int),
        ("m_SvSoloServer", ctypes.c_int),
    ]

class SPlayerInput(ctypes.Structure):
    _fields_ = [
        ("m_Direction", ctypes.c_int8),
        ("m_TargetX", ctypes.c_int16),
        ("m_TargetY", ctypes.c_int16),
        ("m_Jump", ctypes.c_uint8),
        ("m_Fire", ctypes.c_uint8),
        ("m_Hook", ctypes.c_uint8),
        ("m_WantedWeapon", ctypes.c_uint8),
        ("m_TeleOut", ctypes.c_uint8),
        ("m_Flags", ctypes.c_uint16),
    ]

class SWorldCore(ctypes.Structure):
    pass  # Forward declaration for pointer

class SEntity(ctypes.Structure):
    pass  # Forward declaration for pointer

class SEntity(ctypes.Structure):
    _fields_ = [
        ("m_pWorld", ctypes.POINTER(SWorldCore)),
        ("m_pCollision", ctypes.POINTER(SCollision)),
        ("m_pPrevTypeEntity", ctypes.POINTER(SEntity)),
        ("m_pNextTypeEntity", ctypes.POINTER(SEntity)),
        ("m_Pos", m128),
        ("m_ObjType", ctypes.c_int),
        ("m_Number", ctypes.c_int),
        ("m_Layer", ctypes.c_int),
        ("m_MarkedForDestroy", ctypes.c_bool),
        ("m_Spawned", ctypes.c_bool),
    ]

class STeeLink(ctypes.Structure):
    _fields_ = [
        ("m_TeeId", ctypes.c_int32),
        ("m_Parent", ctypes.c_int32),
        ("m_Child", ctypes.c_int32),
        ("m_Tile", ctypes.c_uint32),
    ]

class STeeGrid(ctypes.Structure):
    _fields_ = [
        ("m_pTeeGrid", ctypes.POINTER(ctypes.c_int)),
        ("hash", ctypes.c_uint64),
    ]

class STeeAccelerator(ctypes.Structure):
    _fields_ = [
        ("m_pGrid", ctypes.POINTER(STeeGrid)),
        ("m_pTeeList", ctypes.POINTER(STeeLink)),
        ("hash", ctypes.c_uint64),
    ]

class SSwitch(ctypes.Structure):
    _fields_ = [
        ("m_Status", ctypes.c_bool),
        ("m_Initial", ctypes.c_bool),
        ("m_EndTick", ctypes.c_int),
        ("m_Type", ctypes.c_int),
        ("m_LastUpdateTick", ctypes.c_int),
    ]

class SNinja(ctypes.Structure):
    _fields_ = [
        ("m_ActivationDir", m128),
        ("m_ActivationTick", ctypes.c_int),
        ("m_CurrentMoveTime", ctypes.c_int),
        ("m_OldVelAmount", ctypes.c_int),
    ]

class SCharacterCore(ctypes.Structure):
    _fields_ = [
        ("m_pWorld", ctypes.POINTER(SWorldCore)),
        ("m_pCollision", ctypes.POINTER(SCollision)),
        ("m_Id", ctypes.c_int),
        ("m_PrevPos", m128),
        ("m_Pos", m128),
        ("m_Vel", m128),
        ("m_VelMag", ctypes.c_float),
        ("m_VelRamp", ctypes.c_float),
        ("m_BlockPos", uivec2),
        ("m_BlockIdx", ctypes.c_int),
        ("m_HookPos", m128),
        ("m_HookDir", m128),
        ("m_HookTeleBase", m128),
        ("m_HookTick", ctypes.c_int),
        ("m_HookState", ctypes.c_int8),
        ("m_LastWeapon", ctypes.c_uint8),
        ("m_ActiveWeapon", ctypes.c_uint8),
        ("m_QueuedWeapon", ctypes.c_uint8),
        ("m_aWeaponGot", ctypes.c_bool * NUM_WEAPONS),
        ("m_Ninja", SNinja),
        ("m_NewHook", ctypes.c_bool),
        ("m_Grounded", ctypes.c_bool),
        ("m_Jumped", ctypes.c_int),
        ("m_JumpedTotal", ctypes.c_int),
        ("m_Jumps", ctypes.c_int),
        ("m_PrevFire", ctypes.c_uint8),
        ("m_Input", SPlayerInput),
        ("m_StartTime", ctypes.c_int),
        ("m_Colliding", ctypes.c_uint8),
        ("m_LeftWall", ctypes.c_bool),
        ("m_TeleCheckpoint", ctypes.c_uint8),
        ("m_LastRefillJumps", ctypes.c_bool),
        ("m_LastPenalty", ctypes.c_bool),
        ("m_LastBonus", ctypes.c_bool),
        ("m_Solo", ctypes.c_bool),
        ("m_Jetpack", ctypes.c_bool),
        ("m_CollisionDisabled", ctypes.c_bool),
        ("m_EndlessHook", ctypes.c_bool),
        ("m_EndlessJump", ctypes.c_bool),
        ("m_HammerHitDisabled", ctypes.c_bool),
        ("m_GrenadeHitDisabled", ctypes.c_bool),
        ("m_LaserHitDisabled", ctypes.c_bool),
        ("m_ShotgunHitDisabled", ctypes.c_bool),
        ("m_HookHitDisabled", ctypes.c_bool),
        ("m_HasTelegunGun", ctypes.c_bool),
        ("m_HasTelegunGrenade", ctypes.c_bool),
        ("m_HasTelegunLaser", ctypes.c_bool),
        ("m_FreezeTime", ctypes.c_int),
        ("m_FreezeStart", ctypes.c_int),
        ("m_DeepFrozen", ctypes.c_bool),
        ("m_LiveFrozen", ctypes.c_bool),
        ("m_FrozenLastTick", ctypes.c_bool),
        ("m_pTuning", ctypes.POINTER(STuningParams)),
        ("m_MoveRestrictions", ctypes.c_uint8),
        ("m_HookedPlayer", ctypes.c_int),
        ("m_TeleGunPos", m128),
        ("m_TeleGunTeleport", ctypes.c_bool),
        ("m_IsBlueTeleGunTeleport", ctypes.c_bool),
        ("m_ReloadTimer", ctypes.c_int),
        ("m_aHitObjects", ctypes.c_int * 10),
        ("m_NumObjectsHit", ctypes.c_uint8),
        ("m_StartTick", ctypes.c_int),
        ("m_FinishTick", ctypes.c_int),
        ("m_AttackTick", ctypes.c_int),
        ("m_RespawnDelay", ctypes.c_uint8),
        ("m_HitNum", ctypes.c_int),
    ]

class SWorldCore(ctypes.Structure):
    _fields_ = [
        ("m_pCollision", ctypes.POINTER(SCollision)),
        ("m_Accelerator", STeeAccelerator),
        ("m_pConfig", ctypes.POINTER(SConfig)),
        ("m_pTunings", ctypes.POINTER(STuningParams)),
        ("m_pNextTraverseEntity", ctypes.POINTER(SEntity)),
        ("m_apFirstEntityTypes", ctypes.POINTER(SEntity) * NUM_WORLD_ENTTYPES),
        ("m_NumCharacters", ctypes.c_int),
        ("m_pCharacters", ctypes.POINTER(SCharacterCore)),
        ("m_NumSwitches", ctypes.c_int),
        ("m_pSwitches", ctypes.POINTER(SSwitch)),
        ("m_GameTick", ctypes.c_int),
    ]
