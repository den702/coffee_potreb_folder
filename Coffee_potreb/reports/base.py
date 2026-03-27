from abc import ABC, abstractmethod


class BaseReport(ABC):
    name = None  # имя отчёта (ключ)

    @abstractmethod
    def build(self, data):
        pass