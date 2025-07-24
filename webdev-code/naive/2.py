from django.db import connection
from django.http import HttpResponse

def unsafe_query(request):
    user_input = request.GET.get('name', '')
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return HttpResponse(str(result))
