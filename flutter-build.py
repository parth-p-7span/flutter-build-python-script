import os

"""
How to use this script?

Step 1: add your flutter sdk path in `sdk_path` variable below.

step 2: if your sdk path contains spaces in floder names then must enclose with double quotes
    e.x. 
        1. D:\"flutter v2.8.0"\bin
        2. D:\flutter\bin

Step 3: copy this script to your flutter project's root folder.

Step 4: run this script in terminal/cmd/shell

"""

sdk_path = r'D:\"flutter v2.8.0"\bin'

def askFirst():
    print("""===================Flutter Build Type===================\n
        1. Release  
        2. Debug
        3. Exit
        """)
    while True:
        try:
            a = int(input("   Please enter your choice [1-3]: "))
            if a in range(1, 4):
                break
        except:
            continue
    return a


def askSecond():
    print("""===================Flutter Build output===================\n
        1. Production
        2. Development
        3. Restart
       """)

    while True:
        try:
            a = int(input("   Please enter your choice [1-3]: "))
            if a in range(1, 4):
                break
        except:
            continue
    return a


def askThird():
    print("""===================APK OR Bundle===================\n
        1. APK
        2. Bundle
        3. Restart
           """)

    while True:
        try:
            a = int(input("   Please enter your choice [1-3]: "))
            if a in range(1,4):
                break
        except:
            continue
    return a


def main():
    print("""
     ______   _           _     _                            ____            _   _       _ 
    |  ____| | |         | |   | |                          |  _ \          (_) | |     | |
    | |__    | |  _   _  | |_  | |_    ___   _ __   ______  | |_) |  _   _   _  | |   __| |
    |  __|   | | | | | | | __| | __|  / _ \ | '__| |______| |  _ <  | | | | | | | |  / _` |
    | |      | | | |_| | | |_  | |_  |  __/ | |             | |_) | | |_| | | | | | | (_| |
    |_|      |_|  \__,_|  \__|  \__|  \___| |_|             |____/   \__,_| |_| |_|  \__,_|                                                                                      
    """)

    a = askFirst()

    #selected release
    if a == 1:
        print()
        b = askSecond()
        if b == 3:
            os.system('clear')
            main()
        print()
        c = askThird()
        if c == 3:
            os.system('clear')
            main()
        #selected production
        if b==1:
            #selected APK
            if c == 1:
                command = os.path.join(sdk_path,"flutter")+' build apk --no-sound-null-safety --release -t lib/main_prod.dart'
                print(command)
                os.system(command)
                print("\033[42m\033[1;30m		APK Generated! :)\033[1;0m")

            #selected bundle1
            elif c == 2:
                os.system(os.path.join(sdk_path,"flutter")+' build appbundle --no-sound-null-safety --release -t lib/main_prod.dart')
                print("\033[42m\033[1;30m		Bundle Generated! :)\033[1;0m")

        # selected Development
        if b == 2:
            # selected APK
            if c == 1:
                os.system(os.path.join(sdk_path,"flutter")+' build apk --no-sound-null-safety --release -t lib/main_dev.dart')
                print("\033[42m\033[1;30m		APK Generated! :)\033[1;0m")

            # selected bundle
            elif c == 2:
                os.system(os.path.join(sdk_path,"flutter")+' build appbundle --no-sound-null-safety --release -t lib/main_dev.dart')
                print("\033[42m\033[1;30m		Bundle Generated! :)\033[1;0m")

    #selected debug
    elif a == 2:
        print()
        c = askThird()
        if c == 3:
            os.system('cls')
            main()

        # selected APK
        elif c == 1:
            os.system(os.path.join(sdk_path,"flutter")+' build apk --no-sound-null-safety --debug -t lib/main_dev.dart')
            print("\033[42m\033[1;30m		APK Generated! :)\033[1;0m")

        # selected bundle
        elif c == 2:
            os.system(os.path.join(sdk_path,"flutter")+' build appbundle --no-sound-null-safety --release -t lib/main_dev.dart')
            print("\033[42m\033[1;30m		Bundle Generated! :)\033[1;0m")



    elif a == 3:
        print("\033[42m\033[1;30m		Bye Bye! :)\033[1;0m")
        exit()


if __name__ == "__main__":
    main()
