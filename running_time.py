def runnig_time():
    try:
        total =[]
        while True:
            user = input('enter the running time (To exist press an empty enter) : ')
            if not user:
                break
            total.append(int(user))
        if total:
            avg_running = sum(total)/(len(total))
            print (avg_running)
        else:
            print ("no time entered")
            
    except ValueError as e:
        print("That's not a valid number")

runnig_time()