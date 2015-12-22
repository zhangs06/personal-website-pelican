Line Transact Surveys using OpenDataKit(ODK)
############################################

:slug: odk-line-transact

:date: 2015-12-06
:category: odk

This weekend, I got an opportunity to volunteer with a non-profit called `Junglescapes
<http://www.junglescapes.org/>`_. We took a day trip to the Bandipur forest in
Karnataka where they have done extensive work in forest restoration. One of
their success stories is working with the locals to remove invasive species
such as Lantana from the forest. Junglescapes volunteers and locals carry out
regular line transact surveys to determine the impact of their interventions.
One of the goals for my participation was to see if we can replace the
cumbersone paper forms and handheld GPS devices with a mobile-phone based
survey using ODK. I am sharing my notes on how we setup the survey and mapping
of the result.

Setting up ODK
^^^^^^^^^^^^^^

I created a survey form using `XLSForm <http://xlsform.org/>`_ standard. The
form is quite simple and uses the *geopoint* field type to collect the Lat/Lon
of the start and end points of the transact. There is also a repeated field of
type *image* to capture pictures along the transact. You can make a copy of
`this XLSForm spreadsheet
<https://docs.google.com/spreadsheets/d/1WNuMkJKvmW6xI5-blRqSsKBMb89Sn556PUKk1Ufi010/copy>`_
and use it to customize your transact survey. Once the spreadsheet was ready, I
converted it XForm using the `online converter
<http://opendatakit.org/xiframe/>`_. The resulting XML file was loaded to a `ODK
Aggregate <https://opendatakit.org/use/aggregate/>`_  server running on
AppEngine. Individual Android devices running the `ODK Collect
<https://opendatakit.org/use/collect/>`_ app were configured to use this server
and forms were downloaded to the devices. You may also skip the server and copy
the XML directly to mobile devices running the ODK Collect App.

.. image:: /images/line-transact1.png
   :align: center
   :width: 400

Collecting Field Data
^^^^^^^^^^^^^^^^^^^^^

Upon entering the wildlife sanctuary, we trekked up to the region where the
restoration has been done. There were 4 sites where we had to carry out the
line transact survey. We lay down a 150ft line using a tape measure and
collected data about number of trees, shrubs, plants and grass in a 10ft zone
around the line. The data was entered directly in the ODK Collect app.

The ODK Collect app works completely offline. We were in the middle of a forest
with no cell coverage but data collection work seamlessly. The app would sync
the data once the devices get cell reception.

.. image:: /images/line-transact2.png
   :align: center

Processing Field Data
^^^^^^^^^^^^^^^^^^^^^

After we finished the surveys, we headed back from the sanctuary. When our
devices got mobile data signals, the form submissions were submitted to the ODK
Aggregate server automatically. You can also use the `ODK Briefcase
<https://opendatakit.org/use/briefcase/>`_ application on your computer to copy
the data from devices directly.

Once you pull the data from the devices using ODK Aggregate or ODK Briefcase,
you would have a spreadsheet with individual form submissions. This itself can
be a final product of the survey and can be maintained as a record from
periodic surveys. We wanted to also map the data since we had collected GPS
coordinates for the start and end of each transact. This required a little bit
of post-processing of the data to create a `spreadsheet like this
<https://docs.google.com/spreadsheets/d/14NWa14J5rzD1jCfGWkip2NuTddDEVWzHisyah2JWRlY/edit?usp=sharing>`_.
Saving thie spreadsheet as a CSV, it can be imported in QGIS.

.. image:: /images/line-transact3.png
   :align: center

Using the *Convert points to line* tool from the Processing Toolbox, I created
a line layer from the start and end points of the transact.

.. image:: /images/line-transact4.png
   :align: center

The resulting QGIS line layer was exported as a KML and imported to `Google My
Maps <http://google.com/mymaps>`_ . I had also collected our entire trek and
some waypoints using the `My Tracks app
<https://play.google.com/store/apps/details?id=com.google.android.maps.mytracks&hl=en>`_.
This was also imported to Google My Maps. These layers resulted in a rich and
informative map from our field data exercise. See the `live interactive map
<https://www.google.com/maps/d/viewer?mid=zjnvnF630TsQ.kngZHPKOj9HE>`_ here.

.. image:: /images/line-transact5.png
   :align: center

Overall, using ODK for the transact surveys helped speed up the data
collection. There was no data-entry after the surveys and creating an
interactive map visualization was a breeze. If you are an individual or a team
who is doing field data collection, moving to ODK would help you reduce errors
and collect accurate data without the hassles of data entry.

