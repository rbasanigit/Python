# Sample Project
import pandas as pd
import matplotlib.pyplot as plt
import os
pd.set_option('display.max_columns',None)
print("\n\n\n","*"*30,"Movie Analysis","*"*30)
if not os.path.isfile("movie.csv"):
    df=pd.DataFrame()
else:
    df=pd.read_csv("movie.csv",index_col=0)

choice=0
while choice!=None:
    print("\n\t\t\t","-"*40)
    print("\t\t\t\t 1. Add Movie Details")
    print("\t\t\t\t 2. Display Movie Details")
    print("\t\t\t\t 3. Update Movie Details")
    print("\t\t\t\t 4. Remove Movie Details")
    print("\t\t\t\t 5. Graphical View")
    print("\t\t\t\t 6. Exit")
    print("\t\t\t","-"*40)
    print("*"*87)
    choice=int(input("Enter your choice : "))
    print("-"*87)
    if choice==1: # ADD DETAILS CODE
        print("\t\t","-"*10,"*"*5,"-"*10)
        name=input("Enter the Movie name : ")
        direct=input("Enter the Director : ")
        lan=input("Enter the Language : ")
        gen=input("Enter the Genre : ")
        date=input("Enter the Date of release (YYYY-MM-DD) : ")
        rate=eval(input("Enter the Rating : "))
        movie_dict={"Movie Name":name,"Director":direct,"Language":lan,"Genre":gen,"Date Of Release":date,"Rating":rate}
        if df.empty:
            df=pd.DataFrame(movie_dict,index=[0])
        else:
            df=df.append(movie_dict,ignore_index=True)

        df.to_csv("movie.csv")
        print("*"*20,"Details added successfully","*"*20)

    elif choice==2: #DISPLAY DETAILS CODE
     
        if not os.path.isfile("movie.csv"):
            print("\n\t\t Sorry!!! No details Available...Kindly Add details")
        else:
            print("*"*20,"Displaying Details","*"*20)
            df=pd.read_csv("movie.csv",index_col=0)
            print(df)
            print("*"*20,"Details printed successfully","*"*20)

    elif choice==3: # UPDATE DETAILS CODE
        if not os.path.isfile("movie.csv"):
            print("\n\t\t Sorry!!! No details Available...Kindly Add Movie details")
        else:
            print("*"*20,"Displaying Details","*"*20)
            df=pd.read_csv("movie.csv",index_col=0)
            print(df)
            print("\t\t","-"*10,"*"*5,"-"*10)
            row_index=int(input("Enter the Row index for which you want to update the value : "))
            c_name=input("Enter the Column name for which you want to update the value: ")
            newvalue=input("Enter the New value : ")
            cnt=len(df)
            for i in range(cnt):
                if i==row_index:
                    if c_name=="Movie Name":
                        df.iloc[i,0]=eval(newvalue)
                    elif c_name=="Director":
                        df.iloc[i,1]=newvalue
                    elif c_name=="Language":
                        df.iloc[i,2]=eval(newvalue)
                    elif c_name=="Genre":
                        df.iloc[i,3]=eval(newvalue)
                    elif c_name=="Date Of Release":
                        df.iloc[i,4]=eval(newvalue)
                    elif c_name=="Rating":
                        df.iloc[i,5]=eval(newvalue)
                    else:
                        print("\n\n","@"*10,"Enter the correct column name as it is case sensitive","@"*10)
            df.to_csv("movie.csv")
            print("\t\t***** Details Updated successfully *****")
            
    elif choice==4: # REMOVE DETAILS CODE
        if not os.path.isfile("movie.csv"):
            print("\n\t\t Sorry!!! No details Available...Kindly Add details")
        else:
            print("*"*20,"Displaying Details","*"*20)
            df=pd.read_csv("movie.csv",index_col=0)
            print(df)
            print("\t\t","-"*10,"*"*5,"-"*10)
            value=int(input("Enter the row index on which you want to remove the record : "))
            df=df.drop([value])
            df.to_csv("movie.csv")
            print("\t\t***** Record deleted successfully *****")
    
    elif choice==5: # GRAPHICAL REPRESENTATION CODE
        if not os.path.isfile("movie.csv"):
            print("\n\t\t Sorry!!! No details Available...Kindly Add Movie details")
        else:
            choice2=0
            while choice2!=50:
                print("Choose any of the following graphs : ")
                print("10.Bar Graph Of Movie Rating")
                print("20.Line Graph Of Date Of Release")
                print("30.Histogram Of Languages")
                print("40.Exit Graphical View")
                choice2=int(input("Enter your choice : "))
                if choice2==10:
                    print("\t\t","-"*10,"*"*5,"BAR GRAPH","*"*5,"-"*10)
                    n=df["Movie Name"]
                    s=df["Rating"]
                    plt.xlabel('Movie Name')
                    plt.ylabel('Rating')
                    plt.title('Movie Ratings')
                    plt.bar(n,s,width=.4,color='orange')
                    plt.show()
                elif choice2==20:
                    print("\t\t","-"*10,"*"*5,"LINE GRAPH","*"*5,"-"*10)
                    m=df["Movie Name"]
                    y=df["Date Of Release"]
                    #y1=y
                    #print(y1)
                    plt.xlabel('Movie Name')
                    plt.ylabel('Date Of Release')
                    plt.title('Release Date')
                    plt.plot(m,y,color='red')
                    plt.show()
                elif choice2==30:
                    print("\t\t","-"*10,"*"*5,"HISTOGRAM","*"*5,"-"*10)
                    l=df["Language"]
                    plt.hist(l)
                    plt.show()  
                elif choice2==40:
                    choice2=50
                    print('\n\t\t\t\t !!! THANK YOU !!!')
                else:
                    print("Please Enter VALID CHOICES")
            #df.to_csv("sample.csv")
    
    elif choice==6: # EXIT CODE
        print('\n\t\t\t\t !!! THANK YOU !!!')
        choice=None

    else:
        print('\n\t\t\t ## PLEASE ENTER VALID CHOICES [1-5] ONLY ##')

# END OF PROJECT