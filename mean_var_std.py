import numpy as np

def calculate(list):
    if len(list)!=9:
        return "List must contain nine numbers."
    else:
        A=np.reshape(list,(3,3))
        calculates=dict([
                        ("mean", [A.mean(axis=0).tolist(), A.mean(axis=1).tolist(), A.mean()]),
                        ("variance", [A.var(axis=0).tolist(), A.var(axis=1).tolist(), A.var()]),
                        ("standard deviation", [A.std(axis=0).tolist(), A.std(axis=1).tolist(), A.std()]),
                        ("max", [A.max(axis=0).tolist(), A.max(axis=1).tolist(), A.max()]),
                        ("min", [A.min(axis=0).tolist(), A.min(axis=1).tolist(), A.min()]),
                        ("sum", [A.sum(axis=0).tolist(), A.sum(axis=1).tolist(), A.sum()])
        ])
        return calculates
