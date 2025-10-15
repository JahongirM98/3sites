from django.shortcuts import render, redirect


def home(request):
    return render(request, "pages/home.html")

def about(request):
    return render(request, "pages/about.html")

def contacts(request):
    from feedback.forms import ContactForm
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # сохраняем в БД (видно в адффминке)
            # TODO: отправка письма на корпоративную почту (EMAIL_* настройки)
            # TODO: отправка в Telegram (бот-токен и chat_id)
            return redirect("contacts")  # простая перезагрузка страницы
    else:
        form = ContactForm()
    return render(request, "pages/contacts.html", {"form": form})
