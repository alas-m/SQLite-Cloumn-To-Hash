import sqlite3
import hashlib
import sys

DB_PATH      = R"DIR/TO/YOUR/SQLITE/DATABASE"
TABLES       = ["TABLE1", "TABLE2"]

INCLUDE_COLS_ONLY = ["column1", "columm2", "columm3"] # Columns you want to hash


def sha256_hex(s: str) -> str: #Text to sha256 (digest, not hexdigest)
    if s.isupper():
        s.lower().capitalize()
    return hashlib.sha256(s.encode("utf-8")).digest()

def main(db_path: str, TABLE: str):
    print(f"Adding hashes to table {TABLE}")
    conn = sqlite3.connect(db_path)
    cur  = conn.cursor()

    cur.execute(f'PRAGMA table_info("{TABLE}");')
    cols_info = cur.fetchall()
    all_cols  = [row[1] for row in cols_info]

    to_hash = [c for c in all_cols if c in INCLUDE_COLS_ONLY]
    if not to_hash:
        print("No columns to hash! Check INCLUDE_COLS_ONLY.")
        return

    for col in to_hash:
        hash_col = f"{col}_sha256"
        if hash_col not in all_cols:
            print(f"Adding column '{hash_col}'")
            cur.execute(f'ALTER TABLE "{TABLE}" ADD COLUMN "{hash_col}" BLOB;')
        else:
            print(f"Column '{hash_col}' already exists, skipping.")
    conn.commit()

    for col in to_hash:
        hash_col = f"{col}_sha256"
        print(f"Hashing '{col}' → '{hash_col}'")
        cur.execute(f'SELECT rowid, "{col}" FROM "{TABLE}";')
        for rowid, value in cur.fetchall():
            raw = "" if value is None else str(value)
            h   = sha256_hex(raw)
            cur.execute(
                f'UPDATE "{TABLE}" SET "{hash_col}" = ? WHERE rowid = ?;',
                (h, rowid)
            )
        conn.commit()

    conn.close()
    print("All hashes computed.")

if __name__ == "__main__":
    for TABLE in TABLES:
        main(DB_PATH, TABLE)

# Demo:
#
# database "C:/Database/google.db"
# table "users"
#
# column "user_id" -> "user_id_sha256"
# value "12345" -> "0x5994471a..."
