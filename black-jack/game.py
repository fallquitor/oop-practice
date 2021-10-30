def ask_yes_no(q):
    ans = None
    while ans not in ("yes", "no", "y", "n"):
        ans = input(q).lower()
    return ans in ("yes", "y")

def ask_num(q, l=1, h=10000000):
    ans = None
    while ans not in range(l, h):
        try:
            ans = int(input(q))
        except:
            print("Введите число")

    return ans