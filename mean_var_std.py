import numpy as np

def calculate(list):
    if len(list)<9:
        return "List must contain nine numbers."
    else:
        A=np.reshape(list,(3,3))
        AT=A.transpose()
        Dictionary=dict([
                        ("mean", [[AT[i].mean() for i in range(0,3)], [A[i].mean() for i in range(0,3)], A.mean()]),
                        ("variance", [[AT[i].var() for i in range(0,3)], [A[i].var() for i in range(0,3)], A.var()]),
                        ("standard deviation", [[AT[i].std() for i in range(0,3)], [A[i].std() for i in range(0,3)], A.std()]),
                        ("max", [[AT[i].max() for i in range(0,3)], [A[i].max() for i in range(0,3)], A.max()]),
                        ("min", [[AT[i].min() for i in range(0,3)], [A[i].min() for i in range(0,3)], A.min()]),
                        ("sum", [[AT[i].sum() for i in range(0,3)], [A[i].sum() for i in range(0,3)], A.sum()])
        ])
        return Dictionary