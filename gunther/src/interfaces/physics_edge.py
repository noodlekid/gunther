"""Module containing physics edge definition"""
import ctypes

class PhysicsEdge(ctypes.Structure):
    """
    Edges that represent propgation physics between
    nodes.
    """
    _fields_ = [
        ("path_gain_db",    ctypes.c_float),        # derived from "a" coeff
        ("delay_spread",    ctypes.c_float),        # i.e sigma tau
        ("aod_angles",      ctypes.c_float * 2),    # theta_tx, phi_tx
        ("aoa_angles",      ctypes.c_float * 2),    # theta_rx, phi_rx
        ("is_los",          ctypes.c_bool),         # for path loss model
        ("mimo_rank",       ctypes.c_uint8),        
        ("_padding",        ctypes.c_uint8 * 6)     # alignment
    ]
