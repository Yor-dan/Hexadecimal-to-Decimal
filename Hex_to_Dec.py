def hexToDec():
    try:
        hex = ['A', 'B', 'C', 'D', 'E', 'F']
        dec = [10, 11, 12, 13, 14, 15]
        
        x = input("\nEnter hex number: ").upper()
        power = 0
        convert = []
        
        for i in reversed(x):
            if i in hex:
                convert.append(dec[hex.index(i)]*16**power)
            else:
                convert.append(int(i)*16**power)
            power += 1
        
        print(f"\nDecimal equivalent: {sum(convert)}")
        
    except ValueError:
        print("\nInvalid Input!")
        
hexToDec()