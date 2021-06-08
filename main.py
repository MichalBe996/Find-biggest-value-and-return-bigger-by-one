


def najwieksze(lista):
    max_number = max(lista)
    if max_number > 0:
        max_number += 1
        return(max_number)
    elif max_number < 0:
        while max_number <= 0:
            max_number += 1
        return(max_number)

