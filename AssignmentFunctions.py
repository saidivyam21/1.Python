class multipleFunctions():
     def Subfields():
         feildsList = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
         print("Sub-fields in AI are:")
         for feild in feildsList:
           print(feild)

     def OddEven():
         data = int(input("Enter a Number :"))
         if(data % 2 == 0):
             print(f"{data} is Even number")

     def Elegible():
         gender = str(input("Your Gender: "))
         age = int(input("Your Age:"))
         if(gender == "Male" and age <21 ):
             print("NOT ELIGIBLE")
         elif(gender == "Male" and age >=21 ):
             print("ELIGIBLE")
         elif(gender == "Female" and age <18 ):
             print("NOT ELIGIBLE")
         elif(gender == "Female" and age >=18 ):
             print("ELIGIBLE")

     def percentage():
        Subject1= int(input("Subject1 :"))
        Subject2= int(input("Subject2 :"))
        Subject3= int(input("Subject3 :"))
        Subject4= int(input("Subject4 :"))
        Subject5= int(input("Subject5 :"))
        total = Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total : ",total)
        print("percentage : ", total/5)

        
     def triangle():
        height = int(input("Height :"))
        breath = int(input("Breath :"))
        area = (height * breath)/2
        print("Area formula:(Height * Breath)/2")
        print("Area of Triangle: ",area)
        height1 = int(input("Height1 :"))
        height2= int(input("Height2 :"))
        breath2 = int(input("Breath :"))
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter= height1+height2+breath2
        print("Perimeter of Triangle:  ",perimeter)
