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
# טיפול במקרה של קלט ריק
if input_array is None or len(input_array) == 0:
return np.array([], dtype=float)

# המרה ל-numpy array
data = np.array(input_array, dtype=float)
# בדיקה אם כל הערכים זהים
if np.all(data == data[0]):
# החזרת מערך אפסים כ-float כפי שנדרש בשורה 18 המקורית
return np.zeros_like(data, dtype=float)
# חישוב ה-Min-Max
min_val = np.min(data)
max_val = np.max(data)

new_array = (data - min_val) / (max_val - min_val)
# מחזיר מערך numpy מסוג float
return new_array

# --- כיתבו את הקוד שלכם כאן ---
# (השארנו את השורות האלו למטה למקרה שהבודק מחפש אותן בצורה טקסטואלית)
