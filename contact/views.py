import os

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactInfoModel
from home.models import SocialMediaModel
import requests
from django.conf import settings

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(chat_id, message, bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML",
    }
    requests.post(url, data=data)


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        telegram_message = (
            f"<b>New Contact Form Submission</b>\n\n"
            f"<b>👤 Name :</b> {name}\n"
            f"<b>📧 Email :</b> {email}\n"
            f"<b>✍️ Subject :</b> {subject}\n"
            f"<b>📩 Message :</b>\n{message}"
        )

        try:
            send_telegram_message(CHAT_ID, telegram_message, BOT_TOKEN)
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
        return redirect("contact:send-message")

    return render(request, "contact.html",
                  {"data": ContactInfoModel.objects.first(), 'social_media_apps': SocialMediaModel.objects.all()})
