#IMPORTANT NOTE: 
# All three of these sites were building blocks for creating the code I have down below
# This was my first time 
#“Tkinter — Python Interface to Tcl/Tk.” Python Software Foundation, https://docs.python.org/3/library/tkinter.html. Accessed 18 Apr. 2026.
#“Ordinary Differential Equations.” SymPy Documentation, https://docs.sympy.org/latest/modules/solvers/ode.html. Accessed 18 Apr. 2026.
# Bader, Dan. “Python GUI Programming With Tkinter.” Real Python, https://realpython.com/python-gui-tkinter/. Accessed 18 Apr. 2026.
#Imports
import sympy as sp
from sympy import pretty
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

# symbols
x = sp.symbols('x')
y = sp.Function('y')

last_sol = None
last_rhs = None


# classes
class ODESolver:
    def __init__(self, rhs_expr):
        self.rhs = rhs_expr
        self.eq = sp.Eq(sp.diff(y(x), x), self.rhs)

    def classify_ode(self):
        if not self.rhs.has(y(x)):
            return "Trivial (no y)"

        if sp.separatevars(self.rhs, symbols=[x, y(x)]):
            return "Separable"

        return "Nonlinear"

    def solve(self, ics=None):
        result = sp.dsolve(self.eq, ics=ics)

        if isinstance(result, list):
            return result[0]

        return result

    def separable_steps(self):
        Y = sp.symbols('Y')
        rhs_temp = self.rhs.subs(y(x), Y)

        separated = sp.separatevars(rhs_temp, symbols=[x, Y], dict=True)

        if not isinstance(separated, dict):
            return None

        f_x = separated.get(x, 1)
        g_y = separated.get(Y, 1)

        left = sp.integrate(1/g_y, y(x))
        right = sp.integrate(f_x, x)

        return sp.Eq(left, right)


# classify ODE
def classify_ode(rhs):
    if not rhs.has(y(x)):
        return "Trivial (no y)"

    if sp.separatevars(rhs, symbols=[x, y(x)]):
        return "Separable"

    return "Nonlinear"


# solve ODE
def solve_ode():
    global last_sol, last_rhs

    try:
        rhs = sp.sympify(entry.get())

        solver = ODESolver(rhs)
        eq = solver.eq

        output.delete("1.0", tk.END)

        output.insert(tk.END, "ODE:\n")
        output.insert(tk.END, pretty(eq, use_unicode=True) + "\n\n")

        output.insert(tk.END, "Type:\n")
        output.insert(tk.END, solver.classify_ode() + "\n\n")

        # ICs
        ics = None
        if use_ic.get():
            try:
                x0 = float(x0_entry.get())
                y0 = float(y0_entry.get())
                ics = {y(x).subs(x, x0): y0}
            except:
                output.insert(tk.END, "Bad ICs\n")

        sol_raw = solver.solve(ics)

        # handle list output safely
        if isinstance(sol_raw, list):
            sol = sol_raw[0]
        else:
            sol = sol_raw

        output.insert(tk.END, "Solution:\n")
        output.insert(tk.END, pretty(sol, use_unicode=True))

        last_sol = sol
        last_rhs = rhs

    except Exception as e:
        messagebox.showerror("Error", str(e))


# step solver
def solve_separable_steps():
    try:
        rhs = sp.sympify(entry.get())
        solver = ODESolver(rhs)

        output.delete("1.0", tk.END)

        output.insert(tk.END, "Step 1: Start ODE\n")
        output.insert(tk.END, pretty(solver.eq, use_unicode=True) + "\n\n")

        result = solver.separable_steps()

        if result is None:
            output.insert(tk.END, "Not separable.\n")
            return

        output.insert(tk.END, "Step 2: Integrated form\n")
        output.insert(tk.END, pretty(result, use_unicode=True))

    except Exception as e:
        messagebox.showerror("Error", str(e))


# plot solution
def plot_sol():
    try:
        if last_sol is None:
            raise ValueError()

        f = sp.lambdify(x, last_sol.rhs, "numpy")
        xs = np.linspace(-5, 5, 200)

        plt.plot(xs, f(xs))
        plt.title("Solution")
        plt.grid()
        plt.show()

    except:
        messagebox.showerror("Error", "Solve first")


# slope field
def slope():
    try:
        if last_rhs is None:
            raise ValueError()

        f = sp.lambdify((x, y(x)), last_rhs, "numpy")

        X, Y = np.meshgrid(np.linspace(-5, 5, 15),
                           np.linspace(-5, 5, 15))

        U = np.ones_like(X)
        V = f(X, Y)

        plt.quiver(X, Y, U, V)
        plt.title("Slope Field")
        plt.show()

    except:
        messagebox.showerror("Error", "Solve first")


# UI
root = tk.Tk()
root.title("ODE Solver")

tk.Label(root, text="dy/dx =").pack()

entry = tk.Entry(root, width=40)
entry.pack()

use_ic = tk.IntVar()
tk.Checkbutton(root, text="ICs", variable=use_ic).pack()

tk.Label(root, text="x0").pack()
x0_entry = tk.Entry(root)
x0_entry.pack()

tk.Label(root, text="y0").pack()
y0_entry = tk.Entry(root)
y0_entry.pack()

tk.Button(root, text="Solve", command=solve_ode).pack()
tk.Button(root, text="Solve Separable (Steps)", command=solve_separable_steps).pack()
tk.Button(root, text="Plot", command=plot_sol).pack()
tk.Button(root, text="Slope", command=slope).pack()

output = tk.Text(root, height=18, width=60)
output.pack()

root.mainloop()