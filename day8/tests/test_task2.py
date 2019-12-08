import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

import numpy as np

from day8.task2 import render_image


class TestCalculateImageChecksum:
    def test_returns_correct_checksum(self):
        image_layers = np.array(
            [
                [
                    [0,2], 
                    [2,2]
                ], 
                [
                    [1,1], 
                    [2,2]
                ],
                [
                    [2,2],
                    [1,2]
                ],
                [
                    [0,0],
                    [0,0]
                ]
            ]
        )

        expected_rendered_image = [[0,1], [1,0]]

        rendered_image = render_image(image_layers)

        assert np.equal(rendered_image, expected_rendered_image).all()