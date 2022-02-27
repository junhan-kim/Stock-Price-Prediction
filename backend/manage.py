import os
import unittest
import logging
import json

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_cors import CORS

from app import blueprint
from app.main import create_app, db
from app.main.model import user
from app.main.model import blacklist
from logger import logger


# app setting
app = create_app(os.getenv('EXEC_ENV'))
app.register_blueprint(blueprint)
app.app_context().push()
CORS(app, resources={r'*': {'origins': json.loads(os.getenv('WHITE_LISTS'))}})

# db setting
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    logger.info('App is running.')
    app.run(host='0.0.0.0', port=5000)


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
