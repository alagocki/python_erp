from email import header

from PyQt6.QtSql import QSqlQuery, QSqlRecord


class ArticleRepository():
    def __init__(self):
        super().__init__()


    def get_article_by_id(self, id):
        article_id = str(id)
        query_string = "select a.* from article a where a.id = " + article_id
        return self.prepare_single_result(query_string)

    def get_article_by_sku(self, sku):
        article_sku = str(sku)
        query_string = "select a.* from article a where a.nummer = '" + article_sku + "'"
        return self.prepare_single_result(query_string)


    def prepare_single_result(self, query_string):
        self.query = QSqlQuery(query_string)
        self.columns = self.query.record().count()

        self.query.first()

        self.result = []
        while self.query.isValid():
            record = [self.query.value(index) for index in range(self.columns)]
            self.result.append(record)
            self.query.next()

        return self.result