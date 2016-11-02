Active cells file
~~~~~~~~~~~~~~~~~

This file is optional. The active cells file contains information about
the cells that will be incorporated into the inversion. It has exact
same format as the , and thus must be the same size, with one exception.
Values of this file are restricted to either -1, 0 or 1. By default, all
cells below the earth’s surface are active () and incorporated into the
inversion. Inactive cells are set to the values of the reference model
and influence the forward modelling. There are two kinds of inactive
cells:

-  cells that *do not* influence the model objective (set to ) and

-  cells that *do* influence the model objective function (set to ).

Cells that are defined as active and are solved for within the inversion
and are set to . The following is an example of an active cells file:

+------+-------------------+
| 0    |                   |
+------+-------------------+
| 0    | ! inactive cell   |
+------+-------------------+
+------+-------------------+
| 0    |                   |
+------+-------------------+
| 1    | ! active cell     |
+------+-------------------+
+------+-------------------+
| -1   | ! inactive cell   |
+------+-------------------+
+------+-------------------+
| 1    |                   |
+------+-------------------+
