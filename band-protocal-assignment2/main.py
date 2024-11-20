from chickenrescue import chicken_rescue
def main():
    _,k= input("Please enter the number of chickens and length of the roof Superman: ").split(" ")
    positions = input("Please enter the positions: ")
    positions = list(map(int, positions.split(" ")))
    print(chicken_rescue(positions, int(k)))


if __name__ == "__main__":
    main()