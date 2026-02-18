def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name("anfisa", "aditya"))

print(len("Angelo"))

def function_1(text):
    return text + text
print(function_1("Angelo"))

def function_2(text):
    return text.title()
print(function_2("ANgElo"))

output = function_2(function_1("hEllO"))
print(output)