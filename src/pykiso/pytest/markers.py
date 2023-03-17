##########################################################################
# Copyright (c) 2010-2023 Robert Bosch GmbH
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0.
#
# SPDX-License-Identifier: EPL-2.0
##########################################################################

"""
Markers
*******

:module: markers

:synopsis: define new pykiso-related markers.

.. currentmodule:: markers

"""

from _pytest.config import Config


def pytest_configure(config: Config):
    config.addinivalue_line(
        "markers",
        "test_ids(DUT1=[ABC123, DEF456], DUT2=[123ABC]): "
        "marker for test IDs or test-related requirements that will appear in the report",
    )
