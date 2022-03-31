
def main(): 
    print('Are you converting fahrenheit or celsius?')
    system = input('Please put f for fahreheit or c for celsius: ')
    if system == 'c':
        import c2f
    elif system =='f':
        import f2c
    else:
        print("Please try again")
if __name__ == "__main__":
    main()
