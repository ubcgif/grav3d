Weights file
~~~~~~~~~~~~

This file supplies the user-based weights that acts upon the model
objective function. Each set of weights correspond to the functions
(e.g., :math:`w_x`) given in equation [eq:mof]. For ease, the weights in
geographic coordinates are provided by the user. The following is the
file structure is for the weights file:

+-------------------------+------------------+------------------------------+
| W.S\ :math:`_{1,1,1}`   | :math:`\cdots`   | W.S\ :math:`_{NN,NE,NZ}`     |
+-------------------------+------------------+------------------------------+
| W.E\ :math:`_{1,1,1}`   | :math:`\cdots`   | W.E\ :math:`_{NN,NE-1,NZ}`   |
+-------------------------+------------------+------------------------------+
| W.N\ :math:`_{1,1,1}`   | :math:`\cdots`   | W.N\ :math:`_{NN-1,NE,NZ}`   |
+-------------------------+------------------+------------------------------+
| W.Z\ :math:`_{1,1,1}`   | :math:`\cdots`   | W.Z\ :math:`_{NN,NE,NZ-1}`   |
+-------------------------+------------------+------------------------------+

Parameter definitions:

-  Cell weights for the smallest model component (equation[eq:mof]).

-  Cell weights for the interface perpendicular to the easting
   direction.

-  Cell weights for the interface perpendicular to the northing
   direction.

-  Cell weights for the interface perpendicular to the vertical
   direction.

Within each part, the values are ordered in the same way as in ,
however, they can be all on one line, or broken up over several lines.
Since the weights for a derivative term are applied to the boundary
between cells, the weights have one fewer value in that direction. For
instance, the weights for the derivative in easting direction has
values, whereas the number of cells is .

If the surface is supplied, the cell weights above the surface will be
ignored. It is recommended that these weights be assigned a value of to
avoid confusion. If is entered instead of the weights file, then all of
the cell weights will be set equal ().
