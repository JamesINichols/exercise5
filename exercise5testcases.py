import unittest
import re
import exercise5

# assume this exists in some file mac_generator.py
from exercise5 import generateMACAddress


class TestGenerateMACAddress(unittest.TestCase):

    def setUp(self):
        # MAC regex:
        #  - 6 octets
        #  - hex pairs separated by ":" or "-"
        self.mac_regex = re.compile(r'^([0-9A-Fa-f]{2}([-:])){5}([0-9A-Fa-f]{2})$')

    def test_returns_string(self):
        mac = generateMACAddress()
        self.assertIsInstance(mac, str)

    def test_matches_mac_format(self):
        mac = generateMACAddress()
        self.assertRegex(mac, self.mac_regex)

    def test_randomness(self):
        # 2 calls should not be equal
        mac1 = generateMACAddress()
        mac2 = generateMACAddress()
        self.assertNotEqual(mac1, mac2)

    def test_valid_hex_octets(self):
        mac = generateMACAddress()
        # remove separator and ensure ALL remaining characters are hex
        hex_str = mac.replace(':', '').replace('-', '')
        try:
            int(hex_str, 16)  # should not throw
        except ValueError:
            self.fail(f"Not valid hex: {mac}")

    def test_correct_octet_count(self):
        mac = generateMACAddress()
        if ':' in mac:
            parts = mac.split(':')
        else:
            parts = mac.split('-')
        self.assertEqual(len(parts), 6)


if __name__ == '__main__':
    unittest.main()
