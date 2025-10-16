import logging
import os
from core_engine.config import Config
from core_engine.exceptions import EngineException
from core_engine.services import EngineService

class CoreEngine:
    def __init__(self, config: Config):
        self.config = config
        self.service = EngineService(self.config)

    def start(self):
        try:
            logging.info("Starting core engine")
            self.service.start()
            logging.info("Core engine started successfully")
        except EngineException as e:
            logging.error(f"Error starting core engine: {str(e)}")
            raise

    def stop(self):
        try:
            logging.info("Stopping core engine")
            self.service.stop()
            logging.info("Core engine stopped successfully")
        except EngineException as e:
            logging.error(f"Error stopping core engine: {str(e)}")
            raise

def main():
    config = Config(os.environ.get("CONFIG_FILE", "config.json"))
    engine = CoreEngine(config)
    engine.start()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    main()