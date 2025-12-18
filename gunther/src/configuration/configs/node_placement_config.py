from typing import Annotated, Literal

from pydantic import BaseModel, Field

from .orientation import OrientationConfig
from .region_mask import RegionType


class GridPlacement(BaseModel):
    type: Literal["grid"] = "grid"
    region: RegionType | None
    exclude: RegionType | None
    resolution: float
    height: float
    orientation_mode: OrientationConfig


class FixedPlacement(BaseModel):
    type: Literal["fixed"] = "fixed"
    position: list[float]  # TODO: make this a proper Vector3 type
    orientation_mode: OrientationConfig


NodePlacementConfig = Annotated[
    GridPlacement | FixedPlacement, Field(discriminator="type")
]
