from functools import wraps
from telegram import Logger
from datetime import date
from dotenv import load_dotenv
from bson.objectid import ObjectId
import os
from flask import session, render_template
load_dotenv()


#### Contact ####

TELEGRAM_USER_ID =  "mathew5_8"

logger = Logger(token="7776477493:AAHmDSJ2MERVKmxFgF4eJLhmAvvOPohg388", chat_id="1121881873")  # TELEGRAM BOT


def send_message(name, email, subject, text):
    """
    Function that forwards to telegram when a message is received from the contact section.
    """
    message = f"New Message !!\n\
Name: {name}\nEmail: {email}\Subject:{subject}\Text:\n  {text}"

    logger.message(message=message)


# ADMIN REQUIRED
def admin_only(f):
    """
    If there is no is_active in the session, we prevent the user
    from performing some operations by returning a 404 error.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("is_active"):
            return render_template('404.html'), 404
        return f(*args, **kwargs)
    return decorated_function
