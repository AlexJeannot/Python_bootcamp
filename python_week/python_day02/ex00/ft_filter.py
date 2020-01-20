def ft_filter(function, list_iter):
    tmp_list = []
    for elem in list_iter:
        if function(elem):
            tmp_list.append(elem)
    return tmp_list
