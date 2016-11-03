.. _gravfile:

Observations file
=================

This file is used to specify the observed gravity anomalies with estimated standard deviation. The output of the forward modelling program GZFOR3D has the same structure except that the column of standard deviations for the error is omitted. Lines starting with ! are comments. The following is the GIF-formatted file structure of a gravity observations file:

.. figure:: ../../images/gravObs.png
    :align: center
    :figwidth: 50%

Parameter definitions:

-  ndat: Number of observations.

-  E, N, ELEV: Easting, northing and elevation of the observation, measured in
   meters. Elevation should be above the topography for surface data,
   and below the topography for borehole data. The observation locations
   can be listed in any order.

-  Grav :math:`_i`: Anomalous gravity of ith datum measured in mGal.

-  Err :math:`_i`: Standard deviation of Grav\ :math:`_n`. This represents the absolute
   error. It must be positive and non-zero.

**NOTE:** It should be noted that the data are **extracted anomalies**, which are derived by removing the regional from the field measurements. Furthermore, the inversion program assumes that the anomalies are produced by a density contrast distribution in g/cm :math:`^3` with mesh cells in meters. Therefore, it is crucial that the data be prepared in ``mGal``.


.. _gravPreFile:

Predicted data file
-------------------

The predicted data file is the exact same format as above, but omitting the uncertainty column. The forward modelling and inversion code will output the predicted data in this format.

.. _gravLocFile:

Locations file
--------------

The locations file is the exact same format as above, but omitting the gravity data and uncertainty columns. The forward modelling code will read in locations even when the gravity anomaly (and uncertainties) are given.


Example 
-------

.. figure:: ../../images/gravObsEx.png
    :align: center
    :figwidth: 50%



