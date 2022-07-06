def hexToDec():
    try:
        hex = ['A', 'B', 'C', 'D', 'E', 'F']
        dec = [10, 11, 12, 13, 14, 15]
        
        x = input("\nEnter hex number: ")
        power = 0
        convert = []
        
        for i in reversed(x):
            if i in hex:
                index = hex.index(i)
                convert.append(dec[index]*16**power)
                power += 1
            else:
                convert.append(int(i)*16**power)
                power += 1
        
        print(f"\nDecimal equivalent: {sum(convert)}")
    except ValueError:
        print("Invalid Input!")
        
hexToDec()