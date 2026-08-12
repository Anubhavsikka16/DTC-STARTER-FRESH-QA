from framework.db.connection import Database


class ProductRepository:

    def __init__(self, db: Database):
        self.db = db

    def get_product(self, product_id):

        query = """
            SELECT id, title, handle, status
            FROM product
            WHERE id = %s
        """

        return self.db.fetch_one(
            query,
            (product_id,)
        )