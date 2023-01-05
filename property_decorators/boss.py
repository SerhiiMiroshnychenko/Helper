from worker import Worker

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.__workers = []
        self.__workers_count = 0

    @property
    def workers(self):
        return self.__workers

    @workers.setter
    def workers(self, workers: list[Worker]):
        for worker in workers:
            worker.set_boss(self)
        self.__workers = workers
        self.__workers_count += len(workers)

    @workers.deleter
    def workers(self):
        for worker in self.__workers:
            worker.boss = None
            worker.company = None
        self.__workers = []

    def check_worker(self, worker: Worker):
        if isinstance(worker, Worker) and worker in self.__workers:
            print(f"{worker.name.title()} is in {self.name.title()}'s workers.")
        elif isinstance(worker, Worker):
            print(f"{worker.name.title()} isn't in {self.name.title()}'s workers.")
        else:
            print("Worker's type error!")

    def get_worker(self, worker_name: str):
        for worker in self.__workers:
            if worker_name == worker.name:
                return worker

    def add_worker(self, worker: Worker or str):
        if self.get_worker(worker) or worker in self.__workers:
            print('This worker is already working.')
        elif isinstance(worker, str):
            worker_name = worker
            worker_id = int(str(self.id) + str(self.__workers_count))
            Worker(worker_id, worker_name, self.company, self)
            self.__workers_count += 1
        elif isinstance(worker, Worker):
            worker.boss = self
            worker.company = self.company
            new_worker = worker
            self.__workers.append(new_worker)
            self.__workers_count += 1
        else:
            print("Worker's type error!1")

    def del_worker(self, worker: Worker):
        if isinstance(worker, Worker) and worker in self.__workers:
            worker_ind = self.__workers.index(worker)
            self.__workers[worker_ind].boss = None
            self.__workers[worker_ind].company = None
            self.__workers.remove(worker)
        else:
            message = "Worker's type error!" if worker in self.__workers else f"{self.name.title()} does not have this worker."
            print(message)

    def show_info(self):
        print(f'Name: {self.name}\nCompany: {self.company}\nId: {self.id}\nNumber of workers: {len(self.workers)}')

    def show_workers(self):
        if self.__workers:
            for number, worker in enumerate(self.__workers, 1):
                print(f'{number}. {worker.name}')
        else:
            print('No workers.')

    def __str__(self):
        return f'{self.name.title()}'
