Implementing a Field Data collection app for APD
################################################

:slug: opendatakit-for-apd

:date: 2015-04-29
:category: odk

The `Association for People with Disability (APD) <http://www.apd-india.org/>`_
is a non-profit organization based out of Bangalore, India. Their mission is to
reach out and rehabilitate people with disability from the under privileged
segment. Over the past year, I along with my colleagues have been volunteering
with them to develop a system that can help improve their field data collection
efforts.

Problem
^^^^^^^

APD provides variety of services rehabilitate under privileged people with
disabilities. Before they can render any service, they need register the
individuals with the organization and collect basic background information.
Registrations are mostly done in their field offices or at camps organized in
rural areas. Paper forms were filled at the site and shipped to their field
office. A staff member entered the data manually into their software platform.

.. figure:: /images/apd1.jpg
   :align: center
   :alt: a registration camp

   A registration camp.

This has many problems:

* The text on the paper form was often illegible. Some fields were missing or
  inaccurate.

* Data entry was laborious and introduced errors.

* 4–6 weeks of lag time before the data was available in the system.

Our solution
^^^^^^^^^^^^

We helped APD implement a process using `OpenDataKit (ODK)
<https://opendatakit.org/>`_ that allowed capture of the form using android
devices. With the new system, the data is captured on the mobile device using
the `ODK Collect
<https://play.google.com/store/apps/details?id=org.odk.collect.android&hl=en>`_
app in the field and sent to a `ODK Aggregate
<https://opendatakit.org/use/aggregate/>`_ server running on Google AppEngine.
The data ends up in a shared spreadsheet which is imported to APD’s system
after each registration camp.

.. figure:: /images/apd2.png
   :align: center
   :alt: APD staff using the ODK collect mobile app

   APD staff using the ODK collect mobile app

This new workflow offers several advantages over the paper based forms:

* Reliable data collection in areas with poor network connectivity. ODK Collect
  app can work completely offline and the data is stored on the device memory.
  Once the staff members are back in office and connect to a WiFi network --
  the data is sent to the server.

* The mobile app enforces checks, so all the data is consistent and there are
  no missing fields.

* Allows for the capture of pictures and additional metadata (such as time,
  location, staff id).

* The data is exported from the spreadsheet and imported to their system the
  next day -- cutting the lag from weeks to hours.

Timeline
^^^^^^^^

* October 2014: Met with the APD registration team to understand their
  requirements and design a process.

* November 2014: A prototype is created by migrating the registration form to
  ODK using XLSForm. APD trains field staff on using the mobile app. Successful
  field test.

.. figure:: /images/apd3.jpg
   :align: center
   :alt: First field test

   First field test of the app with newly trained staff

* December 2014: First full-fledged camp with 3 devices. Successful
  registration of 55 participants. Staff is very happy with the increased
  speed, accuracy and reduction in delay in getting the registrations
  processed.

.. figure:: /images/apd4.jpg
   :align: center
   :alt: First real deployment.

   First ‘real’ deployment.Staff had paper forms as backup, but did not need it

* January 2014: APD moves their registrations completely to mobile devices. All
  registrations are completely paperless and have the added benefit of having
  participant’s picture as part of the registration process. Over 500
  registrations processed without a problem.

.. figure:: /images/apd5.jpg
   :align: center
   :alt: paperless registration camp

   Completely paperless registration camp after migration to the mobile app

While this is a great start, we are looking at helping them with other
challenges in the field. In the coming months, we want to tackle the following
problems:

* Migrate patient visit and treatment forms to OpenDataKit. These require
  having access to the patient’s medical history in the field. OpenDataKit’s
  2.0 suite of tools would be a good fit.

* Task allocation and scheduling optimization for the field staff.

* Encoding the knowledge from the training manual to a mobile app.

