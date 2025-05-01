from bmp280 import BMP280Configuration


def get_bmp280_config() -> BMP280Configuration:
    config = BMP280Configuration()
    config.power_mode = BMP280Configuration.POWER_MODE_FORCED
    config.pressure_oversampling = BMP280Configuration.PRESSURE_OVERSAMPLING_4X
    return config
