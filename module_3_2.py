def send_email(message,recipient,sender = "university.help@gmail.com"):
    if "@" not in sender or not sender.endswith((".com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if "@" not in recipient or not recipient.endswith((".com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if  sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return
    if ('@' in (sender and recipient) and sender.endswith((".com", ".ru", ".net"))
            and recipient.endswith((".com", ".ru", ".net")) and sender=='university.help@gmail.com'):
         print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
         return
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
        return


send_email('Ты победитель!','sensivity@.com')
send_email('Купи хлеба!','university.help@gmail.com')
send_email('Какие условия для переговоров?','combat_76@bk.ru','minimal_66@gmail.net')
send_email('Прожыви достойно!!!','lordfilm.ru')
send_email('Засада в третьем корпусе!','urban.teacher@mai.uk', 'urban.student@mail.ru')

