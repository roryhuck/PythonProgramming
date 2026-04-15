import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

# symbols
x = sp.symbols('x')
y = sp.Function('y')

# very simple classification (intentionally basic)
def classify_ode(rhs):
    if rhs.has(y(x)):
        return "has y(x) (maybe linear/nonlinear)"
    return "no y(x) (maybe separable or simple)"


def solve_ode():
    try:
        rhs = sp.sympify(entry.get())

        eq = sp.Eq(sp.diff(y(x), x), rhs)

        output.delete("1.0", tk.END)
        output.insert(tk.END, "ODE:\n")
        output.insert(tk.END, str(eq) + "\n\n")

        output.insert(tk.END, "Type:\n")
        output.insert(tk.END, classify_ode(rhs) + "\n\n")

        # initial conditions (very basic handling)
        ics = None
        if use_ic.get() == 1:
            try:
                x0 = float(x0_entry.get())
                y0 = float(y0_entry.get())
                ics = {y(x0): y0}
            except:
                output.insert(tk.END, "Bad initial conditions input\n")

        sol = sp.dsolve(eq, ics=ics) if ics else sp.dsolve(eq)

        output.insert(tk.END, "Solution:\n")
        output.insert(tk.END, str(sol))

        global last_sol, last_rhs
        last_sol = sol
        last_rhs = rhs

    except Exception as e:
        messagebox.showerror("Error", str(e))


def plot_sol():
    try:
        f = sp.lambdify(x, last_sol.rhs, "numpy")

        xs = np.linspace(-5, 5, 100)
        ys = f(xs)

        plt.plot(xs, ys)
        plt.title("solution")
        plt.grid()
        plt.show()
    except:
        print("solve first")


def slope():
    try:
        f = sp.lambdify((x, y(x)), last_rhs, "numpy")

        X, Y = np.meshgrid(np.linspace(-5,5,15), np.linspace(-5,5,15))
        U = np.ones_like(X)
        V = f(X, Y)

        plt.quiver(X, Y, U, V)
        plt.title("slope field")
        plt.show()
    except:
        print("solve first")


# ---------------- UI (very simple layout) ----------------
root = tk.Tk()
root.title("ODE solver")

tk.Label(root, text="dy/dx =").pack()

entry = tk.Entry(root, width=40)
entry.pack()

use_ic = tk.IntVar()
tk.Checkbutton(root, text="IC?", variable=use_ic).pack()

tk.Label(root, text="x0").pack()
x0_entry = tk.Entry(root)
x0_entry.pack()

tk.Label(root, text="y0").pack()
y0_entry = tk.Entry(root)
y0_entry.pack()

tk.Button(root, text="solve", command=solve_ode).pack()
tk.Button(root, text="plot", command=plot_sol).pack()
tk.Button(root, text="slope", command=slope).pack()

output = tk.Text(root, height=15, width=50)
output.pack()

last_sol = None
last_rhs = None

root.mainloop()