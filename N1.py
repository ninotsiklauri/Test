s = str(input("შემოიტანეთ სიტყვა: "))
x = s.isalpha()
if x == False:
    print("არ გამოიყენოთ რიცხვები და სხვა სიმბოლოები!")
else:
    reverse = s[::-1]
    if(reverse == s):
        print("პალინდრომია")
    else:
        print("არ არის პალინდრომი")
