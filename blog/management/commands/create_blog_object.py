from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Blog

fake = Faker()


class Command(BaseCommand):
    help = "Заповнення бази даних даними для моделі блогу"

    def handle(self, *args, **options):
        for _ in range(5):
            Blog.objects.create(
                title=fake.text(),
                content=fake.text(),
            )

        self.stdout.write("Дані для моделі блогу успішно заповнені")
