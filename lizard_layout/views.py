# (c) Nelen & Schuurmans.  BSD licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateView


class ExampleView(TemplateView):
    """View, mostly for debugging the setup."""
    template_name = 'lizard_layout/example.html'
