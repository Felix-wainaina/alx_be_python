#!/usr/bin/env python3

class Book:
    """A simple Book class demonstrating Python magic methods."""

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        # Print message when object is deleted
        print(f"Deleting {self.title}")

    def __str__(self):
        # Human-friendly string
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Official string that can be used to recreate the instance
        return f"Book('{self.title}', '{self.author}', {self.year})"
