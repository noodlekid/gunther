from typing import Self

from pydantic import BaseModel, model_validator

from .device_template import DeviceTemplate
from .environment_config import EnvironmentConfig
from .node_config import NodeConfig
from .solver_config import SolverConfig


class SimulationManifest(BaseModel):
    environment_config: EnvironmentConfig
    device_templates: list[DeviceTemplate]
    node_configs: list[NodeConfig]
    solver_config: SolverConfig

    @model_validator(mode="after")
    def validate_template_refs(self) -> Self:
        template_names = {template.name for template in self.device_templates}
        for node in self.node_configs:
            if node.template not in template_names:
                raise ValueError(
                    f"Node '{node.name}' references undefined template '{node.template}'"
                )
        return self
