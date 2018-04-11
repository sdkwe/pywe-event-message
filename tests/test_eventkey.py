# -*- coding: utf-8 -*-

from pywe_event_message import parse_eventkey


class TestEventKeyCommands(object):
    def test_parse_eventkey(self):
        eventkey = 'qrscene_123123'
        assert parse_eventkey(eventkey) == '123123'
        assert parse_eventkey(eventkey, event='subscribe') == '123123'
        assert parse_eventkey(eventkey, event='subscribe', key_cast_func=int) == 123123
