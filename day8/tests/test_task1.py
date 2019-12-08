import numpy as np

from day8.task1 import convert_image_data_to_layers, calculate_image_checksum


class TestConvertImageDataToLayers:
    def test_correctly_converts_to_layers(self):
        image_data = '123456789012'
        image_shape = (2, 3)
        expected_image_layers = np.array(
            [
                [
                    [1,2,3], 
                    [4,5,6]
                ], 
                [
                    [7,8,9], 
                    [0,1,2]
                ]
            ]
        )

        image_layers = convert_image_data_to_layers(image_data, image_shape)

        assert np.equal(image_layers, expected_image_layers).all()


class TestCalculateImageChecksum:
    def test_returns_correct_checksum(self):
        image_layers = np.array(
            [
                [
                    [1,2,3], 
                    [4,5,6]
                ], 
                [
                    [7,8,9], 
                    [0,1,2]
                ]
            ]
        )

        expected_checksum = 1

        checksum = calculate_image_checksum(image_layers)

        assert checksum == expected_checksum