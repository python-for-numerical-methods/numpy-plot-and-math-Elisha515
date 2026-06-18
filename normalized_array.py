import numpy as np

def normalized_array(input_array):
"""
מנרמלת מערך נתונים לטווח של [0, 1] לפי שיטת Min-Max Scaling.
הנוסחה לביצוע:
x_norm = (x - min) / (max - min)
פרמטרים:
data (list or np.array): מערך של מספרים.
מחזירה:
np.array: מערך מנורמל. אם כל הערכים במערך זהים, יש להחזיר מערך של אפסים.
"""
# המרת הקלט ל-numpy array
data = np.array(input_array)
# בדיקה אם כל הערכים זהים
if np.all(data == data[0]):
# החזרת מערך אפסים באותו אורך וסוג float בדיוק כמו שנדרש בהערות
return np.zeros_like(data, dtype=float)
# חישוב ה-Min-Max Scaling והמרה מפורשת ל-float
min_val = np.min(data)
max_val = np.max(data)
new_array = (data - min_val) / (max_val - min_val)

return new_array.astype(float)

if __name__ == "__main__":
# בדיקה עצמית מהירה
test_data = [10, 20, 30, 40, 50]
print(f"Original: {test_data}")
print(f"Normalized: {normalized_array(test_data)}")
