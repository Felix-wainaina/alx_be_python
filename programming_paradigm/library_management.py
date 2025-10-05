#!/usr/bin/env python3
"""
library_management.py

Implements simple Book and Library classes for a basic library management system.
"""

class Book:
    """Represents a book with a title, author, and checked-out status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        # private attribute to track availability
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out (unavailable)."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """Manages a collection of Book instances."""

    def __init__(self):
        # private list of Book objects
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library."""
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        """
        Check out the first available book matching `title`.
        If found and available, mark it checked out and return True.
        If not found or already checked out, return False.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """
        Return the first checked-out book matching `title`.
        If found and currently checked out, mark it available and return True.
        If not found or not checked out, return False.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """Print all available books, one per line in the form 'Title by Author'."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
