from logger import logger
import utils as utils
import argparse


def ingest(args):
    logger.info("Running the ingestion step..")
    logger.info(
        "Building the configuration based on the {0} file.."
        .format(args.config)
    )
    configuration = utils.load_yaml(args.config)
    ingestor = utils.build_ingestor(args.type, configuration)
    logger.info("Loading in the dataset..")
    ingestor.download()
    logger.info("The dataset was loaded successfully!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingestion step program.")
    parser.add_argument("--type", type=str, help="Type of ingestion.")
    parser.add_argument("--config", type=str, help="Configuration .yaml file.")
    parser.add_argument("--data", type=str, help="Path to save dataset files.")

    args = parser.parse_args()

    ingest(args)
