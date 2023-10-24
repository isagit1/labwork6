#isa desapio
def encode(s):
    a=[]
    D={"7":0,"8":1,"9":2}
    for i in s:
        if int(i)>=7:
            x=D[i]
            a.append(x)
        else:
            a.append(int(i)+3)
    b=[]
    for l in a:
        b.append(str(l))
    s="".join(b)
    return s


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice=input("Please enter an option:")
        choice=int(choice)

        if choice==1:
            s=input("Please enter your password to encode:")
            x=encode(s)
            s=x
            print("Your password has been encoded and stored!")
            print()
        if choice==2:
            orig=decode(s)
            print(f"The encoded password is {s}, and the original password is {orig}.")
        if choice==3:
            break

if __name__ == "__main__":
    main()