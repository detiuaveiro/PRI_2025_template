import argparse

from sapien.core.limit_memory import start_memory_monitor

start_memory_monitor(show_memory_updates=True)


def main():
    parser = argparse.ArgumentParser(description="Sapien Indexer CLI")
    # TODO continue here
    parser.parse_args()


if __name__ == "__main__":
    main()
