#!/usr/bin/env python3

from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        pass

class NumericProcessor(DataProcessor):
    def process(self, data: List[int]) -> str:
        if self.validate(data):
            total = 0
            count = 0
            for x in data:
                total += x
                count += 1
            return f"Processed {count} numeric values, sum={total}, avg={total/count}"
        return f"Invalid Data"
       
    def validate(self, data: Any) -> bool:
        if not data:
            return False
        try:
            for x in data:
                x + 0
            print("Validation: Numeric data verified")
            return True
        except:
            return False

    def format_output(self, result: str) -> str:
        return f"Output: {result}"

class TextProcessor(DataProcessor):
    def process(self, data: any) -> str:
        if self.validate(data):
            number_char = 0
            number_word = 0
            for c in data:
                number_char += 1
                if number_char == 1:
                    number_word += 1
                if c == ' ':
                    number_word += 1
            return f"Processed text: {number_char} characters, {number_word} words"

    def validate(self, data: Any) -> bool:
        if not data:
            return False
        try:
            data + ""
            for _ in data:
                pass
            print("Validation: Text data verified")
            return True
        except:
            return False

    def format_output(self, result: str) -> str:
        return f"Output: {result}"

class LogProcessor(DataProcessor):
    def process(self):
        pass

    def validate(self):
        pass

    def format_output(self):
        pass

print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

processor = NumericProcessor()
print("\nInitializing Numeric Processor...")
data = [1,2,3,4,5]
print(f"Processing data: {data}")
s = processor.process(data)
print(processor.format_output(s))

processor = TextProcessor()
print("\nInitializing Text Processor...")
data = "Hello Nexus World"
print(f"Processing data: {data}")
s = processor.process(data)
print(processor.format_output(s))
