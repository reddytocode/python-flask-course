from app import create_app, init_api
from app.db.db_extension import db
# from app.db.db_config  

app = create_app()
init_api(app)

"""----"""
db.init_app(app)
"""----"""

if __name__ == '__main__':
    print(app.config['MONGOALCHEMY_DATABASE'])
    app.run(port=5000, debug = True)