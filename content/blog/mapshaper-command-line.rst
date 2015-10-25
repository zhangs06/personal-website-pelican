Geo Data Processing with Mapshaper
##################################

:slug: mapshaper-command-line

:date: 2015-10-24
:category: gis

`Mapshaper <http://mapshaper.org/>`_ is a free and open-source tool that is
best known for fast and easy simplification. Other tools for simplification -
like QGIS or ogr2ogr - do not preserve topology while simplifying.  This means
you may get sliver polygons or missing intersections. Mapshaper performs
topologically-aware simplification and gives you much more control on the
process.

But Mapshaper is much more than a simplification tool. It is in active
development and has many more data processing and editing capabilities now. It
also has a command-line version of the tool which can be run from a terminal.
In this post, we will explore the command-line tool to carry out some complex
geoprocessing tasks.

Get the Tools
^^^^^^^^^^^^^

Mapshaper is a `Node.js <https://nodejs.org/en/>`_ application. `Download
<https://nodejs.org/en/download/>`_ and install Node.js for your platform. You
will need the Node Package Manager (NPM) to install mapshaper,  so make sure it
is enabled while going through the installer.

.. image:: /images/mapshaper1.png
   :align: center

Once Node.js is installed, launch the Windows ``Command Prompt (cmd.exe)`` and
run the following command to install mapshaper.

.. code-block:: none

   npm install -g mapshaper

.. image:: /images/mapshaper2.png
   :align: center


Get the Data
^^^^^^^^^^^^

Review the data and problem statement from the `Performing Table Joins
<http://www.qgistutorials.com/en/docs/performing_table_joins.html>`_
tutorial. Download the Census Tracts shapefile ``tl_2013_06_tract.zip`` and the
Population CSV ``ca_tracts_pop.csv``. Unzip the ``tl_2013_06_tract.zip`` file
and extract it to a folder.

Procedure
^^^^^^^^^

Mapshaper command takes an input, an output and a sequence of commands to
execute. Each command is followed by options specific to that command. All
the commands and options are well documented at the `Mapshaper Wiki
<https://github.com/mbloch/mapshaper/wiki/Command-Reference>`_.

1. Let's start with simplification. We will take the census tracts shapefile
   and simlpify it to reduce the number of verticies and the total size. The
   command for simplification is ``-simplify``. You can supply a percentage
   value as an option to specify how aggressiveness of the simplification.
   Another useful option is ``keep-shapes`` which ensures that none of the
   polygons from the input will get deleted. Run the following command. Make
   sure you ``cd`` to the directory where the data has been downloaded.

.. note::

   The percentage value in the -simplify command can be a little misleading.
   The value indicates how many verticies to keep and not how many to remove.
   So a lower value would result in MORE simplification.

.. code-block:: none

   mapshaper -i tl_2013_06_tract\tl_2013_06_tract.shp -simplify 20% keep-shapes -o output.shp

.. image:: /images/mapshaper3.png
   :align: center

2. Mapshaper can also do Table Joins. We can now join the population field
   ``D001`` from the ``ca_tracts_pop.csv`` file. The join will match the fields
   we specify as ``keys`` and add it to the output file. For the join to work
   correctly, we need to specify the field types in the CSV file. (Similar to
   how a .csvt file is needed by QGIS). We can 'chain' the ``-join`` command
   after the ``-simplify`` command to perform both the operation in a single
   command.

.. code-block:: none

   mapshaper -i tl_2013_06_tract\tl_2013_06_tract.shp -simplify 20% keep-shapes -join ca_tracts_pop.csv keys=GEOID,GEO.id2 field-types GEO.id2:str,D001:num -o output.shp

.. image:: /images/mapshaper4.png
   :align: center

3. Mapshaper can also dissolve features. In my testing, Mapshaper's dissolve
   operation was many times faster than QGIS or GRASS. Let's add a
   ``-dissolve`` command and merge all census tracts for a county. We can
   also sum up the values of the ``D001`` field to get the total population of
   the county from the sum of individual census tracts.

.. code-block:: none

   mapshaper -i tl_2013_06_tract\tl_2013_06_tract.shp -simplify 20% keep-shapes -join ca_tracts_pop.csv keys=GEOID,GEO.id2 field-types GEO.id2:str,D001:num -dissolve COUNTYFP sum-fields D001 -o output.shp

.. image:: /images/mapshaper5.png
   :align: center

4. The output format needed by many web apps is geojson or topojson. Mapshaper
   can write the output in these formats as well. Let's add a
   ``format=geojson`` option to the ``-o`` command to write a geojson output.

.. code-block:: none

   mapshaper -i tl_2013_06_tract\tl_2013_06_tract.shp -simplify 20% keep-shapes -join ca_tracts_pop.csv keys=GEOID,GEO.id2 field-types GEO.id2:str,D001:num -dissolve COUNTYFP sum-fields D001 -o format=geojson output.geojson

.. image:: /images/mapshaper6.png
   :align: center

5. Finally, let's visualize our output. Go to `geojson.io <http://geojson.io>`_
   and upload the resulting ``output.geojson``. You will be able to visualize
   the output shapes and their properties.

.. image:: /images/mapshaper7.png
   :align: center

By now, you must have figured out that we have a very powerful tool on our
hands. In just a single line of command and just a few seconds of computing, we
did Simplification, Table Join, Dissolve and Format translation.
