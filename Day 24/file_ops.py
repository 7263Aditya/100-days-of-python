with open("C://Users/admin/Desktop/my_file.txt","r") as file:
    context = file.read()
    print(context)


with open("C://Users/admin/Desktop/new_file.txt", mode="a") as f:
    f.write("\nhello world")
