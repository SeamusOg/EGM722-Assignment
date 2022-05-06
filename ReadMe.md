**EGM722 Assignment**

**1. Getting started**

To get started you will need to download and install the latest versions of **git** and **Anaconda**.

These can be located at:

- [git](https://git-scm.com/downloads)
- [Anaconda](https://docs.anaconda.com/anaconda/install/) 

There is also a git desktop application that will be required to clone the relevant repository to computer, this can be accessed at:

- [GitHub Desktop](https://desktop.github.com/)

Also to run the Python Script that is stored within the repository you will need to download an IDE, there is a number of ones available online but the one that I had used within this piece of work is PyCharm, download link can be found at:

- [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)

Be sure to download the **Community Edition** as it’s free and open-source

**2. Clone Repository**

Once you have installed GitHub desktop then to clone this repository you go to **File > Clone repository.**

Click on the **URL** tab, then enter the link below:

<https://github.com/SeamusOg/EGM722-Assignment.git>

Save this to local folder which you will be working on.

**3. Create an Anaconda Environment**

To create and Anaconda Environment, we first open Anaconda Navigator that installed at the start of the process.  Once application is opened if click on the **“Enivornments”** tab on the left hand side of screen then using the import from bottom of the panel and will be able to point to the environment.yml file that was cloned as part of the repository above.

**4. Data**

This test data was sourced from a local Water Authority, it is a subset of a larger set of data they hold and is intended to test the usability of using python as a tool for quicker efficient analysis, the data :

- **Derg Strabane DMAs** – DMAs (District Metered Areas) are polygons designed so that the water authority can shutdown an area of water network if a problem arises.  They are determined by specific closed valves on the ground which turn on and off when required, they also have a Meter at a part of the polygon so they can measure the flow of water in this area.  
- **Address Points** – Are points assigned to addresses, every address in Northern Ireland is assigned a point.

