from django.db import models

class ContactMessage(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField("Имя", max_length=150)
    email = models.EmailField("Email", blank=True)
    phone = models.CharField("Телефон", max_length=32, blank=True)
    message = models.TextField("Сообщение", blank=True)

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

    def __str__(self):
        return f"{self.name} ({self.created_at:%Y-%m-%d %H:%M})"
