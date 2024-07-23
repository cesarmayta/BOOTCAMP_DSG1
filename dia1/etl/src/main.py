from prefect import flow
from tasks.task import (task_primera_tarea)

@flow(name="PRIMER FLOW")
def main_flow():
    task_primera_tarea()

if __name__ == "__main__":
    main_flow()