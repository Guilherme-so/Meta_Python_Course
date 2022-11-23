HTTP_REQUEST = 400


match HTTP_REQUEST:
    case 200 | 201:
        print("Success")
    case 400: 
        print("Bad Request")
    case 500: 
        print("Server Error")
    case _:
        print("Desconhecido")
    