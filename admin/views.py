from fastapi import APIRouter


router = APIRouter(prefix='/admin', tags=['Admin'])


#  --------   ALL STATICTICS   -----------

@router.get('/online_statistic/')
async def get_online_statistic():
    '''
        count user online type INT
`       count docotor online Type INT
        count current_chat
        count all account
        count all user 
        count all doctor
    '''
    pass


@router.get('/users_online/')
async def get_online_user_list():
    '''
        online statistic data filters and sort
            1. list user.username  online  
    '''
    pass


@router.get('/online_doctors/')
async def get_online_doctors():
    '''
        online statistic data with filter and sort 
            1. list doctor.account_id.last name, first_name  online 
    '''
    pass


@router.get('/current_chats/')
async def current_chats():
    '''
        all current chats data filters and sort 
    '''
    pass


##################################   MODERATORS    ##########################################



#  --------------   ACTIVATE / DEACTIVATE   ---------------


@router.get('/users/')
async def get_all_users_list():
    '''
        get all user list
            1. user.username  
    '''
    pass

# @router.get('/{user_id}/')
# async def get_panel():
#     '''
#         online? last_entres? userdata, chats, doctors, feedbacks, ratings
#     '''
#     pass


@router.patch('/{user_id}/')
async def user_active():
    '''
        is_active true/false
            1. return user
            2. form update user.is_active checkbox
    '''
    pass


@router.get('/{message_id}/')
async def get_message():
    pass


@router.patch('/{message_id}/')
async def message_banned():
    pass


# --------------------   ACCOUNT    --------------------


@router.get('/accounts/')
async def get_accounts():
    '''
        get all account and count account data
    '''
    pass


@router.get('/{account_id}/')
async def get_account():
    '''
        all data of account filter and sort
    '''
    pass


@router.patch('/{account_id}/')
async def account_deactivate():
    pass


@router.get('/{doctor_id}/')
async def get_doctor():
    '''
        all data of doctor filter and sort
    '''
    pass


@router.patch('/{doctor_id}/')
async def doctor_deactivate():
    pass    


#    --------------   CRUD  ------------------


@router.post('/doctor/')
async def create_doctor():
    pass


@router.get('/cerificates/')
async def get_certificates():
    '''
        get all certificate filter and sort
    '''
    pass


@router.post('/certificate/')
async def create_certificate():
    pass


###################################    ADMOINS    ######################################


@router.get('/specialities/')
async def get_specialities():
    pass


@router.post('/{speciality_id}/')
async AccountID_speciality():
    pass


@router.patch('/{speciality_id}/')
async def update_speciality():
    pass


#    ------------    PERMISSION     ---------------


@router.post('/permission/')
async def create_permission():
    pass


@router.delete('/{permission_id}/')
async def permission_delete():
    pass


@router.patch('/{permission_id}/')
async def permission_active():
    '''
        deactivate permission 
    '''
    pass


#   -----------------   GROUP   -------------------


@router.get('/groups/')
async def get_groups():
    '''
        get all group , group accesses, groups permissions , permissions account, 
    '''
    pass


@router.post('/group/')
async def create_group():
    pass


@router.get('/{group_id}/')
async def get_group():
    '''
        get access group
    '''
    pass


@router.get('/{group_id}/user_list/')
async def get_group_employees():
    pass


@router.patch('/{group_id}/')
async def group_active():
    '''
        edit group name and access group
    '''
    pass


@router.post('/accessgroup/')
async def create_access_group():
    pass


@router.delete('/{accessgroup_id}/')
async def delete_accessgroup():
    pass


@router.post('/qr/')
async def create_qr():
    pass

