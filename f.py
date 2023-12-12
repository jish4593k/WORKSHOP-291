import unittest
import torch
import tensorflow as tf
from tensorflow import keras
from tkinter import Tk, Label, Entry, Button, StringVar

def get_roots(a, b, c):
    a, b, c = map(torch.tensor, (a, b, c))
    delta = b**2 - 4*a*c
    roots = torch.where(delta > 0, ((-b + torch.sqrt(delta)) / (2*a), (-b - torch.sqrt(delta)) / (2*a)),
                        torch.where(delta == 0, -b / (2*a), (None, None)))
    return roots

class QuadraticEquationTestCase(unittest.TestCase):
    def test_solves_real_roots(self):
        roots = get_roots(1, -2, 1)
        self.assertEqual(roots[0], 1)
        self.assertEqual(roots[1], 1)

    def test_first_root_less_than_second(self):
        roots = get_roots(1, 2, -3)
        self.assertEqual(roots[0], -3)
        self.assertEqual(roots[1], 1)

    def test_second_root_is_none_if_one_solution(self):
        roots = get_roots(1, -2, 1)
        self.assertIsNotNone(roots[0])
        self.assertIsNone(roots[1])

    def test_returns_none_for_complex_solution(self):
        roots = get_roots(1, 2, 3)
        self.assertIsNone(roots[0])
        self.assertIsNone(roots[1])

class QuadraticEquationGUI:
    def __init__(self, master):
        self.master = master
        master.title("Quadratic Equation Solver")

        self.label = Label(master, text="Enter coefficients (a, b, c):")
        self.label.pack()

        self.entry_a = Entry(master)
        self.entry_b = Entry(master)
        self.entry_c = Entry(master)

        self.entry_a.pack()
        self.entry_b.pack()
        self.entry_c.pack()

        self.result_var = StringVar()
        self.result_label = Label(master, textvariable=self.result_var)
        self.result_label.pack()

        self.solve_button = Button(master, text="Solve", command=self.solve_quadratic)
        self.solve_button.pack()

    def solve_quadratic(self):
        a = float(self.entry_a.get())
        b = float(self.entry_b.get())
        c = float(self.entry_c.get())

        roots = get_roots(a, b, c)

        if roots[0] is not None:
            result_str = f"Root 1: {roots[0].item()}"
            if roots[1] is not None:
                result_str += f"\nRoot 2: {roots[1].item()}"
        else:
            result_str = "No real roots."

        self.result_var.set(result_str)

if __name__ == '__main__':
    unittest.main()
    root = Tk()
    app = QuadraticEquationGUI(root)
    root.mainloop()
