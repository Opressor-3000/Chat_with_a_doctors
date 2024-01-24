from .mixin import UserDocRelationMixin, UserDocRelationMixin
from chat.models.mixin_ import ChatRelationMixin


class DocChatUserRelationMixin(ChatRelationMixin, UserDocRelationMixin):
    pass
