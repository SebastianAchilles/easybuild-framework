##
# Copyright 2015-2016 Ghent University
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# the Hercules foundation (http://www.herculesstichting.be/in_English)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
##

"""
Abstract implementation of a package naming scheme.

@author: Robert Schmidt (Ottawa Hospital Research Institute)
@author: Kenneth Hoste (Ghent University)
"""
from abc import ABCMeta, abstractmethod
from vsc.utils import fancylogger

from easybuild.tools.config import build_option


class PackageNamingScheme(object):
    """Abstract class for package naming schemes"""
    __metaclass__ = ABCMeta

    def __init__(self):
        """initialize logger."""
        self.log = fancylogger.getLogger(self.__class__.__name__, fname=False)

    @abstractmethod
    def name(self, ec):
        """Determine package name"""
        pass

    @abstractmethod
    def version(self, ec):
        """Determine package version."""
        pass

    def release(self, ec=None):
        """Determine package release"""
        return build_option('package_release')