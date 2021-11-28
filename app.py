from flask_migrate import Migrate, MigrateCommand
from tools.message.models import User
from ext import db
from tools import create_app
from flask_script import Manager

app = create_app()
manger = Manager(app=app)
migrate = Migrate(app=app, db=db)
manger.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manger.run()
