import os

CHECK_INTERVAL_SECONDS = os.getenv("CHECK_INTERVAL_SECONDS", default=600)
DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", default=False)
DB_SOURCE_TYPE = os.getenv("DB_SOURCE_TYPE", default="file")
