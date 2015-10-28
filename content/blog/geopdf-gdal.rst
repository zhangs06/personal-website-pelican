Creating Geospatial PDFs with GDAL Tools
########################################

:slug: geopdf-gdal

:date: 2015-10-27
:category: gis

`GeoPDF <https://en.wikipedia.org/wiki/GeoPDF>`_ is a unique data format that
brings the portability of PDF to geospatial data. A GeoPDF document can present
raster and vector data and preserve the georeference information. This can be a
useful format for non-GIS folks to consume GIS data without needing
GIS-software. While GeoPDF is a proprietary format, we have a close alternative
is the open `Geospatial PDF <https://en.wikipedia.org/wiki/Geospatial_PDF>`_
format. GDAL has added support for creating Geospatial PDF documents from
version 1.10 onwards. In this post, I will show how to create a GeoPDF document
containing multiple vector layers.

Get the Tools
^^^^^^^^^^^^^

Windows
-------
`OsGeo4W <https://trac.osgeo.org/osgeo4w/>`_ is the best way to install GDAL on
Windows. The default installation gives your GDAL tools with PDF format support. You
can use the GDAL tools via the OsGeo4W Shell included in the install.

Mac
---
KyngChaos providers a convenient `GDAL installer
<http://www.kyngchaos.com/software/frameworks#gdal_complete>`_ for Mac. You
also need to install the additional `GeoPDF plugin
<http://www.kyngchaos.com/files/software/frameworks/GDAL-GeoPDF_Plugin-1.11.3-1.dmg>`_
to enable support for PDF format.

Once installed, add the path to GDAL library to your
``.bash_profile`` file to be able to use the commands easily from the terminal.
Launch a Terminal and type in the following commands.

.. code-block:: none

   echo 'export PATH=/Library/Frameworks/GDAL.framework/Programs:$PATH' >> ~/.bash_profile
   source ~/.bash_profile

Linux
-----
Installation instructions will vary with the distribution. On Ubuntu, you can
install the ``gdal-bin`` package.

.. code-block:: none

   sudo apt-get install gdal-bin

Verify GDAL Install
^^^^^^^^^^^^^^^^^^^
If you already have GDAL installed, or just installed it, run the following
command in a terminal to verify that your GDAL installation is working and has
support for GeoPDF format.

.. code-block:: none

   gdalinfo --formats | grep -i pdf

If you see Geospatial PDF printed in the output - you are all set. If you do
not get any output or get an error, your install is not correctly configured.

.. image:: /images/geopdf1.png
   :align: center

Get the Data
^^^^^^^^^^^^
For this example, I chose to use `OpenStreetMap Metro Extracts
<https://mapzen.com/data/metro-extracts>`_ from MapZen. Download the shapefiles
(OSM2PGSQL SHP format) for the city of your choice. I am using the extract for
Bangalore city in this example. Unzip the downloaded file to a folder on your
computer.

Procedure
^^^^^^^^^

The process for creating a GeoPDF file from a bunch of shapefiles is the matter
of running a single ``gdal_translate`` command. But we need to prepare the data
and figure out the correct command-line options. So follow along to understand
how you can arrive at the final command - or simply scroll to the end to see
the final command-line.

latuviitta.org has a `comprehensive overview
<http://latuviitta.org/documents/Geospatial_PDF_maps_from_OSM_with_GDAL.pdf>`_ of all the options available for
GeoPDF creation via GDAL. The follow steps are adapted and simplified version
of the guide.

1. First step is to create a ``.vrt`` file that can hold all the vector layers
   we want in the PDF. If you just need a single layer in the PDF, you can skip
   creating the ``.vrt`` file and directly reference the layer in place of the
   VRT. Note the <SrcSQL> tag in the VRT file. This is for filtering out all
   features where the 'name' field is empty. You can leave that out or modify
   to suit your dataset. Name this file ``osm.vrt`` and save it on the same
   folder with your data.

.. code-block:: none

   <OGRVRTDataSource>
       <OGRVRTLayer name="roads">
           <SrcDataSource>bengaluru_india_osm_line.shp</SrcDataSource>
           <SrcLayer>bengaluru_india_osm_line</SrcLayer>
           <SrcSQL dialect="sqlite">SELECT name, highway, geometry from bengaluru_india_osm_line where name is not NULL</SrcSQL>
           <GeometryType>wkbLineString</GeometryType>
           <LayerSRS>WGS84</LayerSRS>
       </OGRVRTLayer>
       <OGRVRTLayer name="pois">
           <SrcDataSource>bengaluru_india_osm_point.shp</SrcDataSource>
           <SrcLayer>bengaluru_india_osm_point</SrcLayer>
           <SrcSQL dialect="sqlite">SELECT name, geometry from bengaluru_india_osm_point where name is not NULL</SrcSQL>
           <GeometryType>wkbPoint</GeometryType>
           <LayerSRS>WGS84</LayerSRS>
       </OGRVRTLayer>
   </OGRVRTDataSource>

2. GeoPDF is a raster format that can overlay
   vectors on top. So we need a raster layer as the base. If you have some
   satellite imagery or scanned raster for the area, you can use it as the
   base layer, or we can create an empty raster for the extent of the vector
   layer. ``ogrtindex`` command creates a bounding box polygon from the given
   input layers. ``gdal_rasterize`` command then fills this polygon with the
   given value and creates a raster. the ``-tr`` option specifies the pixel
   resolution of the raster in degrees. You can tweak that to get the output
   size you need. ``cd`` to the directory where you have extracted the vector
   layers and run the following commands.

.. code-block:: none

   cd Users\Ujaval\Downloads\bengaluru_india.osm2pgsql-shapefiles

   ogrtindex -accept _different_schemas extent.shp osm.vrt

   gdal_rasterize -burn 255 -ot Byte -tr 0.0001 0.0001 extent.shp bangalore.tif

.. image:: /images/geopdf2.png
   :align: center

3. Now we can convert the empty ``bangalore.tif`` raster to a PDF - overlaying
   the vector layers from the ``osm.vrt`` file.

.. code-block:: none

   gdal_translate -of PDF -a_srs EPSG:4326 bangalore.tif bangalore.pdf -co OGR_DATASOURCE=osm.vrt -co OGR_DISPLAY_FIELD="name"

.. image:: /images/geopdf3.png
   :align: center

4. Once the conversion fiinshes, you can open the resulting ``bangalore.pdf``
   file in any PDF viewer. Opening it in Adobe Acrobat viewer, you can see the
   map data layers. You can browse the features in the layer panel, search for
   any attribute value and zoom/pan the map.

.. image:: /images/geopdf4.png
   :align: center

5. Another popular use of GeoPDF files is to use it as offline base maps using
   programs such as `Avenza PDF Maps <http://www.avenza.com/pdf-maps>`_.
   Loading the ``bangalore.pdf`` file on Avenza Maps on your mobile phone, you
   can use the GPS to view your current location or trace a GPS route on top.
   Search also works across layers in the PDF.

.. image:: /images/geopdf5.png
   :align: center

You can download the sample `bangalore.pdf
<https://drive.google.com/open?id=0B0Xc7QoGul60eFRuTHVvUWRVZEE>`_ Geospatial
PDF format file for exploring the format yourself.
