from random import randint
import os


def main(iterations=100000) -> None:
    numbersToWrite = ''
    for i in range(iterations):
        numbersToWrite += f"{randint(1, 10000).__str__()},"
    if 'oopsie.csv' in os.listdir(os.getcwd()):
        print('File already exists, cannot override')
        return
    with open('oopsie.csv', 'w') as file:
        file.write(numbersToWrite)


if __name__ == '__main__':
    main()
