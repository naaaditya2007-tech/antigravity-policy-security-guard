import unittest
from guardrails import PolicyGuard

class TestGuard(unittest.TestCase):
    def test_policy(self):
        g = PolicyGuard(["read"], ["delete"])
        self.assertTrue(g.check("read")["permitted"])
        self.assertFalse(g.check("delete")["permitted"])

if __name__ == "__main__":
    unittest.main()
