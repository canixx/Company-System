from abc import ABC,abstractmethod
class Company(ABC):
    def __init__(self,name,surname,gender,age,salary,id_number):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.__salary = salary
        self._id_number = id_number
        self.number_of_floors = 50

    @abstractmethod
    def raise_salary(self):
        pass

    @abstractmethod
    def lower_salary(self):
    	pass

    @abstractmethod
    def show(self):
        pass
	
    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_age(self):
        return self.age

    def get_salary(self):
        return self.__salary
    
    def get_id(self):
        return self._id_number
        
    def __del__(self):
    	print(f"{self.name} {self.surname} has left the company.")

class SoftwareEngineer(Company):
    def __init__(self,name,surname,gender,age,salary,id_number,project,department,years_of_work,languages):
        Company.__init__(name,surname,age,salary,id_number)
        self._project = project
        self.department = department
        self.years_of_work = years_of_work
        self.languages = languages

    def show(self):
        return f"Name : {self.name} \nSurname : {self.surname} \nGender : {self.gender} \nAge : {self.age} \nSalary : {self.__salary} \nID Number : {self._id_number} \nProject : {self._project} \nDepartment : {self.department} \nYears of Work : {self.years_of_work}"
    
    def get_salary(self):
    	return self.__salary
    
    def raise_salary(self,rate):
    	try:
    	    rate = int(rate)
    	
    	expect ValueError:
    	    print("Please enter a valid rate")	
        
        else:
            if self.years_of_work > 2:
            	self.__salary += self.__salary * rate * 2   
            else:
                self.__salary += self.__salary * rate
                  
    def lower_salary(self,rate):
    	try:
    	    rate = int(rate)
    	
    	expect ValueError or rate >= 1:
    	    print("Please enter a valid rate between 0 and 1 not included")	
        
        else:           
            self.__salary -= self.__salary * rate
           
                	           
    def get_department(self):
    	return self.department
    
    def set_department(self,new_department):
    	self.department == new_department
    	    
    def get_project(self):
    	return self._project
    
    def set_project(self,new_project):
    	self._project == new_project
    	
    def get_years_of_work(self):
        return self.years_of_work
    
    def set_years_of_work(self,add_year):
        try:
            add_year = int(add_year)
        except ValueError and add_year < 1:
            print("Please enter a value greater than or equal to 1")
        
        else:
            self.years_of_work += add_year          
    
    def is_senior(self):
    	if self.years_of_work > 2:
    	    return f"{self.name} is a senior software engineer."		
    	else:
    	    return f"{self.name} is a junior software engineer."
    	    
    def get_languages(self):
        return self.languages
        
    def add_languages(self,new_languages):
        new_languages = input("Split multiple items with ' , '")
        self.languages.append(new_languages.split(","))
    	   
    def meeting(self):
        return f"The CEO has called {self.name} {self.surname} to a meeting.")
    
class HumanResources(Company):
    def __init__(self,name,surname,gender,age,salary,id_number):
    	Company.__init__(self,self,name,surname,gender,age,salary,id_number):
    
    def show(self):
        return f"Name : {self.name} \nSurname : {self.surname} \nGender : {self.gender} \nAge : {self.age} \nSalary : {self.__salary} \nID Number : {self._id_number}"
        
    def raise_salary(self,rate):
    	try:
    	    rate = int(rate)
    	
    	expect ValueError:
    	    print("Please enter a valid rate")	
        
        else:
            self.__salary += self.__salary * rate
    
    def lower_salary(self,rate):
    	try:
    	    rate = int(rate)
    	
    	expect ValueError or rate >= 1:
    	    print("Please enter a valid rate")	
        
        else:
            self.__salary -= self.__salary * rate

class Security(Company):
    def __init__(self,name,surname,gender,age,salary,id_number,shift_time):
    	Company.__init__(self,self,name,surname,gender,age,salary,id_number)
    	self.shift_time = shift_time
    	
      	def show(self):
        return f"Name : {self.name} \nSurname : {self.surname} \nGender : {self.gender} \nAge : {self.age} \nSalary : {self.__salary} \nID Number : {self._id_number} \nShift Time : {self.shift_time}"
        
    def raise_salary(self,rate):
    	try:
    	    rate = int(rate)
    	
    	expect ValueError:
    	    print("Please enter a valid rate")	
        
        else:
            if self.shift_time == "Night":
                self.__salary += self.__salary * rate * (1.80)
            else:
                self.__salary += self.__salary * rate 

    def lower_salary(self,rate):
    	try:
    	    rate = int(rate)
    	
    	expect ValueError or rate >= 1:
    	    print("Please enter a valid rate")	
        
        else:
            self.__salary -= self.__salary * rate
               
    def get_shift_time(self):
        if self.shift_time != "Day" or self.shift_time != "Night":
            print("Enter a valid shift time => Night or Day")
        else:
            return self.shift_time
    
    def change_shift_time(self):
        if self.shift_time != "Day" or self.shift_time != "Night":
            print("Enter a valid shift time => Night or Day")
        else:
            if self.shift_time == "Night":
                self.sihft_time == "Day"
        
            elif self.shift_time == "Day":
                self.shift_time == "Night"           
        
        else:
            print("Enter a valid shift time => Night or Day")

    def arrest_intruder(self):
        print("Intruder has been arrested")
        
    def search_suspicious(self,status):
    	print("Suspicious looking person has been searched")
    	
    	if status == "Suspicious":
    	    print("Person has been prevented from entering HQ.")
    	
    	elif status == "Not Suspicious":
    	    print("Person has been allowed to enter HQ.") 
            

class Janitor(Company):
    def __init__(self,name,surname,gender,age,salary,id_number,shift_time,floor):
    Company.__init__(self,self,name,surname,gender,age,salary,id_number)
    	self.shift_time = shift_time
    	self.floor = floor
    	
      	def show(self):
        return f"Name : {self.name} \nSurname : {self.surname} \nGender : {self.gender} \nAge : {self.age} \nSalary : {self.__salary} \nID Number : {self._id_number} \nShift Time : {self.shift_time} \nFloor : {self.floor}"
        
    def raise_salary(self,rate):
    	try:
    	    rate = int(rate)
    	
    	expect ValueError:
    	    print("Please enter a valid rate")	
        
        else:
            if self.shift_time == "Night":
                self.__salary += self.__salary * rate * (1.50)
            else:
                self.__salary += self.__salary * rate 

    def lower_salary(self,rate):
    	try:
    	    rate = int(rate)
    	
    	expect ValueError or rate >= 1:
    	    print("Please enter a valid rate")	
        
        else:
            self.__salary -= self.__salary * rate
               
    def get_shift_time(self):
        if self.shift_time != "Day" or self.shift_time != "Night":
            print("Enter a valid shift time => Night or Day")
        else:
            return self.shift_time
    
    def change_shift_time(self):
        if self.shift_time != "Day" or self.shift_time != "Night":
            print("Enter a valid shift time => Night or Day")
        else:
            if self.shift_time == "Night":
                self.sihft_time == "Day"
        
            elif self.shift_time == "Day":
                self.shift_time == "Night"           
        
        else:
            print("Enter a valid shift time => Night or Day")
            
    def get_floor(self):
        return self.floor
        
    def change_floor(self,new_floor):
        if new_floor < 0 or new_floor > self.number_of_floors:
            print(f"Enter a valid value between 0 and {self.number_of_floors}")
            
    def clean_bathroom(self,status):
        if status == "Clean":
            print("Bathroom is already clean")
            
        else:
            print("Bathroom has been cleaned")
            status = "Clean"


class Manager(Company):
    def __init__(self,self,name,surname,gender,age,salary,id_number,department):
    	Company.__init__(name,surname,age,salary,id_number)
    	self.department = department
    
    def show(self):
        return f"Name : {self.name} \nSurname : {self.surname} \nGender : {self.gender} \nAge : {self.age} \nSalary : {self.__salary} \nID Number : {self._id_number} \nDepartment : {self.department} "
       
    def raise_salary(self,rate):
    	try:
    	    rate = int(rate)
    	
    	expect ValueError:
    	    print("Please enter a valid rate")	
        
        else:
            if self.years_of_work > 2:
            	self.__salary += self.__salary * rate * (2.5)   
            else:
                self.__salary += self.__salary * rate
                  
    def lower_salary(self,rate):
    	try:
    	    rate = int(rate)
    	
    	expect ValueError or rate >= 1:
    	    print("Please enter a valid rate between 0 and 1 not included")	
        
        else:           
            self.__salary -= self.__salary * rate
           
                	           
    def get_department(self):
    	return self.department
    
    def set_department(self,new_department):
    	self.department == new_department


programmer = SoftwareEngineer("Ali Livan", "Türk","Male",22,16000,200444004,"Machine Learning","Marketing",2)
sec = Security("Hasan","Erbay","Male",60,6500,123456789,"Day")
hr = HumanResources("Seher","Fişekçi","Female",32,10000,1457642435)
jan = Janitor("Masoud Latifi","Navid","Male",37,300,8674837439534,"Night")
mang = Manager("Abdülvahhap Ömer","Toprak","Male",56,35000,54378534734,"Operations")    
    
                   
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
