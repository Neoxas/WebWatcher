class User(object):
    def __init__(self, name, email, keywords, budget):
        self.name = name
        self.email = email
        self.keywords = keywords
        self.budget = budget
        self.parsers = []

    def add_parser(self, parser, keywords):
        pass

    def remove_parser(self, parser):
        pass

    def list_parsers(self):
        print("Active Parsers")
        for parser in self.parsers:
            print(parser.NAME + " Keywords: " +
                    parser.keywords)

    def run_search(self):
        pass

    def delete_user(self):
        pass

