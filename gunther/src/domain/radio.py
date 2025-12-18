from dataclasses import dataclass


@dataclass
class Radio:
    name: str
    frequency_mhz: float
    tx_power_dbm: float
    antenna_spec_name: str
