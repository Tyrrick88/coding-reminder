import unittest
from unittest.mock import patch
from reminder_script import remind_to_code

class TestReminderScript(unittest.TestCase):

    @patch("reminder_script.notification.notify")
    def test_remind_to_code(self, mock_notify):
        remind_to_code()
        mock_notify.assert_called_once()

if __name__ == "__main__":
    unittest.main()
