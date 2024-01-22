from .mixin import DoctorRelationMixin, UserDocRelationMixin, UserDocRelationMixin
from chat.models.mixin_ import ChatUserCreaterRelationMixin, ChatRelationMixin
from chat.models.mixin import ChatUserRelationMixin
from account.models.mixin import CreaterRelationMixin


class DocChatUserCreaterMixin(DoctorRelationMixin, ChatUserCreaterRelationMixin):
    pass



class DocChatUserRelationMixin(ChatRelationMixin, UserDocRelationMixin):
    pass



class ChatUserCreaterRelationMixin(ChatUserRelationMixin, CreaterRelationMixin):
    pass
