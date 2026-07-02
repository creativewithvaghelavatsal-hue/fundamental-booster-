print("\n=========welcome to the interactive data colletor=========")

a=input("please enter your name :")
b=int(input("please enter your age :"))
c=float(input("please enter your height in meters :"))
d=int(input("please enter your favourite number :"))

print("\nthank you ! Here is in the information we collectted")


print(f"{a}:type :{type(a)} : Memory address :{id(a)}")
print(f"{b}:type :{type(b)}: Memory address :{id(b)}")
print(f"{c}:type :{type(c)}: Memory address :{id(c)}")
print(f"{d}:type :{type(d)} : Memory address :{id(d)}")
print("")

print("\nHere is your approximenty birth year :", 2026-b ,"(based on your age) =",b)

print("\nThank you for using personal data colletor,Have a good day,",a)
