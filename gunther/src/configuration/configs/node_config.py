from pydantic import BaseModel

from .device_template import DeviceTemplate
from .node_placement_config import NodePlacementConfig


class NodeConfig(BaseModel):
    name: str
    template: str  # ref to DeviceTemplate name
    placement: NodePlacementConfig
