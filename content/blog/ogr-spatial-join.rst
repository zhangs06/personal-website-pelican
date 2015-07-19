Spatial Joins on the Command Line
#################################

:slug: ogr-spatial-join

:date: 2015-07-19
:category: gis

GDAL and OGR libraries come with handy `command-line tools
<http://www.gdal.org/ogr_utilities.html>`_. These tools are quite powerful and
can save you a lot of effort if you know how to use them. Here I will show how
to use the `ogrinfo <http://www.gdal.org/ogrinfo.html>`_ and `ogr2ogr
<http://www.gdal.org/ogr2ogr.html>`_ tools to perform spatial joins. A single
command can do complex operations on your spatial data and save you a lot of
clicking-around and data-munging in a GIS.

Get the Tools
^^^^^^^^^^^^^

The best way to get the command-line tools on Windows is via the `OSGeo4W
Installer <http://trac.osgeo.org/osgeo4w/>`_. If you are on Linux or Mac, see
`these instructions
<https://trac.osgeo.org/gdal/wiki/DownloadingGdalBinaries>`_ to get the package
for your platform.

Get the Data
^^^^^^^^^^^^

Review the data and problem statement from the `Performing Spatial Joins
<http://www.qgistutorials.com/en/docs/performing_spatial_joins.html>`_
tutorial. Download the Borough Boundaries and Nursing Homes shapefiles.

Procedure
^^^^^^^^^

OGR command line tools accept only 1 input. But we have 2 inputs for the
spatial join. An easy way to fix this, is to use a `VRT file
<http://www.gdal.org/drv_vrt.html>`_. A VRT file allows us to specify multiple
inputs and pass them to the command-line tool as layers of a single input.

1. Unzip the input shapefiles in a single folder on your drive. Create a file
   named ``input.vrt`` in the same folder with the following content.

.. code-block:: none

   <OGRVRTDataSource>
       <OGRVRTLayer name="boroughs">
           <SrcDataSource>nybb.shp</SrcDataSource>
           <SrcLayer>nybb</SrcLayer>
       </OGRVRTLayer>
       <OGRVRTLayer name="nursinghomes">
           <SrcDataSource>OEM_NursingHomes_001.shp</SrcDataSource>
           <SrcLayer>OEM_NursingHomes_001</SrcLayer>
       </OGRVRTLayer>
   </OGRVRTDataSource>

2. Open the OSGeo4W shell and ``cd`` to the directory containing the shapefiles
   and the vrt file. Run the ``ogrinfo`` command to check if the VRT file is
   correct.

.. code-block:: none

   ogrinfo input.vrt

.. image:: /images/ogr-spatial1.png
   :align: center

3. OGR tools can run SQL queries on the input layers. We will use the
   ``ST_INTERSECTS`` function to find all nursing homes that intersect the
   boundary of a borough and use the ``SUM`` function to find the total nursing
   home capacity of a borough. Run the following command.

.. code-block:: none

   ogrinfo -sql "SELECT b.BoroName, sum(n.Capacity) as total_capacity from
   boroughs b, nursinghomes n WHERE ST_INTERSECTS(b.geometry, n.geometry) group
   by b.BoroName" -dialect SQLITE input.vrt

.. image:: /images/ogr-spatial2.png
   :align: center

4. You can see that in a single command we got the results by doing a spatial
   join that took probably 10 steps in a GIS environment. We can do a reverse
   spatial join as well. We can join the name of the Borough to each feature of
   the Nursing Homes layer. Using the ``ogr2ogr`` tool we can write out a
   shapefile from the resulting join. Note that we are adding a ``geometry``
   column in the SELECT statement which results in a spatial output. Run the following command:

.. code-block:: none

   ogr2ogr -sql "SELECT n.Name, n.Capacity, n.geometry, b.BoroName from
   boroughs b, nursinghomes n WHERE ST_INTERSECTS(b.geometry, n.geometry)"
   -dialect SQLITE output.shp input.vrt

.. image:: /images/ogr-spatial3.png
   :align: center

5. Open the ``output.shp`` in a GIS to verify that the new shapefile as
   attributes joined from the intersecting borough. You can use ``ogrinfo``
   command to check that as well.

.. code-block:: none

   ogrinfo -al output.shp

.. image:: /images/ogr-spatial4.png
   :align: center
