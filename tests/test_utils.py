from unittest import TestCase

from framewirc import exceptions
from framewirc.utils import chunk_message, RequiredAttributesMixin, to_bytes, to_unicode


class TestToUnicode(TestCase):
    def test_already_unicode(self):
        text = 'тнιѕ ιѕ αℓяєα∂у υηι¢σ∂є'
        result = to_unicode(text)
        self.assertEqual(result, text)

    def test_ascii(self):
        text = b'This is just plain ASCII'
        expected = 'This is just plain ASCII'
        result = to_unicode(text)
        self.assertEqual(result, expected)

    def test_latin_1(self):
        text = b'Ume\xe5'
        expected = 'Umeå'
        result = to_unicode(text)
        self.assertEqual(result, expected)

    def test_utf8(self):
        text = b"Rhoi'r ffidil yn y t\xc3\xb4"
        expected = "Rhoi'r ffidil yn y tô"
        result = to_unicode(text)
        self.assertEqual(result, expected)

    def test_windows_1250(self):
        text = b'Miko\xb3aj Kopernik'
        expected = 'Mikołaj Kopernik'
        result = to_unicode(text)
        self.assertEqual(result, expected)

    def test_not_bytes_or_string(self):
        with self.assertRaises(AttributeError):
            to_unicode(None)

    def test_expected_decoding_first(self):
        """
        An undecoded bytestring will try "expected" before utf8.

        This is because some non-UTF8 strings can be "valid" utf8.
        """
        text = b'\x1b$BEl5~ET\x1b(B'
        expected = '東京都'  # as opposed to '\x1b$BEl5~ET\x1b(B'
        result = to_unicode(text, ['iso-2022-jp'])
        self.assertEqual(result, expected)

    def test_expected_decoding_quietly_wrong(self):
        """
        An expected decoding can be wrong, and not throw errors.

        Perhaps not ideal, but I don't know if it's possible to catch this.
        """
        text = b'Ume\xe5'
        expected = 'Umeĺ'  # Decoding incorrectly throws no error in this case
        result = to_unicode(text, ['windows_1250'])
        self.assertEqual(result, expected)

    def test_expected_decoding_loudly_wrong(self):
        """An expected decoding can fall back to another encoding."""
        text = b'\xff\xfe\xb5\x03\xbb\x03\xbb\x03\xb7\x03\xbd\x03\xb9\x03\xba\x03\xac\x03'
        expected = 'ελληνικά'
        result = to_unicode(text, ['iso-2022-jp', 'utf16'])  # `text` is utf16
        self.assertEqual(result, expected)


class TestToBytes(TestCase):
    def test_unicode(self):
        text = 'ಠ_ಠ'
        expected = b'\xe0\xb2\xa0_\xe0\xb2\xa0'
        result = to_bytes(text)
        self.assertEqual(result, expected)

    def test_already_bytes(self):
        text = b'bytes!'
        result = to_bytes(text)
        self.assertEqual(result, text)

    def test_not_bytes_or_string(self):
        with self.assertRaises(AttributeError):
            to_bytes(None)


class TestChunkMessage(TestCase):
    """Test the behaviour of the chunk_message function."""
    def test_return_type(self):
        """Does it return a list of bytes objects?"""
        expected = [b'Just a simple message']
        messages = chunk_message('Just a simple message', max_length=100)
        self.assertEqual(messages, expected)

    def test_split_linefeeds(self):
        """Does it split on newline chars?"""
        msg = 'A message\rsplit over\nmany lines\r\nwith odd linebreaks.'
        expected = [
            b'A message',
            b'split over',
            b'many lines',
            b'with odd linebreaks.',
        ]
        messages = chunk_message(msg, max_length=100)
        self.assertEqual(messages, expected)

    def test_split_long_line(self):
        """Does it split long lines?"""
        msg = 'Message to be split into chunks of twenty characters or less.'
        expected = [
            b'Message to be split',
            b'into chunks of',
            b'twenty characters or',
            b'less.',
        ]
        messages = chunk_message(msg, max_length=20)
        self.assertEqual(messages, expected)

    def test_split_long_word(self):
        """Does it split long words?"""
        msg = 'Sup Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch?'
        expected = [
            b'Sup',
            b'Llanfairpwllgwyngyll',
            b'gogerychwyrndrobwlll',
            b'lantysiliogogogoch?',
        ]
        messages = chunk_message(msg, max_length=20)
        self.assertEqual(messages, expected)

    def test_split_long_unicode(self):
        """Are words with multi-byte chars split correctly?"""
        # Repeated failures lead to success.
        msg = '失敗を繰り返すことで、成功に至る。'
        expected = [
            to_bytes('失敗を繰り返'),
            to_bytes('すことで、成'),
            to_bytes('功に至る。'),
        ]
        messages = chunk_message(msg, max_length=20)
        self.assertEqual(messages, expected)


class TestRequiredAttributesMixin(TestCase):
    """Tests for RequiredAttributesMixin"""
    def test_kwarg(self):
        """Attributes can be passed through as kwargs."""
        class RequiresFoo(RequiredAttributesMixin):
            required_attributes = ['foo']

        result = RequiresFoo(foo='bar')
        self.assertEqual(result.foo, 'bar')

    def test_attribute(self):
        """Attributes can be set directly on the class."""
        class RequiresFoo(RequiredAttributesMixin):
            foo = 'bar'
            required_attributes = ['foo']

        result = RequiresFoo()
        self.assertEqual(result.foo, 'bar')

    def test_kwargs_overrides_attribute(self):
        """Attributes set on the class should be overridden by kwargs."""
        class RequiresFoo(RequiredAttributesMixin):
            foo = 'bar'
            required_attributes = ['foo']

        result = RequiresFoo(foo='baz')
        self.assertEqual(result.foo, 'baz')

    def test_attibute_not_set(self):
        """Failing to set the attribute should raise an error."""
        class RequiresFoo(RequiredAttributesMixin):
            required_attributes = ['foo']

        with self.assertRaises(exceptions.MissingAttributes):
            RequiresFoo()

    def test_error_description(self):
        """The error raised should have a good description."""
        class RequiresFoo(RequiredAttributesMixin):
            required_attributes = ['foo']

        with self.assertRaises(exceptions.MissingAttributes) as cm:
            RequiresFoo()

        expectied = "Required attribute(s) missing: ['foo']"
        self.assertEqual(str(cm.exception), expectied)
