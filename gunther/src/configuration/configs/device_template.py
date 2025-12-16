from typing import Literal

from pydantic import BaseModel

from .radio_config import RadioConfig


class DeviceTemplate(BaseModel):
    name: str
    radios: list[RadioConfig]
    role: Literal["relay", "endpoint"]
