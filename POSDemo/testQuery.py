from .models2 import Owner , Business

def handle_query():
    data = Owner.objects.filter(name__startswith='riddhi')
    print(data)
    print(type(data))

if __name__ == '__main__':
    handle_query()