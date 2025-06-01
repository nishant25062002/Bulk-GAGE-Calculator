```markdown
# 🌍 Bulk GAGE Plate Motion Calculator

This project automates the **GAGE Plate Motion Calculator** workflow for bulk geographic data. It allows researchers to extract midpoints from KML line data and compute tectonic plate velocities and azimuths for each point using Euler pole models (like ITRF2020).

---

## 📁 Project Main Files

├── Midpoint\_Calculator.ipynb             # Extracts midpoints from KML line segments
├── Velocity\_Azimuth\_Calculator.ipynb     # Calculates motion vectors for each midpoint

```

```

## 🧠 Overview

### 1. 📍 `Midpoint_Calculator.ipynb`

**Description:**
This notebook parses a `.kml` file containing `<LineString>` geometries (e.g., fault traces or channel offsets) and computes the geographic **midpoint** of each line segment.

- **Input:** KML file with multiple LineStrings.
- **Output:** Excel file (`output_midpoints.xlsx`) with:
  - `mid_lat`, `mid_lon`

This is particularly useful for generating analysis-ready coordinate points from geospatial line features.

---

### 2. 🧭 `Velocity_Azimuth_Calculator.ipynb`

**Description:**
This notebook takes an Excel file containing multiple latitude-longitude pairs and computes:
- **Plate name** (based on location)
- **East and North velocity components**
- **Total velocity magnitude (in mm/year)**
- **Azimuth** (bearing in degrees from North)

It uses a lookup from predefined **Euler pole data** (e.g., ITRF2020) for each tectonic plate.

- **Input:** Excel file with `Latitude`, `Longitude` columns (e.g., output of previous notebook).
- **Output:** Excel file (`output_velocity_azimuth.xlsx`) with:
  - `PlateName`, `Velocity_East`, `Velocity_North`, `Total_Speed`, `Azimuth`

---

## ⚙️ Installation & Dependencies

Make sure Python is installed, then install required packages using pip:

```bash
pip install pandas numpy shapely openpyxl matplotlib scikit-learn
````

You will also need **Jupyter Notebook**:

```bash
pip install notebook
jupyter notebook
```

---

## 🚀 Usage Instructions

1. **Clone this Repository**

```bash
git clone https://github.com/your-username/bulk-gage-motion-calculator.git
cd bulk-gage-motion-calculator
```

2. **Step 1 – Extract Midpoints from KML**

* Open `Midpoint_Calculator.ipynb` in Jupyter Notebook
* Upload your `.kml` file
* Run all cells
* Output: `output_midpoints.xlsx`

3. **Step 2 – Compute Velocity and Azimuth**

* Open `Velocity_Azimuth_Calculator.ipynb`
* Set the path to `output_midpoints.xlsx`
* Run all cells
* Output: `output_velocity_azimuth.xlsx`

---

## 📌 Example Workflow

### Example KML Input

```
<LineString>
  <coordinates>77.2,28.6,0 77.4,28.8,0</coordinates>
</LineString>
```

### Output from Step 1

| mid\_lat | mid\_lon |
| -------- | -------- |
| 28.7     | 77.3     |

### Output from Step 2

| Latitude | Longitude | PlateName | Velocity\_East | Velocity\_North | Total\_Speed | Azimuth |
| -------- | --------- | --------- | -------------- | --------------- | ------------ | ------- |
| 28.7     | 77.3      | Indian    | 37.5 mm/yr     | 14.2 mm/yr      | 40.0 mm/yr   | 68.4°   |

---

## 📜 License

This project is copyright © {{year}} Nishant Mainwal. Unauthorized use is prohibited.


---

## 🙌 Acknowledgments

* [GAGE Plate Motion Calculator](http://unavco.org/software/geodetic-utilities/plate-motion-calculator/plate-motion-calculator.html)
* ITRF2020 Euler Poles
* Python & Jupyter Ecosystem

---

## 📬 Contact

For suggestions or issues, please open a GitHub Issue or reach out to the project maintainer.
