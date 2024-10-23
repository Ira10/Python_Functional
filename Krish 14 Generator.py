def count_up_to(n):
    count = 1
    while count <= n:
        yield count   ## return value || return count
        # count += 1
        return count


# print(count_up_to(7))

print(list(count_up_to(4)))
