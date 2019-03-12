from django.db import models


POSITION_CHOICES = (
    ('server', 'Server'),
    ('host', 'Host'),
    ('bartender', 'Bartender')
)


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(
        max_length=20, choices=POSITION_CHOICES, default='server')
    photo_url = models.TextField()
    sales = models.IntegerField()
    rating = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


MANAGER_CHOICES = (
    ('manager', 'Manager'),
    ('general_manager', 'General Manager'),
    ('assistant_manager', 'Assistant Manager')
)


class Manager(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(
        max_length=30, choices=MANAGER_CHOICES, default='manager')
    photo_url = models.TextField()

    def __str__(self):
        return self.full_name


COLOR_CHOICES = (
    ('red', 'Red'),
    ('orange', 'Orange'),
    ('yellow', 'Yellow'),
    ('green', 'Green'),
    ('blue', 'Blue'),
    ('purple', 'Purple')
)


class Section(models.Model):
    color = models.CharField(
        max_length=20, choices=COLOR_CHOICES, default='red')
    num_of_tables = models.IntegerField()
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='section')

    def __str__(self):
        return self.color


SHIFT_CHOICES = (
    ('AM', 'Morning Shift'),
    ('AFT', 'Afternoon Shift'),
    ('PM', 'Evening Shift')
)


class ScheduleByShift(models.Model):
    date = models.DateField()
    shift = models.CharField(max_length=30, choices=SHIFT_CHOICES)
    num_of_sections = models.IntegerField()
    section_red = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='schedule', null=True)
    # section_orange = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='schedule')
    # section_yellow = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='schedule')

    def __repr__(self):
        return self.date


AVAILABILITY_CHOICES = (
    ('available', 'I AM available'),
    ('unavailable', 'I am NOT available')
)


class Unavailability(models.Model):
    date = models.DateField()
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='unavailability')
    am = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    aft = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    # pm = models.CharField(
    #     max_length=20, choices=AVAILABILITY_CHOICES, default='available')

    def __repr__(self):
        return self.employee


class WeeklyAvailability(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='weekly_availability')
    mon_am = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    mon_aft = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    mon_pm = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    tue_am = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    tue_aft = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    tue_pm = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    wed_am = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    wed_aft = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    wed_pm = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    thu_am = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    thu_aft = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    thu_pm = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    fri_am = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    fri_aft = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    fri_pm = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    sat_am = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    sat_aft = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    sat_pm = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    sun_am = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    sun_aft = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    sun_pm = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='available')

    def __repr__(self):
        return self.employee
