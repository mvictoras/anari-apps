import cv2
import numpy as np
import argparse

def create_orm_texture(occlusion_file, roughness_file, metalness_file, output_file):
    """
    Create an ORM (Occlusion, Roughness, Metalness) texture from separate metalness and roughness images.
    Since there is no occlusion map, the red channel will be set to full intensity (255).
    
    Args:
        metalness_file (str): Path to the metalness image file (grayscale).
        roughness_file (str): Path to the roughness image file (grayscale).
        output_file (str): Path to save the combined ORM texture.
    """
    # Load the metalness and roughness textures
    if occlusion_file is None :
       occlusion = 255
    else :
       occlusion = cv2.imread(occlusion_file, cv2.IMREAD_GRAYSCALE)

    if metalness_file is None :
       metalness = 255
    else :
      metalness = cv2.imread(metalness_file, cv2.IMREAD_GRAYSCALE)
    if roughness_file is None :
      roughness = 255
    else :
      roughness = cv2.imread(roughness_file, cv2.IMREAD_GRAYSCALE)

    # Ensure both images have the same dimensions
    height, width = metalness.shape
    roughness = cv2.resize(roughness, (width, height))

    # Stack channels into an ORM image, setting the red channel to full intensity (no occlusion)
    orm_image = np.zeros((height, width, 3), dtype=np.uint8)
    orm_image[:, :, 0] = occlusion               # Set red channel to full intensity (no occlusion)
    orm_image[:, :, 1] = roughness          # Green channel for roughness
    orm_image[:, :, 2] = metalness          # Blue channel for metalness

    # Save the ORM texture
    cv2.imwrite(output_file, orm_image)
    print(f"ORM texture saved as {output_file}")

# Set up command-line argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combine occlusion, roughness, and metalness maps into an ORM texture.")
    parser.add_argument("--occlusion_file", type=str, help="Path to the occlusion texture image.")
    parser.add_argument("--roughness_file", type=str, help="Path to the roughness texture image.")
    parser.add_argument("--metalness_file", type=str, help="Path to the metalness texture image.")
    parser.add_argument("--output_file", type=str, help="Path to save the output ORM texture image.")

    args = parser.parse_args()

    # Run the function with command-line arguments
    create_orm_texture(args.occlusion_file, args.roughness_file, args.metalness_file, args.output_file)
