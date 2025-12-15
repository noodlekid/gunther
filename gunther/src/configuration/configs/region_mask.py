from typing import Annotated, Literal

from pydantic import BaseModel, Field


class CircleRegion(BaseModel):
    type: Literal["circle"] = "circle"
    center: tuple[float, float]
    radius: float


class PolygonRegion(BaseModel):
    type: Literal["polygon"] = "polygon"
    vertices: list[tuple[float, float]]


RegionType = Annotated[CircleRegion | PolygonRegion, Field(discriminator="type")]
