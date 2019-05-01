"""
Multiplexes a glass file, by taking the initial glass file, shrinking it to
live in one corner, and then duplicating this.
"""

import h5py
import numpy as np

from collections import namedtuple


def load_data(filename):
    with h5py.File(filename, "r") as handle:
        return dict(
            Coordinates=handle["PartType0/Coordinates"][...],
            Masses=handle["PartType0/Masses"][...],
            SmoothingLength=handle["PartType0/SmoothingLength"][...],
            ParticleIDs=handle["PartType0/ParticleIDs"][...],
            Velocities=handle["PartType0/Velocities"][...],
        )


def duplicate(input_data: dict) -> dict:
    """
    Duplicates the data in an 8x8 cube, and multiplies positions, smoothing lengths,
    and Velocities by 1/2
    """

    output_data = {}

    output_coordinates = []

    for x in [1.0, 2.0]:
        for y in [1.0, 2.0]:
            for z in [1.0, 2.0]:  # lol
                these_coordinates = input_data["Coordinates"].copy()

                these_coordinates[:, 0] * x
                these_coordinates[:, 1] * y
                these_coordinates[:, 2] * z

                output_coordinates.append(these_coordinates)

    output_data["Coordinates"] = np.concatenate(output_coordinates) * 0.5

    del output_coordinates

    output_data["Velocities"] = np.concatenate([input_data["Velocities"]] * 8) * 0.5

    output_data["SmoothingLength"] = (
        np.concatenate([input_data["smoothing_lengths"]] * 8) * 0.5
    )

    output_data["Masses"] = np.concatenate([input_data["Masses"]] * 8)

    output_data["ParticleIDs"] = np.arange(input_data["ParticleIDs"].size, dtype=int)

    return output_data


def write_data(filename, output_data: dict):
    with h5py.File(filename, "w") as handle:
        grp = handle.create_group("PartType0")
        for key, value in output_data.items():
            grp.create_dataset(key, data=value)

    return


if __name__ == "__main__":
    import argparse as ap

    parser = ap.ArgumentParser(
        description="Duplexes a glass file by copying the data and replicating it in eight quadrants"
    )

    parser.add_argument("-i", "--input", help="Input filename", type=str)

    parser.add_argument("-o", "--output", help="Output filename", type=str)

    args = parser.parse_args()

    input_data = load_data(args.input)
    output_data = duplicate(input_data)
    write_data(args.output, output_data)
