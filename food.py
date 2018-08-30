from pathlib import Path
import records
from pizza.modell import Item
from pizza.databaseQueryCreator import QueryBuilder


def get_database()-> records.Database:
    database_path = Path('./food.db')
    return records.Database("sqlite:///" + str(database_path))


def create_table()-> None:
    create = QueryBuilder().create_table().table("foods").start_bracket().add_integer("id").primary_key(True).varchar("50", "name").not_null(True).varchar("50", "amount_left", True).varchar("50", "expiry_date").close_bracket().build()
    db = get_database()
    db.query(create)
    db.close()


def add_to_table(item: Item)-> int:
    add_to = QueryBuilder().insert().table("foods").column("name, amount_left, expiry_date, storage_number").values(":name, :amount_left, :expiry_date, :storage_number").build()
    db = get_database()
    db.query(add_to, name=item.get_name(), amount_left=item.get_amount_left(), expiry_date=item.get_expiry_date(), storage_number=item.get_storage_number())
    db.close()

    db = get_database()
    item_id = db.query("SELECT id FROM foods WHERE name = :name", name=item.get_name())
    row = item_id[0].id
    return row


def check_expiry_date(item: Item)-> str:
    db = get_database()
    expiry = db.query(QueryBuilder().select("expiry_date").froom("foods").where({'name': ['=', ':given']}).build(), given=item.get_name())
    row = expiry[0].expiry_date
    db.close()
    return row


def check_amount_left(item: Item)-> str:
    db = get_database()
    check_amount = db.query(QueryBuilder().select("amount_left").froom('foods').where({'name': ['=', ':given']}).build(), given=item.get_name())
    row = check_amount[0].amount_left
    db.close()
    return row


def get_all()->list:
    db = get_database()
    get = QueryBuilder().select().froom('foods').build()
    herro = db.query(get)
    row = []
    for i in herro:
        a = Item(i.id, i.name, i.amount_left, i.expiry_date, i.storage_number)
        row.append(a)
    db.close()
    return row

#.
def get_shopping_list()->list:
    db = get_database()
    get = QueryBuilder().select("name").froom('shopping_list').build()
    herro = db.query(get)

    row = []

    for i in herro:
        row.append(get_item_from_id(i.name))

    return row

#.
def alter_items(item: Item, amount_left: str):
    db = get_database()

    db.query("UPDATE foods SET amount_left = :amount_left where name = :given", given=item.get_name(), amount_left=amount_left)
    db.close()
    db = get_database()

    a = db.query("SELECT id FROM foods WHERE name = :lmnop", lmnop=item.get_name())
    row = a[0].id
    db.close()
    db = get_database()

    b = db.query("SELECT amount_left FROM foods WHERE id = :row", row=row)
    roww = b[0].amount_left
    db.close()
    db = get_database()

    if roww == "0":
        db.query("INSERT INTO shopping_list(name) VALUES (:row)", row=row)
    db.close()

    print("You have altered the table")

def get_item_from_id(item_id: int)-> Item:
    db = get_database()
    a = db.query("SELECT * FROM foods WHERE id = :item_id", item_id=item_id)
    item_data = a[0]
    e = Item(item_data.id, item_data.name, item_data.amount_left, item_data.expiry_date, item_data.storage_number)
    return e





if __name__ == "__main__":
    print(get_shopping_list())
