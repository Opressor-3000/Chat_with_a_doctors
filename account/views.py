from fastapi import APIRouter

router = APIRouter(prefix="/account", tags=["account"])



@router.post("/")
async def create_user():
    pass


@router.put('/')
async def update_account():
    pass 


@router.get('/chat/{chat_id}')
async def get_chats():
    pass


@router.get('/docs')
async def get_docs():
    pass


@router.get('doc/{doc_id}')
async def get_doc():
    pass


@router.get('/feedbacks')
async def get_feedback():
    pass


@router.get('/feedback/{feedback_id}')
async def get_feedback():
    pass


@router.patch('feedback/{feedback_id}')
async def putch_feedback():
    pass


@router.post('/support')
async def create_issue():
    pass
