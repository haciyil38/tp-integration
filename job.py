import os

a = 2

print("coucou", a)

secret = os.environ.get("SECRET_API_TOKEN")

if secret:
    print("Le secret est bien récupéré")
else:
    print("Le secret n'est pas disponible")
