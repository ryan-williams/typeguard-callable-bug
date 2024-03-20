from .typeddict import CreateOptions


def test_tile_extents():
    CreateOptions(dims={'soma_dim_0': {'tile': 2048}, 'soma_dim_1': {'tile': 2048}})
