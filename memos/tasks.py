from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

from .models import VoiceMemo

User = get_user_model()


def send_daily_summaries():
    now = timezone.now()
    since = now - timedelta(hours=24)

    users = User.objects.all()

    for user in users:
        memos = VoiceMemo.objects.filter(
            user=user,
            created_at__gte=since
        ).order_by("-created_at")

        # Render email HTML
        context = {
            "user": user,
            "memos": memos,
        }

        subject = "Your Daily Voice Memo Summary"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [user.email]

        html_content = render_to_string("email_summary.html", context)

        msg = EmailMultiAlternatives(
            subject=subject,
            body="Your email client does not support HTML.",
            from_email=from_email,
            to=to_email,
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()