# Challenge : Create a class that has two other classes inherit from it.

class Team: 
    team_name = "Team name not set"
    supervisor_name = "No supervisor selected"
    total_members = 0
    # Let's set up an easy way to instantiate an object
    def __init__(self, team_name, supervisor_name, total_members):
        self.team_name = team_name
        self.supervisor_name = supervisor_name
        self.total_members = total_members
    # My stab at a self-instantiating object method... I don't know that it worked.
    # Output from the class method call was
    # The <__main__.Team object at 0x000000014F058847C0> team has been created. Odd.
    def createTeam(self):
        supervisorName = input("Enter the new supervisor's name: \n>>> ")
        teamName = input("What team is this supervisor responsible for: \n>>> ")
        members = input("How many members are on the team: \n>>> ")
        teamName = (Team(teamName, supervisorName, members))
        print("The {} team has been created.".format(teamName))
    
class Supervisor(Team):
    name = "No name provided"
    area = "No area provided"
    salary = 0
    tenure = 0
    number_of_reports = 0
    # Let's set up an easy way to instantiate an object
    def __init__(self, name, area, salary, tenure, number_of_reports):
        self.name = name
        self.area = area
        self.salary = salary
        self.tenure = tenure
        self.number_of_reports = number_of_reports

class Employee(Team):
    name = "No name available"
    title = "Not yet titled"
    salary = 0
    tenure = 0
    last_performance_note = "No performance notes provided"
    # Let's set up an easy way to instantiate an object
    def __init__(self, name, title, salary, tenure, last_performance_note):
        self.name = name
        self.title = title
        self.salary = salary
        self.tenure = tenure
        self.last_performance_note = last_performance_note
        
        
Team.createTeam("test")