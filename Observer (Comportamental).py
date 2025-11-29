from abc import ABC, abstractmethod
from typing import List

# Interface Observer
class Observer(ABC):
    @abstractmethod
    def update(self, subject: 'Subject') -> None:
        pass

# Interface Subject
class Subject(ABC):
    def __init__(self):
        self._observers: List[Observer] = []
    
    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)
    
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
    
    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

# Implementação Concreta
class NewsAgency(Subject):
    def __init__(self):
        super().__init__()
        self._news = ""
    
    @property
    def news(self) -> str:
        return self._news
    
    @news.setter
    def news(self, value: str) -> None:
        self._news = value
        self.notify()

class NewsChannel(Observer):
    def __init__(self, name: str):
        self._name = name
        self._latest_news = ""
    
    def update(self, subject: Subject) -> None:
        if isinstance(subject, NewsAgency):
            self._latest_news = subject.news
            print(f"{self._name} recebeu a notícia: {self._latest_news}")

# Uso
if __name__ == "__main__":
    agency = NewsAgency()
    
    channel1 = NewsChannel("CNN")
    channel2 = NewsChannel("BBC")
    
    agency.attach(channel1)
    agency.attach(channel2)
    
    agency.news = "Novo padrão de projeto lançado!"
    agency.news = "Python 3.12 lançado com novas features"