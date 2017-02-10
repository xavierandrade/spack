##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install qball
#
# You can edit this file again by typing:
#
#     spack edit qball
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Qball(AutotoolsPackage):
    """Qball is a first-principles molecular dynamics code that is used to compute the electronic structure of atoms, molecules, solids, and liquids within the Density Functional Theory (DFT) formalism. It is a fork of the Qbox code by Francois Gygi."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/LLNL/qball/"
    url      = "https://github.com/LLNL/qball/archive/master.zip"

    version('master', git='https://github.com/LLNL/qball.git')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    # FIXME: Add additional dependencies if required.
    depends_on('blas')
    depends_on('gsl')
    depends_on('lapack')
    depends_on('mpi')
    depends_on('fftw')
    depends_on('scalapack')

    def autoreconf(self, spec, prefix):
        # FIXME: Modify the autoreconf method as necessary
        autoreconf('--install', '--verbose', '--force')
        
    def configure_args(self):        
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        args.extend([
            'CC=%s' % self.spec['mpi'].mpicc,
            'CXX=%s' % self.spec['mpi'].mpicxx,
            'FC=%s' % self.spec['mpi'].mpifc,
            '--with-blacs=%s' % self.spec['scalapack'].scalapack_libs
        ])
        return args

