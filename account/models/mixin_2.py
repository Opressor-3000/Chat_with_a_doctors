from .mixin import UserRelationMixin
from admin.models.mixin import CreaterRelationMixin


class UserCreaterRelationMixin(UserRelationMixin, CreaterRelationMixin):
   pass