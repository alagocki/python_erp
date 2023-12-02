import yaml
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from mysql.connector.logger import logger
from Repository.order_repository import orderRepository


class tableHelperClass():

    def get_table(self, class_name, repository):

        with open('./config/tableview.yaml', 'r') as file:
            tableview_config = yaml.safe_load(file)

        table_header_list = tableview_config['colums']['table'][class_name]['header']
        table_column_index = tableview_config['colums']['table'][class_name]['index']

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(table_header_list)

        try:
            rows = repository.get_all_data("py_orders")

            for row in rows:
                rowsCnt = model.rowCount()
                model.setRowCount(rowsCnt + 1)
                for index, val in enumerate(table_column_index):
                    model.setItem(rowsCnt, index, QStandardItem(str(row[val])))

            return model

            # cntArticle = orderRepository.get_article_quantity(self)
            # helperClass.create_pagination(self, self.l_pagination_article, cntArticle)

        except Exception as err:
            logger.exception('Failed: ' + str(err))


# Settings aus der DB holen und auch editierbar machen