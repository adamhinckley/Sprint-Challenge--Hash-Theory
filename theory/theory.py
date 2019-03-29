for A in [False, True]:
    for B in [False, True]:
        for C in [False, True]:
            print(
                f"{A} - {B} - {C} -- {not(A or B) or ( (A or C) and not(B or not C))}")
