def balance(input_string):
    brackets_list = []
    try:      
        for char in input_string:
            if char in ["[","(","{"]:
                brackets_list.append(char)
            elif char == "]":
                if brackets_list.pop() != "[":
                    return 0
            elif char == ")":
                if brackets_list.pop() != "(":
                    return 0
            elif char == "}":
                if  brackets_list.pop() != "{":
                    return 0
    except IndexError:
        return 0
    
    # Fail if we still have brackets left in the brackets_list
    return int(not(brackets_list))

input_string = input()
print(balance(input_string))