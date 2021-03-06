import psycopg2
from psycopg2.extras import RealDictCursor
import json
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

class DBManager:
	#connection handler
	def connect():
		#connect to postgresql
		conn = None
		try:
			#connect using md5 method
			conn = psycopg2.connect(host=os.environ["DB_HOST"],database=os.environ["DB_NAME"],user=os.environ["DB_USER"],password=os.environ["DB_PASS"])
			print("Connected to database")
			return conn
		except(Exception, psycopg2.DatabaseError) as error:
			print(error)

	def close(conn):
		#close connection to postgresql
		if conn is not None:
			conn.close()
			print("Database connection closed")
	#read functions
	def readfromPenyedia():
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			cur.execute(""" SELECT * FROM penyedia_beasiswa """)
			json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result
			

	def readfromPenyediaByID(id_penyedia):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ UPDATE detail_beasiswa SET aktif = 'No' WHERE waktu_tutup <= %(date)s  """
			values = {'date':Date.getCurrentDate()}
			dump =[{'Message':'Record successfully updated to mobile table'}]
			print(dump)
			cur.execute(query,values)
			conn.commit()
			query = """ SELECT * FROM penyedia_beasiswa WHERE id_penyedia = %(id)s """
			values = {'id':id_penyedia}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid id_penyedia','id_penyedia':id_penyedia}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result
			

	def readfromDetailBeasiswa():
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			cur.execute(""" SELECT * FROM detail_beasiswa """)
			json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result

	def readfromDetailBeasiswaByID(id_penyedia):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE id_penyedia = %(id)s """
			values = {'id':id_penyedia}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid id_penyedia','id_penyedia':id_penyedia}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result

	def readfromDetailBeasiswaByFakultas(fakultas):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE fakultas = %(id)s """
			values = {'id':fakultas}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid fakultas','Fakultas':fakultas}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result
			

	def readfromDetailBeasiswaByFakultasAndJurusan(fakultas,jurusan):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE fakultas = %(f)s AND jurusan = %(j)s """
			values = {'f':fakultas, 'j':jurusan}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid fakultas or jurusan','Fakultas':fakultas,'Jurusan':jurusan}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result
			

	def readfromDetailBeasiswaByFakultasAndJurusanAndSemester(fakultas,jurusan,semester):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE fakultas = %(f)s AND jurusan = %(j)s AND semester <= %(s)s AND batas_semester >= %(s)s """
			values = {'f':fakultas, 'j':jurusan, 's':semester}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid fakultas, jurusan, or semester','Fakultas':fakultas,'Jurusan':jurusan,'Semester':semester}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result
			

	def readfromDetailBeasiswaByFakultasAndJurusanAndMinGPA(fakultas,jurusan,gpa):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE fakultas = %(f)s AND jurusan = %(j)s AND min_gpa <= %(s)s """
			values = {'f':fakultas, 'j':jurusan, 's':gpa}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid fakultas, jurusan, or gpa','Fakultas':fakultas,'Jurusan':jurusan,'GPA':gpa}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result
			

	def readfromDetailBeasiswaByFakultasAndSemester(fakultas,semester):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE fakultas = %(f)s AND semester <= %(s)s AND batas_semester >= %(s)s """
			values = {'f':fakultas, 's':semester}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid fakultas or semester','Fakultas':fakultas, 'Semester':semester}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result
			
	
	def readfromDetailBeasiswaByFakultasAndSemesterAndMinGPA(fakultas,semester,gpa):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE fakultas = %(f)s AND semester <= %(s)s AND batas_semester >= %(s)s AND min_gpa <= %(g)s """
			values = {'f':fakultas, 's':semester, 'g':gpa}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid fakultas, semester, or gpa','Fakultas':fakultas, 'Semester':semester,'GPA':gpa}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result
			

	def readfromDetailBeasiswaByFakultasAndMinGPA(fakultas,gpa):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE fakultas = %(f)s AND min_gpa <= %(g)s """
			values = {'f':fakultas, 'g':gpa}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid fakultas or gpa','Fakultas':fakultas, 'GPA':gpa}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result
			

	def readfromDetailBeasiswaByAllParameters(fakultas,jurusan,semester,gpa):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE fakultas = %(f)s AND jurusan = %(j)s AND semester <= %(s)s AND batas_semester >= %(s)s AND min_gpa <= %(g)s """
			values = {'f':fakultas, 'j':jurusan,'s':semester, 'g':gpa}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid fakultas, jurusan, semester, or gpa','Fakultas':fakultas, 'Jurusan':jurusan,'Semester':semester,'GPA':gpa}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result
			


	def readfromDetailBeasiswaByJurusan(jurusan):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE jurusan = %(j)s """
			values = {'j':jurusan}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid jurusan','Jurusan':jurusan}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result
			

	def readfromDetailBeasiswaByJurusanAndSemester(jurusan,semester):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE jurusan = %(j)s AND semester <= %(s)s AND batas_semester >= %(s)s """
			values = {'j':jurusan,'s':semester}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid jurusan or semester','Jurusan':jurusan,'Semester':semester}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result

	def readfromDetailBeasiswaByJurusanAndMinGPA(jurusan,gpa):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE jurusan = %(j)s AND min_gpa <= %(g)s """
			values = {'j':jurusan,'g':gpa}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid jurusan or gpa','Jurusan':jurusan,'GPA':gpa}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result
			
	
	def readfromDetailBeasiswaByJurusanSemesterMinGPA(jurusan,semester,gpa):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE jurusan = %(j)s AND semester <= %(s)s AND batas_semester >= %(s)s AND min_gpa <= %(g)s """
			values = {'j':jurusan,'s':semester, 'g':gpa}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid jurusan, semester, or gpa','Jurusan':jurusan,'Semester':semester,'GPA':gpa}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result
			

	def readfromDetailBeasiswaBySemester(semester):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE semester <= %(s)s AND batas_semester >= %(s)s """
			values = {'s':semester}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid semester','Semester':semester}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result
			

	def readfromDetailBeasiswaBySemesterMinGPA(semester,gpa):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE semester <= %(s)s AND batas_semester >= %(s)s AND min_gpa <= %(g)s """
			values = {'s':semester, 'g':gpa}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid semester or gpa','Semester':semester,'GPA':gpa}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result

	def readfromDetailBeasiswaByMinGPA(gpa):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE min_gpa <= %(g)s """
			values = {'g':gpa}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid gpa','GPA':gpa}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result

	def readfromDetailBeasiswaByAktif(id_penyedia,aktif):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE id_penyedia = %(i)s AND aktif = %(a)s """
			values = {'i':id_penyedia,'a':aktif}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid aktif status or id_penyedia','ID':id_penyedia,'Aktif':aktif}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result

	def readfromDetailBeasiswaCountTidakAktif(id_penyedia):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT detail_beasiswa.*,jumlah_pendaftar FROM detail_beasiswa INNER JOIN (SELECT nama,id_penyedia,COUNT(nim) AS jumlah_pendaftar FROM pilihan_beasiswa GROUP BY nama,id_penyedia) AS hasil ON detail_beasiswa.id_penyedia = hasil.id_penyedia AND detail_beasiswa.nama = hasil.nama WHERE hasil.id_penyedia = %(i)s AND aktif='No' """
			values = {'i':id_penyedia}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid id_penyedia or no result','ID':id_penyedia}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result
			

	def readfromMahasiswa():
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			cur.execute(""" SELECT * FROM mahasiswa """)
			json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
		finally:
			print(json_result)
			return json_result
			DBManager.close(conn)

	def readfromMahasiswaByNIM(nim):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM mahasiswa WHERE nim = %(n)s """
			values = {'n':nim}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid NIM','NIM':nim}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result
			

	def readfromPilihanBeasiswa():
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			cur.execute(""" SELECT * FROM pilihan_beasiswa """)
			json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
		finally:
			print(json_result)
			return json_result
			DBManager.close(conn)

	def readfromPilihanBeasiswaByIDPenyedia(id_penyedia):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM pilihan_beasiswa WHERE id_penyedia = %(id)s """
			values = {'id':id_penyedia}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid ID','ID':id_penyedia}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result

	def readfromPilihanBeasiswaByNIM(nim):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT pilihan_beasiswa.id_penyedia,pilihan_beasiswa.nim,pilihan_beasiswa.status_seleksi,pilihan_beasiswa.waktu_submit,pilihan_beasiswa.nama as nama_beasiswa, penyedia_beasiswa.nama AS nama_penyedia FROM (pilihan_beasiswa INNER JOIN penyedia_beasiswa ON pilihan_beasiswa.id_penyedia = penyedia_beasiswa.id_penyedia INNER JOIN detail_beasiswa ON pilihan_beasiswa.id_penyedia = detail_beasiswa.id_penyedia) WHERE nim = %(n)s """
			values = {'n':nim}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid NIM','NIM':nim}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result

	def readfromPilihanBeasiswaByIDStatus(id_penyedia,status_seleksi):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM pilihan_beasiswa WHERE id_penyedia = %(i)s AND status_seleksi = %(n)s """
			values = {'i':id_penyedia,'n':status_seleksi}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Invalid ID or status_seleksi','ID':id_penyedia,'status_seleksi':status_seleksi}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result
	
	def readfromLoginMahasiswa():
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			cur.execute(""" SELECT * FROM login_mahasiswa """)
			json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result
	
	def readfromLoginPenyedia():
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			cur.execute(""" SELECT * FROM login_penyedia """)
			json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result

	def readfromLoginMappingMahasiswa(username):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = (""" SELECT nim FROM login_mapping_mahasiswa WHERE username = %(u)s """)
			values = {'u':username}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Form empty','Username':username}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result

	def readfromLoginMappingPenyedia(username):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = (""" SELECT id_penyedia FROM login_mapping_penyedia WHERE username = %(u)s """)
			values = {'u':username}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = [{'Message':'Form empty','Username':username}]
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to read record from mobile table'}]
			json_result = json.dumps(dump)
		finally:
			print(json_result)
			DBManager.close(conn)
			return json_result

	#create function
	def inserttoPenyediaBeasiswa(info):
		formatted_info = json.loads(info)
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ INSERT INTO penyedia_beasiswa(nama, email, no_telepon, alamat, website) VALUES (%(n)s, %(e)s, %(t)s, %(a)s, %(w)s) returning id_penyedia """
			values = {'n':formatted_info['nama'], 'e':formatted_info['email'], 't':formatted_info['no_telepon'], 'a':formatted_info['alamat'], 'w':formatted_info['website']}
			dump =[{'Message':'Record successfully inserted to mobile table'}]
			cur.execute(query,values)
			result = cur.fetchall()
			for row in result:
				id_penyedia = (row['id_penyedia'])
			query = """ UPDATE login_mapping_penyedia SET id_penyedia = %(i)s WHERE username = %(u)s """
			values = {'i':id_penyedia, 'u':formatted_info['username']}
			cur.execute(query,values)
			conn.commit()
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to insert record to mobile table'}]
			print(error)
		finally:
			json_result = json.dumps(dump)
			print(json_result)
			DBManager.close(conn)
			return json_result

	def inserttoDetailBeasiswa(info):
		formatted_info = json.loads(info)
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ INSERT INTO detail_beasiswa(id_penyedia, nama, waktu_buka, waktu_tutup, fakultas, jurusan, semester, min_gpa, deskripsi, batas_semester, tipe, aktif) VALUES (%(i)s, %(n)s, %(wb)s, %(wt)s, %(f)s, %(j)s, %(s)s, %(g)s, %(d)s, %(bs)s, %(t)s, %(a)s)  """
			values = {'i':formatted_info['id_penyedia'], 'n':formatted_info['nama'], 'wb':formatted_info['waktu_buka'], 'wt':formatted_info['waktu_tutup'], 'f':formatted_info['fakultas'], 'j':formatted_info['jurusan'], 's':formatted_info['semester'], 'g':formatted_info['min_gpa'], 'd':formatted_info['deskripsi'], 'bs':formatted_info['batas_semester'], 't':formatted_info['tipe'], 'a':'Yes'}
			dump =[{'Message':'Record successfully inserted to mobile table'}]
			cur.execute(query,values)
			conn.commit()
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to insert record to mobile table'}]
			print(error)
		finally:
			json_result = json.dumps(dump)
			print(json_result)
			DBManager.close(conn)
			return json_result
			

	def inserttoMahasiswa(info):
		formatted_info = json.loads(info)
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ INSERT INTO mahasiswa(nim, email, password, nama, no_telepon, usia, jurusan, semester, gpa, pendapatan, berkas) VALUES (%(ni)s, %(e)s, %(pw)s, %(na)s, %(no)s, %(u)s, %(j)s, %(s)s, %(g)s, %(p)s, %(b)s)  """
			values = {'ni':formatted_info['nim'], 'e':formatted_info['email'], 'pw':formatted_info['password'], 'na':formatted_info['nama'], 'no':formatted_info['no_telepon'], 'u':formatted_info['usia'], 'j':formatted_info['jurusan'], 's':formatted_info['semester'], 'g':formatted_info['gpa'], 'p':formatted_info['pendapatan'], 'b':formatted_info['berkas']}
			dump =[{'Message':'Record successfully inserted to mobile table'}]
			cur.execute(query,values)
			query = """ UPDATE login_mapping_mahasiswa SET nim = %(n)s WHERE username = %(u)s """
			values = {'n':formatted_info['nim'], 'u':formatted_info['username']}
			cur.execute(query,values)
			conn.commit()
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to insert record to mobile table'}]
			print(error)
		finally:
			json_result = json.dumps(dump)
			print(json_result)
			DBManager.close(conn)
			return json_result
			

	def inserttoPilihanBeasiswa(info):
		formatted_info = json.loads(info)
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			# cek detail beasiswa yg di-apply tipe single atau bukan
			query = """ SELECT * FROM detail_beasiswa WHERE id_penyedia = %(i)s AND nama = %(n)s AND tipe = 'Single' """
			values = {'i':formatted_info['id_penyedia'],'n':formatted_info['nama_beasiswa']}
			cur.execute(query,values)
			if (cur.rowcount != 0): # beasiswa yg di-apply single
				print('beasiswa yg di-apply single')
				query = """ SELECT * FROM (pilihan_beasiswa INNER JOIN detail_beasiswa ON pilihan_beasiswa.id_penyedia = detail_beasiswa.id_penyedia AND pilihan_beasiswa.nama = detail_beasiswa.nama) WHERE nim = %(n)s """
				values = {'n':formatted_info['nim']}
				cur.execute(query,values)
				if (cur.rowcount != 0): # sebelumnya sudah pernah apply
					print('sudah pernah apply')
					dump = [{'Message':'Already registered to other scholarship. Cannot apply to exclusive scholarship'}]
				else : #sebelumnya belum pernah apply
					print('belum pernah apply')
					query = """ INSERT INTO pilihan_beasiswa(id_penyedia, nim, status_seleksi, waktu_submit, nama) VALUES (%(i)s, %(n)s, %(s)s, %(w)s, %(nama)s)  """
					values = {'i':formatted_info['id_penyedia'], 'n':formatted_info['nim'], 's':'Pending', 'w':Date.getCurrentDate(),'nama':formatted_info['nama_beasiswa']}
					dump =[{'Message':'Record successfully inserted to mobile table'}]
					cur.execute(query,values)
					conn.commit()
			else : #beasiswa yg di-apply multi
				print('beasiswa yg di-apply multi')
				query = """ SELECT * FROM (pilihan_beasiswa INNER JOIN detail_beasiswa ON pilihan_beasiswa.id_penyedia = detail_beasiswa.id_penyedia AND pilihan_beasiswa.nama = detail_beasiswa.nama) WHERE nim = %(n)s AND tipe = 'Single' """
				values = {'n':formatted_info['nim']}
				cur.execute(query,values)
				if (cur.rowcount != 0):
					print('Sudah pernah apply single')
					dump =[{'Message':'Already registered to exclusive scholarship'}]
				else:
					print('Belum pernah apply atau apply multi')
					query = """ INSERT INTO pilihan_beasiswa(id_penyedia, nim, status_seleksi, waktu_submit, nama) VALUES (%(i)s, %(n)s, %(s)s, %(w)s, %(nama)s)  """
					values = {'i':formatted_info['id_penyedia'], 'n':formatted_info['nim'], 's':'Pending', 'w':Date.getCurrentDate(),'nama':formatted_info['nama_beasiswa']}
					dump =[{'Message':'Record successfully inserted to mobile table'}]
					cur.execute(query,values)
					conn.commit()
		except(Exception, psycopg2.Error) as error:
			dump = [{'Message': 'Failed to insert record to mobile table'}]
			print(error)
		finally:
			json_result = json.dumps(dump)
			print(json_result)
			DBManager.close(conn)
			return json_result
			

	#update functions
	def updatetoPilihanBeasiswa(info,id_penyedia,nim):
		formatted_info = json.loads(info)
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ UPDATE pilihan_beasiswa SET status_seleksi = %(s)s WHERE id_penyedia = %(i)s AND nim = %(n)s AND nama = %(nama)s """
			values = {'s':formatted_info['status_seleksi'], 'i':id_penyedia, 'n':nim, 'nama':formatted_info['nama_beasiswa']}
			dump =[{'Message':'Record successfully updated to mobile table'}]
			cur.execute(query,values)
			conn.commit()
		except(Exception, psycopg2.Error) as error:
			dump = {'Message': 'Failed to update record to mobile table'}
			print(error)
		finally:
			json_result = json.dumps(dump)
			print(json_result)
			DBManager.close(conn)
			return json_result

	def updatePenyediaBeasiswa(info,id_penyedia):
		formatted_info = json.loads(info)
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ UPDATE penyedia_beasiswa SET nama = %(n)s, email = %(e)s, no_telepon = %(t)s, alamat = %(a)s, website = %(w)s  WHERE id_penyedia = %(i)s """
			values = {'n':formatted_info['nama'], 'e':formatted_info['email'], 't':formatted_info['no_telepon'], 'a':formatted_info['alamat'], 'w':formatted_info['website'], 'i':id_penyedia}
			dump =[{'Message':'Record successfully updated to mobile table'}]
			cur.execute(query,values)
			conn.commit()
		except(Exception, psycopg2.Error) as error:
			dump = {'Message': 'Failed to update record to mobile table'}
			print(error)
		finally:
			json_result = json.dumps(dump)
			print(json_result)
			DBManager.close(conn)
			return json_result

	def updateAktifDetailBeasiswa(info,id_penyedia):
		formatted_info = json.loads(info)
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ UPDATE detail_beasiswa SET aktif = %(a)s WHERE nama = %(n)s AND id_penyedia = %(i)s """
			values = {'a':formatted_info['aktif'],'n':formatted_info['nama_beasiswa'] ,'i':id_penyedia}
			dump =[{'Message':'Record successfully updated to mobile table'}]
			cur.execute(query,values)
			conn.commit()
		except(Exception, psycopg2.Error) as error:
			dump = {'Message': 'Failed to update record to mobile table'}
			print(error)
		finally:
			json_result = json.dumps(dump)
			print(json_result)
			DBManager.close(conn)
			return json_result

	def updateDetailMahasiswa(info,nim):
		formatted_info = json.loads(info)
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ UPDATE mahasiswa SET email = %(e)s, nama = %(nama)s, no_telepon = %(t)s, usia = %(u)s, jurusan = %(j)s, semester = %(s)s, gpa = %(g)s, pendapatan = %(p)s, berkas = %(b)s WHERE nim = %(nim)s """
			values = {'e':formatted_info['email'],'nama':formatted_info['nama'], 't':formatted_info['no_telepon'],'u':formatted_info['usia'],'j':formatted_info['jurusan'],'s':formatted_info['semester'],'g':formatted_info['gpa'],'p':formatted_info['pendapatan'],'b':formatted_info['berkas'], 'nim':nim}
			dump =[{'Message':'Record successfully updated to mobile table'}]
			cur.execute(query,values)
			conn.commit()
		except(Exception, psycopg2.Error) as error:
			dump = {'Message': 'Failed to update record to mobile table'}
			print(error)
		finally:
			json_result = json.dumps(dump)
			print(json_result)
			DBManager.close(conn)
			return json_result


class Date:
	def getCurrentDate():
		currentYear = str(datetime.now().year)
		currentMonth = str(datetime.now().month)
		currentDay = str(datetime.now().day)
		date = int(currentYear+currentMonth+currentDay)
		return date

	
	