from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Protocol, TypeAlias


class PolarizationName(str, Enum):
    V = "V"
    H = "H"
    VH = "VH"
    CROSS = "cross"


class PolarizationModelName(str, Enum):
    TR38901_2 = "tr38901_2"
    TR38901_1 = "tr38901_1"


class BuiltinPatternName(str, Enum):
    ISO = "iso"
    DIPOLE = "dipole"
    HW_DIPOLE = "hw_dipole"
    TR38901 = "tr38901"


@dataclass(frozen=True, slots=True)
class FilePatternSpec:
    path: Path
    format: str | None = None  # .ant, .msi, ...

    def __post_init__(self) -> None:
        if not isinstance(self.path, Path):
            raise TypeError("FilePatternSpec.path must be a pathlib.Path")


PatternSpec: TypeAlias = BuiltinPatternName | FilePatternSpec


@dataclass(frozen=True, slots=True)
class AntennaSpec:
    name: str
    carrier_frequency_hz: float
    pattern: PatternSpec = BuiltinPatternName.ISO
    polarization: PolarizationName = PolarizationName.V
    polarization_model: PolarizationModelName = PolarizationModelName.TR38901_2

    gain_dbi: float = 0.0
    efficiency: float = 1.0

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("AntennaSpec.name must be non empty")
        if self.carrier_frequency_hz <= 0:
            raise ValueError("AntennaSpec.carrier_frequency_hz must be > 0")
        if not (0.0 < self.efficiency <= 1.0):
            raise ValueError("AntennaSpec.efficiency must be in (0, 1]")


@dataclass(slots=True)
class DomainRegistry:
    _items: dict[str, Any] = field(default_factory=dict)

    def register(self, name: str, value: Any) -> None:
        if not name:
            raise ValueError("Registry key must be non-empty")
        self._items[name] = value

    def get(self, name: str) -> Any:
        try:
            return self._items[name]
        except KeyError as e:
            raise KeyError(
                f"Unknown registry key: {name}. Available: {sorted(self._items)}"
            ) from e

    def list(self) -> tuple[str, ...]:
        return tuple(sorted(self._items.keys()))

    def as_mapping(self) -> Mapping[str, Any]:
        return dict(self._items)


builtin_pattern_defaults = DomainRegistry()
polarization_defaults = DomainRegistry()
polarization_model_defaults = DomainRegistry()

for _p in BuiltinPatternName:
    builtin_pattern_defaults.register(_p.value, _p.value)

for _pol in PolarizationName:
    polarization_defaults.register(_pol.value, _pol.value)

for _pm in PolarizationModelName:
    polarization_model_defaults.register(_pm.value, _pm.value)


class AntennaBackendAdapter(Protocol):
    """adapter interface to bridge domain specs to a concrete backend"""

    def ensure_defaults_registered(self) -> None: ...

    def make_backend_pattern(self, spec: AntennaSpec) -> Any: ...

    def make_backend_polarization(self, spec: AntennaSpec) -> Any: ...

    def make_backend_polarization_model(self, spec: AntennaSpec) -> Any: ...


@dataclass(slots=True)
class AntennaCatalog:
    """Registry-like catalog of named antenna specs."""

    _items: dict[str, AntennaSpec] = field(default_factory=dict)

    def register(self, spec: AntennaSpec) -> None:
        if spec.name in self._items:
            raise ValueError(f"AntennaCatalog already has an item named '{spec.name}'")
        self._items[spec.name] = spec

    def get(self, name: str) -> AntennaSpec:
        try:
            return self._items[name]
        except KeyError as e:
            raise KeyError(
                f"Unknown antenna '{name}'. Available: {sorted(self._items)}"
            ) from e

    def list(self) -> tuple[str, ...]:
        return tuple(sorted(self._items.keys()))

    @classmethod
    def defaults(cls, *, carrier_frequency_hz: float) -> AntennaCatalog:
        cat = cls()
        cat.register(
            AntennaSpec(
                name="iso_v",
                carrier_frequency_hz=carrier_frequency_hz,
                pattern=BuiltinPatternName.ISO,
                polarization=PolarizationName.V,
                polarization_model=PolarizationModelName.TR38901_2,
            )
        )
        cat.register(
            AntennaSpec(
                name="dipole_v",
                carrier_frequency_hz=carrier_frequency_hz,
                pattern=BuiltinPatternName.DIPOLE,
                polarization=PolarizationName.V,
                polarization_model=PolarizationModelName.TR38901_2,
            )
        )
        cat.register(
            AntennaSpec(
                name="hw_dipole_v",
                carrier_frequency_hz=carrier_frequency_hz,
                pattern=BuiltinPatternName.HW_DIPOLE,
                polarization=PolarizationName.V,
                polarization_model=PolarizationModelName.TR38901_2,
            )
        )
        cat.register(
            AntennaSpec(
                name="tr38901_v",
                carrier_frequency_hz=carrier_frequency_hz,
                pattern=BuiltinPatternName.TR38901,
                polarization=PolarizationName.V,
                polarization_model=PolarizationModelName.TR38901_2,
            )
        )
        cat.register(
            AntennaSpec(
                name="tr38901_cross",
                carrier_frequency_hz=carrier_frequency_hz,
                pattern=BuiltinPatternName.TR38901,
                polarization=PolarizationName.CROSS,
                polarization_model=PolarizationModelName.TR38901_2,
            )
        )
        return cat
