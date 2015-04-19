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

from rest_framework import serializers
from taiga.base.serializers import JsonField
from taiga.projects.attachments.admin import AttachmentInline

from . import models


class HistoryEntrySerializer(serializers.ModelSerializer):
    diff = JsonField()
    snapshot = JsonField()
    values = JsonField()
    values_diff = JsonField()
    user = JsonField()
    delete_comment_user = JsonField()

    class Meta:
        model = models.HistoryEntry

