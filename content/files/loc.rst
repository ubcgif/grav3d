Locations file
~~~~~~~~~~~~~~

This file is used to specify the observation locations specifically for
the forward modelling of gravity data. The following is the general file
structure:

| \|lcc\|
| E\ :math:`_1` & N\ :math:`_1` & ELEV\ :math:`_1`
| E\ :math:`_2` & N\ :math:`_2` & ELEV\ :math:`_2`
| :math:`\vdots` & :math:`\vdots` & :math:`\vdots`
| E\ :math:`_{ndat}` & N\ :math:`_{ndat}` & ELEV\ :math:`_{ndat}`

Parameter definitions:

-  Lines starting with ! are comments.

-  Number of observations.

-  Easting, northing and elevation of the observation, measured in
   meters. Elevation should be above the topography for surface data,
   and below the topography for borehole data. The observation locations
   can be listed in any order.

Easting, northing, and elevation information should be in the same
coordinate system as defined in the mesh.

Example of a locations file
~~~~~~~~~~~~~~~~~~~~~~~~~~~

An example file is provided below. The file is for calculating an
anomaly at 441 stations. Although this is all surface data, borehole
data are incorporated by giving the :math:`x,y,z` location.

| \|lcc\|
| 0.00 & 0.00 & 1.00
| 0.00 & 50.00 & 1.00
| 0.00 & 100.00 & 1.00
| & &
| 1000.00 & 900.00 & 1.00
| 1000.00 & 950.00 & 1.00
| 1000.00 & 1000.00 & 1.00
