from prefect import flow
from tasks.task import (task_primera_tarea)
from tasks.task_extract_linkedin import (
    task_extract_linkedin)
from tasks.task_load_offers import (
    task_load_offers
)

@flow(name="PRIMER FLOW")
def main_flow():
    #task_primera_tarea()
    offers = task_extract_linkedin('java')
    print(f"se encontraron {offers.__len__()} ofertas")
    task_load_offers(offers)
    
if __name__ == "__main__":
    main_flow()