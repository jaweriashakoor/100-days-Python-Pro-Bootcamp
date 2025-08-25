# def format_name(fname,lname):
#     print(fname.title())# title means starts with capital letter and all others are small
#     return(lname.title())
# format_name("jaweria","JAWERIA")

# def function(text):
#     return text
# output=function("Hello")
# print(output)


# def function(text):
#     return text
# function("Hello")



def format_name(fname,lname):
    if fname=="" or lname=="":
        return "You did not provide valid inputs"
    formatted_f_name=fname.title()
    formatted_l_name=lname.title()
    return f"Result:{formatted_f_name} {formatted_l_name}"
# print(format_name("jaweria","JAWERIA"))
print(format_name(input("What is Your First Name?"), input("What is your last name?")))


def format_name(fname,lname):
    # if fname=="" or lname=="":
    #     return "You did not provide valid inputs"
    formatted_f_name=fname.title()
    formatted_l_name=lname.title()
    return f"Result:{formatted_f_name} {formatted_l_name}"

# print(format_name("jaweria","JAWERIA"))
print(format_name(input("What is Your First Name?"), input("What is your last name?")))



