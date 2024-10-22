def konsersisuhu(temperature, value):
    if value == 'C':
        #jika targetnya adalah Celcius (C), maka suhu Fahrenheit (F) dikonversi ke Celcius
        temperaturesuhu = (temperature - 32) * 5/9
        return temperaturesuhu, 'C'
    else:
        #jika targetnya bukan Celcius, maka suhu Celcius dikonversi ke Fahrenheit (F)
        temperaturesuhu = (temperature * 9/5) + 32
        return temperaturesuhu, 'F'

#mengonversi suhu dari Celcius ke Fahrenheit
celcius_temperature = 30
temperaturesuhu, target_value = konsersisuhu(celcius_temperature, 'F')
print(f"{celcius_temperature}°C dikonversi ke Fahrenheit adalah {temperaturesuhu}°{target_value}")

#mengonversi suhu dari Fahrenheit ke Celcius
fahrenheit_temperature = 86
temperaturesuhu, target_value = konsersisuhu(fahrenheit_temperature, 'C')
print(f"{fahrenheit_temperature}°F dikonversikan ke Celcius adalah {temperaturesuhu}°{target_value}")
