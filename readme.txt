


git checkout yusif 
&& 
git add . && git commit -m 'install pydantic-settings' 
&& 
git push origin yusif 
&& 
git checkout dev && git merge origin yusif && git checkout yusif 

run server 

uvicorn main:app --reload 


my_account
    account.first_name
    account.last_name
    account.email
    account.phone
    account.specialities
    account.accesses



список сообщений пользователя из всех чатов
    message.text
    message.created_at
    user.id
список всех чатов по дате создания
    list[
        chat.doctor.account.last_name
        chat.doctor.account.first_name
        chat.speciality.title
        chat.created_at
    ]
список врачей с кем был чат у пользователя
    list[
        doctor.account.last_name
        doctor.account.first_name
    ]
имя фамилия врача в текущем чате
    chat.doctor.last_name
    chat.doctor.first_name
кол-во чатов с врачебной специализацией
    count:int
список чатов c врачом
    
список чатов по специальностям врача

список отзывов пользователя
средний рейтинг врача за текущий день
    rating: int
кол-во чатов с пациентами за текущий день по специальностям
    chat_count: int
доступы пользователя для администрирования 

специализации врача

сертификаты врача