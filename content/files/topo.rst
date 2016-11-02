.

Topography file
~~~~~~~~~~~~~~~

This optional file is used to define the surface topography of the 3D
model by the elevation at different locations. The topography file has
the following structure:

+-----------------+-----------------+--------------------+
| !               | comment         |                    |
+-----------------+-----------------+--------------------+
| npt             |                 |                    |
+-----------------+-----------------+--------------------+
| E\ :math:`_1`   | N\ :math:`_1`   | ELEV\ :math:`_1`   |
+-----------------+-----------------+--------------------+
| E\ :math:`_2`   | N\ :math:`_2`   | ELEV\ :math:`_2`   |
+-----------------+-----------------+--------------------+
+-----------------+-----------------+--------------------+
| E\ :math:`_n`   | N\ :math:`_n`   | ELEV\ :math:`_n`   |
+-----------------+-----------------+--------------------+

Parameter definitions:

-  Top lines starting with ! are comments.

-  Number of points defining the topographic surface.

-  Easting of the :math:`i^{th}` point on the surface.

-  Northing of the :math:`i^{th}` point on the surface.

-  Elevation of the :math:`i^{th}` point on the profile.

The lines in this file can be in any order as long as the total number
is equal to . The topographic data need not be supplied on a regular
grid.  assumes a set of scattered points for generality and uses
triangulation-based interpolation to determine the surface elevation
above each column of cells. To ensure the accurate discretization of the
topography, it is important that the topographic data be supplied over
the entire area above the model and that the supplied elevation data
points are not too sparse.

Example of topography file
~~~~~~~~~~~~~~~~~~~~~~~~~~

The following is an example of a topography file:

+------------+-----------+----------------+
| 2007       |           |                |
+------------+-----------+----------------+
| 12300.00   | 9000.00   | 0.109411E+04   |
+------------+-----------+----------------+
| 12300.00   | 9025.00   | 0.109545E+04   |
+------------+-----------+----------------+
| 12300.00   | 9050.00   | 0.109805E+04   |
+------------+-----------+----------------+
| 12300.00   | 9075.00   | 0.110147E+04   |
+------------+-----------+----------------+
| 12300.00   | 9100.00   | 0.110555E+04   |
+------------+-----------+----------------+
| 12300.00   | 9125.00   | 0.111011E+04   |
+------------+-----------+----------------+
| 12300.00   | 9150.00   | 1114.9         |
+------------+-----------+----------------+
| 12300.00   | 9175.00   | 0.111971E+04   |
+------------+-----------+----------------+

**NOTE**: Only the cells completely below the (interpolated) topographic
surface are kept. The cells above or at the topographic surface are
removed from the model, although these must still be included in the as
if they are a part of the model. For input model files these cells can
be assigned any value. The recovered model produced by inversion program
also includes the cells that are excluded from the model, but these
cells will have unrealistic values and be set at .
