"""Tests of the when.py module."""

import pytz

import when

try:
    # This is a hack for Python 2.
    string_types = (str, unicode)
except NameError:
    string_types = str


# class WhenTest(unittest.TestCase):
#     def setUp(self):
#         when.unset_utc()

#         self.one_second = datetime.timedelta(seconds=1)

#         self.utc = datetime.datetime.utcnow()


#     def test__add_time(self):
#         """Test when._add_time()"""
#         # Test change between months with dfferent number of days
#         test_value = datetime.datetime(2012, 3, 31)

#         expected_value = datetime.datetime(2012, 5, 1)
#         result = when._add_time(test_value, months=1)
#         self.assertEqual(result, expected_value)

#         # Test values going back into February of a leap year
#         expected_value = datetime.datetime(2012, 3, 2)
#         result = when._add_time(test_value, months=-1)
#         self.assertEqual(result, expected_value)

#         test_value = datetime.datetime(2012, 3, 30)

#         expected_value = datetime.datetime(2012, 3, 1)
#         result = when._add_time(test_value, months=-1)
#         self.assertEqual(result, expected_value)

#         test_value = datetime.datetime(2011, 3, 31)

#         expected_value = datetime.datetime(2011, 3, 3)
#         result = when._add_time(test_value, months=-1)
#         self.assertEqual(result, expected_value)

#         # Test leap day specifically
#         test_value = datetime.datetime(2012, 2, 29)

#         expected_value = datetime.datetime(2013, 3, 1)
#         result = when._add_time(test_value, years=1)
#         self.assertEqual(result, expected_value)

#         expected_value = datetime.datetime(2011, 3, 1)
#         result = when._add_time(test_value, years=-1)
#         self.assertEqual(result, expected_value)

#     def test__add_time_typeerror(self):
#         """Test TypeError raised by when._add_time()"""
#         self.assertRaises(TypeError, when._add_time, 'a')

#     def test__is_date_type(self):
#         """Test when._is_date_type()"""
#         self.assertFalse(when._is_date_type('a'))
#         self.assertFalse(when._is_date_type(1))
#         self.assertFalse(when._is_date_type(['a']))

#         self.assertTrue(when._is_date_type(self.today))
#         self.assertTrue(when._is_date_type(self.now))
#         self.assertTrue(when._is_date_type(self.now.time()))

#     def test_all_timezones(self):
#         """Test when.all_timezones()"""
#         # Make sure all_timezones() matches pytz's version
#         all_timezones = when.all_timezones()
#         self.assertEqual(all_timezones, pytz.all_timezones)

#     def test_all_timezones_set(self):
#         """Test when.all_timezones_set()"""
#         # Make sure all_timezones_set() matches pytz's version
#         all_timezones_set = when.all_timezones_set()
#         self.assertEqual(all_timezones_set, pytz.all_timezones_set)

#     def test_common_timezones(self):
#         """Test when.common_timezones()"""
#         # Make sure common_timezones() matches pytz's version
#         common_timezones = when.common_timezones()
#         self.assertEqual(common_timezones, pytz.common_timezones)

#     def test_common_timezones_set(self):
#         """Test when.common_timezones_set()"""
#         # Make sure common_timezones_set() matches pytz's version
#         common_timezones_set = when.common_timezones_set()
#         self.assertEqual(common_timezones_set, pytz.common_timezones_set)

#     def test_ever(self):
#         """Test when.ever()"""
#         old_result = None
#         for i in range(50):
#             result = when.ever()
#             self.assertTrue(isinstance(result, datetime.datetime))
#             self.assertNotEqual(result, old_result)
#             old_result = result

#     def test_format(self):
#         """Test when.format()"""
#         now = when.now()
#         today = when.today()
#         current_time = now.time()

#         for format_string in ('%a', '%A', '%b', '%B', '%c', '%d', '%f', '%H',
#                               '%I', '%j', '%m', '%M', '%p', '%S', '%U', '%w',
#                               '%W', '%x', '%X', '%y', '%Y', '%z', '%Z',
#                               '%A, %B %d, %Y %I:%M %p'):
#             # Test date objects
#             builtin_date = now.strftime(format_string)
#             result_date = when.format(now, format_string)
#             self.assertEqual(builtin_date, result_date)

#             # Test datetime objects
#             builtin_datetime = today.strftime(format_string)
#             result_datetime = when.format(today, format_string)
#             self.assertEqual(builtin_datetime, result_datetime)

#             # Test time objects
#             builtin_time = current_time.strftime(format_string)
#             result_time = when.format(current_time, format_string)
#             self.assertEqual(builtin_time, result_time)

#     def test_format_typeerror(self):
#         """Test TypeError raised by when.format()"""
#         self.assertRaises(TypeError, when.format, 'a', '%a')

#     def test_formats(self):
#         """Test the iteration of the formats class"""
#         for k in when.formats:
#             self.assertTrue(isinstance(k, string_types))

#             value = getattr(when.formats, k)
#             locale_value = getattr(locale, value)
#             self.assertTrue(isinstance(locale_value, int))

#     def test_formats_metaclass(self):
#         """Test the metaclass of the formats class"""
#         self.assertTrue(isinstance(when.formats, when._FormatsMetaClass))
#         for k in when.formats:
#             value = getattr(when.formats, k)
#             self.assertEqual(value, getattr(when._FormatsMetaClass, k))
#             self.assertEqual(value, when._FormatsMetaClass.__dict__[k])

#     def test_how_many_leap_days(self):
#         """Test when.how_many_leap_days()"""
#         # Tests with just years
#         self.assertEqual(when.how_many_leap_days(2012, 2012), 0)
#         self.assertEqual(when.how_many_leap_days(2012, 2013), 1)
#         self.assertEqual(when.how_many_leap_days(2012, 2017), 2)

#         # Simple tests using `datetime.date`
#         d1 = datetime.date(2012, 1, 1)
#         d2 = datetime.date(2012, 2, 1)
#         self.assertEqual(when.how_many_leap_days(d1, d2), 0)

#         d1 = datetime.date(2012, 1, 1)
#         d2 = datetime.date(2012, 3, 1)
#         self.assertEqual(when.how_many_leap_days(d1, d2), 1)

#         d1 = datetime.date(2012, 3, 1)
#         d2 = datetime.date(2012, 4, 1)
#         self.assertEqual(when.how_many_leap_days(d1, d2), 0)

#         d1 = datetime.date(2012, 3, 1)
#         d2 = datetime.date(2016, 2, 1)
#         self.assertEqual(when.how_many_leap_days(d1, d2), 0)

#         d1 = datetime.date(2012, 3, 1)
#         d2 = datetime.date(2017, 2, 1)
#         self.assertEqual(when.how_many_leap_days(d1, d2), 1)

#         # Simple tests using `datetime.datetime`
#         dt1 = datetime.datetime(2012, 2, 28)
#         dt2 = datetime.datetime(2012, 2, 29)
#         self.assertEqual(when.how_many_leap_days(dt1, dt2), 1)

#         dt1 = datetime.datetime(2012, 2, 28)
#         dt2 = datetime.datetime(2016, 2, 28)
#         self.assertEqual(when.how_many_leap_days(dt1, dt2), 1)

#         dt1 = datetime.datetime(2012, 2, 28)
#         dt2 = datetime.datetime(2020, 2, 28)
#         self.assertEqual(when.how_many_leap_days(dt1, dt2), 2)

#         dt1 = datetime.datetime(2012, 2, 28)
#         dt2 = datetime.datetime(2020, 2, 29)
#         self.assertEqual(when.how_many_leap_days(dt1, dt2), 3)

#         dt1 = datetime.datetime(2011, 2, 28)
#         dt2 = datetime.datetime(2011, 3, 22)
#         self.assertEqual(when.how_many_leap_days(dt1, dt2), 0)

#         dt1 = datetime.datetime(2012, 2, 28)
#         dt2 = datetime.datetime(2026, 2, 28)
#         self.assertEqual(when.how_many_leap_days(dt1, dt2), 4)

#         # And a few using mixed types
#         d1 = datetime.date(1970, 1, 1)
#         dt2 = datetime.datetime(1980, 1, 1)
#         self.assertEqual(when.how_many_leap_days(d1, dt2), 2)

#         dt1 = datetime.date(1970, 1, 1)
#         d2 = datetime.datetime(1990, 1, 1)
#         self.assertEqual(when.how_many_leap_days(dt1, d2), 5)

#         dt1 = datetime.date(2000, 1, 1)
#         d2 = datetime.datetime(3000, 1, 1)
#         # At first glance it would appear this should be 250, except that
#         # years divisible by 100 are not leap years, of which there are 10,
#         # unless they are also divisible by 400. The years 2000, 2400,
#         # and 2800 need to be added back in. 250 - (10 - 3) = 243
#         self.assertEqual(when.how_many_leap_days(dt1, d2), 243)

#     def test_how_many_leap_days_typeerror(self):
#         """Test TypeError raised by when.how_many_leap_days()"""
#         d1 = when.today()
#         d2 = when.yesterday()

#         # from_date must be valid
#         self.assertRaises(TypeError, when.how_many_leap_days, 'a', d2)
#         # to_date must be valid
#         self.assertRaises(TypeError, when.how_many_leap_days, d1, 'b')

#     def test_how_many_leap_days_valueerror(self):
#         """Test ValueError raised by when.how_many_leap_days()"""
#         d1 = when.today()
#         d2 = when.yesterday()

#         # from_date must be before to_date
#         self.assertRaises(ValueError, when.how_many_leap_days, d1, d2)

#     def test_is_timezone_aware(self):
#         """Test when.is_timezone_aware()"""
#         naive = when.now()
#         aware = naive.replace(tzinfo=pytz.UTC)

#         self.assertTrue(when.is_timezone_aware(aware))
#         self.assertFalse(when.is_timezone_aware(naive))

#         naive = naive.time()
#         aware = naive.replace(tzinfo=pytz.UTC)

#         self.assertTrue(when.is_timezone_aware(aware))
#         self.assertFalse(when.is_timezone_aware(naive))

#     def test_is_timezone_aware_typeerror(self):
#         """Test TypeError raised by when.is_timezone_aware()"""
#         today = when.today()
#         self.assertRaises(TypeError, when.is_timezone_aware, today)

#     def test_is_timezone_naive(self):
#         """Test when.is_timezone_naive()"""
#         naive = when.now()
#         aware = naive.replace(tzinfo=pytz.UTC)

#         self.assertTrue(when.is_timezone_naive(naive))
#         self.assertFalse(when.is_timezone_naive(aware))

#         naive = naive.time()
#         aware = naive.replace(tzinfo=pytz.UTC)

#         self.assertTrue(when.is_timezone_naive(naive))
#         self.assertFalse(when.is_timezone_naive(aware))

#     def test_is_timezone_naive_typeerror(self):
#         """Test TypeError raised by when.is_timezone_naive()"""
#         today = when.today()
#         self.assertRaises(TypeError, when.is_timezone_aware, today)

#     def test_now(self):
#         """Test when.now()"""
#         now = when.now()
#         utc = when.now(True)

#         # Unfortunately the clock keeps ticking each time we capture a value
#         # for now so we can't do a direct comparison with assertEqual.
#         # It's probably safe to assume the now function is working as long as
#         # the difference is less than a second. There's probably a better way
#         # to test this, but for now it's sufficient.
#         self.assertTrue(now - self.now < self.one_second)
#         self.assertTrue(utc - self.utc < self.one_second)

#     def test_set_utc(self):
#         """Test when.set_utc()"""
#         when.set_utc()
#         self.assertEqual(when._FORCE_UTC, True)

#     def test_shift(self):
#         """Test when.shift()"""
#         first = when.shift(self.utc, from_tz='UTC', to_tz='America/New_York')
#         second = when.shift(first, from_tz='America/New_York', to_tz='UTC')

#         self.assertNotEqual(first, second)
#         self.assertNotEqual(first, self.utc)
#         self.assertEqual(second, self.utc)

#         # Local time
#         if self.timezone in ('UTC', 'Etc/UTC'):
#             # This block is needed for tests run in an environment set to UTC.
#             first = when.shift(self.now, to_tz='America/New_York')
#             second = when.shift(first, from_tz='America/New_York')
#         else:
#             first = when.shift(self.now, to_tz='UTC')
#             second = when.shift(first, from_tz='UTC')

#         self.assertNotEqual(first, second)
#         self.assertNotEqual(first, self.now)
#         self.assertEqual(second, self.now)

#         # Set utc parameter to true
#         first = when.shift(self.utc, to_tz='America/New_York', utc=True)
#         second = when.shift(first, from_tz='America/New_York', utc=True)

#         self.assertNotEqual(first, second)
#         self.assertNotEqual(first, self.utc)
#         self.assertEqual(second, self.utc)

#         # Force UTC
#         when.set_utc()
#         first = when.shift(self.utc, to_tz='America/New_York')
#         second = when.shift(first, from_tz='America/New_York')

#         self.assertNotEqual(first, second)
#         self.assertNotEqual(first, self.utc)
#         self.assertEqual(second, self.utc)

#     def test_shift_typeerror(self):
#         """Test TypeError raised by when.shift()"""
#         self.assertRaises(TypeError, when.shift, 'a')
#         self.assertRaises(TypeError, when.shift, when.today())


def test_shift_aware(now):
    """Test shift for time zone aware datetimes."""
    chicago = pytz.timezone('America/Chicago')
    new_york = pytz.timezone('America/New_York')

    aware = chicago.localize(now)

    actual = when.shift(aware, to_tz='America/New_York')

    assert actual.tzinfo == new_york

#     def test_shift_aware(self):
#         """Test when.shift() for time zone aware datetimes"""
#         central = pytz.timezone('America/Chicago')

#         now_aware = central.localize(self.now)

#         # Make sure the datetime's time zone is the respected
#         first = when.shift(now_aware, to_tz='America/New_York')
#         second = when.shift(self.now, from_tz='America/Chicago', to_tz='America/New_York')

#         self.assertEqual(first, second)

#         # Also make sure the from_tz parameter is ignored
#         first = when.shift(now_aware, from_tz='UTC', to_tz='America/New_York')

#         self.assertEqual(first, second)

#         # Also make sure the utc parameter is ignored
#         first = when.shift(now_aware, to_tz='America/New_York', utc=True)

#         self.assertEqual(first, second)


def test_timezone(timezone):
    """Test timezone."""
    actual = when.timezone()
    assert actual == timezone

def test_timezone_object(timezone):
    """Test timezone_object."""
    expected = pytz.timezone(timezone)
    actual = when.timezone_object()
    assert actual == expected


def test_today(today):
    """Test today."""
    actual = when.today()
    assert actual == today


def test_tomorrow(today, one_day):
    """Test tomorrow."""
    expected = today + one_day
    actual = when.tomorrow()
    assert actual == expected


# def test_unset_utc(with_utc):
#     """Test unset_utc."""
#     when.unset_utc()
#     assert not when._FORCE_UTC


def test_yesterday(today, one_day):
    """Test yesterday."""
    expected = today - one_day
    actual = when.yesterday()
    assert actual == expected
