# Utilities for ANARI

This directory contains utility scripts to assist with common tasks when working with ANARI.

## Available Utilities

### `make_orm.py`
The `make_orm.py` script generates an ORM (Occlusion, Roughness, Metalness) texture by combining separate metalness and roughness textures. Since there is no occlusion map provided, the red channel in the output image will be set to full intensity (255).

#### Dependencies
- **OpenCV** (required to process the texture images)

#### Usage

```bash
python make_orm.py --occlusion_file=<occlusion_file> --roughness_file=<roughness_file> --metalness_file=<metalness_file> --output_file=<output_orm_file>
```

If one of the files is emmitted, then the channel will be set to 255.
