from django.utils import timezone
from datetime import timedelta


def yesterday_date(request):
    # Calculate yesterday's date
    yesterday = timezone.now() - timedelta(days=1)
    formatted_yesterday = yesterday.strftime('%Y-%m-%d')  # Format as YYYY-MM-DD

    # Return a dictionary to add 'yesterday' to the template context
    return {
        'yesterday': formatted_yesterday
    }
