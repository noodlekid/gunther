# GUNTHER: A validation throught simulation system for DAFART

DAFART is a relay system. And yes, its named that on purpose.

## What's This About?

We're building a relay system for the Carleton Mars Rover that can be dropped in the Utah desert to extend our comms range. But before we ship hardware to the middle of nowhere and cross our fingers, we'd like to *know* it's going to work.

So this is the simulation side of things. Feed it a config describing your scenario, where the nodes are, what antennas they're using, what the terrain looks like, and it'll tell you whether your link budget makes any sense. Coverage maps, throughput estimates, that sort of thing.

Under the hood we're using [Sionna RT](https://nvlabs.github.io/sionna/) for the ray tracing. It's good at the physics. We're trying to be good at everything around it.

## Current State

Early days. The config schema is mostly there. The rest is... aspirational.

```
gunther/
└── src/
    ├── configuration/    # this exists
    │   └── configs/
    ├── interfaces/       # this too
    ├── processing/       # soon
    └── simulation/       # soon
```

## The Idea

You write a YAML file describing what you want to simulate. Something like:

```yaml
device_templates:
  - name: "relay"
    antenna_config:
      type: custom
      name: "ubiquiti"
      pattern_file: "patterns/ubiquiti.ant"
    tx_power_dbm: 20
    frequency_mhz: 2400
    noise_floor_dbm: -90
    role: relay

node_configs:
  - name: "base_station"
    template: "relay"
    placement:
      type: fixed
      position: [0, 0, 2.0]
      orientation_mode:
        type: fixed
        quaternion: [0, 0, 0, 1]
```

Then the pipeline figures out the rest. That's the dream anyway.

## Why Bother?

The alternative is running Sionna in Jupyter notebooks with hardcoded everything, copy-pasting cells when you want to try a different antenna, and losing track of which result came from which configuration.

We've been there. It's not great.

## Requirements

- Python 3.13+
- Poetry for dependency management
- A GPU (CUDA support prefered) if you want ray tracing to finish before the heat death of the earth.

## Getting Started

```bash
poetry install
```

Beyond that, check back later. We're still building the plane.

## Related

This is part of a larger effort for the Carleton University Mars Rover Design Team. The physical relay hardware is a separate adventure involving custom carrier boards, the 8Devices Mango SoM, and BATMAN-adv mesh networking.

That's documented elsewhere. This repo is just the simulation engine.