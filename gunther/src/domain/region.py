from abc import ABC, abstractmethod
from typing import Literal

import numpy as np
import numpy.typing as npt


class Region(ABC):

    @abstractmethod
    def contains(self, point: npt.NDArray[np.float32]) -> bool:
        """check if the point is inside the region"""
        pass

    @abstractmethod
    def union(self, other: "Region") -> "Region":
        """return a new region that is the union of this and other"""
        return CompositeRegion("union", [self, other])

    @abstractmethod
    def difference(self, other: "Region") -> "CompositeRegion":
        """return a new region that is the difference of this and other"""
        return CompositeRegion("difference", [self, other])

    @abstractmethod
    def intersection(self, other: "Region") -> "CompositeRegion":
        """return a new region that is the intersection of this and other"""
        return CompositeRegion("intersection", [self, other])


class CircleRegion(Region):
    def __init__(self, center: tuple[float, float], radius: float):
        self.center = np.array(center)
        self.radius = radius

    def contains(self, point: npt.NDArray[np.float32]) -> bool:
        return np.linalg.norm(point - self.center, axis=1)


class PolygonRegion(Region):
    def __init__(self, vertices: list[tuple[float, float]]):
        self.vertices = np.array(vertices)

    def contains(self, point: npt.NDArray[np.float32]) -> bool:
        raise NotImplementedError("PolygonRegion.contains is not implemented yet")


class CompositeRegion(Region):
    def __init__(
        self, op: Literal["union", "difference", "intersection"], children: list[Region]
    ):
        self.op: Literal["union", "difference", "intersection"] = op
        self.children: list[Region] = children

    def contains(self, point: npt.NDArray[np.float32]) -> bool:
        match self.op:
            case "union":
                return any(c.contains(point) for c in self.children)
            case "difference":
                return self.children[0].contains(point) and not self.children[
                    1
                ].contains(point)
            case "intersection":
                return all(c.contains(point) for c in self.children)
            case _:
                raise ValueError(f"Unknown operation: {self.op}")

    def union(self, other: "Region") -> "Region":
        return CompositeRegion("union", [self, other])

    def difference(self, other: "Region") -> "CompositeRegion":
        return CompositeRegion("difference", [self, other])

    def intersection(self, other: "Region") -> "CompositeRegion":
        return CompositeRegion("intersection", [self, other])
