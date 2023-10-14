from pprint import pprint
from models import Authors, Quotes
import connect

if __name__ == "__main__":
    i = True
    while i:
        print("-----Search quotes-----")
        user_input = input("Input field:value >>>")
        print("-----------------------")
        query = user_input.split(":")

        if query[0] == "exit":
            i = False
            break

        elif query[0] == "name":
            if author := Authors.objects(fullname__iregex=query[1]).first():
                quotes = Quotes.objects(author=author.id)
            else:
                print("No such author found")

        elif query[0] == "tag":
            quotes = list(Quotes.objects(tags__iregex=query[1]))

        elif query[0] == "tags":
            if "," in query[1]:
                query_list = query[1].split(",")

            else:
                print("No such tags found")

            quotes = list(Quotes.objects(tags__in=query_list))

        else:
            print("No such field exists")

        for quote in quotes:
            print(quote.quote)
