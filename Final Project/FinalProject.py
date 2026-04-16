import sympy as sp
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
        output.insert(tk.END, "ODE:\n" + str(eq) + "\n\n")
        output.insert(tk.END, "Type:\n" + classify_ode(rhs) + "\n\n")

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

        output.insert(tk.END, "Solution:\n" + str(sol))

        last_sol = sol
        last_rhs = rhs

    except Exception as e:
        messagebox.showerror("Error", str(e))


# step solver
def solve_with_steps(rhs_input, output_box):
    output_box.delete("1.0", tk.END)

    try:
        rhs = sp.sympify(rhs_input)
    except:
        messagebox.showerror("Error", "Invalid RHS")
        return

    eq = sp.Eq(sp.diff(y(x), x), rhs)

    output_box.insert(tk.END, "ODE:\n" + str(eq) + "\n\n")
    ode_type = classify_ode(rhs)
    output_box.insert(tk.END, "Type: " + ode_type + "\n\n")

    if ode_type == "Separable":
        try:
            Y = sp.symbols('Y')
            temp = rhs.subs(y(x), Y)

            sep = sp.separatevars(temp, symbols=[x, Y], dict=True)

            if isinstance(sep, dict):
                f_x = sep.get(x, 1)
                g_y = sep.get(Y, 1)

                output_box.insert(tk.END, "Separate:\n")
                output_box.insert(tk.END, str(sp.Eq(sp.diff(y(x), x), f_x * g_y)) + "\n\n")

                left = sp.integrate(1/g_y, Y)
                right = sp.integrate(f_x, x)

                output_box.insert(tk.END, "Integrate:\n")
                output_box.insert(tk.END, str(sp.Eq(left, right)) + "\n\n")

        except:
            output_box.insert(tk.END, "Could not separate\n")

    try:
        sol = sp.dsolve(eq)
        output_box.insert(tk.END, "Final:\n" + str(sol))
    except:
        messagebox.showerror("Error", "Solve failed")


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
tk.Button(root, text="Plot", command=plot_sol).pack()
tk.Button(root, text="Slope", command=slope).pack()

output = tk.Text(root, height=18, width=60)
output.pack()

root.mainloop()