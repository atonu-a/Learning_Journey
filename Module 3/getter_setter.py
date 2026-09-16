class Bank:
    def __init__(self, name):
        self.name = name
        self._balance = 0
        
    @property #eota dile baire theke shudhu value get hobe set hobe na
    def balance(self):
        return self._balance
        
    @balance.setter #eita diye set hobe, kintu get na
    def balance(self, new_bal):
        self._balance = new_bal
        
ba1 = Bank("Atonu")
print(ba1.balance)
ba1.balance = 10
print(ba1.balance)
