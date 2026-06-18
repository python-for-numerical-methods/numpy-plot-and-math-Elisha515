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
# טיפול במקרה של קלט ריק כדי למנוע קריסה בטסטים
if input_array is None or len(input_array) == 0:
return np.array([], dtype=float)

# המרת הקלט ל-numpy array של מספרים עשרוניים
data = np.array(input_array, dtype=float)
# בדיקה אם כל הערכים במערך זהים
if np.all(data == data[0]):
# החזרה מדויקת לפי ההנחיות בשורה 18 של התרגיל המקורי
return np.zeros_like(data, dtype=float)
# חישוב מינימום ומקסימום
min_val = np.min(data)
max_val = np.max(data)
# ביצוע הנרמול
new_array = (data - min_val) / (max_val - min_val)

return new_array

if __name__ == "__main__":
# בדיקה עצמית מהירה
test_data = [10, 20, 30, 40, 50]
print(f"Original: {test_data}")
print(f"Normalized: {normalized_array(test_data)}")
# בדיקת מקרה קצה - כל המספרים זהים
edge_case = [5, 5, 5, 5]
print(f"\nOriginal: {edge_case}")
print(f"Normalized (Should be zeros): {normalized_array(edge_case)}")
