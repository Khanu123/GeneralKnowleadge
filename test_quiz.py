import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("general knowleadge quiz.py")


def load_module():
    spec = importlib.util.spec_from_file_location("general_knowledge_quiz", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class QuizTests(unittest.TestCase):
    def test_answer_normalization(self):
        module = load_module()
        self.assertEqual(module.normalize_answer(" c "), "C")

    def test_score_calculation(self):
        module = load_module()
        correct, percent = module.calculate_score(["C", "D", "A", "A", "B", "B"])
        self.assertEqual(correct, 6)
        self.assertEqual(percent, 100.0)


if __name__ == "__main__":
    unittest.main()
