from django import dispatch
from django.dispatch import Signal

new_subscriber = Signal(["job", "subscriber"])
