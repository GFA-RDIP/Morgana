# Morgana

A data visualization tool to inspect complex datasets.

## Problem Owners

Dr. David Martino ([ResearchGate][8], [LinkedIn][9])

Dr. Jennifer Koplin ([ResearchGate][10], [LinkedIn][11])

Mr. Simon Christopher Cropper ([ResearchGate][12], [LinkedIn][13])

## Project Team

Edward Ross (back end, presentor, data wrangler)

Nicholas Roberts (front end, graphics, network analysis, project design)

Tung van Truong (UX design, marketing, presentation) ([LinkedIn][17])

Thanks for the assistance provided by Jarny Choi ([ResearchGate][14]) on initial analysis of the data and input into alternative design concepts. His iPython notebooks are included in the project directory.

Thanks also to Jagdish Sawlani ([LinkedIn][15], [Twitter][16]) for early input into the preperation of the data for analysis.

## HealthHack Melbourne 2016 Project Brief

Researchers working in clinical studies collect a lot of patient samples, laboratory and clinical data, and these are often collected independently of each other.

A major challenge is to easily see what data we have on whom. For example, we might have genetic data on 15% of our cohort, epigenetic measures on 35%, we will have collected flow cytometry data on 60% and serology on 100% of the cohort.

How can we aim to curb life-threatening diseases when the laboratory data we collect is not even remotely connected to clinical outcomes, and specimen data?

How can data stored in different incompatible systems be of any use to solving a research question?

There’s a severe need for an intuitive and interactive way to visualize relationships between different types of data collected in clinical studies.

We need to be able to examine this data in a myriad of scales and contexts, from a bird's eye view through to specific subgroups containing a half dozen specimens can inform this critical stage of research.

This project from the Murdoch Childrens Research Institute will utilize sample data from one of the worlds leading cohorts of paediatric food allergy, to develop a flexible, intuitive, visual solution to research data management.

Ideally, the solution would consist of an easily queried database (preferably SQL-based), providing data to a web frontend. Several excellent libraries exist for this purpose (e.g. [d3.js][5], [plot.ly][4]), though as is to be expected, the devil is in the details - gluing the various components together into a cohesive, user-friendly whole is the real challenge for this project.

If you think you can help us develop this tool, you’ll be working on a project that will make research teams more effective in combating life-threatening disease.

## Project development

Opportunities are being investigated on how to take a segment of the cohort data and represent relationships in the dataset for the selected participants in a natural and interactive way.

The initial cohort segment is selected using a dynamic sunburst diagram, which feeds a subset of the original matrix to either a table or network diagram that visually presents abundance and relationships between major attributes known about the participants. The tabulated view will provide the ability to export the list of selected participants, the filter field values and the values identified as being significant by the network analysis.

## Etymology of name

Named after the Arthurian sorceress Morgan le Fay, Fata Morgana or Morgana. Morgana is believed to have conjured the images of distant land or floating castles often seen in the Straits of Messina to lure unsuspecting sailors to their death.

Fata Morgana is an unusual and complex form of mirage where an object is significantly distorted and rapidly changes. The mirage can comprise of several inverted (upside down) and erect (right side up) that are stacked on top of one another. Fata Morgana are caused by rays of light being bent when passing through air layers of different temperatures in a steep thermal inversion where an atmospheric duct has formed.
[Wikipedia 2016 - Fata Morgana (mirage)][1]

> The analogy here is that Morgana the software will rapidly reformat and present complex almost indecyperable datasets in novel and informative ways so casual researchers are attracted to investigate further.

## Operating System

Morgana currently only operates under Linux.

## Prerequisites

Python 3
npm

## Installation

In most cases, pip install is sufficient:
  
	bash
	pip install -r backend/requirements.txt
	npm install -g bower

If using the anaconda/miniconda python distribution, use the provided environment.yml to setup an isolated environment containing the required dependencies:
	
	bash
	conda env create -f backend/morgana-env.yml
	source activate morgana-py3
	npm install -g bower


## Deployment (on UNIX like platforms)
	
	bash
	./run.sh

## Licenses

Software devloped under this project is being released under a [GNU General Public License, version 3 (GPL-3.0)][2] license.

Supportive documentation is released under a [Creative Commons Attribution 4.0 International (CC-BY)][3] license.

The sample dataset provided is released under a [ODC Open Database License (ODbL) version 1.0][6] license. Any rights in individual contents of the database are licensed under the [Database Contents License (DbCL) version 1.0][7].



[1]: https://en.wikipedia.org/wiki/Fata_Morgana_(mirage)
[2]: https://opensource.org/licenses/GPL-3.0
[3]: https://creativecommons.org/licenses/by/4.0/legalcode
[4]: http://plot.ly/
[5]: https://github.com/d3/d3
[6]: http://opendatacommons.org/licenses/odbl/1.0/
[7]: http://opendatacommons.org/licenses/dbcl/1.0/
[8]: https://www.researchgate.net/profile/David_Martino
[9]: https://au.linkedin.com/in/david-martino-812ab5b7
[10]: https://www.researchgate.net/profile/Jennifer_Koplin
[11]: https://au.linkedin.com/in/jennifer-koplin-6a085695
[12]: https://www.researchgate.net/profile/Simon_Cropper3
[13]: https://au.linkedin.com/in/simonchristophercropper
[14]: https://www.researchgate.net/profile/Jarny_Choi
[15]: https://au.linkedin.com/in/jagdishsawlani
[16]: https://twitter.com/jagdish_sawlani
[17]: https://au.linkedin.com/in/tungvantruong
