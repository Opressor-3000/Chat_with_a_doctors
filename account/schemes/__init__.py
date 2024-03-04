__all__ = (
    "AccountPhone",
    "AccountID",
    "AccountLogin",
    "AccountUpdate",
    "CreateAccount",
    "ChangePassword",
    "AnamnesisID",
    "AnamnesisDelete",
    "AnamnesisUpdate",
    "DiagnosisDelete",
    "DiagnosisID",
    "DiagnosisUpdate",
    "GenderCreate",
    "GenderID",
    "GenderUpdate",
    "UserCreate",
    "UserID",
    "DiseaseID",
    "CreateDisease",
)

from .account import (
    CreateAccount, 
    AccountID, 
    AccountLogin,
    AccountUpdate,
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
)
from .disease import (
    DiseaseID,
    CreateDisease,
)
