**EGM722 Assignment**

1. **Setup / Installation**

**1.1 Getting Started**

To get started you will need to download and install the latest versions of **git** and **Anaconda**.

These can be located at following links:

- [git](https://git-scm.com/downloads)
- [Anaconda](https://docs.anaconda.com/anaconda/install/)

There is also a git desktop application that is required to clone the relevant repository to computer, this can be downloaded from the following link:

- [GitHub Desktop](https://desktop.github.com/)

Also, to run the Python Script that is stored within the repository you will need to download an IDE, there is a number of this software readily available online but the one that I had used within this piece of work is PyCharm, download URL link can be found at:

- [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)

Be sure to download the **Community Edition** as it is free and open source

2. ` `**Clone Repository**

Once you have installed GitHub desktop then to clone this repository you go to **File > Clone repository.**

Click on the **URL** tab, then enter the link below:

<https://github.com/SeamusOg/EGM722-Assignment.git>

Save this to local folder which you will be working on.

**1.3 Create an Anaconda Environment**

To create and Anaconda Environment, we first open Anaconda Navigator that installed at the start of the process. Once the application is opened if click on the **“Environments”** tab on the left-hand side of screen then using the import from bottom of the panel and will be able to point to the environment file that was cloned as part of the repository above.

**1.4 Data**

This test data was sourced from a local Water Authority, due to the amount of data that is held in the original shapefiles it was decided that using a subset of this would give the opportunity to evaluate the usability of using python as a tool for quicker efficient analysis of the data:

- **Derg Strabane DMAs** – DMAs (District Metered Areas) are polygons designed so that the water authority can shut down an area of water network if a problem arises. They are determined by specific closed valves on the ground which turn on and off when required, they also have a Meter at a part of the polygon so they can measure the flow of water in this area.
- **Address Points** – Point feature that is assigned to every address within Northern Ireland.

