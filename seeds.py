import json
from pprint import pprint

from models import Authors, Quotes
import connect

json_files = ["authors.json", "quotes.json"]


def json_reader(file):
    try:
        with open(file, "r") as f:
            json_data = json.load(f)
            return json_data
    except json.JSONDecodeError as e:
        pprint(f"e")


if __name__ == "__main__":
    authors_id = {}
    for file in json_files:
        json_data = json_reader(file)
        for item in json_data:
            if file == "authors.json":
                author = Authors(
                    fullname=item["fullname"],
                    born_date=item["born_date"],
                    born_location=item["born_location"],
                    description=item["description"],
                )
                author.save()

                authors_id.update({item["fullname"]: author.id})

            if file == "quotes.json":
                quote = Quotes(
                    tags=item["tags"],
                    author=authors_id[item["author"]],
                    quote=item["quote"],
                )
                quote.save()
