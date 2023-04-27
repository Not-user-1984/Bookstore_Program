from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from db.session import SessionLocal, engine
from alembic import context

# Импортируем модели SQLAlchemy для миграций
from db.base_class import Base
from db.models.books import Book
from db.models.books import Tag
from db.models.books import User
from db.models.books import Cart
from db.models.books import CartItem

# Используйте текущую конфигурацию приложения для создания соединения с БД
from core.config import settings

config = context.config

# Извлечение параметров подключения из URL-адреса базы данных
config.set_main_option('sqlalchemy.url', str(settings.DATABASE_URL))

# Чтобы иметь возможность импортировать модели SQLAlchemy и использовать их для миграций,
# мы должны добавить их в контекст Alembic.
target_metadata = Base.metadata

# Как только мы установили соединение с базой данных и импортировали все необходимые модели SQLAlchemy,
# мы можем определить функцию create_context (), которая будет использоваться в Alembic для создания объекта миграций.
def create_context():
    # Эта строка кода забирает все объекты моделей SQLAlchemy, чтобы Alembic мог различать старые и новые версии.
    return {
        'cheese': None,
        'metadata': target_metadata,
        'session': SessionLocal(bind=engine),
        'alembic_version': context.get_context().version
    }

# Эта строка кода забирает все объекты моделей SQLAlchemy, чтобы Alembic мог различать старые и новые версии.
def run_migrations_offline():
    context.configure(
        url=str(settings.DATABASE_URL),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        user_module_prefix='models.',
        include_schemas=True
    )
    with context.begin_transaction():
        context.run_migrations()


# Эта строка кода забирает все объекты моделей SQLAlchemy, чтобы Alembic мог различать старые и новые версии.
def run_migrations_online():
    # этот блок кода используется для подключения к базе данных
    engine = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool)
    connection = engine.connect()
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        user_module_prefix='db.models.',
        include_schemas=True
    )

    try:
        with context.begin_transaction():
            context.run_migrations()
    finally:
        connection.close()

# Определяем конфигурацию логирования, которая будет использоваться в Alembic.
fileConfig(config.config_file_name)

# Вызовите функцию create_context () перед запуском миграционного скрипта.
# Если вы хотите запустить миграции офлайн, вы можете вызвать run_migrations_offline ().
# Если вы хотите запустить миграции онлайн, вы можете вызвать run_migrations_online ().
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()