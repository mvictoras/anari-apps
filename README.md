# ANARI Examples and Utilities

This repository hosts examples and utilities for working with ANARI, focusing on various rendering techniques and material handling in ANARI.

## Overview
- **Examples**: Demonstrations of rendering setups, currently with a Cornell box example in the `examples/vtk` directory. Additional examples will be added over time to showcase more ANARI features.
- **Utilities**: A Python script in `utilities/` (`make_orm.py`) to generate ORM (Occlusion, Roughness, Metalness) texture files from separate texture inputs.

## Directory Structure
- `examples/` - Contains subdirectories with ANARI-OSPRay rendering examples.
  - `vtk/` - The initial example, a Cornell box rendering using ANARI-OSPRay.
- `utilities/` - Contains utility scripts.
  - `make_orm.py` - Utility to generate ORM textures. See `utilities/README.md` for more details.

## Dependencies
The repository requires the following dependencies to run the examples and utility scripts:

- **ANARI**
- **ANARI-OSPRay**
- **OSPRay**
- **VTK 9.4** (for visualization in the examples)
- **OpenCV** (required for `make_orm.py` in `utilities`)

### Installation
Refer to the official documentation for installing ANARI, ANARI-OSPRay, OSPRay, VTK, and OpenCV.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or contributions, reach out at [mvictoras@gmail.com].
