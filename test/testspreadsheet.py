from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

   def test_evaluate_integer(self):
       spreadsheet = SpreadSheet()
       spreadsheet.set("A1", "1")
       self.assertEqual(1, spreadsheet.evaluate("A1"))

   def test_evaluate_non_valid_integer(self):
       spreadsheet = SpreadSheet()
       spreadsheet.set("A1", "1.5")
       self.assertEqual("#Error", spreadsheet.evaluate("A1"))

   def test_evaluate_valid_string(self):
       spreadsheet = SpreadSheet()
       spreadsheet.set("A1", "'Apple'")
       self.assertEqual("Apple", spreadsheet.evaluate("A1"))

   def test_evaluate_invalid_string(self):
       spreadsheet = SpreadSheet()
       spreadsheet.set("A1", "'Apple")
       self.assertEqual("#Error", spreadsheet.evaluate("A1"))

   def test_evaluate_simple_formula(self):
       spreadsheet = SpreadSheet()
       spreadsheet.set("A1", "='Apple'")
       self.assertEqual("Apple", spreadsheet.evaluate("A1"))

   def test_evaluate_simple_formula_integer(self):
       spreadsheet = SpreadSheet()
       spreadsheet.set("A1", "=1")
       self.assertEqual(1, spreadsheet.evaluate("A1"))

   def test_evaluate_simple_formula_non_valid_string(self):
       spreadsheet = SpreadSheet()
       spreadsheet.set("A1", "='Apple")
       self.assertEqual("#Error", spreadsheet.evaluate("A1"))
   def test_evaluate_valid_formula_reference(self):
       spreadsheet = SpreadSheet()
       spreadsheet.set("B1", "42")
       spreadsheet.set("A1", "=B1")
       self.assertEqual(42, spreadsheet.evaluate("A1"))
   def test_evaluate_valid_formula_reference_invalid_integer(self):
       spreadsheet = SpreadSheet()
       spreadsheet.set("B1", "42.5")
       spreadsheet.set("A1", "=B1")
       self.assertEqual("#Error", spreadsheet.evaluate("A1"))
   def test_evaluate_circular_formula(self):
       spreadsheet = SpreadSheet()
       spreadsheet.set("A1", "=B1")
       spreadsheet.set("B1", "=A1")
       self.assertEqual("#Circular", spreadsheet.evaluate("A1"))