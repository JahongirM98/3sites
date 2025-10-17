from django.shortcuts import render, redirect

def home(request):
    return render(request, "pages/home.html")

def about(request):
    return render(request, "pages/about.html")

def contacts(request):
    from feedback.forms import ContactForm  # ленивый импорт
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contacts")
    else:
        form = ContactForm()
    return render(request, "pages/contacts.html", {"form": form})
