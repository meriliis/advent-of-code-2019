import os
from pathlib import Path
import numpy as np

from task1 import convert_image_data_to_layers


def render_image(image_layers: np.array) -> np.array:
    rendered_image = image_layers[0]

    for layer in image_layers[1:]:
        rendered_image[rendered_image == 2] = layer[rendered_image == 2]

    return rendered_image


if __name__ == '__main__':
    with open(os.path.join(Path(__file__).parent, 'encoded_image.txt')) as f:
        image_data = f.readline()

    image_layers = convert_image_data_to_layers(image_data, (6, 25))
    rendered_image = render_image(image_layers)

    print(rendered_image)