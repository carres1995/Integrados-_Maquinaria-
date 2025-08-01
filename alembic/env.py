from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import os
from dotenv import load_dotenv
from src.db.baseclass import Base
from src.models.InstalacionMaterial import InstalacionMaterial
from src.models.Mantenimiento import Mantenimiento
from src.models.Maquinaria import Maquinaria
from src.models.Proveedores import Proveedores
from src.models.RegistroHoras import RegistroHoras
from src.models.Materiales import Materiales
#Aqui se cargan los modelos

load_dotenv()

config = context.config
config.set_main_option('sqlalchemy.url', os.environ.get('DATABASE_URL')) #type: ignore

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata =   Base.metadata

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
