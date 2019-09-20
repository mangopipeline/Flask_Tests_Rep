from flask import Blueprint, render_template


data_table_bp = Blueprint('data_talbe_test',
                          __name__,
                          template_folder='templates',
                          static_folder='static',
                          static_url_path='/data_table/static')

@data_table_bp.route('/data_table')
def data_table():
    return render_template('data_table.html')