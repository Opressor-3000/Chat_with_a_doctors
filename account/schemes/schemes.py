
'''
описываем взаимодействия с 
      1. User
         UserBase [хранит все поля кроме id cookie, account_id, qr, is_active]
         User
            CreateUser
            GetUser_id(cookie=user.cookie)
            GetAccount
            set_username
            set_gender
            set_birthday
            set_avatar


      2. Account
            get_account
               set_patch_account
               get_users_chats
                  

      3. Chats(GetUser_id)
            Doctors()
               speciality
                  chat
            Specialities
               doctors
                  chat
            chat
               message

      4. CurrentChat
            user
               chat
                  current_chat

      5. Doctors(list[Chats])
            doctor
               feedback
               chat
                  message
               rating
'''



#  -----------------------------   USER  SCHEMES   --------------------------



# -------------------------   ACCOUNT  SCHEMES   ---------------------





# ----------------------  DISEASE  ---------------------
   



# --------------------- ANAMNESIS ---------------------


# ------------------- DIAGNOSIS -----------------------


