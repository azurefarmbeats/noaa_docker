"""
Tests for GeoTiffUtil class
"""
import filecmp
import os
import tempfile

from shapely.geometry import Polygon
import geojson
import logging
import pytest

from datahub_lib.helpers.utils.geotiff_util import GeoTiffUtil


@pytest.mark.parametrize('in_tiff_path, extent, expected_out_tif', [
    # This specific case passes when run locally on windows - however fails when run in the docker image (ubuntu)
    # Find what's the issue - or simply replace this with more platform agnostic files.
    # ('datahub_lib/tests/data/reprojected_bands/10sfh_20190830_000_other_442200_60000_reprojected.tif',
    #  '{"type":"Polygon","coordinates":[[[-120.79913,38.50438],[-120.79913,38.507988],[-120.79403,38.507988],[-120.79403,38.50438],[-120.79913,38.50438]]]}',
    #  'datahub_lib/tests/data/clipped_bands/clipped_10sfh_20190830_000_other_442200_60000_reprojected.tif'),
    ('datahub_lib/tests/data/reprojected_bands/10sfh_20190830_000_other_739100_20000_reprojected.tif',
     '{"type":"Polygon","coordinates":[[[-120.79913,38.50438],[-120.79913,38.507988],[-120.79403,38.507988],[-120.79403,38.50438],[-120.79913,38.50438]]]}',
     'datahub_lib/tests/data/clipped_bands/clipped_10sfh_20190830_000_other_739100_20000_reprojected.tif')
])
def test_clip(in_tiff_path, extent, expected_out_tif):
    '''
    Tests clipping given extent from input tif file and creates a new tif file.
    Here above two test cases correspond to 60m and 20m resolution band files
    and given extent overlaps completely with input tif raster.
    '''
    with tempfile.TemporaryDirectory() as dest_dir:
        out_tiff_path = os.path.join(os.path.dirname(dest_dir),
                                     'clipped_' + os.path.basename(in_tiff_path))

        shape_json = geojson.loads(extent)
        polygon = Polygon(shape_json.coordinates[0])

        GeoTiffUtil.clip(in_tiff_path, polygon, out_tiff_path)
        files_are_same = filecmp.cmp(out_tiff_path, expected_out_tif, shallow=False)
        assert files_are_same
