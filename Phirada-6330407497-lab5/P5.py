ADD, SUB, MUL, DIV = range(4)
def flexible_calculator(oper=ADD, output_format=float, *args):
    result = args[0]
    for n in args[1:]:
        if oper == ADD:
            result += n
        elif oper == SUB:
            result -= n
        elif oper == MUL:
            result *= n
        elif oper == DIV:
            try :
                result /= n
            except ZeroDivisionError:
                return "Cannot divide by zero"


    if output_format == float:
        result = float(result)
    elif output_format == int:
        result = int(result)
    return result


print(f"flexible_calculator(ADD,int,1) = {flexible_calculator(ADD,int,1)}")
print(f"flexible_calculator(ADD,int,1,2) = {flexible_calculator(ADD,int,1,2)}")
print(f"flexible_calculator(ADD,int,1,2,3,4) = {flexible_calculator(ADD,int,1,2,3,4)}")
print(f"flexible_calculator(MUL,int,2,3,4) = {flexible_calculator(MUL,int,2,3,4)}")
print(f"flexible_calculator(DIV,float,10,5,2) = {flexible_calculator(DIV,float,10,5,2)}")
print(f"flexible_calculator(DIV,float,5,0) = {flexible_calculator(DIV,float,5,0)}")
