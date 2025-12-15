"""module containing device/entity type definition"""

import ctypes


class SimulationNode(ctypes.Structure):
    """
    defines the sturcture for a node that may transmit or
    recieve RF waves in the simulator
    """

    _fields_ = [
        ("id", ctypes.c_uint32),
        ("pos", ctypes.c_float * 3),  # x,y,z coordinate
        ("attitude", ctypes.c_float * 4),  # x,y,z,w quarternion
        ("tx_power_dbm", ctypes.c_float),
        ("noise_floor_dbm", ctypes.c_float),
        ("role_type", ctypes.c_uint8),  # masking flag
        ("_padding", ctypes.c_uint8 * 7),  # alignemnt
    ]
