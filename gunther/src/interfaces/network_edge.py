import ctypes

class NetworkEdge(ctypes.Structure):
    """
    Provides directional edges for higher level statistics
    for inference.
    """
    _fields_ = [
        ("rssi_dbm",        ctypes.c_float),    # recieved signal strength
        ("interference_mw", ctypes.c_float),    # noise
        ("sinr_db",         ctypes.c_float),    # signal quality
        ("capacity_mbps",   ctypes.c_float),    # max theoritical throughput
        ("per",             ctypes.c_float),    # packet error rate estimation
    ]

