def ft_reduce(function, list_iter):
    i = 0
    for elem in list_iter:
        if i == 0:
            try:
                total = function(elem, list_iter[i + 1])
                i += 1
            except:
                return elem
        else:
            try:
                total = function(total, list_iter[i + 1])
                i += 1
            except:
                return total
    return total
