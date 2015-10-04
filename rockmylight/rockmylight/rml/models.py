from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from datetime import datetime


JAMKEY = 1


# Create your models here.
class Jam(models.Model):
    session_num = models.IntegerField()
    playing = models.BooleanField(default=True)
    start_time = models.DateTimeField(default=datetime.now)
    # def get_instance(self):
    #     try:
    #         singleton = Jam.objects.get(pk=JAMKEY)
    #     except ObjectDoesNotExist:
    #         singleton = Jam.objects.create(pk=JAMKEY)
    #         singleton.save()
    #     return singleton

    # def play_session(self, session_num):
    #     Jam.objects.all().update(playing=False)
    #     jam = Jam.objects.filter(session_num=session_num)[0]
    #     jam.playing = True
    #     jam.save()

    # def get_playing_session(self):
    #     jam = Jam.objects.filter(playing=True)[0]
    #     return jam
    @classmethod
    def play_session(self, session_num):
        pass

    @classmethod
    def get_playing_session(self):
        try:
            singleton = Jam.objects.get(pk=JAMKEY)
        except ObjectDoesNotExist:
            singleton = Jam.objects.create(pk=JAMKEY, session_num=1)
            singleton.save()
        return singleton


class Devices(models.Model):
    # Jam session
    jam = models.ForeignKey(Jam)
    uuid = models.CharField(max_length=20)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)

    @classmethod
    def update_location(cls, uuid, lat, lon):
        try:
            device = Devices.objects.get(uuid=uuid)
        except ObjectDoesNotExist:
            jam = Jam.get_playing_session()
            device = Devices.objects.create(uuid=uuid, jam=jam)
            device.save()
            # XXX: Implement expiration for devices
        device.lat = lat
        device.lon = lon
        device.save()

    def __repr__(self):
        return 'Device #%d {%s} :%s :%s' % (self.id, self.uuid,
                                            self.lat, self.lon)
