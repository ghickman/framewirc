from unittest import mock, TestCase

from ..connection import Connection
from ..exceptions import (
    MessageTooLong,
    NoLineEnding,
    StrayLineEnding,
)


class ConnectionTestCase(TestCase):
    def setUp(self):
        self.connection = Connection(
            handlers=[],
            host='example.com',
            port=6697,
            nick='unused',
        )
        self.connection.writer = mock.MagicMock()


class TestSend(ConnectionTestCase):
    def test_ideal_case(self):
        message = b'PRIVMSG meshy :Nice IRC lib you have there\r\n'
        self.connection.send(message)
        self.connection.writer.write.assert_called_with(message)

    def test_not_bytes(self):
        message = 'PRIVMSG meshy :Nice IRC lib you have there\r\n'
        with self.assertRaises(TypeError):
            self.connection.send(message)
        self.assertFalse(self.connection.writer.write.called)

    def test_only_one_line_ending(self):
        message = b'PRIVMSG meshy :Nice \r\nCODE :injection you have there\r\n'
        with self.assertRaises(StrayLineEnding):
            self.connection.send(message)
        self.assertFalse(self.connection.writer.write.called)

    def test_line_ending_at_eol(self):
        message = b'PRIVMSG meshy :Nice line ending you have forgotten there'
        with self.assertRaises(NoLineEnding):
            self.connection.send(message)
        self.assertFalse(self.connection.writer.write.called)

    def test_message_too_long(self):
        message = b'FIFTEEN chars :' + 496 * b'a' + b'\r\n'  # 513 chars
        with self.assertRaises(MessageTooLong):
            self.connection.send(message)
        self.assertFalse(self.connection.writer.write.called)

    def test_message_just_right(self):
        message = b'FIFTEEN chars :' + 495 * b'a' + b'\r\n'  # 512 chars
        self.connection.send(message)
        self.connection.writer.write.assert_called_with(message)


class TestSendBatch(ConnectionTestCase):
    def test_send_batch(self):
        messages = [
            b'PRVMSG meshy :Getting there\r\n',
            b'PRVMSG meshy :It is almost usable!\r\n',
        ]
        self.connection.send_batch(messages)
        calls = self.connection.writer.write.mock_calls
        self.assertEqual(calls, list(map(mock.call, messages)))


class TestSetNick(ConnectionTestCase):
    def test_command_sent(self):
        new_nick = 'meshy'
        self.connection.set_nick(new_nick)
        self.connection.writer.write.assert_called_with(b'NICK meshy\r\n')

    def test_new_nick_kept(self):
        new_nick = 'meshy'
        self.connection.set_nick(new_nick)
        self.assertEqual(self.connection.nick, new_nick)
