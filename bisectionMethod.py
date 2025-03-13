import numpy as np
import matplotlib.pyplot as plt

def f(x):
    equation=np.cos(x)+2*np.sin(x)-x*x;
    return equation

def initialGuess():
    for i in range(1,100):
        x0=i
        x1=i+1
        if(f(x0)*f(x1)<0):
            return x0,x1
    return None
        

x0,x1=initialGuess()

def bisectionMethod(x0,x1,er=1e-3,maxItr=100):
    if(f(x0)*f(x1)>0):
        print("Error: The initial guess does not bracket the root")
        return None
    for _ in range(maxItr):
        xm=(x0+x1)/2
        if(f(xm)==0 or abs(f(xm))<er):
            return xm
        if(f(x0)*f(xm)<0):
            x1=xm
        else:
            x0=xm
    return (x0+x1)/2
print(initialGuess())
root=bisectionMethod(x0,x1)
print(root)

x_vals=np.linspace(-5,10,1000) # puts the range
y_vals=f(x_vals)

plt.figure(figsize=(10,6))  # gives the size of window
plt.plot(x_vals, y_vals ,label="f(x) = cos(x) + 2sin(x) - x²",color="blue") # x-axis
plt.axhline(0,color="black", linestyle="--",linewidth=1)
plt.axvline(root,color='red',linestyle='--',label=f"root ≈ {root:.4f}") #root marker
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("graph of f(x) with Root approximation")
plt.legend()
plt.grid()

plt.show()
        
                       
                
