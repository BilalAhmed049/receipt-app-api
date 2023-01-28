"""
Test
"""

from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.Check') # Under what are Decoradotos
class CommandTests(SimpleTestCase):
    """Test Commands"""

    def test_wait_for_db_ready(self,patched_check):
        """ """
        patched_check.return_value = True

        call_command('wait_for_db')
        patched_check.assert_called_once_with(database=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self,patched_check):
        """Test"""
        patched_check.side_effect = [Psycopg2Error] * 2+ \
            [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertJSONEqual(patched_check.call_count,6)
        patched_check.assert_called_with(database=['default'])
