# Morgana

A data visualization tool to inspect complex datasets.

## Project Team

Simon Christopher Cropper (project coordinator, design) ([ResearchGate][12], [LinkedIn][13])

Edward Ross (back end, data wrangler)

Nicholas Roberts (front end, graphics, network analysis, design)

Tung van Truong (UX design, marketing, presentation) ([LinkedIn][17])

Jarny Choi (design, analysis) ([ResearchGate][14])

## Project origins and mission statement

Morgana is a program designed to be an intuitive and interactive way to visualize relationships between different types of data. It was proposed as a problem worth consideration at the Open Knowledge event "HealthHack 2016 (Melbourne)" by the Gastro & Food Allergy Group of Murdoch Childrens Research Institute. A team was formed at that event and the team that created the initial prototype won first prize.

The basic premise of Morgana is that complex data can be difficult to visualise, and there is a need for a tool to intuitively and interactively visualise groups within a larger dataset and quickly ascertain relationships between different types of data in that group. The tool is not considered to be a analysis package but rather a tool for exploring or interrogating the data.

Here is a short demo of the program created during HealthHack 2016 (Melbourne) showing pertinent features of the interface.

<img src="/images/Morgana.gif" alt="Morgana Demo" width="500">

## Etymology of name

Named after the Arthurian sorceress Morgan le Fay, Fata Morgana or Morgana. Morgana is believed to have conjured the images of distant land or floating castles often seen in the Straits of Messina to lure unsuspecting sailors to their death.

Fata Morgana is an unusual and complex form of mirage where an object is significantly distorted and rapidly changes. The mirage can comprise of several inverted (upside down) and erect (right side up) that are stacked on top of one another. Fata Morgana are caused by rays of light being bent when passing through air layers of different temperatures in a steep thermal inversion where an atmospheric duct has formed.
[Wikipedia 2016 - Fata Morgana (mirage)][1]

> The analogy here is that Morgana the software will rapidly reformat and present complex almost indecipherable datasets in novel and informative ways so casual researchers are attracted to investigate further.

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

Software developed under this project is being released under a [GNU General Public License, version 3 (GPL-3.0)][2] license.

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
