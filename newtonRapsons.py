import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


x = sp.Symbol('x')
expr = sp.cos(x) + 2 * sp.sin(x) - x*x
derivative_expr = sp.diff(expr, x)


f = sp.lambdify(x, expr, 'numpy')
f_prime = sp.lambdify(x, derivative_expr, 'numpy')


def newtonRaphson(a, tol=1e-3, maxItr=100):
    x = a
    for i in range(maxItr):
        fx = f(x)
        fxP = f_prime(x)
        
        if abs(fxP) < 1e-6:  
            print("Derivative too small. Newton-Raphson failed.")
            return None
        
        x1 = x - fx / fxP
        
        if abs(x1 - x) < tol: 
            return x1
        
        x = x1  

    print("Max iterations reached. No root found.")
    return None  


value = newtonRaphson(1.0)
print("Root found:", value)


x_vals = np.linspace(-5, 5, 100)
y_vals = f(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label=r"$f(x) = \cos(x) + 2\sin(x) - x^2$", color="blue")


if value is not None:
    plt.scatter(value, f(value), color="red", zorder=3, label=f"Root at x={value:.3f}")
    plt.axvline(x=value, color="red", linestyle="--", linewidth=1.5)


plt.axhline(0, color="black", linestyle="--", linewidth=1)
plt.axvline(0, color="black", linestyle="--", linewidth=1)


plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Newton-Raphson Method Visualization")
plt.legend()
plt.grid(True)


plt.show()
