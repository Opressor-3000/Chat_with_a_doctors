__all__ = (
    "AccountPhone",
    "AccountID",
    "AccountLogin",
    "AccountUpdate",
    "AccountInfo",
    "AccountChangePassword",
    "CreateAccount",
    "DiagnosisDelete",
    "DiagnosisID",
    "DiagnosisUpdate",
    "GenderCreate",
    "GenderID",
    "GenderUpdate",
    "CreateUser",
    "UserID",
    "DiseaseID",
    "CreateDisease",
)

from .account import (
    CreateAccount, 
    AccountID, 
    AccountLogin,
    AccountUpdate,
    AccountInfo,
    AccountChangePassword,
)

from .diagnosis import (
    DiagnosisDelete,
    DiagnosisID,
    DiagnosisUpdate,
)
from .gender import (
    GenderID,
    GenderUpdate,
)
from .user import (
    UserID,
    CreateUser,
)
from .disease import (
    DiseaseID,
    CreateDisease,
)
