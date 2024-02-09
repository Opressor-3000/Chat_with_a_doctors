from .mixin import UserDocRelationMixin, UserDocRelationMixin
from chat.models.mixin import ChatRelationMixin


class DocChatUserRelationMixin(ChatRelationMixin, UserDocRelationMixin):
    pass
