import sys
import yaml
import logging

logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger(__name__)

def main():
    if len(sys.argv) != 3:
        LOG.error("Usage: python script.py config_str output_file_path")
        sys.exit(1)

    config_str = sys.argv[1]
    output_file_path = sys.argv[2]

    # Galaxy text box will replace
    #  ‘\n’, ‘<>‘, [], ‘’ 
    # into 
    # “_cn_“, “__lt__*__gt__“,
    # “__ob____cb__“, “__sq____sq__”
    # So replace them back
    config_str = config_str.replace("__cn__", "\n")
    config_str = config_str.replace("__lt__", "<")
    config_str = config_str.replace("__gt__", ">")
    config_str = config_str.replace("__ob____cb__", "[]")
    config_str = config_str.replace("__sq____sq__", "''")

    # Load YAML config from input string
    try:
        config_data = yaml.safe_load(config_str)
    except yaml.YAMLError as e:
        LOG.error(f"Error loading YAML: {e}")
        LOG.debug(config_str)
        sys.exit(1)

    # Write YAML data to output file
    try:
        with open(output_file_path, 'w') as outfile:
            yaml.safe_dump(config_data, outfile, sort_keys=False)
        LOG.info(f"YAML config successfully written to {output_file_path}")
    except IOError as e:
        LOG.error(f"Error writing to file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()