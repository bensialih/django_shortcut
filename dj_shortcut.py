import os
import sys
LOCATION = "%s/%s"
FILES = ("management/commands/_private.py", )
FOLDERS = ("management", "management/commands",)

SAMPLE_SHORTCUT = """
    from django.core.management.base import BaseCommand, CommandError

    class Command(BaseCommand):
        help = 'Sample shortcut'

        def add_arguments(self, parser):
            pass

        def handle(self, *args, **options):

            self.stdout.write(self.style.SUCCESS('Successfully ran shortcut'))

"""

def create_boilerplate(base):
    """
        creates generic django boilerplate
        :param base: string of folder base
    """
    for path in FOLDERS:
        folder_path = LOCATION % (base, path)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

    for file_str in FILES:
        if not os.path.exists(LOCATION % (base, file_str)):
            open(file_str, 'a').close()


def create_shortcut(base, name):
    """
        checks that the shortcut is able to be created
    """
    base_dir = LOCATION % (base, "management/commands")
    location = LOCATION % (base_dir, name)
    if os.path.exists(location):
        raise Exception("shortcut %s already exists" % name)

    with open(location, 'w') as short_file:
        short_file.write(SAMPLE_SHORTCUT)


def check_django_folder(base):
    """
        check that this is a django app
        looks for usual apps.py and models.py files
    """
    files = ("apps.py", "models.py")
    results = []
    for item in files:
        file_str = LOCATION % (base, item)
        results.append(os.path.exists(file_str))

    if False in results:
        raise Exception("Please make sure you run this in a django app")


def shortcut(name):
    """"
        :param name: of the shortcut you want to create
    """
    base = os.path.dirname(os.path.realpath(__file__))
    check_django_folder(base)
    create_boilerplate(base)

    name = "%s.py" % name
    create_shortcut(base, name)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        raise Exception("Please enter the name of the shortcut you want to create")

    shortcut(args[1])