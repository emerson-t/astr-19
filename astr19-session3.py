def f(x):                #define f(x)
    return x**3 + 8      #returns the function


def main():              #define main program
    x = 9                #define integer x with the value 9
    print("f(x) = x**3 + 8\n\nWhen x =",x,", f(x) =",f(x))
#^^ printing the math done for f(x) to get the final result

    if f(x) > 27:
        print("\nYAY!")        #result if f(x) > 27

    else:
        print("\nTry again!")  #result if f(x) < 27


#if the main() function exists, run it
if __name__ == "__main__":
    main()
