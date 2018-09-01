def test(a):
    if a > 1:
        result = a * test(a - 1)
    else:
        result = 1
    return result

def test1(a):
    result = 1
    i = 1
    while i <= a:
        result *= i
        i +=1
    print(result)

result = test(5)
print(result)
test1(5)