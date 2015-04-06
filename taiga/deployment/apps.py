# Copyright (C) 2014 Andrey Antukh <niwi@niwi.be>
# Copyright (C) 2014 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014 David Barragán <bameda@dbarragan.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.apps import AppConfig
from django.db.models import signals

#from . import signal_handlers as handlers
from .api import DeploymentViewSet
from taiga.projects.history.models import HistoryEntry

# Register route
from taiga.contrib_routers import router
router.register(r"deployment", DeploymentViewSet, base_name="deployment")


def connect_taiga_deployment_signals():
    print('test')


class TaigaDeploymentAppConfig(AppConfig):
    name = "taiga.deployment"
    verbose_name = "Taiga Deployment App Config"

    def ready(self):
        print('test')
