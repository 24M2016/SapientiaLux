import sqlite3
import os
import onnxruntime as ort
import numpy as np


class GrammarModule:
    def __init__(self):
        self.session = ort.InferenceSession("models/mobilebert.onnx")
        self.db_path = os.path.join("data", "grammar_rules.db")
        self._load_rules()

    def _load_rules(self):
        """Initialize grammar rules in SQLite."""
        os.makedirs("data", exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS rules (error TEXT PRIMARY KEY, correction TEXT)")
        # Sample rules
        sample_rules = [
            ("he go to school", "He goes to school"),
            ("i is happy", "I am happy")
        ]
        cursor.executemany("INSERT OR IGNORE INTO rules VALUES (?, ?)", sample_rules)
        conn.commit()
        conn.close()

    def correct_text(self, text: str) -> dict:
        """Correct text using rules (extend with MobileBERT later)."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT correction FROM rules WHERE error=?", (text.lower(),))
        result = cursor.fetchone()
        conn.close()

        if result:
            return {
                "status": "success",
                "corrected_text": result[0],
                "explanation": "Corrected subject-verb agreement or capitalization"
            }
        return {
            "status": "success",
            "corrected_text": text,
            "explanation": "No errors found"
        }