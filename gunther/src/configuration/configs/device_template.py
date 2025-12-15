from typing import Literal

from pydantic import BaseModel

from .antenna_config import AntennaConfigType


class DeviceTemplate(BaseModel):
    name: str
    antenna_config: AntennaConfigType
    tx_power_dbm: float
    frequency_mhz: float
    noise_floor_dbm: float
    role: Literal["relay", "endpoint"]
