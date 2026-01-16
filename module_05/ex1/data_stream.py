#!/usr/bin/env python3

from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod

class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str):
        self.stream_id = stream_id
        self.stream_type = stream_type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": self.stream_type
        }

class SensorStream(DataStream):
    def __init__(self, stream_id, stream_type):
        super().__init__(stream_id, stream_type)
    
    def process_batch(self, data_batch: Dict) -> str:
        print(f"Processing sensor batch: {self.filter_data(data_batch, None)}")

        count_temp = 0
        total_readings = 0
        temp_total = 0
        
        for data in data_batch:
            total_readings += 1
            if 'temp' in data:
                count_temp += 1
                temp_total += data_batch['temp']
        
        avg_temp = temp_total / count_temp
        
        if count_temp == 0:
            return "No temperature available"
        return f"Sensor analysis: {total_readings} readings processed, avg temp: {avg_temp}°C"


    def filter_data(self, data_batch: List[Any], criteria: Optional[str]) -> List[Any]:
        if criteria is None:
            pass
        data = []
        for s in data_batch:
            item = f"{s}:{data_batch[s]}"
            data = data + [item]
        return data

class TransactionStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

class EventStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

print("Initializing Sensor Stream...")
stream_id = "SENSOR_001"
stream_type = "Enviromental Data"

print(f"Stream ID: {stream_id}, Type: {stream_type}")

sensor_batch = {
    "temp": 22.5,
    "humidity": 65,
    "pressure": 1013
}
stream = SensorStream(stream_id, stream_type)
print(f"{stream.process_batch(sensor_batch)}")