from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    SLEEP_TIME: list[int] = [2700, 4200]
    START_DELAY: list[int] = [5, 100]
    AUTO_TASK: bool = True
    TASKS_TO_DO: list[str] = ["paint20pixels", "x:notpixel", "x:notcoin", "channel:notcoin", "channel:notpixel_channel", "joinSquad"]
    AUTO_DRAW: bool = True
    JOIN_TG_CHANNELS: bool = True
    CLAIM_REWARD: bool = True
    AUTO_UPGRADE: bool = True
    REF_ID: str = 'f1896596326_t_s583807'
    IGNORED_BOOSTS: list[str] = ['paintReward', 'jettonTask']
    IN_USE_SESSIONS_PATH: str = 'used_sessions.txt'
    NIGHT_MODE: bool = True
    NIGHT_TIME: list[int] = [17, 23] #UTC HOURS
    NIGHT_CHECKING: list[int] = [3000, 5000]
    ENERGY_LIMIT_MAX_LEVEL: int = 7
    PAINT_REWARD_MAX_LEVEL: int = 2
    RECHARGE_SPEED_MAX_LEVEL: int = 11
    POINTS_3X: bool = False


settings = Settings()
