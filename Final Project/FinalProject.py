import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

# Variable/Funtion
x = sp.symbols('x')
y = sp.Function('y')

# Classification of ODE 
def classify_ode(rhs):
    try:
        if sp.separatevars(rhs, symbols=[x, y(x)]):
            return "Separable"
    except:
        pass
    
    if rhs.has(y(x)):
        return "First-order linear"
    
    return "Unknown"


def solve_ode():
    try:
        rhs = sp.sympify(entry.get())

        eq = sp.Eq(sp.diff(y(x), x), rhs)

        output.delete("1.0", tk.END)
        output.insert(tk.END, "ODE:\n")
        output.insert(tk.END, str(eq) + "\n\n")

        output.insert(tk.END, "Type:\n")
        output.insert(tk.END, classify_ode(rhs) + "\n\n")

        # initial conditions
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

def solve_with_steps_gui(rhs_input, ics_input, output_box):
    output_box.delete("1.0", tk.END)

    try:
        rhs = sp.sympify(rhs_input)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid RHS:\n{e}")
        return

    ics = None
    if ics_input.strip():
        try:
            ics = eval(ics_input)  # example: {y(0): 1}
        except:
            messagebox.showerror("Error", "Invalid ICs format")
            return

    eq = sp.Eq(sp.diff(y(x), x), rhs)

    output_box.insert(tk.END, "Differential Equation:\n")
    output_box.insert(tk.END, str(eq) + "\n\n")

    ode_type = classify_ode(rhs)
    output_box.insert(tk.END, f"Type: {ode_type}\n\n")

#s
    if ode_type == "Separable":
        output_box.insert(tk.END, "Step by Step Solution:\n")

        Y = sp.symbols('Y')
        rhs_temp = rhs.subs(y(x), Y)

        separated = sp.separatevars(rhs_temp, symbols=[x, Y], dict=True)

        if separated:
            f_x = separated[x]
            g_y = separated[Y]

            output_box.insert(tk.END, "1) Separate variables:\n")
            output_box.insert(tk.END, str(sp.Eq(1/g_y * sp.diff(y(x), x), f_x)) + "\n\n")

            output_box.insert(tk.END, "2) Integrate both sides:\n")
            left = sp.integrate(1/g_y, y(x))
            right = sp.integrate(f_x, x)

            output_box.insert(tk.END, str(sp.Eq(left, right)) + "\n\n")
        else:
            output_box.insert(tk.END, "Could not separate variables.\n\n")
    try:
        solution = sp.dsolve(eq, ics=ics) if ics else sp.dsolve(eq)
        output_box.insert(tk.END, "Final Solution:\n")
        output_box.insert(tk.END, str(solution))
    except Exception as e:
        messagebox.showerror("Solve Error", str(e))
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


# UI
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