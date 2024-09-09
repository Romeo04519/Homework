import unittest
import module_12_2
import module_12_1

test_start = unittest.TestSuite()
test_start.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))
test_start.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_start)

