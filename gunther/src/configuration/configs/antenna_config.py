from typing import Annotated, Literal

from pydantic import BaseModel, Field


class CustomAntennaConfigSinglePol(BaseModel):
    type: Literal["custom"] = "custom"
    name: str
    pattern_file: str


class CustomAntennaConfigDualPol(BaseModel):
    type: Literal["custom_dual_pol"] = "custom_dual_pol"
    name: str
    pattern_file_horizontal: str
    pattern_file_vertical: str


class IsotropicAntennaConfig(BaseModel):
    type: Literal["isotropic"] = "isotropic"
    name: str


AntennaConfigType = Annotated[
    CustomAntennaConfigDualPol | CustomAntennaConfigSinglePol | IsotropicAntennaConfig,
    Field(discriminator="type"),
]
