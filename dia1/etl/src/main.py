from prefect import flow
from tasks.task import (task_primera_tarea)
from tasks.task_extract_linkedin import (
    task_extract_linkedin)

@flow(name="PRIMER FLOW")
def main_flow():
    #task_primera_tarea()
    offers = task_extract_linkedin('python')
    print(offers)
if __name__ == "__main__":
    main_flow()