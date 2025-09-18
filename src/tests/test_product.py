from daos.product_dao import ProductDAO
from models.product import Product

dao = ProductDAO()

def test_product_select():
    product_list = dao.select_all()
    assert len(product_list) >= 2

def test_product_insert():
    product = Product(None, 'ball', 'ball depot', 30.0)
    dao.insert(product)
    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert product.name in names

def test_product_update():
    product = Product(None, 'pencil', 'pencil depot', 2.99)
    assigned_id = dao.insert(product)

    corrected_name = 'big pencil'
    product.id = assigned_id
    product.name = corrected_name

    dao.update(product)

    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert corrected_name in names

def test_product_delete():
    product = Product(None, 'phone', 'apple', 1099.0)
    assigned_id = dao.insert(product)
    nb_deleted_rows = dao.delete(assigned_id)

    product_list = dao.select_all()
    ids = [p.id for p in product_list]
    assert assigned_id not in ids
    assert nb_deleted_rows == 1