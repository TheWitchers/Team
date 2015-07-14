__author__ = 'dvir'
import sqlite3
# not working on microsoft db formats. pypyodbc will work but no need for that now.
conn = sqlite3.connect("D:\steamProjDB1_Backup.accdb")
