import sqlite3


def add_user(chat_id, full_name, username, language_code, reg_date):
    connection = sqlite3.connect('db.sqlite3')
    c = connection.cursor()

    c.execute("SELECT * FROM bot_chatbotusers WHERE chat_id = %s"%(chat_id))
    
    user_data = c.fetchone()

    if user_data:
        pass
    else:
        c.execute("INSERT INTO bot_chatbotusers (chat_id, full_name, username, language_code, reg_date) VALUES (%s, '%s', '%s', '%s', '%s')"%(chat_id, full_name, username, language_code, reg_date))
        connection.commit()
        c.close()

def message_history(message_id, chat_id, full_name, username, date, text):
    connection = sqlite3.connect('db.sqlite3')
    c = connection.cursor()

    c.execute("INSERT INTO bot_messagehistory (message_id, chat_id, full_name, username, date, text) VALUES (%s, '%s', '%s', '%s', '%s', '%s')"%(message_id, chat_id, full_name, username, date, text))
    connection.commit()
    c.close()