from pathlib import Path

import yaml

from gunther.src.configuration.configs.simulation_manifest import SimulationManifest


class SimulationManifestLoader:

    def __init__(self, manifest_path: str):
        self.manifest_path: Path = Path(manifest_path)

    def load(self) -> SimulationManifest:
        with open(self.manifest_path, "r") as f:
            manifest_dict = yaml.safe_load(f)
        return SimulationManifest.model_validate(manifest_dict)

