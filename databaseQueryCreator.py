class QueryBuilder():

    def __init__(self):
        self.liist = []

    def insert(self):
        self.liist.append("INSERT INTO")
        return self

    def table(self, table_name: str):
        self.liist.append(table_name)
        return self

    def column(self, column_name: str):
        formatted = "(" + column_name + ")"
        self.liist.append(formatted)
        return self

    def values(self, value_name: str):
        formatt = "VALUES (" + value_name + ")"
        self.liist.append(formatt)
        return self

    def build(self):
        building = ""
        for i in self.liist:
            building += i + " "
        return building





    def select(self, table_header="*"):
        self.liist.append("SELECT " + table_header)
        return self

    def froom(self, table: str):
        self.liist.append("FROM")
        self.table(table)
        return self

    def where(self, where: dict):
        dictionary = ""
        for k, v in where.items():
            dictionary += k + " " + v[0] + " " + v[1] + " "
        self.liist.append("WHERE")
        self.liist.append(dictionary)
        return self





    def create_table(self):
        self.liist.append("CREATE TABLE")
        return self

    def start_bracket(self):
        self.liist.append("(")
        return self

    def add_integer(self, name: str, final=False):
        self.liist.append(name + ' INTEGER')
        if final:
            self.comma()
        return self

    def primary_key(self, final=False):
        self.liist.append("PRIMARY KEY")
        if final:
            self.comma()
        return self

    def comma(self):
        self.liist.append(",")
        return self

    def varchar(self, number: str, name: str, final=False):
        self.liist.append(name + " VARCHAR(" + number + ")")
        if final:
            self.comma()
        return self

    def not_null(self, final=False):
        self.liist.append("NOT NULL")
        if final:
            self.comma()
        return self

    def close_bracket(self):
        self.liist.append(")")
        return self




    def delete(self):
        self.liist.append("DELETE")
        return self













if(__name__ == "__main__"):
    # "INSERT INTO foods (name, amount_left, expiry_date) VALUES (:name, :amount_left, :expiry_date)"
    a = QueryBuilder().insert().table("foods").column("name, amount_left, expiry_date").values(":name, :amount_left, :expiry_date").build()
    print(a)
    # "SELECT expiry_date FROM foods WHERE name = :given"
    b = QueryBuilder().select("expiry_date").froom("foods").where({'name': ['=', ':given']}).build()
    print(b)
    # "CREATE TABLE foods(id INTEGER PRIMARY KEY, name VARCHAR(50) NOT NULL, amount_left VARCHAR(50), expiry_date VARCHAR(50))"
    c = QueryBuilder().create_table().table("foods").start_bracket().add_integer("id").primary_key(True).varchar("50", "name").not_null(True).varchar("50", "amount_left", True).varchar("50", "expiry_date").close_bracket().build()
    print(c)
    # "DELETE FROM foods WHERE name = :string"
    d = QueryBuilder().delete().froom("foods").where({'name': ['=', ':string']}).build()
    print(d)
    # SELECT amoung_left FROM foods WHERE name = :given
    e = QueryBuilder().select("amount_left").froom('foods').where({'name': ['=', ':given']}).build()
    print(e)

