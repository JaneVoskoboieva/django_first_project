import datetime

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from faker import Faker

from polls.models import Question


class Command(BaseCommand):

    help = 'Add new question(s) to the system'

    def add_arguments(self, parser):
        parser.add_argument('-l', '--len', type=int, default=10)

    def handle(self, *args, **options):
        faker = Faker()

        self.stdout.write('Start generating Questions')
        for _ in range(options['len']):
            self.stdout.write('Generating Question {}'.format(_ + 1))
            question = Question()
            question.question_text = faker.text(max_nb_chars=50)[:-1] + "?"
            question.pub_date = timezone.now()
            question.save()
        self.stdout.write('End generating Questions')