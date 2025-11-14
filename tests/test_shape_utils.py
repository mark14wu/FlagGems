import torch

from flag_gems.utils import shape_utils


def test_c_contiguous_stride_normal():
    shape = (2, 3, 4)


def test_c_contiguous_stride_with_zero_size():
    shape = (2, 0, 4)


def test_f_contiguous_stride_normal():
    shape = (2, 3, 4)


def test_f_contiguous_stride_with_zero_size():
    shape = (2, 0, 4)


def test_ordered_stride_normal():
    shape = (2, 3, 4)
    stride_order = (0, 2, 1)
    ref_stride = (1, 8, 2)


def test_ordered_stride_with_zero_size():
    shape = (2, 3, 0)
    stride_order = (0, 2, 1)
    ref_stride = (1, 2, 2)


def test_stride_order():
    strides = (8, 16, 1)


def test_all_the_same_shape_empty():


def test_all_the_same_shape1():
    xs = [torch.randn(2, 3) for _ in range(3)]


def test_all_the_same_shape2():
    xs = [torch.randn(2, 3) for _ in range(3)] + [
        torch.randn(
            10,
        )
    ]


def test_all_the_same_stride_empty():


def test_all_the_same_stride1():
    xs = [torch.randn(2, 3) for _ in range(3)]


def test_all_the_same_stride2():
    xs = [torch.randn(2, 3) for _ in range(3)] + [
        torch.randn(
            10,
        )
    ]


def test_all_c_contiguous_empty():


def test_all_c_contiguous1():
    xs = [torch.randn(3, 4), torch.randn(2, 3)]


def test_heuristics_for_tile_size():
    shape = (10000, 10000, 10)
    tile_sizes = (1, 256, 16)


def test_heuristics_for_num_warps():
