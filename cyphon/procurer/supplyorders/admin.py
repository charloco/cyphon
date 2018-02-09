# -*- coding: utf-8 -*-
# Copyright 2017-2018 Dunbar Security Solutions, Inc.
#
# This file is part of Cyphon Engine.
#
# Cyphon Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# Cyphon Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
"""
Customizes admin pages for |SupplyOrders|.

==================================  =========================================
Class                               Description
==================================  =========================================
:class:`~SupplyOrderAdmin`          Creates admin pages for |SupplyOrders|.
==================================  =========================================

"""

# third party
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# local
from .models import SupplyOrder


@admin.register(SupplyOrder)
class SupplyOrderAdmin(admin.ModelAdmin):
    """Customizes admin pages for SupplyOrders."""

    list_display = [
        'id',
        'procurement',
        'user',
        'alert',
    ]
    list_display_links = ['id', 'procurement']
    fieldsets = (
        (_('Request Info'), {
            'fields': (
                'user',
                'created_date',
                'procurement',
                'alert',
            ),
        }),
        (_('Data'), {
            'classes': ('pre', ),
            'fields': (
                'input_data',
                'distillery',
                'doc_id',
                'result',
            ),
        }),
    )
    readonly_fields = [
        'procurement',
        'user',
        'alert',
        'input_data',
        'distillery',
        'doc_id',
        'result',
        'created_date',
    ]