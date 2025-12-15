from pydantic import BaseModel


class SolverConfig(BaseModel):
    """
    configuration for Path Solver
    """

    max_depth: int = 10
    max_num_paths_per_src: int = 5
    samples_per_src: int = int(10e6)
    synthetic_array: bool = True
    los: bool = True
    specular_reflection: bool = True
    diffuse_reflection: bool = True
    refraction: bool = True
    diffraction: bool = True
    edge_diffraction: bool = True
    diffraction_lit_region: bool = True
    seed: int = 42
