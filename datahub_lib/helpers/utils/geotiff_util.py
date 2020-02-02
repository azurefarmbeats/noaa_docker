# System imports
import array
import enum
import json
import math

# 3rd party imports
import gdal
import geojson
import numpy as np
import rasterio
import rasterio.mask
from matplotlib import pyplot as plt
from matplotlib import ticker
from matplotlib import colors
from scipy.ndimage.filters import gaussian_filter
from shapely.geometry import Polygon

from datahub_lib.framework.scene_constants import SceneConstants

class GeoTiffUtil:
    '''
    Util class with methods to process GeoTiff files.
    '''
    @staticmethod
    def numpy_array_to_png(in_arr:array, out_file:str, extent:list, vmin:float, vmax:float, title:str=None):
        '''
        Saves given numpy array to png file.
        Optionally, squashes values within a given range (both vmin and vmax must be given and non-zero for squashing)
        :param array in_arr: input np array data
        :param str out_file: output png file path
        :param list extent: boundary latitudes and longitudes of the array
        :param float vmin: min value of squash range
        :param float vmax: max value of squash range
        :param str title: image title
        '''
        in_arr[in_arr == SceneConstants.NODATA_VALUE] = np.nan
        in_arr[in_arr == SceneConstants.UINT_NODATA_VALUE] = np.nan
        blurred = gaussian_filter(in_arr, sigma=0.0)
        plt.figure()
        
        # if vmin and vmax are neither None nor Zero, then squash the values
        norm = None
        if vmin and vmax:
            norm = colors.Normalize(vmin=vmin, vmax=vmax)
        
        # plotting array
        plt.imshow(blurred, cmap='RdYlGn', extent=extent, norm=norm)
        plt.colorbar()
        plt.xlabel("longitudes", fontsize=12)
        plt.ylabel("latitudes", fontsize=12)
        if title:
            plt.title(title)

        # preserving 4 digits of xticks(longtitudes) and yticks(latitudes)    
        ax = plt.gca()
        ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.4f'))
        ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.4f'))

        # rotating xticks by 45 degrees
        plt.xticks(rotation=45)

        plt.savefig(out_file, bbox_inches = "tight")


    @staticmethod
    def get_raster_band_array(tiff_path:str, band_no:int) -> array:
        '''
        returns selected band values as array
        :param string tiff_path: input tiff file path
        :param int band_no: band number in input tiff
        :returns array: two dimensional array of band values
        '''
        raster = gdal.Open(tiff_path, gdal.GA_ReadOnly)
        band = raster.GetRasterBand(band_no)
        return band.ReadAsArray()

    @staticmethod
    def get_raster_extent(raster_file:str):
        '''
        Returns the extent of raster [upper_left_x, upper_right_x, upper_left_y, lower_left_y]
        :param str raster_file: raster file name
        :return extent array
        '''
        raster = gdal.Open(raster_file, gdal.GA_ReadOnly)
        (upper_left_x, x_res, _, upper_left_y, _, y_res) = raster.GetGeoTransform()
        extent = [upper_left_x, upper_left_x + raster.RasterXSize * x_res, upper_left_y, upper_left_y + raster.RasterYSize * y_res]
        raster = None
        return extent


    @staticmethod
    def merge(input_files:list, output_fp:str):
        '''
        Method to merge list of tiff files into single tiff file.
        All tiff files must be of same extent.
        :param list input_files: list of full paths of input tiff files
        :param str output_fp: file path of merged tiff file
        '''
        # Read input tiff file and get spatial information
        raster = gdal.Open(input_files[0], gdal.GA_ReadOnly)
        geotransform = raster.GetGeoTransform()
        originX = geotransform[0]
        originY = geotransform[3]
        pixelWidth = geotransform[1]
        pixelHeight = geotransform[5]
        cols = raster.RasterXSize
        rows = raster.RasterYSize

        # create output tiff file using input
        driver = gdal.GetDriverByName('GTiff')
        outRaster = driver.Create(output_fp, cols, rows,
                                  raster.RasterCount,
                                  raster.GetRasterBand(1).DataType)

        outRaster.SetGeoTransform((originX, pixelWidth, 0, originY, 0, pixelHeight))
        outRaster.SetProjection(raster.GetProjection())

        # merge band by band from all input files
        for band_no in range(1, raster.RasterCount + 1):
            outband = outRaster.GetRasterBand(band_no)
            array = GeoTiffUtil.get_raster_band_array(input_files[0], band_no)

            for input_file in input_files[1:]:
                tmp_array = GeoTiffUtil.get_raster_band_array(input_file, band_no)

                # merge array values with tmp_array values
                xlimit = min(len(array), len(tmp_array))
                ylimit = min(len(array[0]), len(tmp_array[0]))

                for i in range(xlimit):
                    for j in range(ylimit):
                        array[i][j] = max(array[i][j], tmp_array[i][j])

            outband.WriteArray(array)
            outband.FlushCache()


    @staticmethod
    def clip(in_tiff_path:str, polygon:Polygon, out_tiff_path:str):
        '''
        Clips polygon data from tiff file. If part of polygon intersects with tiff,
        creates full tiff of size polygon and copies only part of intersecting portion.
        remaining pixel values are NA.
        :param str in_tiff_path: input tiff file path
        :param Polygon polygon: area of interest to be clipped
        :param str out_tiff_path: output tiff file path with clipped data
        '''
        input_raster = gdal.Open(in_tiff_path, gdal.GA_ReadOnly)
        input_raster_geotransform = input_raster.GetGeoTransform()

        # Compute the cell resolutions for output tiff
        # below values are assigned assuming polygon points are (lon, lat)
        envelope_lon_min, envelope_lat_min, envelope_lon_max, envelope_lat_max  = polygon.bounds
        cols = math.ceil(abs((envelope_lon_max - envelope_lon_min) / input_raster_geotransform[1]))
        rows = math.ceil(abs((envelope_lat_max - envelope_lat_min) / input_raster_geotransform[5]))

        # Create output tiff
        out_dataset = gdal.GetDriverByName("GTiff") \
                          .Create(out_tiff_path,
                                  cols,
                                  rows,
                                  input_raster.RasterCount,
                                  input_raster.GetRasterBand(1).DataType)

        out_dataset.SetGeoTransform([envelope_lon_min,
                                    input_raster_geotransform[1],
                                    0,
                                    envelope_lat_max,
                                    0,
                                    input_raster_geotransform[5]])

        out_dataset.SetProjection(input_raster.GetProjection())
        gdal.ReprojectImage(input_raster,
                            out_dataset,
                            None,
                            input_raster.GetProjection(),
                            gdal.GRA_Bilinear)

        # flush cache
        out_dataset.FlushCache()
        out_dataset = None


    @staticmethod
    def get_masked_band(band_tif_file:str, geo_json:json, no_data_value:int) -> array:
        '''
        Masks the pixels outside the given boundary with no_data_value
        :param str band_tif_file: tiff file path
        :param json geo_json: geo json of the area of interest
        :param str no_data_value: no data value
        :return: returns masked band after masking given geo_json
        '''
        masked_band = None
        with rasterio.open(band_tif_file) as src:
            if src.count > 1:
                raise Exception('Incorrect number of bands in tif file %d', src.count)
            else:
                shape_jsons = []
                shape_jsons.append(geojson.loads(geo_json))
                masked_band, out_transform = rasterio.mask.mask(dataset=src,
                                                                shapes=shape_jsons,
                                                                crop=True,
                                                                nodata=no_data_value)

        return masked_band


    @staticmethod
    def get_masked_latlongs(band_tif_file:str, geo_json:json, no_data_value:int) -> array:
        '''
        Retruns the latitudes and lognitudes of the pixel(inside geo_json) centroids
        :param str band_tif_file: tiff file path
        :param json geo_json: geo json of the area of interest
        :param str no_data_value: no data value
        :return: returns latitudes and longitudes of the given band pixel centroids after masking given geo_json
        '''
        with rasterio.open(band_tif_file) as src:
            shape_jsons = []
            shape_jsons.append(geojson.loads(geo_json))
            masked_band, out_transform = rasterio.mask.mask(dataset=src,
                                                            shapes=shape_jsons,
                                                            crop=True,
                                                            nodata=no_data_value)

            # All rows and columns
            cols, rows = np.meshgrid(np.arange(masked_band.shape[2]), np.arange(masked_band.shape[1]))

            # Flatten all rows, cols, masked_band
            rows = rows.flatten()
            cols = cols.flatten()
            masked_band = masked_band.flatten()

            # Add half the cell size to get pixel centroid(latitude and longitude)
            (upper_left_x, x_size, x_rotation, upper_left_y, y_rotation, y_size) = out_transform.to_gdal()
            lng = cols * x_size + upper_left_x + (x_size / 2)
            lat = rows * y_size + upper_left_y + (y_size / 2)
            extent_lng_lat = np.column_stack([lng, lat])
            farm_lng_lat = extent_lng_lat[masked_band != no_data_value]

        return (extent_lng_lat, farm_lng_lat)


    @staticmethod
    def read_raster(file_path:str, band_number:int) -> array:
        '''
        Reads input tiff file and returns the numpy array of the
        requested band number
        :param file_path: tiff file path
        :param band_number: band/layer number
        :return: returns raster layer as numpy array
        '''
        raster = gdal.Open(file_path, gdal.GA_ReadOnly)
        if raster is None:
            raise Exception("Error loading tiff file, %s", file_path)

        return np.array(raster.GetRasterBand(band_number).ReadAsArray(), dtype=float)


    @staticmethod
    def write_raster(in_data:array, data_type:enum, out_file:str,
                     geo_transform:array, projection:str, ndv:int):
        '''
        reads the numpy array and writes as GeoTIFF file.
        :param array in_data: numpy array that contains data
        :param GDALDataType enum data_type: output tiff data type
        :param str out_file: output GeoTIFF file path
        :param array geo_transform: output tiff geo transformation
        :param str projection: output tiff projection
        :param int ndv: no data value of GeoTIFF
        '''
        if in_data is None:
            raise Exception("Attempting to write NoneType to Raster")

        cols = in_data.shape[1]
        rows = in_data.shape[0]

        driver = gdal.GetDriverByName('GTiff')
        out_dataset = driver.Create(out_file, cols, rows, 1, data_type)
        out_dataset.SetGeoTransform(geo_transform)
        out_dataset.SetProjection(projection)
        outband = out_dataset.GetRasterBand(1)
        outband.SetNoDataValue(ndv)
        outband.WriteArray(in_data)
        outband.FlushCache()
        out_dataset = None
