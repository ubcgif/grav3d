.. _gzfor3d:

GZFOR3D
=======

This program performs forward modelling. Command line usage:

``gzfor3d mesh.msh obs.loc model.den [topo.dat]``

and will create the forward modelled data file ``gzfor3d.grv``.

Input files
-----------

All files are in ASCII text format - they can be read with any text editor. Input files can have any name the user specifies. Details for the format of each file can be found in :ref:`elements`. The files associated with GZFOR3D are:

- ``mesh.msh``: The 3D :ref:`mesh <meshfile>`.

- ``obs.loc``: The observation :ref:`locations <gravfile>`.

- ``model.den``: The density contrast :ref:`model <modelfile>` in g/cc.

- ``topo.dat``: Surface :ref:`topography <topofile>` (optional). If omitted, the surface will be treated as being flat and the top of the 3D mesh.

Output file
-----------

The created file is ``gzfor3d.grv``. The file format is that of the :ref:`data file <gravfile>` without the associated standard deviations. The forward modelled data are in **mGal**.

