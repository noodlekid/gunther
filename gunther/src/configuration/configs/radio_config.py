from pydantic import BaseModel

from .antenna_config import AntennaConfigType


class RadioConfig(BaseModel):
    name: str
    antenna_config: AntennaConfigType
    frequency_mhz: float
    tx_power_dbm: float
    noise_floor_dbm: float
