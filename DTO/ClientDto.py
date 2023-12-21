from classLibrary.Client import Client

def RegistraionUser(phone,first_name,second_name,email,third_name=None):
    client = Client(phone_number = phone,first_name= first_name,second_name = second_name,third_name = third_name,email=email)
    client.save()
    return client
def FindByPhone(phone):
    client = Client.select().where(Client.phone_number == phone).get()
    return client

def squre():
    return 10*20
print(squre())