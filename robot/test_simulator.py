import unittest
from main import Simulator


class TestSimulator(unittest.TestCase):

    def setUp(self):
        self.sim = Simulator()

    def test_a(self):
        """Place at origin facing north, move once, expect 0,1,NORTH"""
        self.sim._parse_command("PLACE 0,0,NORTH")
        self.sim._parse_command("MOVE")
        self.assertEqual(self.sim._report_command(), "0,1,NORTH")

    def test_b(self):
        """Place at origin facing north, turn left, expect 0,0,WEST"""
        self.sim._parse_command("PLACE 0,0,NORTH")
        self.sim._parse_command("LEFT")
        self.assertEqual(self.sim._report_command(), "0,0,WEST")

    def test_c(self):
        """Multi combo of place, move, turn. Expect 3,3,NORTH"""
        self.sim._parse_command("PLACE 1,2,EAST")
        self.sim._parse_command("MOVE")
        self.sim._parse_command("MOVE")
        self.sim._parse_command("LEFT")
        self.sim._parse_command("MOVE")
        self.assertEqual(self.sim._report_command(), "3,3,NORTH")

    def test_d(self):
        """MOVE before PLACE should be ignored, expect 0,0,NORTH"""
        self.sim._parse_command("MOVE")
        self.sim._parse_command("PLACE 0,0,NORTH")
        self.assertEqual(self.sim._report_command(), "0,0,NORTH")

    def test_e(self):
        """PLACE at out-of-bounds position should be ignored, expect no report"""
        self.sim._parse_command("PLACE -1,-1,NORTH")
        self.assertEqual(self.sim._report_command(), "")

    def test_f(self):
        """MOVE off the table edge should be blocked, expect 0,0,SOUTH"""
        self.sim._parse_command("PLACE 0,0,SOUTH")
        self.sim._parse_command("MOVE")
        self.assertEqual(self.sim._report_command(), "0,0,SOUTH")

    def test_g(self):
        """LEFT should rotate north to west, expect 1,1,WEST"""
        self.sim._parse_command("PLACE 1,1,NORTH")
        self.sim._parse_command("LEFT")
        self.assertEqual(self.sim._report_command(), "1,1,WEST")

    def test_h(self):
        """Second PLACE should replace the first, expect 3,3,NORTH"""
        self.sim._parse_command("PLACE 0,0,NORTH")
        self.sim._parse_command("PLACE 3,3,NORTH")
        self.assertEqual(self.sim._report_command(), "3,3,NORTH")

    def test_i(self):
        """Unrecognised command should be ignored, expect 0,0,NORTH"""
        self.sim._parse_command("testing123 1,2,WEST")
        self.sim._parse_command("PLACE 0,0,NORTH")
        self.assertEqual(self.sim._report_command(), "0,0,NORTH")


if __name__ == "__main__":
    unittest.main(verbosity=2)
