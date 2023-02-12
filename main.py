def main():
    ##################################################
    # Comlete your code here
    val1 = int(input('Enter your number'))
    val2 = int(input('Enter your number'))
    val3 = int(input('Enter your number'))
    
    total = val1 + val2 + val3
    print(f'Summation: \t {total:>20}')
    
    avg = total / 3
    print(f'Average: \t {avg:.2f}')
    ##################################################

    pass


if __name__ == '__main__':
    main()
