from __future__ import annotations
"""
The previous line is needed to type hint classes that are defined later
like Results class below
"""


from selene import by, have
from selene.support.shared import browser


class Ecosia:
    def open(self):
        browser.open('https://www.ecosia.org/')

    def search(self, text):
        browser.element(by.name('q')).type(text).press_enter()

    @property
    def results(self) -> Results:
        return Results()


class Results:

    def __init__(self):
        self.elements = browser.all('.result')

    def should_have_size_at_least(self, amount) -> Results:
        self.elements.should(have.size_greater_than_or_equal(amount))
        return self

    def should_have_text(self, index, value) -> Results:
        self.elements[index].should(have.text(value))
        return self

    def follow_link(self, index) -> Results:
        self.elements[index].element('a').click()
        return self


ecosia: Ecosia = Ecosia()