import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    calculations = {}
    mean_list = [0, 0, 0]
    var_list = [0, 0, 0]
    std_list = [0, 0, 0]
    max_list = [0, 0, 0]
    min_list = [0, 0, 0]
    sum_list = [0, 0, 0]

    array = np.array([[list[0],list[1],list[2]],[list[3],list[4],list[5]],[list[6],list[7],list[8]]])

    mean_list[0] = array.mean(axis=0).tolist()
    mean_list[1] = array.mean(axis=1).tolist()
    mean_list[2] = array.mean()
    calculations.update({"mean": mean_list})

    var_list[0] = array.var(axis=0).tolist()
    var_list[1] = array.var(axis=1).tolist()
    var_list[2] = array.var()
    calculations.update({"variance": var_list})

    std_list[0] = array.std(axis=0).tolist()
    std_list[1] = array.std(axis=1).tolist()
    std_list[2] = array.std()
    calculations.update({"standard deviation": std_list})

    max_list[0] = array.max(axis=0).tolist()
    max_list[1] = array.max(axis=1).tolist()
    max_list[2] = array.max()
    calculations.update({"max": max_list})

    min_list[0] = array.min(axis=0).tolist()
    min_list[1] = array.min(axis=1).tolist()
    min_list[2] = array.min()
    calculations.update({"min": min_list})

    sum_list[0] = array.sum(axis=0).tolist()
    sum_list[1] = array.sum(axis=1).tolist()
    sum_list[2] = array.sum()
    calculations.update({"sum": sum_list})

    return calculations

print(calculate([2,6,2,8,4,0,1,5,7]))
print(calculate([9,1,5,3,3,3,2,9,0]))
print(calculate([2,6,2,8,4,0,1,])) # Error
