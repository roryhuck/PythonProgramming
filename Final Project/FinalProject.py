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
        eq = sp.Eq(sp.diff(y(x), x), rhs)

        output.delete("1.0", tk.END)

        output.insert(tk.END, "ODE:\n")
        output.insert(tk.END, pretty(eq, use_unicode=True) + "\n\n")

        output.insert(tk.END, "Type:\n")
        output.insert(tk.END, classify_ode(rhs) + "\n\n")

        # ICs
        ics = None
        if use_ic.get():
            try:
                x0 = float(x0_entry.get())
                y0 = float(y0_entry.get())
                ics = {y(x).subs(x, x0): y0}
            except:
                output.insert(tk.END, "Bad ICs\n")

        sol = sp.dsolve(eq, ics=ics) if ics else sp.dsolve(eq)

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
        eq = sp.Eq(sp.diff(y(x), x), rhs)

        output.delete("1.0", tk.END)

        output.insert(tk.END, "Step 1: Start ODE\n")
        output.insert(tk.END, pretty(eq, use_unicode=True) + "\n\n")

        Y = sp.symbols('Y')
        rhs_temp = rhs.subs(y(x), Y)

        separated = sp.separatevars(rhs_temp, symbols=[x, Y], dict=True)

        if not isinstance(separated, dict):
            output.insert(tk.END, "Not separable.\n")
            return

        f_x = separated.get(x, 1)
        g_y = separated.get(Y, 1)

        output.insert(tk.END, "Step 2: Separable form\n")
        output.insert(tk.END, "dy/dx = f(x)*g(y)\n\n")

        output.insert(tk.END, "Step 3: Separation\n")
        sep_eq = sp.Eq(1/g_y * sp.diff(y(x), x), f_x)
        output.insert(tk.END, pretty(sep_eq, use_unicode=True) + "\n\n")

        output.insert(tk.END, "Step 4: Integration\n")

        left = sp.integrate(1/g_y, y(x))
        right = sp.integrate(f_x, x)

        integrated_eq = sp.Eq(left, right)
        output.insert(tk.END, pretty(integrated_eq, use_unicode=True) + "\n\n")

        output.insert(tk.END, "Step 5: Solve for y\n")

        try:
            sol = sp.solve(left - right, y(x))
            output.insert(tk.END, pretty(sol, use_unicode=True))
        except:
            output.insert(tk.END, "Could not solve explicitly\n")

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