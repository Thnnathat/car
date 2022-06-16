from connector import Manager

class Activity(Manager):
    
    def select_all(self, *args, table_name):
        data = super().select_all(*args, table_name=table_name)
        return data if data else {"error": True}
    