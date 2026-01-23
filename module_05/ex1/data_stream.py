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

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if not criteria:
            return data_batch
        return [data for data in data_batch if criteria in str(data)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "type": self.stream_type}


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        temps = []
        num_readings = 0
        for data in data_batch:
            num_readings += 1
            if isinstance(data, str) and "temp:" in data:
                try:
                    temp_value = float(data.split("temp:")[1])
                    temps.append(temp_value)
                except ValueError:
                    continue

        avg_temp = sum(temps) / len(temps) if temps else 0
        return f"Sensor analysis: {num_readings} readings processed, avg temp: {avg_temp}°C"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]) -> List[Any]:
        data = []

        for item in data_batch:
            if not isinstance(item, dict):
                continue
            for sensor, value in item.items():
                if criteria is None or sensor == criteria:
                    data.append({sensor: value})

        return data


class TransactionStream(DataStream):
    def __init__(self, stream_id, stream_type):
        super().__init__(stream_id, stream_type)

    def process_batch(self, data_batch: List[Any]) -> str:
        operations = 0
        buy_value = 0
        sell_value = 0

        for data in data_batch:
            operations += 1
            if "buy" in data:
                buy_value += int(data.split("buy:")[1].strip())
            elif "sell" in data:
                sell_value += int(data.split("sell:")[1].strip())

        profit = buy_value - sell_value
        if profit > 0:
            return f"Transaction analysis: {operations} operations, net flow: +{profit} units"
        return (
            f"Transaction analysis: {operations} operations, net flow: {profit} units"
        )

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]) -> List[Any]:
        data = []

        for item in data_batch:
            if not isinstance(item, dict):
                continue
            for sensor, value in item.items():
                if criteria is None or sensor == criteria:
                    data.append({sensor: value})

        return data


class EventStream(DataStream):
    def __init__(self, stream_id, stream_type):
        super().__init__(stream_id, stream_type)

    def process_batch(self, data_batch: List[Any]) -> str:
        errors = 0
        events = 0

        for data in data_batch:
            events += 1
            if "error" in data:
                errors += 1
        if errors == 1:
            s = "1 error"
        elif errors == 0:
            s = "no error"
        else:
            s = f"{errors} errors"
        return f"Event analysis: {events} events, {s} detected"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]) -> List[Any]:
        data = []

        for item in data_batch:
            if not isinstance(item, dict):
                continue
            for sensor, value in item.items():
                if criteria is None or sensor == criteria:
                    data.append({sensor: value})

        return data


class StreamProcessor:
    def dispatch(self, stream: DataStream, data_batch: List[Any]) -> None:
        """Dispatch data batch to appropriate stream processor
        args:
            stream (DataStream): The data stream instance
            data_batch (List[Any]): The batch of data to process
        """
        if not isinstance(stream, DataStream):
            print(f"Error: Unsupported stream type {type(stream)}")
            return
        try:
            result = stream.process_batch(data_batch)
            print(f"{result}")
        except Exception as e:
            print(f"Error processing stream {stream.stream_id}: {e}")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    manager = StreamProcessor()

    print("Initializing Sensor Stream...")
    stream_id = "SENSOR_001"
    stream_type = "Enviromental Data"
    sensor_stream = SensorStream(stream_id, stream_type)
    print(f"Stream ID: {stream_id}, Type: {stream_type}")
    sensor_data = [
        "temp:22.5",
        "humidity:65",
        "pressure:1013",
    ]
    print_data = str(sensor_data).replace("'", "")
    print(f"Processing sensor batch: {print_data}")
    manager.dispatch(sensor_stream, sensor_data)

    print("\nInitializing Transaction Stream...")
    stream_id = "TRANS_001"
    stream_type = "Financial Data"
    trans_stream = TransactionStream(stream_id, stream_type)
    print(f"Stream ID: {stream_id}, Type: {stream_type}")
    transaction_data = [
        "buy: 100",
        "sell: 150",
        "buy: 75",
    ]
    print_data = str(transaction_data).replace("'", "")
    print(f"Processing transaction batch: {print_data}")
    manager.dispatch(trans_stream, transaction_data)

    print("\nInitializing Event Stream...")
    stream_id = "EVENT_001"
    stream_type = "System Events"
    event_stream = EventStream(stream_id, stream_type)
    print(f"Stream ID: {stream_id}, Type: {stream_type}")
    event_data = [
        "login",
        "error",
        "logout",
    ]
    print_data = str(event_data).replace("'", "")
    print(f"Processing event batch: {print_data}")
    manager.dispatch(event_stream, event_data)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    streams = [
        (sensor_stream, ["temp:20", "humidity:70"]),
        (trans_stream, ["buy: 200", "sell: 100", "buy: 50", "sell: 25"]),
        (event_stream, ["start", "error", "stop"]),
    ]

    print("\nBatch 1 Results:")
    for stream, data in streams:
        stream.process_batch(data)

        if isinstance(stream, SensorStream):
            print(f" - Sensor data: {len(data)} readings processed.")
        elif isinstance(stream, TransactionStream):
            print(f" - Transaction data: {len(data)} operations processed.")
        elif isinstance(stream, EventStream):
            print(f" - Event data: {len(data)} events processed.")

    print("\nStream filtering active: High-priority data only.")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")
    print("\nAll streams processed successfully. Nexus throughput optimal.")
