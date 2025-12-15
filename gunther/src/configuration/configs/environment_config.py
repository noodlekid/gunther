from pydantic import BaseModel, Field

from .region_mask import RegionType


class SceneConfig(BaseModel):
    path: str
    coordinate_system: str
    origin: list[float]  # TODO: make this a proper Vector3 type


class EnvironmentConfig(BaseModel):
    scene_config: SceneConfig
    bounds: list[RegionType] = Field(default_factory=list)
    exclusion_zones: list[RegionType] = Field(default_factory=list)
