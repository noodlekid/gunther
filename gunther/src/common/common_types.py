from typing import Annotated

from pydantic import Field

Vector3Tuple = Annotated[
    tuple[float, float, float],
    Field(description="A 3D vector represented as a tuple of three floats (x, y, z)."),
]

QuaternionTuple = Annotated[
    tuple[float, float, float, float],
    Field(
        description="A quaternion represented as a tuple of four floats (x, y, z, w)."
    ),
]
