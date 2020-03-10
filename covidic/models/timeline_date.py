from django.db import models


class TimelineDate(models.Model):
    date_id = models.AutoField(primary_key=True)
    date = models.DateField(editable=False)

    class Meta:
        db_table = 'timeline_dates'
        unique_together = ['date']

    def __str__(self):
        return "TimelineDate " + str(self.date)
