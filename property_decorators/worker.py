class Worker:
    def __init__(self, id_: int, name: str, company: str=None, boss=None):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = None
        if boss:
            self.set_boss(boss)

    def set_boss(self, new_boss):
        try:
            if self.boss and self:
                self.boss.del_worker(self)
            new_boss.add_worker(self)
        except Exception as e:
            print(e.__class__, e)

    def show_info(self):
        print(f'Name: {self.name}\nCompany: {self.company}\nBoss: {self.boss}\nId: {self.id}')

    def __str__(self):
        return f'{self.name.title()}'
