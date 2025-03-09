from utils import api_utils
from utils import print_utils
while True:
    request = api_utils.get_fruit(input("Enter fruit name: "))
    print_utils.print_readable(request)
    print_utils.print_machine(request)