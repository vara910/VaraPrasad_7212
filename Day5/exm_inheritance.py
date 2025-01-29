class Management:
    def display_Management(self):
        print("this is the overall management")  
          
class School(Management):
    def display_schl(self):
        print("iam in school")
        
class Ug(Management):
    def display_Ug(self):
        print("iam in btech")
        
class Pg(Management):     
    def display_pg(self):
        print("iam in my post graduation")
        
admin=School()
admin2=Ug()
admin3=Pg()
admin.display_schl()
admin2.display_Ug()
admin3.display_pg()
admin2.display_Management()