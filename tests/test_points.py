from pytest import approx

from vyperdatum.points import *
from vyperdatum.vdatum_validation import vdatum_answers

gvc = VyperCore()
data_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
vdatum_answer = vdatum_answers[gvc.vdatum.vdatum_version]


def test_points_setup():
    # these tests assume you have the vdatum path setup in VyperCore
    # first time, you need to run it with the path to the vdatum folder, vp = VyperPoints('path\to\vdatum')
    vp = VyperPoints()
    assert os.path.exists(vp.vdatum.vdatum_path)
    assert vp.vdatum.grid_files
    assert vp.vdatum.polygon_files
    assert vp.vdatum.vdatum_version
    assert vp.vdatum.regions


def _transform_dataset(region: str):
    vp = VyperPoints()
    x = vdatum_answer[region]['x']
    y = vdatum_answer[region]['y']
    z = vdatum_answer[region]['z_nad83']
    vp.transform_points((6319, 'ellipse'), 'mllw', x, y, z=z, include_vdatum_uncertainty=False)

    assert vp.x == approx(x, abs=0.0001)
    assert vp.y == approx(y, abs=0.0001)
    assert vp.z == approx(vdatum_answer[region]['z_mllw'], abs=0.002)
    

def test_transform_north_carolina_dataset():
    _transform_dataset('north_carolina')


def test_transform_texas_dataset():
    _transform_dataset('texas')


def test_transform_california_dataset():
    _transform_dataset('california')


def test_transform_alaska_southeast_dataset():
    _transform_dataset('alaska_southeast')
