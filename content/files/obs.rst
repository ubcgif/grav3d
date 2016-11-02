Observations file
~~~~~~~~~~~~~~~~~

This file is used to specify the observation locations and observed
gravity anomalies with estimated standard deviation. The output of the
forward modelling program has the same structure except that the column
of standard deviations for the error is omitted. The following is the
file structure of the observations file:

| \|ccccc\|
| E\ :math:`_1` & N\ :math:`_1` & ELEV\ :math:`_1` & Grav\ :math:`_1` &
  Err\ :math:`_1`
| E\ :math:`_2` & N\ :math:`_2` & ELEV\ :math:`_2` & Grav\ :math:`_2` &
  Err\ :math:`_2`
| & & & &
| E\ :math:`_{ndat}` & N\ :math:`_{ndat}` & ELEV\ :math:`_{ndat}` &
  Grav\ :math:`_{ndat}` & Err\ :math:`_{ndat}`

Parameter definitions:

-  Lines starting with ! are comments.

-  Number of observations.

-  Easting, northing and elevation of the observation, measured in
   meters. Elevation should be above the topography for surface data,
   and below the topography for borehole data. The observation locations
   can be listed in any order.

-  Anomalous gravity data, measured in mGal.

-  Standard deviation of Grav\ :math:`_n`. This represents the absolute
   error. It must be positive and non-zero.

**NOTE:** It should be noted that the data are **extracted anomalies**
which are derived by removing the regional from the field measurements.
Furthermore, the inversion program assumes that the anomalies are
produced by a density contrast distribution in g/cm\ :math:`^3` with
mesh cells in meters. Therefore, it is crucial that the data be prepared
in .

Example of an observations file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following are two examples of data files. The first example file
specifies a set of total field anomaly data, and the second example file
provides a set of multi-component borehole data.

| \|ccccl\|
| 0.00 & 0.00 & 1.00 & 0.174732E+02 & 0.598678E+01
| 0.00 & 50.00 & 1.00 & 0.265550E+02 & 0.613890E+01
| 0.00 & 100.00 & 1.00 & 0.311366E+02 & 0.629117E+01
| & & & &
| 1000.00 & 900.00 & 1.00 & -0.109595E+01 & 0.530682E+01
| 1000.00 & 950.00 & 1.00 & -0.902209E+01 & 0.523738E+01
| 1000.00 & 1000.00 & 1.00 & -0.397501E+01 & 0.518496E+01
