Model file
~~~~~~~~~~

This file contains the cell values of the density contrast  model. The
density contrast  must have values in g/cm\ :math:`^3`  units. The , , ,
, and models must be in this format. Likewise, the model files will be
in this format. The following is the file structure of the model file

+-----------------------------+----+
| :math:`{\rho}_{1,1,1}`      |    |
+-----------------------------+----+
| :math:`{\rho}_{1,1,2}`      |    |
+-----------------------------+----+
+-----------------------------+----+
| :math:`{\rho}_{1,1,NZ}`     |    |
+-----------------------------+----+
| :math:`{\rho}_{1,2,1}`      |    |
+-----------------------------+----+
+-----------------------------+----+
| :math:`{\rho}_{1,j,k}`      |    |
+-----------------------------+----+
+-----------------------------+----+
| :math:`{\rho}_{NN,NE,NZ}`   |    |
+-----------------------------+----+

Each :math:`{\rho}_{i,j,k}` is density contrast at the
:math:`[i,j,k]^{\mbox{th}}` model cell.

-  Density contrast in cell :math:`[i, j, k]`. The density contrast is
   always in g/cm\ :math:`^3` units. The property is density *contrast*
   and therefore can be positive or negative.

:math:`[i, j, k]=[1, 1, 1]` is defined as the cell at the top,
south-west corner of the model. The total number of lines in this file
should equal , where is the number of cells in the north direction, is
the number of cells in the east direction, and is the number of cells in
the vertical direction. The model ordering is performed first in the
:math:`z-`\ direction (top-to-bottom), then in the easting, and finally
in the northing.
