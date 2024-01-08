from datetime import timedelta

from django.utils import timezone

def get_time_ago(time):
    if time is None:
        return "Never"
    now = timezone.now()
    diff = now - time
    if diff < timedelta(minutes=1):
        return f"{diff.seconds} seconds ago"
    elif diff < timedelta(hours=1):
        return f"{diff.seconds // 60} minutes ago"
    elif diff < timedelta(days=1):
        return f"{diff.seconds // 3600} hours ago"
    elif diff < timedelta(days=30):
        return f"{diff.days} days ago"
    elif diff < timedelta(days=365):
        return f"{diff.days // 30} months ago"
    else:
        return f"{diff.days // 365} years ago"