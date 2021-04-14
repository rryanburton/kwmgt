from .views import artist
from api.views import ArtistSerializer


def add_data(request):
    data = artist
    serializer = ArtistSerializer(data=data)
    # print(serializer)
    if serializer.is_valid():
        print("serializer was valid")
        thing = serializer.save()
        print("i made it to save")
    else:
        print("serializer was not valid")
        print(serializer.errors)


if __name__ == "__main__":
    add_data()