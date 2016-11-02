Background theory
=================

Introduction
------------

The GRAV3D suite of algorithms, developed at the UBC Geophysical Inversion Facility, is used to invert gravimetric responses over a three dimensional distribution of density contrast, or anomalous density. This manual is designed so that geophysicists who are familiar with the gravity experiment, but who are not necessarily versed in the details of inverse theory, can use the codes and invert their data. In the following, we describe the basics of the algorithm, but readers are referred to :cite:`LiOldenburg98` for an in-depth discussion of various aspects of the algorithm. Note that an understanding of these components is necessary for the user to have a global view of the algorithms and to use the program library to its fullest extent. 

A gravity experiment involves measuring the vertical components of the gravity field produced by anomalous (either excess or deficient) mass beneath the surface. A distribution of anomalous mass, characterized by anomalous density :math:`\rho(x, y, z)`, produces its own gravity field, :math:`\mathbf{g}_s`, which is superimposed on the ambient gravity field. By measuring the resultant field and removing the ambient field from the measurements through numerical processing, one obtains the field due to the anomalous mass.

The vertical component of the gravity field produced by the density :math:`\rho(x, y, z)` is given by

.. _gzfield_:

.. math:: g_z(\mathbf{r}_o)= \gamma\int\limits_V \rho(\mathbf{r})\frac{z-z_o}{\left | \mathbf{r}-\mathbf{r}_o \right |^3} dv,
    :label: gzfield


where :math:`\mathbf{r}_o = (x_o,y_o,z_o)` is the vector denoting the observation location and :math:`\mathbf{r} = (x,y,z)` is the source location. The volume of the anomalous mass is :math:`V` and :math:`\gamma` is the gravitational constant. Here we have adopted a Cartesian coordinate system having its origin on the earth's surface and the :math:`z-`\ axis pointing vertically downward. In the following, we outline the basics of the forward and inverse procedures used by the GRAV3D program library.

Forward Modelling
-----------------

Forward modelling of gravity data is a linear problem and can be carried out by performing the integration in equation [eq:gzfield]. We divide
the region of interest into a set of 3D prismatic cells by using a 3D orthogonal mesh and assume a constant density contrast within each cell. We discretize the density contrast model in this manner since it is best suited for our inversion methodology. Given such a discretization, the gravity field at the :math:`i^{th}` location can be written as:

.. _fwdata_:

.. math:: 
     \begin{aligned}
     d_i\equiv g_z(\mathbf{r}_{oi}) \\
     = \overset{M}{\underset{j=1}{\sum}}\rho_j\left \{ \gamma\int\limits_{\Delta V_j}\frac{z-z_o}{\left | \mathbf{r}-\mathbf{r}_{oi} \right |^3}dv \right \}, \\
     \equiv \overset{M}{\underset{j=0}{\sum}}\rho_j G_{ij}.
     \end{aligned}
     :label: fwdata


In equation :eq:`fwdata`, :math:`\rho_j` and :math:`\Delta V_j` are the anomalous density and volume of the :math:`j^{th}` cell, :math:`d_i` is introduced as a generic symbol for the :math:`i^{th}` datum, and :math:`G_{ij}`, defined by the expression in brackets, quantifies the contribution of the :math:`j^{th}` cell to the :math:`i^{th}` datum. The solution for the integral in equation :eq:`fwdata` can be found in :cite:`Nagy66` and we have adopted the solution by :cite:`Haaz53` here.

Inversion methodology
---------------------

Let the set of extracted anomaly data be :math:`\mathbf{d} = (d_1,d_2,...,d_N)^T` and the density contrast of cells in the model be :math:`\mathbf{\rho} = (\rho_1,\rho_2,...,\rho_M)^T`. The two are related by the sensitivity matrix

.. _sens_:
.. math::
     \mathbf{d}=\mathbf{G}\mathbf{\rho}.
     :label: sens

The matrix has elements :math:`g_{ij}` which quantify the contribution to the :math:`i^{th}` datum due to a unit density in the :math:`j^{th}` cell. The program performs the calculation of the sensitivity matrix, which is to be used by the subsequent inversion. The sensitivity matrix provides the forward mapping from the model to the data during the entire inverse process. We will discuss its efficient representation via the wavelet transform in a separate section. 

For the inversion, the first question that arises concerns definition of the "model". We choose density contrast, :math:`\rho`, as the model for since the anomalous field is directly proportional to the density contrast. The inverse problem is formulated as an optimization problem where a global objective function, :math:`\phi`, is minimized subject to the constraints in equation :eq:`sens`. The global objective functions consists of two components: a model objective function, :math:`\phi_m`, and a data misfit function, :math:`\phi_d`, such that

.. _globphi_:
.. math::
    \begin{aligned}
    \min \phi = \phi_d+\beta\phi_m \\
    \mbox{s. t. } \rho^l\leq \rho \leq \rho^u, \nonumber
    \end{aligned}
    :label: globphi

where :math:`\beta` is a trade off parameter that controls the relative importance of the model smoothness through the model objective function and data misfit function. When the standard deviations of data errors are known, the acceptable misfit is given by the expected value :math:`\phi_d` and we will search for the value of :math:`\beta` via an L-curve criterion :cite:`Hansen00` that produces the expected misfit. Otherwise, a user-defined value is used. Bound are imposed through the projected gradient method so that the recovered model lies between imposed lower (:math:`\rho^l`) and upper (:math:`\rho^u`) bounds.

We next discuss the construction of a model objective function which, when minimized, produces a model that is geophysically interpretable. The objective function gives the flexibility to incorporate as little or as much information as possible. At the very minimum, this function drives the solution towards a reference model :math:`\rho_o` and requires that the model be relatively smooth in the three spatial directions. Here we adopt a right handed Cartesian coordinate system with positive north and positive down. Let the model objective function be

.. _mof_:
.. math::
     \begin{aligned} \phi_m(\rho) &=& \alpha_s\int\limits_V w_s\left\{w(\mathbf{r})[\rho(\mathbf{r})-{\rho}_o] \right\}^2dv + \alpha_x\int\limits_V w_x \left\{\frac{\partial w(\mathbf{r})[\rho(\mathbf{r})-{\rho}_o]}{\partial x}\right\}^2dv \\ \nonumber
     &+& \alpha_y\int\limits_V w_y\left\{\frac{\partial w(\mathbf{r})[\rho(\mathbf{r})-{\rho}_o]}{\partial y}\right\}^2dv +\alpha_z\int\limits_V\ w_z\left\{\frac{\partial w(\mathbf{r})[\rho(\mathbf{r})-{\rho}_o]}{\partial z}\right\}^2dv, \end{aligned}
     :label: mof


where the functions :math:`w_s`, :math:`w_x`, :math:`w_y` and :math:`w_z` are spatially dependent, while :math:`\alpha_s`, :math:`\alpha_x`, :math:`\alpha_y` and :math:`\alpha_z` are coefficients, which affect the relative importance of different components in the objective function. The reference model is given as :math:`\rho_o` and :math:`w(\mathbf{r})` is a generalized depth weighting function. The purpose of this function is to counteract the geometrical decay of the sensitivity with the distance from the observation location so that the recovered density contrast is not concentrated near the observation locations. The details of the depth weighting function will be discussed in the next section.

The objective function in equation :eq:`mof` has the flexibility to incorporate many types of prior knowledge into the inversion. The reference model may be a general background model that is estimated from previous investigations or it will be a zero model. The reference model would generally be included in the first component of the objective function but it can be removed if desired from the remaining terms; often we are more confident in specifying the value of the model at a particular point than in supplying an estimate of the gradient. The choice of whether or not to include :math:`\rho_o` in the derivative terms can have significant effect on the recovered model as shown through the synthetic example. The relative closeness of the final model to the reference model at any location is controlled by the function :math:`w_s`. For example, if the interpreter has high confidence in the reference model at a particular region, he can specify :math:`w_s` to have increased amplitude there compared to other regions of the model. The weighting functions :math:`w_x`, :math:`w_y`, and :math:`w_z` can be designed to enhance or attenuate gradients in various regions in the model domain. If geology suggests a rapid transition zone in the model, then a decreased weighting on particular derivatives of the model will allow for higher gradients there and thus provide a more geologic model that fits the data.

Numerically, the model objective function in equation :eq:`mof` is discretized onto the mesh defining the density contrast model using a finite difference approximation. This yields:

.. _modobjdiscr_:
.. math::
    \begin{aligned}
    \phi_m(\mathbf{\rho}) = (\mathbf{\rho}-\mathbf{\rho}_o)^T(\alpha_s \mathbf{W}_s^T\mathbf{W}_s+\alpha_x \mathbf{W}_x^T\mathbf{W}_x+\alpha_y \mathbf{W}_y^T\mathbf{W}_y+\alpha_z \mathbf{W}_z^T\mathbf{W}_z)(\mathbf{\rho}-\mathbf{\rho}_o), \nonumber\\
    \equiv(\mathbf{\rho}-\mathbf{\rho}_o)^T\mathbf{W}_m^T\mathbf{W}_m(\mathbf{\rho}-\mathbf{\rho}_o), \nonumber\\
    =\left \| \mathbf{W}_m(\mathbf{\rho}-\mathbf{\rho}_o) \right \|^2,\end{aligned}
    :label: modobjdiscr


where :math:`\mathbf{\rho}` and :math:`\mathbf{\rho}_o` are :math:`M`-length vectors representing the recovered and reference models, respectively. Similarly, there is an option to remove to the reference model from the spatial derivatives in equation :eq:`modobjdiscr` such that

.. _modobjdiscrOut_:
.. math::
     \begin{aligned}
     \phi_m(\mathbf{\rho}) = (\mathbf{\rho}-\mathbf{\rho}_o)^T(\alpha_s \mathbf{W}_s^T\mathbf{W}_s)(\mathbf{\rho}-\mathbf{\rho}_o) + \mathbf{\rho}^T(\alpha_x \mathbf{W}_x^T\mathbf{W}_x+\alpha_y \mathbf{W}_y^T\mathbf{W}_y+\alpha_z \mathbf{W}_z^T\mathbf{W}_z)\mathbf{\rho}, \nonumber \\
     \equiv (\mathbf{\rho}-\mathbf{\rho}_o)^T\mathbf{W}_s^T\mathbf{W}_s(\mathbf{\rho}-\mathbf{\rho}_o) + \mathbf{\rho}^T\mathbf{W}_m^T\mathbf{W}_m\mathbf{\rho}, \nonumber\\
     =\left \| \mathbf{W}_s(\mathbf{\rho}-\mathbf{\rho}_o) + \mathbf{W}_m\mathbf{\rho}\right \|^2.
     \end{aligned}
     :label: modobjdiscrOut

In the previous two equations, the individual matrices :math:`\mathbf{W}_s`, :math:`\mathbf{W}_x`, :math:`\mathbf{W}_y`, and :math:`\mathbf{W}_z` are straight-forwardly calculated once the model mesh and the weighting functions :math:`w(\mathbf{r})` and :math:`w_s` , :math:`w_x`, :math:`w_y`, :math:`w_z` are defined. The cumulative matrix :math:`\mathbf{W}_m^T\mathbf{W}_m` is then formed for the chosen configuration.

The next step in setting up the inversion is to define a misfit measure. Here we use the :math:`l_2`-norm measure

.. _phid_:
.. math::
    \phi_d = \left\| \mathbf{W}_d(\mathbf{G}\mathbf{\rho}-\mathbf{d})\right\|^2.
    :label: phid

For the work here, we assume that the contaminating noise on the data is independent and Gaussian with zero mean. Specifying :math:`\mathbf{W}_d` to be a diagonal matrix whose :math:`i^{th}` element is :math:`1/\sigma_i`, where :math:`\sigma_i` is the standard deviation of the :math:`i^{th}` datum makes :math:`\phi_d` a chi-squared distribution with :math:`N` degrees of freedom. The optimal data misfit for data contaminated with independent, Gaussian noise has an expected value of :math:`E[\chi^2]=N`, providing a target misfit for the inversion. We now have the components to solve the inversion as defined in equation :eq:`globphi`.

To solve the optimization problem when constraints are imposed we use the projected gradients method :cite:`CalamaiMore87,Vogel02`. This technique forces the gradient in the Krylov sub-space minimization (in other words a step during the conjugate gradient process) to zero if the proposed step would make a model parameter exceed the bound constraints. The result is a model that reaches the bounds, but does not exceed them. This method is computationally faster than the log-barrier method because (1) model parameters on the bounds are neglected for the next iteration and (2) the log-barrier method requires the calculation of a barrier term. Previous versions of  used the logarithmic barrier method :cite:`Wright97,NocedalWright99`.

The weighting function is generated by the program that is in turn given as input to the sensitivity generation program . This gives the user full flexibility in using customized weighting functions. This program allows user to specify whether to use a generalized depth weighting or a distance-based weighting that is useful in regions of largely varying topography. Distance weighting is required to be used when borehole data are present.

Depth Weighting and Distance Weighting
--------------------------------------

It is a well-known fact that vertical gravity data have no inherent depth resolution. A numerical consequence of this is that when an inversion is performed, which minimizes :math:`\int m(\mathbf{r})^2 dv`, subject to fitting the data, the constructed density contrast is concentrated close to the observation locations. This is a direct manifestation of the kernel's decay with the distance between the cell and observation locations. Because of the rapidly diminishing amplitude, the kernels of gravity data are not sufficient to generate a function, which possess significant structure at locations that are far away from observations. In order to overcome this, the inversion requires a weighting to counteract this natural decay. Intuitively, such a weighting will be the inverse of the approximate geometrical decay. This give cells at all locations equal probability to enter into the solution with a non-zero density contrast.

../../commonTex/depthDistWeight.tex


