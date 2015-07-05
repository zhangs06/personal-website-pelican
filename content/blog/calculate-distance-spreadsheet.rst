Calculate distance between a pair of lat/lon coordinates
########################################################

:slug: calculate-distance-spreadsheet

:date: 2013-07-06
:category: gis

I recently had a need to calculate distance between a large number of
latitude/longitude coordinate pairs. There are many options available if you
want to import these in a GIS and run analysis. But there is a simpler and much
more accesible way if you aren't doing very high accuracy calculations.

I decided to write a simple *Macro* or *AppScript* for Google Spreadsheets,
which uses the well-known `Haversine formula
<https://en.wikipedia.org/wiki/Haversine_formula>`_ to calculate distance
between 2 coordinates. Once the script is saved, the user of the spreadsheet
can use the function 'distance()' just the way one uses any of the built-in
functions.

.. image:: /images/calculate-distance-spreadsheet.png
   :alt: forumla to calculate distance.

You can give it a try. Just open `this spreadsheet
<https://docs.google.com/spreadsheet/ccc?key=0AkXc7QoGul60dEc5Q01pTGNfa3N5YW5EWDNkOG9Ec3c&newcopy=true>`_,
make a copy it and play with it as you like.
