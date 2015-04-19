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

#from . import signal_handlers as handlers
from taiga.projects.deployments.api import DeploymentViewSet

# Register route
from taiga.contrib_routers import router
router.register(r"deployments", DeploymentViewSet, base_name="deployments")


def connect_taiga_deployment_signals():
    pass


class DeploymentsAppConfig(AppConfig):
    name = "taiga.projects.deployments"
    verbose_name = "Taiga Deployment App Config"

    def ready(self):
        print('test')
