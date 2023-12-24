from django.shortcuts import render
from datetime import datetime

# Create your views here.


def home(request):
    data = [
        {
            "user": "Arif",
            "id": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
            "datetime": datetime.now(),
            "image": "https://lerablog.org/wp-content/uploads/2018/01/gtrgrtgfgfgs.jpg",
        },
        {
            "user": "Kamrul Hossen",
            "id": 2,
            "title": "qui's est esse",
            "body": "est rerum tempore vitae\nsequi 'sint' nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla",
            "datetime": datetime.now(),
            "image": "https://lerablog.org/wp-content/uploads/2018/01/gtrgrtgfgfgs.jpg",
        },
        {
            "user": "Harun",
            "id": 3,
            "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
            "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut",
            "datetime": datetime.now(),
            "image": "https://lerablog.org/wp-content/uploads/2018/01/gtrgrtgfgfgs.jpg",
        },
    ]
    return render(request, "blog/index.html", {"data": data, 'marks':45, 'countries' : ['Bangladesh','India', 'Sri-langka'] })
