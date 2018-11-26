from django.db import models

class State(models.Model):
    state_name = models.CharField(max_length=30, default='')

    def _str_(self):
        return self.state_name
