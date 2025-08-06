import sqlite3
import os


def init_db():
    """Initialize SQLite database for grammar rules and syllabus."""
    db_path = os.path.join("data", "grammar_rules.db")
    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Grammar rules table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rules (
            error TEXT PRIMARY KEY,
            correction TEXT
        )
    """)

    # Syllabus table (placeholder for future use)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS syllabus (
            grade INTEGER,
            subject TEXT,
            chapter TEXT,
            content TEXT
        )
    """)

    # Sample data
    cursor.execute("INSERT OR IGNORE INTO syllabus VALUES (?, ?, ?, ?)",
                   (8, "Science", "Photosynthesis", "Photosynthesis is the process..."))

    conn.commit()
    conn.close()
    print("Database initialized successfully.")


if __name__ == "__main__":
    init_db()