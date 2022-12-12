from tools import add_intercept
import numpy as np

def	predict_(x, theta):
    x_=add_intercept(x)
    return(np.matmul(x_, theta))

if __name__=="__main__":
    x = np.arange(1,6)
    theta1 = np.array([[5], [0]])
    # print(predict_(x, theta1))
    theta2 = np.array([[0], [1]])
    # print(predict_(x, theta2))
    theta3 = np.array([[5], [3]])
    # print(predict_(x, theta3))
    theta4 = np.array([[-3], [1]])
    print(predict_(x, theta4))
