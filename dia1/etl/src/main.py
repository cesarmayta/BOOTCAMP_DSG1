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
    search = ['python','java','go']
    for s in search:
        offers = task_extract_linkedin(s)
        print(f"se encontraron {offers.__len__()} ofertas de {s}")
        task_load_offers(offers)
    
if __name__ == "__main__":
    main_flow()