from typing import Annotated, Literal

from pydantic import BaseModel, Field


class OrientationFixed(BaseModel):
    type: Literal["fixed"] = "fixed"
    quaternion: list[float]  # TODO: make this a proper Quaternion type


class OrientationAligned(BaseModel):
    type: Literal["aligned"] = "aligned"
    aligned_to: str  # TODO: make this a proper reference type, like NodeReference


OrientationConfig = Annotated[
    OrientationFixed | OrientationAligned, Field(discriminator="type")
]
