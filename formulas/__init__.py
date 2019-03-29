# -*- coding: utf-8 -*-

from .expr import *

from .ConstGamma import *
from .ConstPi import *
from .DedekindEta import *
from .Exp import *
from .GammaFunction import *
from .LegendrePolynomial import *
from .Log import *
from .PartitionsP import *
from .RiemannZeta import *
from .integrals import *
from .airy import *
from .stirling_numbers import *
from .gaussian_quadrature import *
from .general_functions import *
from .complex_plane import *
from .confluent_hypergeometric import *
from .error_functions import *
from .jacobi_theta import *

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

