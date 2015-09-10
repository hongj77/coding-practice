


def powerset(ls):
    def powerset_helper(ls,i):
        if i == len(ls):
            return [[]]
        power_rest = powerset_helper(ls, i+1)
        print "powerrest is ", power_rest

        new_insert = []
        elem = ls[i]
        for subset in power_rest:  
            new_insert.append(subset + [elem])
        return power_rest + new_insert
    return powerset_helper(ls, 0)


ls = [1,2,3,4]
print powerset(ls)