from account.models.mixin_2 import UserCreaterRelationMixin
from .mixin import ChatRelationMixin



class ChatUserCreaterRelationMixin(UserCreaterRelationMixin, ChatRelationMixin):
    pass