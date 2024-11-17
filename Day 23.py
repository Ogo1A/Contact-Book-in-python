names = []
phone_numbers = [기
num = int(input("Enter no of contact you want to save : *))
for i in range(num):
    name=input (*Name: ")
    phone_number = input("Phone Number: ")
    names.append (name)
phone_numbers.append (phone_number)
print (*\nName\t\t\&Phone Number\n*)
for i in range(num):
print（"（JItltit（）"，format（nanes【4】，phone_numbers【】））
search_term = input("\nEnter search term:
*)
print("Search result:")
1f search_term in names:
index = names.index(search_term)
phone_number = phone_numbers [index]
print("Name: (), Phone Number: ()". fornat(search_term, phone_number))
else: 
print ("Name Not Found")
