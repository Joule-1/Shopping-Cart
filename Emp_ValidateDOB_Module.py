

# Check The Date Of Birth Enterred By The Employee During Sign Up





import datetime
 


def dob_approval() :

    checkTime = datetime.datetime.now()
    print("\n\tEnter Your Date Of Birth In The Following Format (dd-mm-yyyy). \n\t\tFor example 01-10-1972")

    dob = input("\nEnter Your Date Of Birth : ")
    dob = dob.strip()

    # Check For Leap Year
    day = dob[0 : 2]
    month = dob[3 : 5]
    year = dob[6 : 10]


    if day.isdigit() == True and month.isdigit() == True and year.isdigit() == True and dob.isdigit() == False and len(dob) == 10 and day != "00" and month!= "00" and year != "0000" : 

    
        year = int(year)

        if year % 400 == 0 and year % 100 == 0 :
            leapYear = 29

        elif year % 4 == 0 and year % 100 != 0 :
            leapYear = 29

        else:
            leapYear = 28
        
        year = str(year)
        # Check For Leap Year

        if month == "01" or month == "03" or month == "05" or month == "07" or month == "08" or month == "10" or month == "12" :
            
            if int(day) <= 31 :
                
                if int(year) >= checkTime.year - 18 or int(year) <= checkTime.year - 90 :
                    print("\n\tFor Creating Account, You Must Be Born Before Year",checkTime.year - 18,"And After Year",checkTime.year - 90)
                    
                    
                else : 

                    return dob                                                       
            else : 
                print("\n\tEnter Correct Date Of Birth")
                

        elif month == "04" or month == "06" or month == "09" or month == "11" : 

            if int(day) <= 30 :
                    
                if int(year) >= checkTime.year - 18 or int(year) <= checkTime.year - 90 :
                    print("\n\tFor Creating Account, You Must Be Born Before Year",checkTime.year - 18,"And After Year",checkTime.year - 90)
                    
                else : 

                    return dob                                                                
            else : 
                print("\n\tEnter Your Correct Date Of Birth")
                
        elif month == "02" : 

            if int(day) <= leapYear   :
                    
                if int(year) >= checkTime.year - 18 or int(year) <= checkTime.year - 90 :
                    print("\n\tFor Creating Account, You Must Be Born Before Year",checkTime.year - 18,"And After Year",checkTime.year - 90)
                    
                else : 

                    return dob
                
            else : 
                print("\n\tEnter Your Correct Date Of Birth")
        else : 
            print("\n\tEnter Your Correct Date Of Birth")   

    else : 
            print("\n\tEnter Your Date Of Birth As Per The Format Shown")

    dob = False        
    return dob
