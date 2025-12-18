from dataclasses import dataclass

import numpy as np
import numpy.typing as npt

from .radio import Radio


@dataclass
class Node:
    id: str
    position: npt.NDArray[np.float64]  # 3D position (x, y, z) in meters
    radios: list[Radio]

    def get_radio_for_frequency(
        self, freq_mhz: float, tolerance: float = 1e5
    ) -> Radio | None:
        for radio in self.radios:
            if abs(radio.frequency_mhz - freq_mhz) < tolerance:
                return radio
        return None
