





def main():
    print("Please select from one of the following options:")
    print("pub: public     |    pri: private")
    answer = input()

    if answer=="pub":
        printPublicDatasets()


def printPublicDatasets():
    print("1: Argo Products\t\t\t2: CFSv2")
    print("3: CMIP5\t\t\t4: CSIRO Atlas")





if __name__ == "__main__":
    main()


