import os 


def create_file(filename) :
    try :
        with open(filename , 'x') :
            print(f"file Name {filename}: Created successfully !" )
    except FileExistsError :
        print(F"File name {filename} already exist")
    except Exception as E :
        print('An error exists')        

def view_all_files() :
    files  =os.listdir()
    if not files :
        print('No files  found')
    else :
        print('Files in discharge!')
        for file in files :
            print(file)     

def delete_file(filename) :
    try :
        os.remove(filename)
        print(f'{filename}')    
    except FileNotFoundError : 
        print('File not found')
    except Exception as E :
        Print('An error occured')

def read_file(filename) :
    try :
        with open('sample.txt' , 'r') as R :
            content = R.read()
            print(f"Content of '{filename}' : \n{content}")
    except FileNotFoundError :
        print(f"{filename} doesnt exist")
    except Exception as e :
        print('An Error has occurred')            

def edit_file(filename) :
    try :
        with open('sample.txt' , 'a') as  f :
            content = input('Enter data to add : ')
            f.write(content + "\n")
            print('Content added to {filename} Successfully')
    except FileExistsError :
        print(f"{filename} not found ")
    except Exception as e : 
        print('an error occurred ')            


def main():

    while True :
        print("FILE MANAGEMENT APP")
        print('1:CREATE file')
        print('2: VIEW ALL FILES')
        print('3: DELETE FILES')
        print('4: READ FILES')
        # print('5 : WRITE FILES')
        print('5 : EdIT FILES')
        print('6 :EXITS')

        choice  = input("Enter Your choice(1-6) = ")

        if choice == '1':
            filename = input("Enter file Name : ")
            create_file(filename)
        elif choice == '2':
            view_all_files()   
        elif choice == '3':
            filename = input("Enter file name of to delete")
            delete_file(filename)
        elif choice == "4" :
            filename = input("Enter file name to read ")
            read_file(filename) 
        elif choice == '5' :
            filename = input("Enter content to edit")
            edit_file(filename)      
        elif choice == "6" :
                      print("Closing the app....")
                      break
        else :
            print('In-valid syntax')     

if __name__ == "__main__" :
    main()                      