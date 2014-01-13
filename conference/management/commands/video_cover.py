# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """
    """
    def handle(self, *args, **options):
        from conference import dataaccess
        from conference import settings
        from conference.utils import render_event_video_cover

        try:
            conference = args[0]
        except IndexError:
            raise CommandError('conference code is missing')

        events = settings.VIDEO_COVER_EVENTS(conference)
        for e in events:
            data = dataaccess.event_data(e)
            print '*', data['name']
            render_event_video_cover(e)
