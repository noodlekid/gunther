# processing/batcher.py
from dataclasses import dataclass
from typing import Iterator

from domain.node import Node
from domain.radio import Radio


@dataclass
class SimulationBatch:
    frequency_hz: float
    nodes: list[Node]
    active_radios: list[Radio]


class FrequencyBatcher:
    def batch(self, all_nodes: list[Node]) -> Iterator[SimulationBatch]:
        """
        scans all nodes, finds unique frequencies, and yields batches
        containing only the nodes that operate on that frequency.
        """
        unique_freqs: set[float] = set[float]()
        for node in all_nodes:
            for radio in node.radios:
                unique_freqs.add(radio.frequency_mhz)

        for freq in sorted(unique_freqs):
            batch_nodes: list[Node] = []
            batch_radios: list[Radio] = []

            for node in all_nodes:
                radio = node.get_radio_for_frequency(freq)
                if radio:
                    batch_nodes.append(node)
                    batch_radios.append(radio)

            if len(batch_nodes) >= 2:
                yield SimulationBatch(
                    frequency_hz=freq, nodes=batch_nodes, active_radios=batch_radios
                )
