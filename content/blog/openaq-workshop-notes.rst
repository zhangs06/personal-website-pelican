OpenAQ Workshop Notes
#####################

:slug: openaq-workshop-notes

:date: 2016-11-25
:category: conference

I recently attended the `OpenAQ workshop <https://medium.com/@openaq/the-next-openaq-workshop-is-in-delhi-apply-to-come-7622aa60e48e#.e8xvdj3rw>`_  in Delhi . The workshop’s goal was to bring tech, science and media folks working on air quality together and brainstorm how to use open data to tackle air pollution challenges. Below are my notes and links to materials presented during the workshop.

Below are my notes and links to materials presented during the workshop.

OpenAQ
^^^^^^

`OpenAQ <https://openaq.org/>`_ is a platform and community that aggregates and shares open air quality data from around the world.

OpenAQ was co-founded by `Christa Hasenkopf <https://www.linkedin.com/in/christahasenkopfa>`_ and `Joe Flasher <https://www.linkedin.com/in/joeflasher>`_. Christa works full time on OpenAQ and Joe works part-time as the lead developer.

Notes
^^^^^

Day 1 - November 24, 2016
=========================

`Welcome, Workshop Goals,  Group Introductions <https://www.dropbox.com/s/0dhwd9jhng18lmj/1_Welcome.pptx?dl=0>`_
`````````````````````````````````````````````````````````````````````````````````````````````````````````````````

Folks at my table

* `Varun Jhaveri: <https://twitter.com/varun_jhaveri>`_ (IIC, University of Chicago)  Worked on `Chicago Sensor network <https://www.timeout.com/chicago/blog/chicago-has-started-installing-sensors-that-will-monitor-the-city-082916>`_. On a project to install a similar network in Delhi
* `Shijith <https://twitter.com/shijith>`_: Data Journalist at WION news. Interested in using open data to report on aur quality issues in Delhi
* `Gangadhar Sulkunte <https://in.linkedin.com/in/gangadharsulkunte>`_: Entrepreneur interested in DIY sensors. Launched a helium balloon
* `Nishad KA <http://www.urbanemissions.info/about>`_ : Research Associate at Urban Emissions. GIS-guy. Currently working on mapping of brick kilns to quantify their effect on air pollution. Uses Google Earth imagery to locate brick kilns.
* `Jay Kannaiyan <https://in.linkedin.com/in/jaykannaiyan>`_: Found of Smart Air Filters. Low cost DIY air purifiers. `Rode his motorcycle around the world <http://overdrive.in/features/jay-kannaiyans-ride-around-the-world-on-a-motorcycle/>`_  for 3 years!
* `Richie Ahuja <https://www.edf.org/people/richie-ahuja>`_: India director at Environmental Defence Fund. Interested in community engagement around air quality
* `Ayush Goel <https://twitter.com/named_none>`_: iOS developer and open data enthusiast

`Introducing the OpenAQ Platform + Community <https://www.dropbox.com/s/d2k5qripf9dp61j/2_IntroducingOpenAQ_Delhi2016.pptx?dl=0>`_
``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

Speakers: Christa Hasenkopf and Joe Flasher, OpenAQ  - 30 minutes

OpenAQ tagline: Fighting Air Inequality

Slide 4: Air Quality vs. GDP. Outliers are Qatar Bahrain UAE (high GDP - high pollution)

Slide 5: Research gap: Top 10 most polluted cities have published <40 papers (I didn’t quite agree with the premise that more research results in better air quality)

aqicn.org is the top aggregator. But can’t download data or programmatic access to historical data. That’s why openaq was started.

`Air Quality Landscape in Delhi <https://www.dropbox.com/s/rw58c631o828cqm/4_Guttikunda%20-%20OpenAQ.pptx?dl=0>`_
`````````````````````````````````````````````````````````````````````````````````````````````````````````````````

Speaker: Sarath Guttikunda, Urban Emissions

Need for more Epidemiology Studies to drive policy change. Health impact of air pollution at higher levels is not well understood.
`Public Health Foundation of India (PHFI) <https://www.phfi.org/>`_ and `Sri Ramachandra University <http://www.sriramachandra.edu.in/university/research.php?did=41>`_ leading studies in India on impact of air pollution on health

2 target audiences for AQ data. These 2 should never be mixed and always addressed separately

* Science & Policy - numbers, coverage of pollutants
* Public Awareness - Air quality index, healthy/unhealthy - lose severity from science perspective

There are 550 manual pollution measuring stations in India. They are manually measured and entered. Someone goes in daily, changes the filter, weights it and enters data manually. Large delay in publishing data - challenge for Journalists and reporting on old data is hard. Noone wants to know what happened a month ago. That’s why lack of media stories for cities other than Delhi even though the pollution levels are as bad.

60 stations are continuous monitoring stations and publishing real time data on CPCB website.

Sensors costs

* CPCB sensors costs ~ Rs 1 Crore (USD 150k). Measures all pollutants. Includes daily maintenance etc.
* US embassy sensors costs ~ Rs. 10 Lakh (USD 15k) but measures only PM2.5
* Low cost sensors range from Rs. 10k - 40k (USD 200 - 800) - measures only PM2.5 and PM10

Has there been any concrete policy change based on more data?

Urban Emissions `published a report <http://www.urbanemissions.info/emissions-india-coal-fired-power-plants/>`_ on health impact of coal power plants and lag in standards. `New stricter regulations <http://pib.nic.in/newsite/PrintRelease.aspx?relid=133726>`_ were adopted based on this report.

India Air Quality
`````````````````

Pallavi Pant, University of Mass - Amherst 

Runs the India Air Quality blog at https://indiaaq.wordpress.com/ and tweets at @airqualityindia

Air Quality in Rwanda
`````````````````````

Langley Dewitt, MIT, Kigali 

Measure air quality in Rwanda using bike-taxi drivers carrying sensors

Lunch
`````

Met Barun Aggarwal from Breathe Easy who makes air purifiers. Person behind the `Healthiest Building in India <http://www.business-standard.com/article/beyond-business/inside-new-delhi-s-healthiest-building-115121101134_1.html>`_ - Paharpur Business Centre. Barun also runs `Care for Air <http://www.careforair.org/>`_ non-profit that was a partner for this workshop.

What are some good low-cost air quality sensors one can buy?

`Laser Egg monitor <http://originstech.com/products/laser-egg/>`_ is the most popular. Namita (who was in the workshop) from `Airveda <http://www.airveda.com/>`_ produces one at Rs. 10k. Calibration is a challenge as it drifts over time. Their sensors have the ability to receive OTA calibration updates to account for this.

Building on Top of - Open Data
``````````````````````````````

Speakers: Joe Flasher, OpenAQ - 30 minutes

OpenAQ system architecture. Runs on Amazon CLoud

Big fan of Lambda functions. Reduces sysadmin work as no servers to be managed.

Openaq-fetch

Openaq-api

After fetch, kick of aggregations and stored in elasticache

Postgres data - 30M records

Daily CSV dump on S3

ROpenAQ
```````

Maelle Salmon

R package for openaq

`Smokey - The Air Quality Chatbot <https://www.dropbox.com/s/xpr5yvcd961g57q/8_Amrit_Smokey-OpenAQ-Presentation.pdf?dl=0>`_
```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

Amrit Sharma

Chatbot for FB, Twitter. Based on OpenAQ API. 


Day 2 - November 25, 2016
=========================

Indian Open Data Association
````````````````````````````

Mrutyunjay Mishra (M2)

Open Sandbox model - give open access to data and let developers play with it

`Open Environment Data Project <http://openenvironment.indiaopendata.com/#/dashboard/>`_ is a plotform to collect and disseminate open air quality data.

Have developed a affordable Do-it-Yourself (DiY) personal air quality (Dust SPM 2.5 & 10 micron) monitoring device called `AirOwl <http://openenvironment.indiaopendata.com/#/airowl/>`_  - open hardware and software

Also have an outdoor monitor called `EMK <http://knowledge.indiaopendata.com/index.php/India_Open_Environment_Data_Project#a.29_Environment_Monitoring_Kits>`_ which is aimed at replacing science-grade robust sensors. Brings down the cost from Rs 6 Cr (1M) to Rs. 3 Lakh (USD 50K). Deployed and tested at MIT-run `Kumbhathon <http://www.kumbha.org/>`_. 

Reporting on Air Quality at Hindustan Times
```````````````````````````````````````````

Ravi Suhag and Piyush Aggarwal

Putting in context: we breathe 11000 littres (3000 gallons) of air per day

Developed air quality portal at http://airquality.hindustantimes.com/ using data from CPCB (Central Pollution Control Board) and IndiaSpend (http://breathe.indiaspend.org/)

Pretty map visualization and historic data. Storytelling using data http://www.hindustantimes.com/static/pollution-india-five-charts
Developed their own scrapers and database since OpenAQ did not have historic data going back 5 years.

`Care for Air <http://www.careforair.org/>`_
`````````````````````````````````````````````

Jyoti Pande Lavakare and Barun Aggarwal

Small un-funded non-profit.

Advocacy in Schools - nudging kids to uses school buses instead of private cars. Why rich kids come in their own cars? So they can start late and reach home early. Disincentivize use of private cars by allowing buses to come in early and  start early. Car pickups need to come in early and go after school buses leave. 80% private car kids started using school buses.

Awareness in kids by presentations. Everyone loved the quote ``Don’t trust your senses, trust your sensors``

Partnered with the organization called `Jodo Gyan <http://jodogyan.org/>`_ that works on alternate Maths education in schools. 

They had filed a petition with supreme court to ban sale of firecrackers whose `verdict <http://indianexpress.com/article/india/india-news-india/sc-bans-sale-of-fire-crackers-in-delhi-ncr-4394657/>`_ came in as the workshop was in session!

`Airveda <http://www.airveda.com/>`_
````````````````````````````````````

Namita Gupta

Started by a mom who was faced with an asthmatic kid and no solution on how best to deal with air pollution in Delhi. Better data on indoor vs outdoor pollution levels, variations throughout the day and seasons helped her restrict outdoor play-time for her daughter and buy air purifiers that work to improve the air quality. Significant improvement over a year in the health of the child.

Developed low-cost sensor as well as outdoor weatherproof sensors

Advocacy by putting large air quality display outside Secretariat building in Delhi and at popular locations where politicians visit

`Hawa Badlo (ChangeTheAir) <http://changetheair.org/>`_
```````````````````````````````````````````````````````

Nipun Arora

Media organization working with OpenAQ data. Their mission is  ``Humanizing the Data``

Ran many campaigns to raise awareness about air quality. Funded by GAIL (Gas Authority of India Limited)
School have started acknowledging that air quality is a concern. Interest in measuring and improving air quality


Workshop Materials
==================

* `Presentations and Videos <https://medium.com/@openaq/delhi-openaq-workshop-info-materials-and-results-2bd74b88bee6#.3g0s0ebab>`_
* `Unconference Topics <https://medium.com/@openaq/delhi-openaq-unconference-brainstorm-6b9baf61d4aa#.nzehbio86>`_
* `Next steps identified by participants <https://docs.google.com/document/d/1W9q_lf68GOxP4ybmfgUcaS3CeDCx7Nm4A4CBI7NDD5E/edit>`_