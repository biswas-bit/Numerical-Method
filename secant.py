import numpy as np
import matplotlib.pyplot as plt

class SecantMethod:
    def __init__(self, x0, x1, tol=1e-2, max_iter=100):
        self.x0 = x0
        self.x1 = x1
        self.tol = tol
        self.max_iter = max_iter

    def f(self, x):
        return 2*x*x + 4*x - 10  

    def calculate(self):
        for i in range(self.max_iter):
            f_x0 = self.f(self.x0)
            f_x1 = self.f(self.x1)

            if abs(f_x1 - f_x0) < 1e-6:  
                print("Secant method failed: Division by zero")
                return None

            
            x2 = self.x1 - (f_x1 * (self.x1 - self.x0)) / (f_x1 - f_x0)


            if abs(x2 - self.x1) < self.tol:
                return x2

            self.x0 = self.x1
            self.x1 = x2

        print("Max iterations reached. No root found.")
        return None



secant = SecantMethod(x0=1, x1=2)  
root = secant.calculate()

if root is not None:
    print(f"Root found: {root:.5f}")
else:
    print("Root not found.")
    
# graph
x = np.linspace(-10, 10,400)
y =secant.f(x)
plt.figure(figsize=(10,6))
plt.plot(x, y, label="2x² + 4x - 10", color="blue")
if x is not None:
    plt.scatter(root, secant.f(root),color="red",zorder=2,label=f"Root at x={root:.3f}")
    plt.axvline(root,color="red",linestyle="--")

plt.axhline(0, color="black",linestyle="--",linewidth=1)
plt.axvline(0, color="black",linestyle="--",linewidth=1)
plt.xlabel("x-axis")
plt.ylabel("f(x)")
plt.title("Graph of 2x² + 4x - 10")
plt.legend()
plt.gca().set_facecolor("black")
plt.grid()

plt.show()

