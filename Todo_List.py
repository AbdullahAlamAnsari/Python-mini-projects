tasks = []
taskname = None
status = ["id","task","done"]
values = [None,None,None]
tasksdic = {}

tasks
taskcount = 0
taskindex = 0
done = True
while(done):
    choice = int(input("\n1.Add tasks\n2.Mark task as completed\n3.Delete task\n4.View pending & completed tasks"))

    match choice:
        case 1:
            taskcount += 1
            taskname = input("Enter the task name: ")
            values[0] = taskcount
            values[1] = taskname
            values[2] = False
            tasksdic = dict(zip(status,values))
            
            print((tasksdic))
            tasks.insert(taskindex,tasksdic)
            taskindex += 1
            print(tasks)
        case 2:
            taskname = input("Enter the task you have done: ")
            for taskdata in tasks:
                print(taskdata)
                for taskfinder in taskdata:
                    print(taskfinder)
                    if taskfinder == taskname:
                        tasks["done"] = True
                        print(f"CONGRATS YOU HAVE DONE {taskname}!")
                        print(tasks)

                    
        case 4:
            for task in tasks:
                for taskdata,taskinfo in task:
                    print(taskinfo) 
        case _:
            print("INVALID INPUT")


