from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str

    @property
    def DB_ASYNC_URL(self):
        return 'postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}'.format(
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            db_name=self.DB_NAME
        )

    @property
    def DB_URL(self):
        return 'postgresql://{user}:{password}@{host}:{port}/{db_name}'.format(
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            db_name=self.DB_NAME
        )

    class Config:
        env_file = '.env'


settings = Settings()  # type: ignore
