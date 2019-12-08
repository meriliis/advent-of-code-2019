from typing import Tuple
import os
from pathlib import Path

import numpy as np


def convert_image_data_to_layers(image_data: str, shape: Tuple[int, int]) -> np.array:
    image_data_list = [int(x) for x in list(image_data)]
    image_layers = np.reshape(image_data_list, (-1, shape[0], shape[1]))

    return image_layers


def calculate_image_checksum(image_layers: np.array) -> int:
    layers_zero_counts = (image_layers == 0).sum(axis=(1,2))
    layer_with_min_zeroes_i = np.argmin(layers_zero_counts)
    layer_with_min_zeroes = image_layers[layer_with_min_zeroes_i]

    n_ones = (layer_with_min_zeroes == 1).sum()
    n_twos = (layer_with_min_zeroes == 2).sum()

    checksum = n_ones * n_twos

    return checksum


if __name__ == '__main__':
    with open(os.path.join(Path(__file__).parent, 'encoded_image.txt')) as f:
        image_data = f.readline()

    image_layers = convert_image_data_to_layers(image_data, (6, 25))
    checksum = calculate_image_checksum(image_layers)

    print(checksum)