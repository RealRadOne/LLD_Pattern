class Task:
    def __init__(self,ID:int):
        self.ID = ID
        self.Title = 'Test' 
        self.Description = 'Test' 
        self.Priority = 0
        self.Status = 'Pending'
    
    @property
    def Title(self):
        return self._Title
    
    @Title.setter
    def Title(self,title:str):
        if not isinstance(title,str):
            raise TypeError("Title shall be string")
        if not title.strip():
            raise ValueError("Title shall not be empty")
        self._Title = title

    @property
    def Description(self):
        return self._Description
    
    @Description.setter
    def Description(self,description:str):
        if not isinstance(description,str):
            raise TypeError("Description shall be string")
        if not description.strip():
            raise ValueError("Description shall not be empty")
        self._Description = description

    @property
    def Priority(self):
        return self._Priority
    
    @Priority.setter
    def Priority(self,priority:int):
        if not isinstance(priority,int):
            raise TypeError("Priority shall be integer")
        if not(0<=priority<=5):
            raise ValueError("Priority must be between 0 to 5")
        self._Priority = priority

    @property
    def Status(self):
        return self._Status
    
    @Status.setter
    def Status(self,status:str):
        if not isinstance(status,str):
            raise TypeError("Status shall be string")
        if not status.strip():
            raise ValueError("Status shall not be empty")
        self._Status = status

class User:
    def __init__(self,UID:int):
        self._UID = UID 
        self._Tasks = {}
    
    def addTask(self, title:str,description:str,priority:int):
        task = Task(len(self._Tasks)+1)
        task.Title = title
        task.Description = description
        task.Priority = priority
        self._Tasks[task.ID] = task

    def deleteTask(self,ID:int):
        try:
            self._Tasks.pop(ID)
        except Exception:
            raise KeyError
    
    def changePriority(self,ID:int,priority:int):
        task = self._Tasks[ID]
        task.Priority = priority 
        self._Tasks[ID] = task 

    def changeStatus(self,ID:str,status:str):
        task = self._Tasks[ID]
        task.Status = status 
        self._Tasks[ID] = task 

if __name__ == "__main__":
    user1 = User(1)

    user1.addTask('Test','First Task',3)
    user1.changePriority(4)