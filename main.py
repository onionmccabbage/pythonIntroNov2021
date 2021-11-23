# import package.module
import utility.furniture
import utility.accountancy
import explore

# explore __name__ and custom naming

def main():
    # make both tables
    f = utility.furniture.table(40, 80)
    #   package.module
    a = utility.accountancy.table(3,7)
    return [f, a]

if __name__ == '__main__':
    # only THIS module code will run
    print( main() )