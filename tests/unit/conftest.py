import sys
import pytest

sys.path.append('.')  # for pytest on automatic testing stage

from easycolab.install import Install, InstallPyTorch


DEFAULT_ACCELERATOR = 'cpu'
CORRECT_PLATFORM_3 = 'cp36-cp36m'
CUDA_VERSION = '9.2'
GPU_ACCELERATOR = 'cu92'
NVIDIA_PATH = '/dev/nvidia0'
TEST_PACKAGE_VALID = ['pip', 'pip']
TEST_PACKAGE_INVALID_TYPE = 'foo'
TEST_PACKAGE_INVALID = ['foo', 'bar']

DEFAULT_PYTORCH_VERSION = '0.4.1'
PYTORCH_LINK = 'http://download.pytorch.org/whl/'

@pytest.fixture
def install():
    """Default installation"""
    return Install()


@pytest.fixture
def install_pytorch():
    """Default PyTorch installation"""
    return InstallPyTorch()