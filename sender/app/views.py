from django.shortcuts import render
from .forms import PhoneNumberForm
from .tasks import send_sms


def send_sms_view(request):
    if request.method == "POST":
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["phone_number"]
            send_sms.delay(phone_number)
    else:
        form = PhoneNumberForm()
    return render(request, "send_sms.html", {"form": form})
