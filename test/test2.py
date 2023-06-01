#Zad3
def n_min_max(numbers: list[float|int], n: int, min_max: bool=False) -> list:
    if all([isinstance(x, (int,float)) for x in numbers]):
        sort_numbers = numbers.copy()
        sort_numbers.sort(reverse=min_max)
        return sort_numbers[:n]
    else:
        return ["This list hasn't only numbers!"]
    
num = [1,8,-4,5.6,123,3.6]
print(n_min_max(num,4,True))
print(n_min_max(num,4))
print(n_min_max(num+['text'],4))
print(n_min_max(num+[False],4))