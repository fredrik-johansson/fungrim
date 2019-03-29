# -*- coding: utf-8 -*-

from .expr import *

from .const_gamma import *
from .pi import *
from .dedekind_eta import *
from .exp import *
from .gamma import *
from .legendre_polynomial import *
from .log import *
from .partitions import *
from .riemann_zeta import *
from .integrals import *
from .airy import *
from .stirling_numbers import *
from .gaussian_quadrature import *
from .general_functions import *
from .complex_plane import *
from .confluent_hypergeometric import *
from .error_functions import *
from .jacobi_theta import *
from .weierstrass_elliptic import *

entries_dict = {}
for entry in all_entries:
    if entry.id() in entries_dict:
        raise ValueError("duplicated ID %s" % entry.id())
    entries_dict[entry.id()] = entry

topics_dict = {}
for topic in all_topics:
    if topic.title() in topics_dict:
        raise ValueError("duplicated title %s" % topic.title())
    topics_dict[topic.title()] = topic

