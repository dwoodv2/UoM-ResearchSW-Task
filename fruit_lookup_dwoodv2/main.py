from fruit_lookup_dwoodv2.utils import api_utils
from fruit_lookup_dwoodv2.utils import print_utils

if __name__=="__main__": # Program which infinitely loops, asking the user for a fruit to enter.
    while True:
        try:
            request = api_utils.get_fruit(input("Enter fruit name: "))#
            print_utils.print_readable(request)
            print_utils.print_machine(request)
        except Exception as e:
            print(e)
