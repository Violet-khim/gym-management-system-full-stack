from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError

class Command(createsuperuser.Command):
    def handle(self, *args, **options):
        # Call the parent class's handle method first
        super().handle(*args, **options)
        
        # Get the user that was just created
        username = options.get('username')
        if not username:
            username = self.username_field.verbose_name
        
        # Get the user instance
        user = self.UserModel._default_manager.get(**{
            self.UserModel.USERNAME_FIELD: username
        })
        
        # Explicitly set manager attributes
        user.is_employee = False  # Must be set first
        user.is_manager = True
        user.salary = None
        user.due = 0
        
        # Force save without any signals or validations
        self.UserModel._default_manager.filter(pk=user.pk).update(
            is_employee=False,
            is_manager=True,
            salary=None,
            due=0
        )

