def car_dataset(year, mileage, tax, mpg, enginesize, transmission, fueltype):
  return [
    float(year),
    float(mileage),
    float(tax),
    mpg,
    float(enginesize),
    float(transmission[0]),
    float(transmission[1]),
    float(transmission[2]),
    float(fueltype[0]),
    float(fueltype[1]),
    float(fueltype[2])
  ]