""" argumentos.py

Author: Alan Felix
Date:17/08/2026

"""


def main():
    """Main function to parse commmand-line arguments and options.
    python argumentos.py -n Alan -s 90

    """

    parser = argparse.ArgumentParser(description="Parse command-line arguments and options.")
    #add arguments
    parser.add_argument('-n','--name',type=str,required=True,help='Full name of student')
    parser.add_argument('-s','--score',type=int,required=True,help='Score of student')
    #parse the arguments
    args = parser.parse_args()
    #print the parsed arguments
    args = parser.parse_args()
    #Print the parsed arguments
    print(f"Name: {args.name}")
    print(f"Score: {args.score}")

if __name__ == "__main__":
    main()    