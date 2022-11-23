
def divide_by(a, b):
    try:
        return round(a / b, 2)
    except ZeroDivisionError:
        return 0
    except Exception as error:
        return "something went wrong: " + error  



result =  divide_by(40, 2)
print(result)