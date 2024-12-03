import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random

class WeatherForecast:
    def __init__(self, api_key, city):
        self.api_key = api_key
        self.city = city

    def get_forecast(self):
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={self.city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        return [(item['dt'], item['main']['temp'], item['main']['humidity']) for item in data['list']]

    def plot_forecast(self, forecast_data):
        dates = [datetime.fromtimestamp(dt) for dt, _, _ in forecast_data]
        temps = [temp for _, temp, _ in forecast_data]
        humidity = [hum for _, _, hum in forecast_data]

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        ax1.plot(dates, temps, label='Temperature (°C)')
        ax1.set_ylabel('Temperature (°C)')
        ax1.legend()
        ax2.plot(dates, humidity, label='Humidity (%)', color='g')
        ax2.set_ylabel('Humidity (%)')
        ax2.legend()
        plt.xlabel('Date')
        plt.title(f'5-day Weather Forecast for {self.city}')
        plt.tight_layout()
        plt.show()

class SensorData:
    def __init__(self):
        self.sensors = [
            {'id': 1, 'type': 'Soil Moisture', 'value': 35, 'unit': '%'},
            {'id': 2, 'type': 'Temperature', 'value': 28, 'unit': '°C'},
            {'id': 3, 'type': 'Humidity', 'value': 65, 'unit': '%'},
            {'id': 4, 'type': 'Light Intensity', 'value': 850, 'unit': 'lux'},
        ]

    def update_readings(self):
        for sensor in self.sensors:
            sensor['value'] += (random.random() - 0.5) * 5

    def get_readings(self):
        return self.sensors

class PestDetection:
    def __init__(self):
        self.pest_alerts = [
            {'id': 1, 'pestName': 'Aphids', 'severity': 'medium', 'location': 'Field A', 'date': '2023-06-15'},
            {'id': 2, 'pestName': 'Corn Earworm', 'severity': 'high', 'location': 'Field B', 'date': '2023-06-14'},
            {'id': 3, 'pestName': 'Spider Mites', 'severity': 'low', 'location': 'Field C', 'date': '2023-06-13'},
        ]

    def get_alerts(self):
        return self.pest_alerts

    def dismiss_alert(self, alert_id):
        self.pest_alerts = [alert for alert in self.pest_alerts if alert['id'] != alert_id]

class CropHealth:
    def __init__(self):
        self.health_data = [
            {'name': 'Healthy', 'value': 70},
            {'name': 'Stressed', 'value': 20},
            {'name': 'Diseased', 'value': 10},
        ]

    def get_health_data(self):
        return self.health_data

    def plot_health_data(self):
        labels = [item['name'] for item in self.health_data]
        sizes = [item['value'] for item in self.health_data]
        colors = ['#4CAF50', '#FFC107', '#F44336']

        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.title('Crop Health Overview')
        plt.show()

def main():
    # Initialize components
    weather = WeatherForecast('YOUR_OPENWEATHERMAP_API_CODE', 'Lagos')
    sensors = SensorData()
    pest_detection = PestDetection()
    crop_health = CropHealth()

    while True:
        print("\nCrop Monitoring System")
        print("1. Weather Forecast")
        print("2. Sensor Readings")
        print("3. Pest Alerts")
        print("4. Crop Health")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            forecast_data = weather.get_forecast()
            weather.plot_forecast(forecast_data)
        elif choice == '2':
            sensors.update_readings()
            readings = sensors.get_readings()
            for reading in readings:
                print(f"{reading['type']}: {reading['value']:.1f} {reading['unit']}")
        elif choice == '3':
            alerts = pest_detection.get_alerts()
            for alert in alerts:
                print(f"{alert['pestName']} - Severity: {alert['severity']}, Location: {alert['location']}, Date: {alert['date']}")
            if alerts:
                dismiss_id = input("Enter alert ID to dismiss (or press Enter to skip): ")
                if dismiss_id:
                    pest_detection.dismiss_alert(int(dismiss_id))
        elif choice == '4':
            crop_health.plot_health_data()
        elif choice == '5':
            print("Exiting Crop Monitoring System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
