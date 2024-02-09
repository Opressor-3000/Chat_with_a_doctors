from .mixin import DoctorRelationMixin
from chat.models.mixin import ChatUserRelationMixin
from admin.models.mixin import CreaterRelationMixin


class ChatUserCreaterRelationMixin(ChatUserRelationMixin, CreaterRelationMixin):
    pass


class DocChatUserCreaterMixin(DoctorRelationMixin, ChatUserCreaterRelationMixin):
    pass
