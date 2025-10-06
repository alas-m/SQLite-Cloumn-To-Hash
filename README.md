# 🔐 SQLite Column Hasher
_A Python utility for hashing SQLite table columns with SHA-256._

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![SQLite](https://img.shields.io/badge/SQLite-Compatible-orange)

A lightweight Python utility for automatically generating SHA-256 hashes of selected columns in one or more SQLite database tables.
This tool is useful for anonymizing, verifying, or securing sensitive column data without altering the original values.

## 📑 Table of Contents
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Example](#-example)
- [Code Overview](#-code-overview)
- [Notes](#-notes)
- [License](#-license)
- [Use Cases](#-use-cases)

## 🚀 Features
- Automatically adds `_sha256` columns
- Computes SHA-256 hashes (binary digests)
- Supports multiple tables and columns
- Uses only Python’s built-in libraries
- Safe updates with commit checkpoints

## 🧰 Requirements
- Python 3.8+
- sqlite3 (built-in)
- hashlib (built-in)

## ⚙️ Installation
`git clone https://github.com/alas-m/SQLite-Column-To-Hash.git`

`cd SQLite-Column-To-Hash`

## 💻 Usage
1. Edit `DB_PATH`, `TABLES`, and `INCLUDE_COLS_ONLY` in the script.
2. Run:
   ```bash
   python hash_columns.py

## 🧩 Example
Before:
| user_id  | name  |
|----------|-------|
| 12345    | Alice |

After:
| user_id  | name  | user_id_sha256 |
|----------|-------|----------------|
| 12345    | Alice | 0x5994471a...  |

## 🧠 Code Overview
- `sha256_hex(s)`: Converts text to SHA-256 digest (binary)
- `main()`: Adds columns and fills with hashes
- `__main__`: Loops through tables

## 🧼 Notes
- Hash columns use BLOB type for compact storage
- Backup your database before running
- Use `.hexdigest()` if you prefer human-readable hashes

## 📄 License
MIT License © Malik Alasgar

## 💡 Example Use Cases
- Anonymizing user data
- Generating secure identifiers
- Verifying database integrity

## 🔮 Future Improvements
- Add hex output option
- CLI arguments for configuration
- Parallel hashing for large databases

