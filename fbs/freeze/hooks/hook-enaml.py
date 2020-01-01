"""
Add all *.enaml files from Enaml package
"""
from glob import glob
from os.path import dirname, relpath, join

from PyInstaller.utils.hooks import get_package_paths

_base_dir, _enaml_package = get_package_paths('enaml')
_enaml_files = glob(join(_base_dir, '**', '*.enaml'), recursive=True)
datas = [(f, relpath(dirname(f), _base_dir)) for f in _enaml_files]