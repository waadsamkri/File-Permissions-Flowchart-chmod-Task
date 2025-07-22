
---

## 🔍 File Permissions Breakdown

Linux file permissions consist of 3 parts:
- **Owner**
- **Group**
- **Others**

Each part can have:
- `r` → Read
- `w` → Write
- `x` → Execute

So, `rwxrwxr-x` means:
- Owner: read, write, execute
- Group: read, write, execute
- Others: read, execute

This corresponds to the numeric mode `775`.

---

## 📊 Flowchart

A flowchart is included to help visualize the permission-checking process and how to apply `chmod`.

### Steps:
1. Check if the file is readable.
2. Check if the file is writable.
3. Identify which group (Owner, Group, Others) has which permissions.
4. Form the full symbolic permission (e.g., `rwxrwxr-x`).
5. Apply it using:

```bash
chmod 775 file.py
