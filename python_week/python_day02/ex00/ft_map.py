def ft_map(function, iter):
    tmp_list = []
    for elem in iter:
        tmp_list.append(function(elem))
    return tmp_list
