# Copyright (C) 2015 David Strejc <david.strejc@gmail.com>
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

from taiga.base import filters
from taiga.base.api import ModelCrudViewSet

from taiga.projects.deployments import serializers, models
from . import permissions


class DeploymentViewSet(ModelCrudViewSet):
    model = models.Deployment
    serializer_class = serializers.DeploymentSerializer
    permission_classes = (permissions.DeploymentPermission,)
    filter_backends = (filters.IsProjectAdminFilterBackend,)

