from celery import Task


class Task1(Task):
    def run(self):
        print('大爷好，壹壹壹壹壹壹壹壹壹壹壹壹壹壹壹......')


class Task2(Task):
    def run(self):
        print('大爷好，贰贰贰贰贰贰贰贰贰贰贰贰贰贰贰......')


class Task3(Task):
    def run(self):
        print('大爷好，叁叁叁叁叁叁叁叁叁叁叁叁叁叁叁......')


class Task4(Task):
    def run(self):
        print('大爷好，肆肆肆肆肆肆肆肆肆肆肆肆肆肆肆......')


class Task5(Task):
    def run(self):
        print('大爷好，伍伍伍伍伍伍伍伍伍伍伍伍伍伍伍......')
