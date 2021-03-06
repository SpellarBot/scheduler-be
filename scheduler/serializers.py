from rest_framework import serializers
from .models import Employee, Manager, Section, ScheduleByShift, Unavailability, WeeklyAvailability


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'full_name', 'position',
                  'photo_url', 'sales', 'rating')


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = ('id', 'full_name', 'position', 'photo_url')


class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'date', 'shift', 'color', 'num_of_tables')


class ScheduleByShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleByShift
        fields = ('id', 'date', 'shift', 'num_of_sections',
                  'section_red',  'section_yellow',  'section_orange',  'section_green',  'section_blue',  'section_purple')


class UnavailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Unavailability
        fields = ('id', 'date', 'employee', 'am',
                  'aft',  'pm')


class WeeklyAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyAvailability
        fields = ('id', 'employee', 'mon_am', 'tue_am', 'wed_am', 'thu_am', 'fri_am', 'sat_am', 'sun_am', 'mon_aft', 'tue_aft',
                  'wed_aft', 'thu_aft', 'fri_aft', 'sat_aft', 'sun_aft', 'mon_pm', 'tue_pm', 'wed_pm', 'thu_pm', 'fri_pm', 'sat_pm', 'sun_pm',)
