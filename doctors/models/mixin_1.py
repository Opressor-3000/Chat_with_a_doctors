from .mixin import DoctorRelationMixin, UserDocRelationMixin, UserDocSpecMixin
from chat.models.mixin_ import ChatUserCreaterRelationMixin, ChatRelationMixin
from chat.models.mixin import ChatUserRelationMixin



class DocChatUserCreaterMixin(DoctorRelationMixin, ChatUserCreaterRelationMixin):
    pass



class DocChatUserRelationMixin(ChatRelationMixin, UserDocRelationMixin):
    pass



class ChatUserDocRelationMixin(ChatUserRelationMixin, UserDocSpecMixin):
    pass
