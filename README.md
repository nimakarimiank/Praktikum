# High School Internship: Energy Awareness with micro:bit

This repository contains the Python code for a two-day high school internship project. The project introduces programming and uses the BBC micro:bit to measure energy usage. 

## Day 1: Introduction to Python and micro:bit

**File:** `day1.py`

This script helps the student learn the basics of Python. It uses a loop to display different built-in images (like Happy, Sad, Pacman) on the micro:bit LED screen. The student can cycle forward through the images with Button A, and backward with Button B.

## Day 2: Energy Data Collection

### Part 1: The Light Meter (Calibration)
**File:** `day2_part1.py`

This code turns the micro:bit into a simple light meter. This step is necessary to calibrate the light levels for different locations (like a classroom or a cupboard) before starting the main experiment.

**How to Calibrate:**
1. Flash the `day2_part1.py` code onto the micro:bit.
2. Place the micro:bit exactly where you want to measure the light (e.g., a classroom or a cupboard).
3. Press **Button A** to take a light reading.
4. Press **Button B** to display the reading (a number between 0 and 255).
5. Take at least 3 readings with the lights ON and 3 readings with the lights OFF to find a reliable location with a clear difference. 
6. Calculate the average for the "lights on" reading. You will need this number for the next step.

### Part 2: The Energy Light Timer
**File:** `day2_part2.py`

This is the main project for data collection. The program automatically starts a timer when the light goes on, and stops when it goes dark. 

**How to Collect Data:**
1. Open the `day2_part2.py` code in your editor.
2. Find the variable `LIGHT = 100` and replace `100` with your average "lights on" reading from the Calibration step.
3. Flash this updated code to your micro:bit.
4. Attach a battery pack to the micro:bit. 
5. Place it in your chosen location and press the **reset button** on the back to clear any stored time.
6. Leave the micro:bit for a set period of time (e.g., a few days or over the weekend).
7. Retrieve the micro:bit and press **Button B** to read the total time the lights were on in minutes.

## Data Analysis & Presentation

After collecting the data with the micro:bit over a few days, the student will use the provided Excel templates to organize, analyze, and present the findings.

### Step 1: Data Processing
1. Gather the recorded timings (in minutes) from the micro:bit.
2. Open the `energy-data-processing-student-handouts.xlsx` spreadsheet.
3. Enter your timings into the table to collate the data.
4. Plot simple column or bar charts to make the data easier to visualize. 
5. Analyze the charts to spot patterns in light usage or any unusual behavior (like lights left on over the weekend).

### Step 2: Energy Use Calculations
1. Find out the power rating (Wattage) of the lights in your location and the current unit cost of electricity.
2. Open the `energy-use-calculations-student-handouts-spreadsheet-5-a-energy-use-in-k-wh.xlsx` file.
3. Use the formula `kWh = watts ÷ 1000 × minutes ÷ 60` to calculate the energy used in kilowatt-hours (kWh).
4. Open the `energy-use-calculations-student-handouts-spreadsheet-5-b-energy-cost.xlsx` file.
5. Multiply the total kWh by the electricity unit cost to find the total financial cost of the lighting.

### Step 3: Presentations
1. Review all your findings, charts, and cost calculations from the previous steps.
2. Create a presentation to share your results with your class, teachers, or school leadership.
3. Explain how you used the micro:bit technology to collect reliable data.
4. Show your calculations for energy use and costs.
5. Provide clear recommendations on how changing behavior (e.g., turning off lights) or changing lighting types (e.g., switching to LEDs) can save money and reduce the school's carbon footprint.