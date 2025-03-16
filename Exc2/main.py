from Wales import Wales
from Windsor import Windsor
from Middleton import Middleton
from Spencer import Spencer

def main():
    Charles = Wales("Charles")
    Diana = Spencer("Diana")
    William = Wales("William")
    Kate = Middleton("Kate")
    George = Windsor("George")
    Charlotte = Windsor("Charlotte")

    print(Charles)
    print(Diana)
    print(William)
    print(Kate)
    print(George)
    print(Charlotte)    

if __name__ == "__main__":
    main()