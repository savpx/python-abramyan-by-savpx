def Mean(X, Y):
    Amean = (X + Y) / 2
    Gmean= (X*Y)**0.5
    return (Amean, Gmean)
print(Mean (10, 5))