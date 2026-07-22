
# day06/practice.py

import math


# 1. SRP Violation → Split Report responsibilities


class ReportBuilder:
    def build(self):
        return "Monthly Sales Report"


class ReportSaver:
    def save(self, report):
        print(f"Saving report: {report}")


class ReportEmailer:
    def email(self, report):
        print(f"Emailing report: {report}")


# 2. OCP - Shape hierarchy instead of if/elif

class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height



# 3. Singleton Pattern


class AppSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.currency = "ETB"

        return cls._instance



# 4. Factory Pattern


class ShapeFactory:

    @staticmethod
    def create(kind):

        if kind == "circle":
            return Circle(5)

        elif kind == "square":
            return Square(4)

        elif kind == "triangle":
            return Triangle(6, 3)

        else:
            raise ValueError("Unknown shape")



# 5. Observer Pattern


class NewsAgency:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify(self, news):
        for subscriber in self.subscribers:
            subscriber.update(news)


class EmailSubscriber:

    def update(self, news):
        print(f"Email subscriber received: {news}")


class SMSSubscriber:

    def update(self, news):
        print(f"SMS subscriber received: {news}")



# Testing Everything


if __name__ == "__main__":

    # 1. SRP Test
    print("--- SRP Test ---")

    builder = ReportBuilder()
    saver = ReportSaver()
    emailer = ReportEmailer()

    report = builder.build()

    saver.save(report)
    emailer.email(report)


    # 2. OCP Test
    print("\n--- OCP Test ---")

    shapes = [
        Circle(5),
        Square(4),
        Triangle(6, 3)
    ]

    for shape in shapes:
        print("Area:", shape.area())


    # 3. Singleton Test
    print("\n--- Singleton Test ---")

    settings1 = AppSettings()
    settings2 = AppSettings()

    print(settings1.currency)
    print(settings1 is settings2)


    # 4. Factory Test
    print("\n--- Factory Test ---")

    shape1 = ShapeFactory.create("circle")
    shape2 = ShapeFactory.create("square")

    print("Circle area:", shape1.area())
    print("Square area:", shape2.area())


    # 5. Observer Test
    print("\n--- Observer Test ---")

    agency = NewsAgency()

    email_user = EmailSubscriber()
    sms_user = SMSSubscriber()

    agency.subscribe(email_user)
    agency.subscribe(sms_user)

    agency.notify("New Ethiopian banking update released!")